#!/usr/bin/env python3
"""Local SQLite teaching fixture; no network, real money, model, or workflow engine."""
import argparse
import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path


def connect(path):
    db = sqlite3.connect(path, timeout=10, isolation_level=None)
    db.execute('PRAGMA foreign_keys=ON')
    return db


def initialize(path):
    with connect(path) as db:
        db.executescript('''
        CREATE TABLE IF NOT EXISTS authority (
          intent TEXT PRIMARY KEY, beneficiary TEXT NOT NULL,
          cents INTEGER NOT NULL CHECK(cents > 0), version INTEGER NOT NULL,
          expires INTEGER NOT NULL, allowed INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS effects (
          receipt INTEGER PRIMARY KEY, intent TEXT NOT NULL,
          beneficiary TEXT NOT NULL, cents INTEGER NOT NULL,
          version INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS attempts (
          attempt TEXT PRIMARY KEY, intent TEXT NOT NULL, result TEXT NOT NULL);
        INSERT OR IGNORE INTO authority VALUES ('D-41-credit','P-9',12000,1,100,1);
        ''')


def query(path, intent):
    with connect(path) as db:
        rows = db.execute('SELECT receipt,beneficiary,cents,version FROM effects WHERE intent=? ORDER BY receipt', (intent,)).fetchall()
    # Absence in this read does not fence a request still in flight.
    return {'state': 'present' if rows else 'unknown', 'effects': rows,
            'limit': 'A read with no effect is not proof of final absence.'}


def request(path, attempt, cents=12000, beneficiary='P-9', version=1,
            now=10, lose_reply=False, unsafe=False, intent='D-41-credit'):
    db = connect(path)
    try:
        db.execute('BEGIN IMMEDIATE')
        prior = db.execute('SELECT 1 FROM attempts WHERE attempt=?', (attempt,)).fetchone()
        if prior:
            db.rollback()
            return {'state': 'attempt_id_reused'}
        authority = db.execute('SELECT beneficiary,cents,version,expires,allowed FROM authority WHERE intent=?', (intent,)).fetchone()
        if not authority or authority[:3] != (beneficiary, cents, version):
            state = 'binding_conflict'
        elif not authority[4] or now >= authority[3]:
            state = 'authority_denied'
        else:
            existing = db.execute('SELECT receipt,beneficiary,cents,version FROM effects WHERE intent=? ORDER BY receipt', (intent,)).fetchall()
            if existing and not unsafe:
                state = 'existing_effect' if len(existing) == 1 and existing[0][1:] == (beneficiary,cents,version) else 'reconcile_conflict'
            else:
                db.execute('INSERT INTO effects(intent,beneficiary,cents,version) VALUES (?,?,?,?)', (intent,beneficiary,cents,version))
                state = 'committed'
        db.execute('INSERT INTO attempts VALUES (?,?,?)', (attempt,intent,state))
        db.commit()
        if lose_reply and state in ('committed','existing_effect'):
            return {'state': 'timeout', 'effect_from_caller_view': 'unknown'}
        return {'state': state}
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()


def child(path, *args):
    return json.loads(subprocess.check_output([sys.executable, str(Path(__file__).resolve()), str(path), *args], text=True))


def demo():
    # Every command executes in a fresh interpreter against the same on-disk participant.
    with tempfile.TemporaryDirectory(prefix='workflow-lost-reply-') as directory:
        good = Path(directory)/'governed.sqlite'
        bad = Path(directory)/'unsafe.sqlite'
        results = {}
        for path in (good,bad):
            child(path,'init')
        results['caller_after_commit'] = child(good,'attempt','--attempt','a1','--lose-reply')
        results['query_after_process_restart'] = child(good,'query')
        results['same_intent_new_attempt'] = child(good,'attempt','--attempt','a2')
        results['changed_amount'] = child(good,'attempt','--attempt','a3','--cents','15000')
        child(good,'revoke')
        results['after_revocation'] = child(good,'attempt','--attempt','a4')
        results['original_effect_survives_revocation'] = child(good,'query')
        child(bad,'attempt','--attempt','b1','--unsafe','--lose-reply')
        child(bad,'attempt','--attempt','b2','--unsafe')
        results['negative_control_duplicate_effects'] = child(bad,'query')
        print(json.dumps(results,indent=2))


def main():
    if sys.argv[1:] == ['demo']:
        demo(); return
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('database'); p.add_argument('action',choices=['init','query','attempt','revoke'])
    p.add_argument('--attempt',default='a1'); p.add_argument('--cents',type=int,default=12000)
    p.add_argument('--beneficiary',default='P-9'); p.add_argument('--version',type=int,default=1)
    p.add_argument('--now',type=int,default=10); p.add_argument('--lose-reply',action='store_true')
    p.add_argument('--unsafe',action='store_true',help='Deliberately disable intent deduplication for the negative control')
    a=p.parse_args()
    if a.action=='init':
        initialize(a.database); result={'state':'initialized'}
    elif a.action=='query': result=query(a.database,'D-41-credit')
    elif a.action=='revoke':
        with connect(a.database) as db:
            db.execute("UPDATE authority SET allowed=0 WHERE intent='D-41-credit'")
        result={'state':'revoked'}
    else: result=request(a.database,a.attempt,a.cents,a.beneficiary,a.version,a.now,a.lose_reply,a.unsafe)
    print(json.dumps(result))

if __name__=='__main__': main()
