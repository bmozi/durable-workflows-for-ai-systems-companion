# Did the credit happen?

A participant commits a fictional $120 credit and the caller loses the reply.
Predict the number of effects before running anything. Should a timeout be
reported as failure, success, or unknown? What would you ask the participant?

From this directory, with Python 3 and its standard library:

```bash
python3 lab.py demo
python3 -m unittest -v test_lab.py
```

The demo uses temporary on-disk SQLite databases and new Python processes.
It makes no network calls, uses no credentials, transfers no money, and deletes
its temporary databases on exit. `lab.py DATABASE init` creates a fixture only
at the path you supply; use a new disposable path for manual exploration.

## Read the result

The caller sees `timeout`. A new process queries one stored effect. A second
attempt under the same approved intent returns `existing_effect`. A changed
amount is a `binding_conflict`. Revoking authority prevents further execution;
it does not erase the existing credit, which can still be queried in this fixture.

The negative control deliberately disables intent deduplication: two attempts
produce two effects totaling $240. Restoring the governed path detects those
conflicting effects and requires reconciliation; it does not silently return
one convenient receipt.

## Change the condition

Run the tests for changed beneficiary, decision version, expiry, and concurrent
processes. Explain why the empty query returns `unknown`: the absence of a row
in a read cannot establish that a delayed original request will never commit.
In a real participant, safe resubmission depends on the actual contract,
including retention, parameter binding, late-arrival handling, and fencing.

## What this establishes

This is a deterministic teaching fixture. SQLite serializes the effect check
and commit with `BEGIN IMMEDIATE`; independent invocations observe persistent
participant rows. The caller's lost reply is simulated after commit, not a
real network fault. Authority is a local table and a supplied integer clock,
not production authentication. There is no real workflow engine, model call,
notice delivery, tenant isolation, retention expiry, distributed consensus,
power-loss test, or production payment guarantee. Passing tests establish only
the named fixture behavior. The original Northbridge experiments remain unrun.

The supplied answer does not claim that one effect closes a dispute. Approval,
correct parameters, notice, residue, and the beneficiary's promised outcome
still need their own evidence and owner. This lab isolates one boundary so you
can see it clearly.
