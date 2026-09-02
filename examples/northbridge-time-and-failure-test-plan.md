# Northbridge Time-and-Failure Test Plan

**Example state:** `constructed`

**Validation state:** `unrun`

**Continuity:** Constructed sequence `NB-DURABLE-01`

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
completed example demonstrates use of the
[blank plan](../time-and-failure-test-plan.md). It is a plan, not a test report.
No case has run, and no artifact exists. Completion does not validate the
workflow or establish any usability, technical, business, privacy,
accessibility, or safety result.

## 1. Test subject

| Field | Constructed decision |
| --- | --- |
| Workflow and definition version | `NB-DISPUTE-CREDIT/v0-proposed` |
| Business promise and invariant | Reach one authorized partner-dispute disposition; never infer finance effect absence from a timeout |
| Test environment and isolation | `planned`; frozen nonproduction fixture, exact topology `unknown` |
| External effects replaced or safely sandboxed | `planned`; finance-effect double plus authoritative query fixture; suitability `unrun` |
| Clock-control mechanism | `planned`; deterministic business-calendar and UTC clock controls |
| State reset and evidence retention | `planned`; fresh instance IDs, immutable attempt/effect/decision bundle and hashes |
| Test owner | Proposed: Service Operations test owner; Partner Operations and Finance review business assertions |
| Business operation identity | `NB-RETRY-01`: one authorized dispute-credit operation for one workflow instance |
| Attempt identity and correlation rule | A unique attempt ID links to `NB-RETRY-01`; exact format and retention remain `unknown` |
| Attempt, elapsed-time, capacity, cost, and action budgets | Finite values are required but remain `unknown`; the fixture must freeze each value before execution |
| Current execution and recovery authority | Service Operations may execute the fixture; Partner Operations owns the promise; Finance authority governs effects and reconciliation; approvals remain `proposed` |

## 2. Evidence layers

| Layer | What it can show | What it cannot prove alone | Artifact location |
| --- | --- | --- | --- |
| State-model or unit | Candidate transitions reject prohibited moves | Runtime recovery or finance outcome | `planned`; not assigned |
| Deterministic replay | Same frozen history yields declared internal state | External credit effect | `planned`; not assigned |
| Controlled-time | Deadline, late-decision, and calendar transitions | Production clock behavior or acceptable business timing | `planned`; not assigned |
| Failure injection | Response at named loss/ack boundaries | Exhaustive failure coverage | `planned`; not assigned |
| Integration | Candidate identity/query contract across components | Production business validity | `planned`; not assigned |
| End-to-end scenario | One frozen fixture preserves the proposed promise path | General reliability or usability | `planned`; not assigned |
| Operational observation | Future deployed traces might expose waiting/ownership | Correct business outcome by itself | `planned`; no deployment assumed |
| Business reconciliation | Finance and workflow records can be compared | Universal absence of unseen effects | `planned`; not assigned |

## 3. Time scenarios

| Scenario | Time manipulation | Expected state and owner | Deadline behavior | Required evidence | Result |
| --- | --- | --- | --- | --- | --- |
| Dependency responds just before timeout | Advance finance response to one tick before caller deadline | `CREDIT_REQUESTED`; Partner Operations owns promise | Preserve remaining ten-day budget | Clock, attempt, response, state trace | `planned` / `unrun` |
| Dependency succeeds after caller timeout | Commit credit after caller stops waiting | `CREDIT_OUTCOME_UNKNOWN` until query; Finance reconciliation confirms | Timeout consumes wait budget, not promise | Finance ledger, lost response, query, state trace | `planned` / `unrun` |
| Human decision arrives before escalation | Decide before constructed first-escalation threshold | `APPROVAL_PENDING` to next authorized state; Partner Operations owns promise | Cancel pending escalation idempotently | Task/claim/authority/time trace | `planned` / `unrun` |
| Human decision arrives after escalation | Deliver original review after reassignment | Late decision retained as superseded; current owner unchanged | No deadline reset | Both decisions, leases, transition guard | `planned` / `unrun` |
| Business calendar crosses weekend/holiday | Advance across a fictional nonbusiness interval | State remains owned; aging uses governed calendar | Business deadline pauses only if policy says so | Calendar version and UTC/business-time trace | `planned` / `unrun` |
| Daylight-saving or time-zone boundary | Shift local representation while UTC clock advances | No duplicated/skipped transition | Deadline derived from approved calendar, not wall-clock guess | Clock inputs and transition times | `planned` / `unrun` |
| Delayed trigger is missed during outage | Stop scheduler across escalation time | Recovery detects overdue task and acts once | Remaining business deadline preserved | Scheduler history, recovery trace, owner | `planned` / `unrun` |
| Recurring trigger overlaps prior run | Start two aging sweeps | One escalation decision per task identity | No multiplied deadline extension | Trigger/decision identities | `planned` / `unrun` |
| Policy/version changes while waiting | Change authority policy during backoff/review | Recheck authority; quarantine if incompatible | No automatic reset | Old/new policy, version, state/owner trace | `planned` / `unrun` |

## 4. Failure and repetition scenarios

| Injection point | Failure or mutation | Expected retry/stop behavior | Business invariant | Compensation/recovery | Evidence | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Before checkpoint | Worker loss | Resume only from durable evidence; do not infer dispatch | Promise remains owned | Query/reconstruct or quarantine | History, queue, state/owner trace | `planned` / `unrun` |
| After checkpoint, before effect | Worker loss | Repeat only if effect known absent and authorized | At most permitted finance effect | Governed retry or quarantine | Checkpoint and finance absence evidence | `planned` / `unrun` |
| After effect, before acknowledgement | Ambiguous timeout | Stop blind retry; enter query/reconciliation | Timeout is not outcome | `NB-STATE-01` then `NB-COMP-01` if duplicate confirmed | Attempt/effect/query ledgers | `planned` / `unrun` |
| Message delivery | Duplicate | Coalesce by stable transition identity | No duplicate state transition or prohibited notice | Reconcile/correct notification | Delivery and transition ledger | `planned` / `unrun` |
| Dependency | Unavailable or throttled | Consume finite policy; stop/transfer on exhaustion | Business deadline survives technical exhaustion | Reconciliation or manual resolution | Attempts, budgets, exhaustion owner | `planned` / `unrun` |
| Parallel branch | Partial success | Do not close while finance/evidence branch unresolved | Terminal outcome needs all required evidence | Reconcile branch and preserve owner | Branch/convergence record | `planned` / `unrun` |
| Human task | Unassigned or abandoned | Expire claim; recheck and reassign or stop | Queue is not owner | `NB-HUMAN-01` escalation | Offer, claim, lease, state trace | `planned` / `unrun` |
| Compensation | Transient then terminal failure | Finite attempts; transfer to named owner | Repair is a new promise | Governed residue/accepted-loss decision | Compensation attempts and authority | `planned` / `unrun` |
| Durable state | Incompatible or poisoned | Quarantine; no speculative replay | Original meaning remains reconstructable | Authorized repair/migration | Version/history/conflict bundle | `planned` / `unrun` |
| Migration | Interrupted midway | Detect cohort and before/after state; resume or reverse only by plan | No instance loses owner or promise | Version plan recovery path | Migration identity and state comparison | `planned` / `unrun` |
| Retry cohort, no jitter | Correlated contention baseline | Apply the frozen no-jitter policy without changing other inputs | Preserve finite budgets and the partner promise | Stop or transfer on declared exhaustion | Attempt-time distribution, dependency load, and budget trace | `planned` / `unrun` |
| Retry cohort, selected jitter | Paired correlated-load challenge | Apply only the selected jitter change under the same fixture | Preserve finite budgets and the partner promise | Stop or transfer on declared exhaustion | Comparable attempt-time, load, and deadline trace | `planned` / `unrun` |
| Authority or policy | Permission changes between attempts | Recheck before another attempt; stop on absent authority | No finance effect under stale permission | Reconcile or transfer to current authority | Old/new policy, actor scope, attempts, and state transition | `planned` / `unrun` |

## 5. Outcome assertions

- The promise has a visible business owner in every open state.
- Every open instance is progressing, waiting under policy, escalated, or
  quarantined with a recovery owner.
- No timeout or retry creates an unsupported finance outcome.
- Every terminal state links current authority, rationale, and effect evidence.
- Compensation preserves original effects and remaining uncertainty.
- Deadline behavior uses the frozen calendar/policy version.
- Definition, policy, and transition history can be reconstructed.
- The test evidence package follows a still-to-be-approved data and credential
  boundary; no privacy claim is made.

## 6. Negative and boundary results

| Expected claim | Counterexample or failed test to retain | Scope affected | Planned decision | Owner | Result |
| --- | --- | --- | --- | --- | --- |
| Query-before-retry prevents duplicate credit | Stable query identity is unavailable | Retry and compensation | Stop finance effects; redesign contract or manual reconcile | Finance reconciliation | `planned` / `unrun` |
| Escalation assigns an owner | Alert fires but nobody claims the task | Human workflow | Preserve ownerless-state evidence; repair assignment model | Service Operations | `planned` / `unrun` |
| Version migration preserves meaning | Old `UNKNOWN` state maps to false `FAILED` | Migration | Halt migration and keep old cohort | Change owner | `planned` / `unrun` |

## 7. Exit gate

| Gate | Required evidence | Disposition | Evidence state | Approver |
| --- | --- | --- | --- | --- |
| Time semantics verified | Frozen clock/calendar traces and boundary cases | `blocked` | `planned` / `unrun` | Partner Operations |
| Duplicate and ambiguity outcomes verified | Attempt/effect/reconciliation bundle | `blocked` | `planned` / `unrun` | Finance authority |
| Compensation and residual harm verified | Compensation failures plus residue decision | `blocked` | `planned` / `unrun` | Finance and Partner Operations |
| Human delay and escalation verified | Queue/claim/late-decision fixtures | `blocked` | `planned` / `unrun` | Partner Operations |
| Version and recovery behavior verified | Cohort and interrupted-migration fixtures | `blocked` | `planned` / `unrun` | Change owner |
| Business reconciliation completed | Independent terminal reconstruction | `blocked` | `planned` / `unrun` | Partner Operations |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Planned cases | Decision IDs | Applicable blank worksheet | State |
| --- | --- | --- | --- |
| Checkpoint, replay, lost acknowledgement | `NB-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md) and chapter in the book's source record | `constructed`; `unrun` |
| Timeout, backoff, finite budgets, exhaustion | `NB-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md) and chapter in the book's source record | `constructed`; `unrun` |
| Duplicate effect, offset ambiguity, residue | `NB-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md) and chapter in the book's source record | `constructed`; `unrun` |
| Claim expiry, authority mutation, late decision | `NB-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md) and chapter in the book's source record | `constructed`; `unrun` |

Filling this plan demonstrates test-design placement. The linked blanks are not
populated source records. This plan provides no execution evidence and no claim
that the workflow or template is valid.
