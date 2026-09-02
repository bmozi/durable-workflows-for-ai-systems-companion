# Northbridge Workflow Responsibility-and-Progress Brief

**Example state:** `constructed`

**Validation state:** `unrun`

**Continuity:** Constructed sequence `NB-DURABLE-01`

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
completed example demonstrates use of the
[blank brief](../workflow-responsibility-and-progress-brief.md). It is not an
incident, transcript, approved design, or test result. Completion does not
validate the workflow or establish any usability, technical, business,
privacy, accessibility, or safety result.

## 1. Business promise

| Field | Constructed decision |
| --- | --- |
| Workflow name and version | `NB-DISPUTE-CREDIT/v0-proposed` |
| Initiating business condition | Partner Operations accepts a partner dispute for governed review |
| Promise made | Reach an authorized credit, reasoned rejection, governed cancellation, or named manual-resolution disposition |
| Promise made to whom | The submitting Northbridge partner |
| Business owner until closure | Partner Operations |
| Technical operating owner | Service Operations |
| Maximum acceptable duration | Ten business days, a constructed design value rather than an approved policy |
| Business deadline and calendar | Northbridge business calendar, time zone and holiday source `unknown` |
| Acceptable terminal outcomes | `CREDIT_CONFIRMED`, `REJECTED_WITH_REASON`, `CANCELLED_BY_AUTHORITY`, or `MANUAL_RESOLUTION_ACCEPTED` |
| Unacceptable or prohibited outcomes | Ownerless wait; duplicate credit beyond policy; closure from a timeout alone; approval outside scope |
| Cancellation meaning | Stop new effects, preserve history, and close only with Partner Operations authority and partner-facing disposition |
| Evidence required at closure | Intake identity, decision authority, finance effect evidence when relevant, terminal reason, owner, times, and policy versions |

## 2. Participation and authority

| Participant | Role in promise | May start | May advance | May approve | May compensate | May cancel | May recover or migrate | Evidence required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Partner | Supplies dispute | Submit only | Supply requested information | No | No | Withdraw request, subject to policy | No | Partner and dispute identity |
| Partner Operations | Business-promise owner | Accept intake | Move nonfinancial review states | Within documented nonfinancial scope | No finance effect | Under cancellation policy | Authorize business recovery disposition | Actor, scope, rationale, policy version |
| Service Operations | Technical operator | No | Resume or quarantine under runbook | No credit authority | No | No | Execute approved recovery/migration | Operation identity, runbook authority, trace |
| Finance service | Credit-effect authority | No | Record finance request/outcome | Enforce finance authorization only | Execute authorized offset only | No | Query/reconcile finance effects | Stable effect identity and ledger evidence |
| Authorized exception reviewer | Human decision role | No | Approve, reject, abstain, or request information within scope | Only within current amount/purpose/policy scope | No | No | No | Eligibility, delegation, conflict, rationale |
| Finance reconciliation | Resolves unknown credit outcome | No | Move `CREDIT_OUTCOME_UNKNOWN` after authoritative query | No new credit by inference | Only after separate authorization | No | Reconcile, not silently retry | Query result, ledger identity, discrepancy record |

Authentication does not grant business authority. Tenant, subject, amount,
purpose, policy, and delegation scope remain separate checks.

## 3. Authoritative state and progress

| State | Business meaning | Entry evidence | Owner while here | Allowed next actions | Timing policy | Failure or ambiguity response | Exit evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `RECEIVED` | Promise is open | Accepted intake identity | Partner Operations | Validate or request information | Ten-day clock begins by proposed rule | Assign visible owner or escalate | Validation record |
| `UNDER_REVIEW` | Dispute meaning and authority are being evaluated | Review task identity | Partner Operations | Reject, request information, or prepare credit | Aging signal; exact subdeadline `unknown` | Reassign abandoned work | Decision record |
| `APPROVAL_PENDING` | Credit needs scoped human authority | Offered and claimed task record | Partner Operations keeps promise; actual reviewer owns task | Approve, reject, abstain, request information | Constructed two-business-day task window | Escalate without inventing authority | Signed decision with policy version |
| `CREDIT_REQUESTED` | One authorized credit operation was issued | `NB-RETRY-01` operation and attempt identity | Partner Operations | Await receipt or query | Remaining business deadline | On timeout, do not infer failure | Finance receipt or transition to unknown |
| `CREDIT_OUTCOME_UNKNOWN` | Finance effect may be absent or present | Lost or conflicting acknowledgement | Partner Operations; Finance reconciliation owns confirmation | Query, reconcile, quarantine, or separately authorize another action | Immediate visible escalation; no blind retry | Preserve `unknown` | Authoritative finance evidence and reconciliation record |
| `RESOLUTION_READY` | Candidate terminal disposition has evidence | Decision plus effect/rejection evidence | Partner Operations | Verify closure evidence or reopen | Before business deadline or governed exception | Stop if evidence or authority conflicts | Closure checklist |
| `CLOSED` | Promise ended under one accepted disposition | Authorized terminal record | Partner Operations for post-close correction | Appeal/correction only | Retention policy `unknown` | Preserve original history | Reconstructable terminal package |
| `QUARANTINED` | Progress is intentionally stopped | Stop reason and owner | Named recovery owner; Partner Operations keeps promise | Repair, reconcile, migrate, cancel, or manual resolution | Explicit recovery deadline `unknown` | Escalate if no permitted action | Authorized recovery disposition |

Every nonterminal state must expose the current owner, remaining deadline,
permitted action, and evidence needed to distinguish waiting from lost work.

## 4. Effects and dependencies

| Action or effect | Owning system or party | Invocation path | Outcome evidence | Ambiguous-outcome test | Repeat rule | Compensation or reconciliation |
| --- | --- | --- | --- | --- | --- | --- |
| Accept dispute | Partner Operations | Intake capability | Accepted intake record | Duplicate submission fixture | Coalesce only under defined dispute identity | Reconcile duplicate intake |
| Record approval | Approval service | Human-task transition | Actor, authority, rationale, policy version | Late and conflicting decision fixture | Never overwrite silently | Governed correction/appeal |
| Issue credit | Finance service | Governed finance command | Finance ledger/receipt by stable effect identity | Commit followed by lost acknowledgement | Query before any repeat; current authority required | `NB-COMP-01` reconciliation then eligible offset, if authorized |
| Notify partner | Communication service | Closure action | Delivery attempt and content version | Delivery outcome unknown | Repeat only under communication policy | Corrective notice; original cannot be unsent |

## 5. Invariants

- Exactly one acceptable business outcome means one authorized terminal
  disposition; it does not mean one runtime attempt.
- The workflow must never turn a timeout into proof that a credit failed.
- A terminal state is invalid unless the promise owner, authority, reason, and
  relevant external-effect evidence are reconstructable.
- A repeated attempt is safe only when the first effect is known absent or the
  finance operation's repeat-safety contract is established for the same
  identity and lifetime.
- A compensation is complete only when its separate effect, authority,
  remaining residue, and beneficiary obligations are recorded.
- Human or agent action is valid only when current scoped authority is checked;
  an AI recommendation, if any, is an input rather than authority or evidence.

## 6. Version and recovery obligations

| Question | Constructed decision |
| --- | --- |
| How is definition/version identity recorded? | Definition version on every instance and transition |
| What happens to open instances after change? | Cohort them; do not migrate by default |
| How are incompatible states quarantined? | Enter `QUARANTINED` with old version, reason, owner, and allowed recovery |
| Who may repair, resume, cancel, or migrate? | Service Operations executes only a disposition authorized by the relevant business and finance owners |
| What history must remain immutable? | Intake, attempts, decisions, effects, reconciliations, compensations, and migration transitions |
| What recovery evidence is retained? | Versioned state history, effect queries, authority records, before/after state, and outcome reconciliation |

## 7. Evidence gate

| Claim to challenge | Evidence that could support it | Evidence that could disprove it | Owner | State |
| --- | --- | --- | --- | --- |
| Promise always has an owner | Frozen state/owner reconstruction | Any open state without actionable owner | Partner Operations | `planned` / `unrun` |
| Every open state can progress or escalate | Controlled clock and orphan fixtures | Indefinite wait or alert without transfer | Service Operations | `planned` / `unrun` |
| Repetition cannot create prohibited duplicate credit | Attempt ledger plus finance reconciliation | Duplicate or unexplained credit | Finance reconciliation | `planned` / `unrun` |
| Running instances survive approved change | Cohort and interruption fixtures | Lost meaning, authority, or owner | Change owner | `planned` / `unrun` |
| Closure is reconstructable and authorized | Independent closure reconstruction | Missing authority, effect, or rationale | Partner Operations | `planned` / `unrun` |

## 8. Unknowns and stop conditions

- Unknowns generation must not invent: finance query semantics, amount limits,
  calendar, authority policy, queue capacity, retention, and migration support.
- Human decision required: acceptable terminal policy, retry eligibility,
  compensation eligibility, authority scope, and accepted residue.
- Stop execution when effect state is unknown, authority is stale, evidence
  conflicts, or version compatibility is not established.
- Escalate to Partner Operations and the appropriate effect owner when the
  business deadline or reconciliation deadline is exhausted.
- Redesign if tests expose ownerless states, blind repeats, unreconstructable
  decisions, or migration that changes the original promise.

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Brief field | Decision ID | Applicable blank worksheet and chapter section | Transfer state |
| --- | --- | --- | --- |
| Durable state and effect ambiguity | `NB-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md); Chapter 5, “A checkpoint is a claim” in the book's source record | `constructed`; test `unrun` |
| Repeat rule and attempts | `NB-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md); Chapter 6, “Build the attempt model” in the book's source record | `constructed`; test `unrun` |
| Credit repair and residue | `NB-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md); Chapter 7, “Design compensation” in the book's source record | `constructed`; eligibility `unrun` |
| Approval owner and authority | `NB-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md); Chapter 8, “Identity is not authority” in the book's source record | `constructed`; usability `unrun` |

The trace shows where a future user could record the contested reasoning. It is
not evidence that these decisions were approved or that the workflow works.
