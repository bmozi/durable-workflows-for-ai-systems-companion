# Northbridge Compensation-and-Failure Matrix

**Example state:** `constructed`

**Validation state:** `unrun`

**Continuity:** Constructed sequence `NB-DURABLE-01`; decision
`NB-COMP-01`

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
completed example demonstrates use of the
[blank matrix](../compensation-and-failure-matrix.md). It is not a finding that
a credit, duplicate, repair, loss, or approval occurred. Completion does not
validate compensation or establish any usability, technical, business,
privacy, accessibility, or safety result.

## Workflow context

| Field | Constructed decision |
| --- | --- |
| Workflow and version | `NB-DISPUTE-CREDIT/v0-proposed` |
| Business promise | Reach an authorized partner-dispute disposition while preserving the meaning and evidence of every finance effect |
| Business owner | Partner Operations |
| Compensation authority | Finance authority for any offset; Partner Operations for partner-facing disposition; exact policy remains `unknown` |
| Maximum recovery window | `unknown`; must be shorter than or explicitly governed against the constructed ten-business-day promise |
| Residual harm owner | Partner Operations for the open partner obligation; Finance for ledger discrepancy |

## Effect classification

| Step or external effect | Business effect | Confirmation evidence | Response eligibility or inverse preconditions | Conditions or deadline | Duplicate risk | Ambiguous-outcome probe | Compensation, semantic undo, or reconciliation | Authority | Residue or residual harm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Record exception approval | Permits one scoped finance operation | Actor, delegation, amount/purpose scope, policy version, rationale | Correction is conditional on a current authorized path; original decision history remains | Authority current at operation time | Conflicting or late decisions | Query decision identity and supersession state | Governed correction or appeal; semantic undo is not assumed | Authorized exception role | Review delay; original decision remains visible |
| Issue dispute credit | Changes partner finance position | Finance ledger/receipt by stable effect identity | `unknown` until finance confirms the effect and current offset or inverse eligibility | Confirm effect and current response eligibility before deadline | A blind repeat may create a second credit | Query finance by operation/effect identity | Reconcile first; consider authorized compensation or semantic undo only if its distinct preconditions hold | Finance service plus current business authority | Timing, fees, notice, accounting entries, partner observation |
| Send partner resolution notice | Communicates a disposition | Message identity, content version, delivery attempt | Semantic undo is ineligible because the notice cannot be unsent; corrective notice eligibility remains policy-bound | Only after supported disposition | Duplicate or contradictory message | Query message attempt and content history | Corrective notice and reconciliation, not deletion | Partner Operations communication policy | Confusion, delay, trust cost |
| Execute offsetting finance action | Creates a new finance effect | Separate compensation identity and ledger receipt | Conditional on confirmed duplicate, current authority, and verified inverse or compensation preconditions | Confirm duplicate and inverse preconditions; current authority | Duplicate offset | Query compensation identity before repeat | Reconcile or escalate; never hide original credits | Finance authority | Residue may remain even when ledger balances |

## Failure-response decisions

| Failure or ambiguity | Known state | Unknown state | Safe immediate action | Retry rule | Stop condition | Compensation trigger | Escalation owner | Required evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Credit acknowledgement lost | Request was sent | Credit may be absent or present | Enter `CREDIT_OUTCOME_UNKNOWN`; query finance | No blind repeat | Query unavailable or evidence conflicts | None until effect is confirmed | Finance reconciliation | Operation/attempt ledger and finance query |
| Two credits confirmed | Two ledger effects exist | Offset eligibility and residue | Freeze new credit attempts; evaluate `NB-COMP-01` | Offset has separate finite attempt policy | Authority stale or inverse condition fails | Current policy authorizes one offset | Finance authority; Partner Operations retains promise | Both effects, authority, eligibility, partner obligation |
| Offset acknowledgement lost | Offset request was sent | Offset may be absent or present | Query compensation identity | No blind repeat | Evidence conflict or budget exhaustion | Already open; remains an owned promise | Finance reconciliation | Compensation attempt and ledger evidence |
| Corrective notice cannot be delivered | Notice attempt exists | Partner receipt | Preserve disposition; govern communication recovery | Per communication policy, still `unknown` | Communication budget/deadline exhausted | Not a finance compensation trigger | Partner Operations | Attempt ledger and final communication disposition |
| No eligible offset exists | Original effects remain | Acceptable residue | Reconcile and seek governed loss/notice decision | None | No permitted repair | Not applicable | Partner Operations and Finance authority | Policy, effects, notice/appeal decision |

## Response vocabulary

| Response | Constructed use |
| --- | --- |
| Retry | Repeat only a proven-safe attempt under stable identity and current authority |
| Compensate | Create a separately authorized offsetting finance action; do not erase original credits |
| Semantic undo | Assert a domain inverse only after exact current inverse conditions are verified; preserve the original effect and residue |
| Reconcile | Compare the workflow attempt ledger with authoritative finance effects |
| Escalate | Transfer a bounded decision and context to named Finance/Partner Operations owners |
| Accept loss | Record remaining residue only under named authority and policy |
| Stop | Prevent further finance effects while evidence or authority is unresolved |
| Manual resolution | Create owned human work with deadline, scope, and audit record |

## Compensation invariants

- Original finance effects and their evidence remain immutable.
- Every offset has its own operation, attempt, authority, and outcome identity.
- Repeating an offset cannot be permitted without known first-effect state.
- A failed or ambiguous offset remains owned by Finance reconciliation while
  Partner Operations retains the partner promise.
- A balanced ledger is not by itself evidence that partner-facing residue or
  beneficiary obligations ended.

## Failure tests

| Planned challenge | Expected governed response | Required artifact | Result |
| --- | --- | --- | --- |
| Failure before credit effect | Preserve absent/present distinction; query if transmission occurred | Attempt/effect trace | `planned` / `unrun` |
| Credit commits; acknowledgement is lost | Enter unknown and query before repeat | Lost-ack trace and finance query | `planned` / `unrun` |
| Duplicate credit request | Prevent or reveal second effect under stable identity | Attempt and effect ledgers | `planned` / `unrun` |
| Offset commits; acknowledgement is lost | Query compensation identity before repeat | Compensation ledger | `planned` / `unrun` |
| Offset fails transiently then terminally | Exhaust finite policy and transfer responsibility | Failure/exhaustion record | `planned` / `unrun` |
| Compensation window expires | Stop automatic attempts; obtain governed disposition | Clock and authority record | `planned` / `unrun` |
| Policy or authority changes | Recheck eligibility; reject stale approval | Policy mutation trace | `planned` / `unrun` |
| Evidence sources disagree | Quarantine and reconcile | Conflict bundle and decision | `planned` / `unrun` |

## Decision record

| Decision | Rationale | Evidence | Remaining uncertainty | Owner | Revisit trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| Reconcile any unknown credit before considering another effect | Timeout does not establish the finance outcome | Constructed `NB-STATE-01` and `NB-RETRY-01` reasoning | Query contract and policy approval remain unknown | Finance reconciliation; Partner Operations keeps promise | Finance cannot query by stable identity | `constructed`; test `unrun` |
| Treat an eligible offset as semantic repair, not rollback | Original effects and residue survive | Constructed response classification | Eligibility, limits, fees, notice, and appeal remain unknown | Finance authority | Policy or effect evidence changes | `constructed`; eligibility `unrun` |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Matrix field | Decision ID | Applicable blank worksheet and chapter | State |
| --- | --- | --- | --- |
| Credit effect confirmation and ambiguity probe | `NB-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md); Chapter 5 in the book's source record | `constructed`; experiment `unrun` |
| Query-before-repeat and finite attempts | `NB-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md); Chapter 6 in the book's source record | `constructed`; policy test `unrun` |
| Offset eligibility, identity, residue, and failure owner | `NB-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md); Chapter 7 in the book's source record | `constructed`; tests `unrun` |
| Authority change and manual-resolution owner | `NB-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md); Chapter 8 in the book's source record | `constructed`; authority test `unrun` |

This trace identifies where future contested reasoning could be recorded. It is
not evidence that compensation is eligible, possible, or effective.
