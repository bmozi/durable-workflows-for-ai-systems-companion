# Northbridge Workflow Version-and-Migration Plan

**Example state:** `constructed`

**Validation state:** `unrun`

**Continuity:** Constructed sequence `NB-DURABLE-01`

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
completed example demonstrates use of the
[blank plan](../workflow-version-and-migration-plan.md). It does not show that
an inventory, migration, replay, rollback, or recovery worked. Completion does
not validate the workflow or establish any usability, technical, business,
privacy, accessibility, or safety result.

## 1. Change identity

| Field | Constructed decision |
| --- | --- |
| Workflow | `NB-DISPUTE-CREDIT` |
| Current and target versions | `v0-proposed` to `v1-proposed` |
| Change owner | Proposed joint owner: Service Operations change lead and Partner Operations business owner |
| Business reason | Make unknown finance outcomes, operation/attempt identities, human-task ownership, and version evidence explicit |
| Changed meaning, policy, code, schema, timing, or dependency | New `CREDIT_OUTCOME_UNKNOWN` state; stable operation/attempt fields; approval claim lease; explicit policy/definition versions; candidate finance query integration |
| Effective date and business calendar | `unknown`; no cutover authorized |
| Reversal deadline | `unknown`; must be chosen before release |
| Approving authorities | Partner Operations for promise/state meaning; Finance for effect/query contract; Service Operations for technical execution; records remain `proposed` |

## 2. Semantic compatibility

| Dimension | Current meaning | Target meaning | Compatible for running work? | Evidence | Decision owner |
| --- | --- | --- | --- | --- | --- |
| Promise and terminal outcomes | Existing promise/terminal mapping not retained in this fixture | Explicit authorized dispositions and owner | `unknown`; do not infer | Versioned state/terminal comparison `planned` / `unrun` | Partner Operations |
| State and transition meaning | Timeout may be represented in a generic failure path | Timeout leads to explicit unknown/reconciliation when effect may exist | No automatic mapping | Cohort/state-history review `planned` / `unrun` | Partner Operations and Service Operations |
| Authority and approval | Assignment/authority fields may be incomplete | Actual owner, scope, delegation, conflict, policy version | `unknown` | Authority mutation fixtures `planned` / `unrun` | Partner Operations |
| Deadlines and escalation | Existing clock semantics `unknown` | Versioned business calendar and evidence-bearing escalation | `unknown` | Controlled-time comparison `planned` / `unrun` | Partner Operations |
| Retry and idempotency | Attempt/operation identity may not be separate | Stable operation plus unique attempts and query-before-repeat | No unless identities can be reconstructed | Ledger reconciliation `planned` / `unrun` | Finance and Service Operations |
| Compensation and recovery | Generic rollback/failure meaning may exist | Reconcile, compensate, manual resolution, or accepted residue remain distinct | No automatic mapping | Response classification `planned` / `unrun` | Finance and Partner Operations |
| Evidence and retention | Existing retained history/lifecycle `unknown` | Versioned decision/effect/migration links; lifecycle still `unknown` | `unknown` | Records/lifecycle review `planned` / `unrun` | Evidence owner `unknown` |

## 3. Instance cohorts

No cohort count has been observed. Every identification rule and treatment below
is `constructed`; discovery remains `planned` / `unrun`.

| Cohort | Identification rule | Count/evidence | Treatment | Reason | Owner | Reversibility | Completion evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not started | No instance identity before cutover | `unknown`; inventory unrun | Start new work on target version only after approval | Avoid unnecessary migration | Service Operations | Stop new starts before effects | Admission/version report |
| Open before changed state | `v0` and no finance request/human claim | `unknown` | Controlled cutover only if state/authority mapping passes | Fewer external effects, but meaning still needs proof | Partner Operations | Return to `v0` before target-only transition if supported | Before/after state and owner |
| Waiting on external party | `v0` requesting partner information | `unknown` | Continue old definition unless timing/policy compatibility is approved | Preserve promise/communication meaning | Partner Operations | Old-version continuation | Terminal/response evidence |
| Waiting on human decision | Active `v0` review task | `unknown` | Continue old or reissue under target with explicit supersession; never duplicate silently | Ownership and late-decision risk | Partner Operations | Reissue may leave residue | Claim/decision/supersession trace |
| Partially effected | Finance request sent or credit effect possible | `unknown` | Quarantine and reconcile before migration | Effect ambiguity cannot be mapped to failure | Finance reconciliation | State repair may be irreversible | Attempt/effect/reconciliation bundle |
| Compensating or recovering | Offset/recovery open | `unknown` | Continue under original recovery plan unless explicit compatible mapping | Repair is its own promise | Finance reconciliation | `unknown` | Compensation identity/outcome |
| Poisoned or incompatible | Missing identity, corrupt history, or unmappable state | `unknown` | Quarantine for governed repair/manual resolution | Speculative migration could change meaning | Named recovery owner | `unknown`; decide per instance | Authorized repair disposition |

## 4. Migration mechanics and authority

| Step | Preconditions | Authorized actor | State/effect change | Idempotency identity | Failure response | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Freeze inventory | No migration started; version queries defined | Service Operations change role | None | Migration run ID | Stop if inventory cannot be reconciled | Frozen cohort report/hash |
| Classify cohort | Source state/history and effect links available | Service Operations plus relevant business/effect owner | Classification only | Instance plus migration run | Quarantine ambiguity | Classification rationale |
| Transform eligible state | Approved field/state mapping and current authority | Migration operator under change approval | Add target fields; do not create finance effect | Instance, source version, target version | Record partial status; resume or reverse only by plan | Before/after state and mapping version |
| Reconcile external effects | Stable finance query and authority | Finance reconciliation | Update evidence link/state, not ledger by inference | Finance operation/effect identity | Quarantine conflicts | Finance query/result bundle |
| Release cohort | Validation gates pass for that cohort | Change owner and business owner | Allow target execution | Cohort release ID | Reblock on negative result | Approval, version, monitor, rollback limits |

## 5. Validation and release

| Gate | Test or evidence | Negative case | Disposition | Evidence state | Approver |
| --- | --- | --- | --- | --- | --- |
| Cohorts completely identified | Frozen inventory/reconciliation | Instance missing version or cohort | `blocked` | `planned` / `unrun` | Change owner |
| Historical meaning preserved | Independent state/terminal reconstruction | `UNKNOWN` becomes false `FAILED` | `blocked` | `planned` / `unrun` | Partner Operations |
| State transformation verified | Before/after schema and transition fixtures | Partial or repeated transform | `blocked` | `planned` / `unrun` | Service Operations |
| External effects reconciled | Finance attempt/effect comparison | Unlinked or contradictory credit | `blocked` | `planned` / `unrun` | Finance authority |
| Interrupted migration recoverable | Fail each mechanics step | Ownerless or double-transformed instance | `blocked` | `planned` / `unrun` | Change owner |
| Monitoring distinguishes versions | Version/cohort dashboards and alerts | Mixed versions appear identical | `blocked` | `planned` / `unrun` | Service Operations |
| Rollback limits understood | Reversal matrix for each cohort | Target-only effect blocks reversal | `blocked` | `planned` / `unrun` | Partner Operations and Finance |
| Business owner accepts residual risk | Named residue/unknown decision | Generic acceptance without scope | `blocked` | `planned` / `unrun` | Partner Operations |

## 6. Recovery and audit

- Detect partial migration through a per-instance migration state linked to the
  frozen run and before/after versions.
- During interruption, source state and external finance evidence remain
  separate authorities; a migration flag cannot establish the finance effect.
- Service Operations may execute repair, resume, or reversal only under the
  relevant business/finance disposition.
- Original workflow, attempt, effect, decision, and migration history remains
  immutable; corrections append.
- Operators distinguish old obligations from migration defects by source
  version, last authorized transition, effect links, cohort, and failure step.
- Halt on incomplete inventory, unmappable meaning, effect conflict, stale
  authority, missing owner, or a failed interruption fixture.

## Final decision record

| Decision | Supported scope | Evidence | Residual uncertainty | Owner | Revisit trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| Do not bulk-migrate partially effected or recovering instances | Constructed `v0` cohorts with possible finance effects | Chapter 5–7 reasoning only; no execution evidence | Counts, runtime semantics, finance query, and repair eligibility unknown | Partner Operations and Finance reconciliation | A frozen cohort experiment supports a narrower treatment | `constructed`; `unrun` |
| Start target-only admissions before considering eligible cutover | Not-started work after approval | Proposed isolation rule | Effective date, controls, and rollback unapproved | Change owner | Admission/version gate fails | `constructed`; `unrun` |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Version-plan field | Decision ID | Applicable blank worksheet | Transfer boundary |
| --- | --- | --- | --- |
| Checkpoint/replay compatibility and unknown effect | `NB-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md) | `constructed`; replay/migration `unrun` |
| Operation/attempt identity and authorization recheck | `NB-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md) | `constructed`; identity reconstruction `unrun` |
| Compensation/recovery cohort and residue | `NB-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md) | `constructed`; eligibility `unrun` |
| Human-task claim, supersession, and policy version | `NB-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md) | `constructed`; late-decision test `unrun` |

The plan demonstrates how proposed decisions can be organized. The linked
blanks are not populated source records. It provides no evidence that migration
is possible, complete, recoverable, or acceptable.
