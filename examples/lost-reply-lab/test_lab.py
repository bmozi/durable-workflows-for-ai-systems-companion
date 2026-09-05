import concurrent.futures
from pathlib import Path
import tempfile
import unittest
import lab

class EffectBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db=Path(self.tmp.name)/'participant.sqlite'
        lab.child(self.db,'init')

    def test_commit_then_lost_reply_survives_process_restart(self):
        self.assertEqual(lab.child(self.db,'attempt','--lose-reply')['state'],'timeout')
        self.assertEqual(len(lab.child(self.db,'query')['effects']),1)

    def test_distinct_attempts_same_intent_do_not_duplicate(self):
        lab.child(self.db,'attempt','--attempt','a1','--lose-reply')
        self.assertEqual(lab.child(self.db,'attempt','--attempt','a2')['state'],'existing_effect')
        self.assertEqual(len(lab.query(self.db,'D-41-credit')['effects']),1)

    def test_changed_amount_does_not_inherit_approval(self):
        lab.request(self.db,'a1')
        self.assertEqual(lab.request(self.db,'a2',cents=15000)['state'],'binding_conflict')
        self.assertEqual(lab.query(self.db,'D-41-credit')['effects'][0][2],12000)

    def test_changed_beneficiary_rejected_without_effect(self):
        self.assertEqual(lab.request(self.db,'a1',beneficiary='P-10')['state'],'binding_conflict')
        self.assertEqual(lab.query(self.db,'D-41-credit')['effects'],[])

    def test_stale_decision_version_rejected(self):
        self.assertEqual(lab.request(self.db,'a1',version=2)['state'],'binding_conflict')

    def test_expiry_boundary_denies_new_effect(self):
        self.assertEqual(lab.request(self.db,'a1',now=100)['state'],'authority_denied')
        self.assertEqual(lab.query(self.db,'D-41-credit')['effects'],[])

    def test_revocation_stops_execution_but_does_not_erase_history(self):
        lab.request(self.db,'a1')
        lab.child(self.db,'revoke')
        self.assertEqual(lab.request(self.db,'a2')['state'],'authority_denied')
        self.assertEqual(len(lab.query(self.db,'D-41-credit')['effects']),1)

    def test_empty_query_remains_unknown(self):
        self.assertEqual(lab.query(self.db,'D-41-credit')['state'],'unknown')

    def test_concurrent_processes_share_one_commit_boundary(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(lambda i:lab.child(self.db,'attempt','--attempt',f'a{i}'),range(4)))
        self.assertEqual(len(lab.query(self.db,'D-41-credit')['effects']),1)

    def test_negative_control_really_duplicates(self):
        lab.request(self.db,'a1',lose_reply=True,unsafe=True)
        lab.request(self.db,'a2',unsafe=True)
        effects=lab.query(self.db,'D-41-credit')['effects']
        self.assertEqual(len(effects),2)
        self.assertEqual(sum(x[2] for x in effects),24000)
        self.assertEqual(lab.request(self.db,'a3')['state'],'reconcile_conflict')

if __name__=='__main__': unittest.main()
