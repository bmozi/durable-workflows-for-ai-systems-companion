# Retry, Timeout, Backoff, and Exhaustion Safety Record

**Use boundary:** Illustrative field tool; not certification or proof of
production fitness

**Primary chapter:** Chapter 6, *Retries, Timeouts, and Backoff*

**Research basis:** WF-R006 is `sourced` in the research register; the
dated research note cited in the book
supports the bounded propositions used here. Named experiments and applications
remain `unrun`; completing this asset changes no evidence state.

**Validation state:** `unrun`. No retry classification, deadline propagation,
backoff, jitter, correlated-failure, capacity, cost, or ambiguous-effect result
is recorded here.

**Nonclaim:** This record recommends no universal retry count, delay, multiplier,
cap, jitter distribution, or failure classification. Completing it does not
prove an operation is idempotent, a timed-out effect did not occur, or a retry
policy is safe in production.

## What this tool helps you decide

A retry is another attempt. A timeout says that one participant stopped waiting.
Backoff changes when another attempt begins. Jitter changes how many callers line
up at the same moment. None of those controls decides whether repeating the
business operation is allowed.

Use this record for one operation and one failure boundary at a time:

1. identify the operation and every attempt;
2. state what is known about the prior effect;
3. classify failures without confusing transport status with business meaning;
4. set finite attempt, time, capacity, and cost budgets;
5. name the exhaustion transition and next owner; and
6. plan tests that can disprove the policy.

Use the governed evidence vocabulary. Every planned case remains `unrun` until
inputs, topology, failure injection, results, and limits are retained.

## 1. Operation and responsibility

| Field | Decision |
| --- | --- |
| Decision record ID | |
| Workflow and definition version | |
| Open business promise | |
| Business-promise owner | |
| Operation and business meaning | |
| Operation authority | |
| External system and authoritative effect record | |
| Stable business-operation identity | |
| Attempt identity and correlation rule | |
| Permitted number of business effects | |
| Prohibited duplicate or missing outcome | |
| Business deadline and calendar | |
| Recovery or reconciliation owner | |

## 2. Attempt model

| Dimension | Decision | Evidence or source | Unknown | Reversal trigger |
| --- | --- | --- | --- | --- |
| First-attempt knowledge: absent, present, or unknown | | | | |
| Retry eligibility | | | | |
| Repeat-safety mechanism | | | | |
| Query-before-retry rule | | | | |
| Attempt identity | | | | |
| Idempotency-key lifetime and scope | | | | |
| Concurrency or compare-and-set condition | | | | |
| Authorization recheck per attempt | | | | |
| Deadline remaining per attempt | | | | |
| Evidence retained per attempt | | | | |

Do not write “idempotent” without stating the exact effect, identity scope,
concurrency rule, retention lifetime, and failure that the mechanism does not
cover.

## 3. Failure classification

| Failure or observation | What it establishes | What remains unknown | Retry eligible? | Required check before action | Next owner if not retried |
| --- | --- | --- | --- | --- | --- |
| Connection not established | | | yes / no / conditional / unknown | | |
| Connection lost after request transmission | | | yes / no / conditional / unknown | | |
| Client deadline expired | Caller stopped waiting | Server work or external effect may continue | conditional / unknown | | |
| Dependency asks caller to wait | Requested delay only | Authority, safety, and first-attempt outcome | conditional / unknown | | |
| Explicit policy or authorization rejection | | | | | |
| Malformed input or invariant violation | | | | | |
| Capacity or quota rejection | | | | | |
| Dependency reports permanent failure | | | | | |
| Acknowledgement lost after effect | | Effect may be present | conditional / unknown | Query or reconcile | |
| Evidence sources disagree | | | no until governed decision | | |

A “retryable” status is transport or product evidence. It is not permission to
repeat a consequential business effect.

## 4. Time, backoff, jitter, and budgets

| Control | Scope | Proposed value or rule | Evidence supporting it | Budget consumed | Owner | State |
| --- | --- | --- | --- | --- | --- | --- |
| Per-attempt timeout | | | | | | `proposed` |
| End-to-end technical deadline | | | | | | `proposed` |
| Business deadline | | | | | | `proposed` |
| Initial backoff | | | | | | `proposed` |
| Backoff growth and cap | | | | | | `proposed` |
| Jitter distribution | | | | | | `proposed` |
| Maximum attempts | | | | | | `proposed` |
| Maximum elapsed retry time | | | | | | `proposed` |
| Capacity or concurrency budget | | | | | | `proposed` |
| Cost, quota, or action budget | | | | | | `proposed` |

### Deadline propagation

| Hop | Budget received | Elapsed time | Budget forwarded | Cancellation cooperation | Work that may outlive caller | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

State whose clock each timeout governs. A client deadline, worker timeout,
external-provider timeout, human deadline, and business deadline may expire at
different times.

## 5. Exhaustion transition

| Budget or condition exhausted | State entered | Further attempts allowed? | Required next action | New owner | Escalation deadline | Closure or recovery evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Attempt count | | | | | | |
| Elapsed retry time | | | | | | |
| Business deadline | | | | | | |
| Cost or quota | | | | | | |
| Capacity or load-shedding threshold | | | | | | |
| Authority or policy becomes invalid | | | | | | |
| Outcome remains ambiguous | | no blind retry | Query / reconcile / compensate / human decision / quarantine / stop | | | |

Exhausting attempts stops one mechanism. It does not close the business promise
unless an authorized terminal outcome and its evidence say so.

## 6. Negative and boundary cases

Challenge the policy when:

- an HTTP method is nominally idempotent but triggers notification, billing,
  metering, or another non-idempotent side effect;
- the dependency returns a retry hint but the first effect is unknown;
- many instances start together and an unjittered policy synchronizes them;
- jitter spreads requests but causes one instance to miss its business deadline;
- an unlimited-attempt default consumes a finite cost, quota, or action budget;
- the client cancels while server or downstream work continues;
- the failure classifier treats policy, malformed input, or invariant failure as
  transient;
- an idempotency record expires while the workflow can still retry;
- authorization changes between attempts; or
- the retry eventually succeeds after creating a prohibited duplicate effect.

## 7. Planned failure and load challenges

| Challenge | Frozen input or topology | Expected safe response | Business invariant | Evidence required | Result |
| --- | --- | --- | --- | --- | --- |
| Identical callers use the same unjittered backoff | | | | Attempt-time distribution and dependency load | `unrun` |
| Candidate jitter policy under the same fixture | | | | Comparable retained trace | `unrun` |
| Deadline expires after effect commit, before response | | Query before retry | | External receipt and attempt ledger | `unrun` |
| Downstream services consume the propagated budget | | | | Per-hop clock trace | `unrun` |
| Failure class changes from transient to permanent | | Stop or transfer responsibility | | Classification and transition evidence | `unrun` |
| Attempt budget exhausts before business deadline | | | | Named next owner and state | `unrun` |
| Business deadline exhausts while attempts remain | | Stop or governed exception | | Deadline and authority record | `unrun` |
| Authorization changes during backoff | | Recheck before attempt | | Policy version and rejection evidence | `unrun` |

Preserve a negative result in which no retry or a simpler bounded mechanism is
the correct choice.

## 8. AI implementation brief boundary

### AI may draft candidate machinery from completed decisions

- attempt and operation identifiers;
- timeout, cancellation, backoff, jitter, and budget configuration;
- failure classifiers with explicit unknown outcomes;
- query-before-retry and reconciliation paths;
- exhaustion transitions and operator views; and
- deterministic test cases for the frozen policy.

### AI must not invent

- whether the operation is safe to repeat;
- the meaning of a failure or timeout;
- idempotency scope, lifetime, or authority;
- retry counts, delay values, jitter distribution, or capacity limits;
- permission to exceed a business deadline, quota, or cost budget;
- authorization for another attempt; or
- a successful outcome when only execution success is known.

### Required generation stop conditions

Stop and request a human decision when first-attempt effect state is unknown,
repeat safety is unspecified, no finite budget exists, deadline ownership is
unclear, authorization cannot be rechecked, evidence sources disagree, or the
exhaustion transition lacks a named owner.

No claim is made here about AI-generated artifact speed, quality, reliability,
or benefit.

## 9. Evidence gate

| Claim to challenge | Supporting evidence required | Disproving or boundary evidence | Owner | State |
| --- | --- | --- | --- | --- |
| Every attempt is uniquely attributable | Attempt ledger correlated to one operation | Missing, reused, or ambiguous attempt identity | | `planned` / `unrun` |
| Unknown outcomes do not trigger blind retry | Lost-acknowledgement and timeout traces | Repetition before query or reconciliation | | `planned` / `unrun` |
| Retry traffic respects finite budgets | Controlled load and clock results | Budget overrun, synchronized burst, or deadline theft | | `planned` / `unrun` |
| Exhaustion preserves responsibility | State and owner reconstruction | Ownerless wait or false terminal failure | | `planned` / `unrun` |
| No prohibited duplicate business effect occurs | External effect ledger and reconciliation | Duplicate, missing, or unexplained effect | | `planned` / `unrun` |

## 10. Constructed Northbridge application

**Continuity mode:** Independent constructed review fixture; not continuity
evidence.

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
row is constructed design material, not an incident, observed failure, or
experiment result.

| Operation | First-attempt knowledge | Retry rule | Budgets | Exhaustion response | Owner | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Request one authorized finance credit for a dispute | `unknown` after the credit request may have committed and its acknowledgement is lost | Do not retry blindly; query by stable operation identity or reconcile. Another attempt requires current authority and proven repeat safety. | Exact attempts, elapsed time, capacity, and cost remain `unknown`; they must fit inside the constructed ten-business-day promise. | Enter governed effect reconciliation; escalation does not relabel ambiguity as failure or completion. | Partner Operations retains the partner promise; Finance reconciliation owns effect confirmation. | `constructed`; policy test `unrun` |

The row does not prove that finance supports a stable query or idempotency
contract, that another attempt is safe, or that the proposed owners have
approved this design.

## 11. Decision and reversal record

| Decision | Reason | Evidence used | Unknown or residual risk | Owner | Revisit or reversal trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | `proposed` |

Transfer planned time, load, and ambiguity cases into the existing
[Time-and-Failure Test Plan](time-and-failure-test-plan.md). Transfer partial
effect responses into the existing
[Compensation-and-Failure Matrix](compensation-and-failure-matrix.md). A planned
transfer remains `unrun` until its own evidence is retained.
