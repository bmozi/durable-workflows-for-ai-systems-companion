# Aster Vale Time-and-Failure Test Plan

**Example state:** `scenario`

**Validation state:** `unrun`

**Scenario identity:** `AVO-CAMPAIGN-01`

**Disclosure:** Aster Vale Observatory is an unrelated fictional scenario. This
completed example demonstrates use of the
[blank plan](../time-and-failure-test-plan.md). It is not a test report; no
case has run and no artifact exists. Completion does not validate the workflow
or establish any usability, technical, scientific, business, privacy,
accessibility, or safety result.

## 1. Test subject

| Field | Scenario decision |
| --- | --- |
| Workflow and definition version | `AVO-OBSERVING-CAMPAIGN/v0-proposed` |
| Business promise and invariant | Reach one authorized campaign disposition; never infer capture absence from caller timeout |
| Test environment and isolation | `planned`; frozen simulator fixture, exact topology `unknown` |
| External effects replaced or safely sandboxed | `planned`; instrument-command and raw-store doubles; suitability `unrun` |
| Clock-control mechanism | `planned`; deterministic UTC, schedule-window, and campaign-deadline controls |
| State reset and evidence retention | `planned`; new campaign IDs with immutable command/capture/decision bundle and hashes |
| Test owner | Proposed: Platform Operations; Program, Instrument, and Data roles review their assertions |
| Business operation identity | `AVO-RETRY-01`: one authorized observation command for one campaign/window disposition |
| Attempt identity and correlation rule | A unique attempt ID links to `AVO-RETRY-01`; exact format and retention remain `unknown` |
| Attempt, elapsed-time, capacity, cost, and action budgets | Finite values are required but remain `unknown`; the fixture must freeze each value before execution |
| Current execution and recovery authority | Platform Operations may execute the fixture; Program Operations owns the promise; Instrument Operations governs command/capture effects; approvals remain `proposed` |

## 2. Evidence layers

| Layer | What it can show | What it cannot prove alone | Artifact location |
| --- | --- | --- | --- |
| State-model or unit | Candidate transitions reject prohibited moves | Instrument or scientific outcome | `planned`; not assigned |
| Deterministic replay | Same history yields declared internal state | External capture effect | `planned`; not assigned |
| Controlled-time | Window, deadline, and late-decision transitions | Production timing or scientific acceptability | `planned`; not assigned |
| Failure injection | Response at named loss/ack boundaries | Exhaustive failure coverage | `planned`; not assigned |
| Integration | Candidate identity/query links across components | Operational validity | `planned`; not assigned |
| End-to-end scenario | One frozen campaign follows a proposed disposition | General reliability, usability, or scientific value | `planned`; not assigned |
| Operational observation | Future traces might expose ownership/waiting | Correct campaign outcome alone | `planned`; no deployment assumed |
| Business reconciliation | Workflow/instrument/raw-store records can be compared | Universal absence of unseen effects | `planned`; not assigned |

## 3. Time scenarios

| Scenario | Time manipulation | Expected state and owner | Deadline behavior | Required evidence | Result |
| --- | --- | --- | --- | --- | --- |
| Dependency responds just before timeout | Return instrument receipt one tick before caller deadline | `OBSERVATION_REQUESTED`; Program Operations owns promise | Preserve remaining window/campaign budget | Clock, command, receipt, state trace | `planned` / `unrun` |
| Dependency succeeds after caller timeout | Begin capture after caller stops waiting | `OBSERVATION_OUTCOME_UNKNOWN` until query | Timeout consumes wait budget, not campaign promise | Instrument/raw-store/query trace | `planned` / `unrun` |
| Human decision arrives before escalation | Decide target change before threshold | `EXCEPTION_REVIEW` advances under current authority | Cancel pending escalation once | Task/claim/authority/time trace | `planned` / `unrun` |
| Human decision arrives after escalation | Return original decision after reassignment | Late decision superseded; current owner unchanged | No deadline reset | Decision, lease, transition guard | `planned` / `unrun` |
| Business calendar crosses weekend/holiday | Advance across program closure interval | State stays owned under defined policy | Campaign clock behavior follows frozen policy | Calendar/version trace | `planned` / `unrun` |
| Daylight-saving or time-zone boundary | Change local display while UTC advances | No repeated/skipped trigger | UTC window remains authoritative | UTC/local rendering and transition times | `planned` / `unrun` |
| Delayed trigger is missed during outage | Stop scheduler across window-preparation trigger | Detect overdue work and assign once | Remaining window visible | Scheduler/recovery/owner trace | `planned` / `unrun` |
| Recurring trigger overlaps prior run | Start two campaign-aging sweeps | One escalation per task identity | No multiplied deadline or command | Trigger and transition identities | `planned` / `unrun` |
| Policy/version changes while waiting | Change calibration/authority policy during review | Recheck; quarantine incompatible campaign | No automatic clock reset | Old/new policy, state/owner trace | `planned` / `unrun` |

## 4. Failure and repetition scenarios

| Injection point | Failure or mutation | Expected retry/stop behavior | Business invariant | Compensation/recovery | Evidence | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Before checkpoint | Worker loss | Resume only from durable state; do not infer command dispatch | Campaign remains owned | Reconstruct or quarantine | History/queue/state trace | `planned` / `unrun` |
| After checkpoint, before effect | Worker loss | Repeat only when command known absent and authorized | No prohibited extra observation | Governed retry or quarantine | Checkpoint/instrument absence evidence | `planned` / `unrun` |
| After effect, before acknowledgement | Ambiguous timeout | Stop blind command; query instrument/raw store | Timeout is not capture outcome | `AVO-STATE-01`, then `AVO-COMP-01` if repair eligible | Attempt/effect/query ledgers | `planned` / `unrun` |
| Message delivery | Duplicate | Coalesce by transition identity | No contradictory disposition notice | Reconcile/correct notice | Delivery/transition ledger | `planned` / `unrun` |
| Dependency | Unavailable or throttled | Consume finite policy; transfer on exhaustion | Campaign deadline survives technical exhaustion | Manual resolution or governed non-execution | Attempts/budgets/owner | `planned` / `unrun` |
| Parallel branch | Partial success | Do not close while manifest or command evidence unresolved | Terminal package needs required provenance | Reconcile branch | Branch/convergence record | `planned` / `unrun` |
| Human task | Unassigned or abandoned | Expire claim; recheck and reassign or stop | Queue is not owner | `AVO-HUMAN-01` escalation | Offer/claim/lease trace | `planned` / `unrun` |
| Compensation | Transient then terminal replacement failure | Finite attempts; transfer responsibility | Repair is a new promise | Record residue/non-execution disposition | Replacement attempts/authority | `planned` / `unrun` |
| Durable state | Incompatible or poisoned | Quarantine; no speculative replay | Proposal meaning stays reconstructable | Authorized repair/migration | Version/history/conflict bundle | `planned` / `unrun` |
| Migration | Interrupted midway | Detect cohort and resume/reverse only by plan | No campaign loses promise/owner | Version-plan recovery | Migration identity/state comparison | `planned` / `unrun` |
| Retry cohort, no jitter | Correlated contention baseline | Apply the frozen no-jitter policy without changing other inputs | Preserve finite budgets and the campaign promise | Stop or transfer on declared exhaustion | Attempt-time distribution, instrument load, and budget trace | `planned` / `unrun` |
| Retry cohort, selected jitter | Paired correlated-load challenge | Apply only the selected jitter change under the same fixture | Preserve finite budgets and the campaign promise | Stop or transfer on declared exhaustion | Comparable attempt-time, load, and deadline trace | `planned` / `unrun` |
| Authority or policy | Permission changes between attempts | Recheck before another command; stop on absent authority | No instrument effect under stale permission | Reconcile or transfer to current authority | Old/new policy, actor scope, attempts, and state transition | `planned` / `unrun` |

## 5. Outcome assertions

- Every open campaign has a visible business owner.
- Every instance is progressing, waiting under policy, escalated, or
  quarantined with a recovery owner.
- No timeout or retry creates an unsupported observation/capture claim.
- Every terminal disposition links proposal, authority, command/capture
  evidence or explicit absence evidence, and rationale.
- Replacement actions preserve original history and changing-condition residue.
- Deadline behavior uses the frozen UTC schedule and policy version.
- Definition, proposal, calibration, authority, and transition versions remain
  reconstructable.
- The planned evidence lifecycle still requires owner review; no privacy or
  scientific-validity conclusion is implied.

## 6. Negative and boundary results

| Expected claim | Counterexample or failed test to retain | Scope affected | Planned decision | Owner | Result |
| --- | --- | --- | --- | --- | --- |
| Query-before-repeat prevents extra command | Instrument cannot correlate command to capture | Retry/compensation | Stop commands; redesign contract or manual reconcile | Instrument Operations | `planned` / `unrun` |
| Escalation assigns a reviewer | Alert fires but no eligible reviewer claims | Human work | Preserve evidence; repair assignment or stop | Platform Operations | `planned` / `unrun` |
| Migration preserves meaning | Old capture state maps to false non-execution | Migration | Halt migration and retain old cohort | Change owner | `planned` / `unrun` |

## 7. Exit gate

| Gate | Required evidence | Disposition | Evidence state | Approver |
| --- | --- | --- | --- | --- |
| Time semantics verified | Frozen UTC/window/deadline traces | `blocked` | `planned` / `unrun` | Program Operations |
| Duplicate and ambiguity outcomes verified | Command/capture/reconciliation bundle | `blocked` | `planned` / `unrun` | Instrument Operations |
| Compensation and residual harm verified | Replacement failures and residue decision | `blocked` | `planned` / `unrun` | Program Operations |
| Human delay and escalation verified | Queue/claim/late-decision fixtures | `blocked` | `planned` / `unrun` | Program Operations |
| Version and recovery behavior verified | Cohort/interrupted-migration fixtures | `blocked` | `planned` / `unrun` | Change owner |
| Business reconciliation completed | Independent terminal reconstruction | `blocked` | `planned` / `unrun` | Program Operations |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Planned cases | Decision IDs | Applicable blank worksheet | State |
| --- | --- | --- | --- |
| Checkpoint, replay, lost acknowledgement | `AVO-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md) and chapter in the book's source record | `scenario`; `unrun` |
| Timeout, backoff, budgets, exhaustion | `AVO-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md) and chapter in the book's source record | `scenario`; `unrun` |
| Replacement ambiguity and residue | `AVO-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md) and chapter in the book's source record | `scenario`; `unrun` |
| Claim expiry, authority mutation, late decision | `AVO-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md) and chapter in the book's source record | `scenario`; `unrun` |

This completed plan demonstrates how to place challenges and evidence needs.
The linked blanks are not populated source records. No challenge ran, and the
scenario workflow is not validated.
