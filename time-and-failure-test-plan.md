# Time-and-Failure Test Plan

**Use boundary:** Illustrative field tool; not certification or proof of
production fitness

**Validation state:** `unrun`. Completing this plan does not prove that a
workflow survives failure, preserves an invariant, prevents repeated effects,
or behaves safely in production.

Use the evidence states `constructed`, `scenario`, `planned`, `unrun`,
`observed`, `tested`, `reported`, `sourced`, `bounded`, `inferred`, `proposed`,
and `unknown` exactly. A planned case remains `planned` / `unrun` until its
inputs, execution, result, limits, and artifact location are retained.

Use this plan to test the workflow's continuing business promise under
controlled time, failure, repetition, and recovery. A passing happy path is not
enough.

## 1. Test subject

| Field | Decision |
| --- | --- |
| Workflow and definition version | |
| Business promise and invariant | |
| Test environment and isolation | |
| External effects replaced or safely sandboxed | |
| Clock-control mechanism | |
| State reset and evidence retention | |
| Test owner | |
| Business operation identity | |
| Attempt identity and correlation rule | |
| Attempt, elapsed-time, capacity, cost, and action budgets | |
| Current execution and recovery authority | |

## 2. Evidence layers

| Layer | What it can show | What it cannot prove alone | Artifact location |
| --- | --- | --- | --- |
| State-model or unit | | | |
| Deterministic replay | | | |
| Controlled-time | | | |
| Failure injection | | | |
| Integration | | | |
| End-to-end scenario | | | |
| Operational observation | | | |
| Business reconciliation | | | |

## 3. Time scenarios

| Scenario | Time manipulation | Expected state and owner | Deadline behavior | Required evidence | Result |
| --- | --- | --- | --- | --- | --- |
| Dependency responds just before timeout | | | | | planned / unrun |
| Dependency succeeds after caller timeout | | | | | planned / unrun |
| Human decision arrives before escalation | | | | | planned / unrun |
| Human decision arrives after escalation | | | | | planned / unrun |
| Business calendar crosses weekend/holiday | | | | | planned / unrun |
| Daylight-saving or time-zone boundary | | | | | planned / unrun |
| Delayed trigger is missed during outage | | | | | planned / unrun |
| Recurring trigger overlaps prior run | | | | | planned / unrun |
| Policy/version changes while waiting | | | | | planned / unrun |

## 4. Failure and repetition scenarios

| Injection point | Failure or mutation | Expected retry/stop behavior | Business invariant | Compensation/recovery | Evidence | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Before checkpoint | worker loss | | | | | planned / unrun |
| After checkpoint, before effect | worker loss | | | | | planned / unrun |
| After effect, before acknowledgement | ambiguous timeout | | | | | planned / unrun |
| Message delivery | duplicate | | | | | planned / unrun |
| Dependency | unavailable or throttled | | | | | planned / unrun |
| Parallel branch | partial success | | | | | planned / unrun |
| Human task | unassigned or abandoned | | | | | planned / unrun |
| Compensation | transient then terminal failure | | | | | planned / unrun |
| Durable state | incompatible or poisoned | | | | | planned / unrun |
| Migration | interrupted midway | | | | | planned / unrun |
| Retry cohort, no jitter | correlated contention baseline | | | | | planned / unrun |
| Retry cohort, selected jitter | paired correlated-load challenge | | | | | planned / unrun |
| Authority or policy | permission changes between attempts | | | | | planned / unrun |

## 5. Outcome assertions

Do not stop at “all steps completed.” Assert:

- the promise always had a visible owner;
- every open instance was progressing, waiting under policy, escalated, or
  governed for recovery;
- no prohibited business effect occurred more than allowed;
- every terminal outcome had sufficient authorization and evidence;
- compensation preserved the original history and residual uncertainty;
- deadlines used the approved calendar and escalation semantics;
- version identity and transition history were reconstructable; and
- protected data and credentials were not exposed by test evidence.

## 6. Negative and boundary results

| Expected claim | Counterexample or failed test | Scope affected | Decision | Owner |
| --- | --- | --- | --- | --- |
| | | | | |

## 7. Exit gate

| Gate | Required evidence | State | Approver |
| --- | --- | --- | --- |
| Time semantics verified | | blocked | |
| Duplicate and ambiguity outcomes verified | | blocked | |
| Compensation and residual harm verified | | blocked | |
| Human delay and escalation verified | | blocked | |
| Version and recovery behavior verified | | blocked | |
| Business reconciliation completed | | blocked | |

Passing this plan proves only the tested workflow, version, dependencies,
scenarios, and environment. Record what production variation remains outside
the evidence. `Blocked` above is a gate disposition, not an evidence state; the
underlying cases remain `planned` / `unrun` until retained results exist.
