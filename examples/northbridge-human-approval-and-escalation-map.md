# Northbridge Human Approval-and-Escalation Map

**Example state:** `constructed`

**Validation state:** `unrun`

**Continuity:** Constructed sequence `NB-DURABLE-01`; decision
`NB-HUMAN-01`

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
completed example demonstrates use of the
[blank map](../human-approval-and-escalation-map.md). It does not show that a
queue, authority rule, deadline, privacy control, or decision worked.
Completion establishes no usability, technical, business, privacy,
accessibility, or safety result.

## 1. Decision definition

| Field | Constructed decision |
| --- | --- |
| Human decision or task | Decide whether a dispute credit outside the ordinary automated path may proceed, must be rejected, needs more information, or must be escalated |
| Why automation may not decide | Constructed policy assigns exception judgment and authority to a human role; exact policy remains `unknown` |
| Business-promise owner | Partner Operations |
| Authorized role or individual | A currently eligible credit-exception reviewer who has actually claimed the task |
| Subject, tenant, amount, geography, or policy scope | Partner, dispute, tenant, amount band, purpose, region, policy version, delegation, and conflict must all match; exact limits `unknown` |
| Required context and evidence | Dispute identity, submitted evidence versions, requested amount, applicable policy, finance history relevant to this dispute, and known conflicts |
| Allowed decisions | Approve one scoped operation; reject with reason; request information; abstain; escalate |
| Prohibited decisions | Approve outside scope; infer missing evidence; create a finance effect directly; overwrite a superseding decision |
| Required rationale | Policy clause plus concise evidence-based reason; free text alone is insufficient |
| Effect of no decision | Task ages, transfers through governed escalation, and eventually enters manual resolution; no automatic approval |

## 2. Queue and workload

| Field | Constructed decision |
| --- | --- |
| Assignment mechanism | Offer to eligible population, then atomically claim as actual owner with an expiring lease |
| Offered population and eligibility rule | Reviewers currently eligible for the partner, tenant, amount band, purpose, region, policy version, delegation, and conflict checks; the approved population remains `unknown` |
| Actual owner | The eligible reviewer recorded as claimant for this task; no actual person is represented by this constructed example |
| Claim or lease expiry | Expiring claim required; duration and renewal rule remain `unknown` pending an authorized policy decision |
| Named queue owner | Service Operations owns queue health; Partner Operations retains the business promise |
| Capacity assumption and evidence | Proposed capacity threshold exists but its value and evidence are `unknown`; do not infer from queue creation |
| Prioritization rule | Business-deadline remaining, then received time; exceptions require recorded rationale |
| Duplicate-task handling | One active task identity per workflow/decision; duplicates quarantined and linked |
| Reassignment rule | Recheck eligibility, authority, conflict, and remaining time; preserve prior owner/history |
| Late or superseded decision handling | Retain as superseded; do not advance the workflow unless a current authorized correction path accepts it |
| Abandonment detection | Claim lease expiry or explicit release creates an orphan signal and named recovery action |
| Privacy/classification constraints | Present only the fields required for the decision; classification, access, retention, redaction, and correction rules remain `unknown` pending owner approval |
| Operator support and recovery path | Service Operations may release/reassign/quarantine; it may not approve the credit |

## 3. Time and escalation

The scenario uses a proposed Northbridge business calendar. Time zone, holiday
source, and approved values remain `unknown`; the values below are constructed
review fixtures.

| Stage | Maximum wait | Reminder or signal | Escalation target | Authority gained or changed | Context transferred | Workflow action |
| --- | --- | --- | --- | --- | --- | --- |
| Initial assignment | Four business hours | Unclaimed-task aging signal | Queue owner | None | Task identity, scope, age, required evidence | Re-offer or assign under policy |
| First escalation | One business day total | Claim/decision overdue | Partner Operations duty owner | May authorize reassignment; no credit authority inferred | Prior owner, evidence versions, remaining deadline | Recheck eligibility and reassign or request information |
| Final escalation | Two business days total | Decision still absent | Named exception authority | Only authority explicitly documented by current policy | Full decision record minus prohibited content | Decide, abstain, or enter manual resolution |
| Deadline exhaustion | Constructed ten-business-day promise exhausted | Business-deadline signal | Partner Operations accountable owner | No automatic expansion | Entire state/effect/decision history and unknowns | Stop new effects; choose governed terminal or manual-resolution disposition |

A late decision is recorded as superseded and cannot advance the workflow unless
a currently authorized correction path accepts it.

## 4. Delegation, substitution, and conflict

| Condition | Authorized substitute | Scope and duration | Conflict check | Approval evidence | Revocation path |
| --- | --- | --- | --- | --- | --- |
| Absence | Another eligible reviewer selected by the assignment policy | This task only until decision/lease expiry | Current partner, dispute, and organizational conflict | Eligibility and delegation record | Queue owner releases claim and records reason |
| Capacity overflow | Overflow pool only if independently eligible | Stated amount/purpose/tenant bands for a bounded interval | Re-evaluate separation and conflicts | Policy version and allocation evidence | Partner Operations disables pool and reassigns |
| Emergency | Named duty authority, if policy explicitly grants it | Narrow task and time window; no implied finance-operation authority | Current conflict and scope checks still required | Emergency policy, actor, start/end, rationale | Authority expiry plus task re-evaluation |
| Organizational change | Newly mapped role after policy/identity update | Only after fresh subject and delegation checks | Former and new reporting/conflict relationships | Change record and current authorization | Business administrator revokes stale mappings |

## 5. Decision evidence

| Required record | Constructed value or rule |
| --- | --- |
| Task/workflow/decision identity | `NB-DURABLE-01`, stable task ID, `NB-HUMAN-01` |
| Actor and delegated authority | Actor, subject represented, tenant, role, delegation source, scope, and expiry |
| Evidence version presented | Immutable references to the exact review bundle; content lifecycle remains `unknown` |
| Decision, rationale, and policy version | Structured outcome, cited policy clause, concise reason, abstention/escalation if used |
| Assigned/viewed/claimed/decided/escalated times | UTC instants plus the business-calendar rule used for deadline decisions |
| Conflicting or superseded decisions | Preserve all; only current authorized transition may take effect |
| Downstream effect identity/outcome | Link to `NB-RETRY-01` operation and authoritative finance effect |
| Appeal/override/correction path | New authorized decision linked to the original; never silent overwrite |

No claim is made that this proposed record is privacy-complete, accessible,
usable, legally sufficient, or appropriately retained.

## 6. Human-centered failure tests

| Planned challenge | Expected governed response | Evidence needed | Result |
| --- | --- | --- | --- |
| No qualified reviewer available | Stop automatic progress; assign named escalation owner | Eligibility snapshot and state/owner trace | `planned` / `unrun` |
| Assigned reviewer leaves or loses authority | Expire claim; recheck substitute | Identity/authority mutation | `planned` / `unrun` |
| Workload exceeds assumption | Surface aging; invoke governed overflow or stop | Queue/claim/age trace | `planned` / `unrun` |
| Two reviewers answer differently | Preserve both; accept only current authorized transition | Concurrent decision history | `planned` / `unrun` |
| Late decision arrives | Mark superseded unless correction path accepts | Controlled-time transition trace | `planned` / `unrun` |
| Context is missing, stale, or prohibited | Request information, abstain, or stop | Evidence-version/access trace | `planned` / `unrun` |
| Reviewer acts outside scope | Reject transition and escalate | Authorization mutation | `planned` / `unrun` |
| AI recommendation anchors reviewer | Present provenance/limitations or remove input; observe without claiming effect | Blinded protocol and consent boundary | `planned` / `unrun` |
| Correction or appeal follows effect | Preserve original and execute authorized correction path | Decision/effect/correction chain | `planned` / `unrun` |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Map field | Decision ID | Applicable blank worksheet and chapter | State |
| --- | --- | --- | --- |
| Finance effect shown to reviewer | `NB-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md); [Chapter 5](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch05-durable-execution-and-checkpointing.md) | `constructed`; effect test `unrun` |
| Deadline and exhaustion | `NB-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md); [Chapter 6](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch06-retries-timeouts-and-backoff.md) | `constructed`; clock test `unrun` |
| Authority for offset/accepted residue | `NB-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md); [Chapter 7](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch07-compensation-rather-than-rollback.md) | `constructed`; eligibility `unrun` |
| Offered population, actual owner, lease, scope, late decision | `NB-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md); [Chapter 8](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch08-human-approval-and-escalation.md) | `constructed`; practitioner test `unrun` |

The completed map shows where proposed ownership and authority could be made
explicit. The linked blanks are not populated source records, and the example
does not show that a human decision is correct, fair, independent, safe, or
effective.
