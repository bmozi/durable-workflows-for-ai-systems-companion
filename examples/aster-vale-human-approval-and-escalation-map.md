# Aster Vale Human Approval-and-Escalation Map

**Example state:** `scenario`

**Validation state:** `unrun`

**Scenario identity:** `AVO-CAMPAIGN-01`; decision `AVO-HUMAN-01`

**Disclosure:** Aster Vale Observatory is an unrelated fictional scenario. This
completed example demonstrates use of the
[blank map](../human-approval-and-escalation-map.md). It does not show that a
reviewer, queue, scientific decision, privacy control, or escalation worked.
Completion establishes no usability, technical, scientific, business,
privacy, accessibility, or safety result.

## 1. Decision definition

| Field | Scenario decision |
| --- | --- |
| Human decision or task | Decide whether a proposed target or observing-window change may proceed, must be rejected, needs more information, or must be escalated |
| Why automation may not decide | The fictional policy delegates contextual exception judgment and authority to a duty astronomer; exact criteria remain `unknown` |
| Business-promise owner | Program Operations |
| Authorized role or individual | A currently eligible duty astronomer who has claimed the task and passes conflict/scope checks |
| Subject, tenant, amount, geography, or policy scope | Proposal, instrument, target class, window, program, policy version, competence, delegation, and conflict |
| Required context and evidence | Approved proposal version, requested change, reason, remaining window, instrument status reference, and relevant policy criteria |
| Allowed decisions | Approve scoped change; reject; request information; abstain; escalate |
| Prohibited decisions | Change unrelated proposal terms; command the instrument directly; infer missing evidence; accept a late superseded task silently |
| Required rationale | Structured policy criterion plus a concise reason tied to the presented evidence version |
| Effect of no decision | Preserve current approved plan if still possible; otherwise stop new command and enter governed reschedule/manual resolution |

## 2. Queue and workload

| Field | Scenario decision |
| --- | --- |
| Assignment mechanism | Offer to an eligible duty population, then claim as actual owner with lease |
| Offered population and eligibility rule | Duty astronomers currently eligible for the proposal, instrument, target class, program, competence, policy, delegation, and conflict checks; the approved population remains `unknown` |
| Actual owner | The eligible duty astronomer recorded as claimant for this task; no actual person is represented by this scenario |
| Claim or lease expiry | Expiring claim required; duration and renewal rule remain `unknown` pending an authorized scenario policy |
| Named queue owner | Observatory Platform Operations owns queue health; Program Operations keeps the campaign promise |
| Capacity assumption and evidence | One on-duty eligible reviewer is proposed; capacity and evidence remain `unknown` |
| Prioritization rule | Remaining observing-window time, then campaign deadline; overrides require reason |
| Duplicate-task handling | One active exception identity per campaign/change; duplicate offers link to it |
| Reassignment rule | Recheck competence, scope, conflict, delegation, and remaining window |
| Late or superseded decision handling | Retain as superseded; do not change an executed command or terminal disposition without a new authorized correction |
| Abandonment detection | Claim lease expires or owner releases; orphan signal names recovery owner |
| Privacy/classification constraints | Present only proposal/change data needed for the decision; classification, identity, access, retention, and deletion rules remain `unknown` |
| Operator support and recovery path | Platform Operations may release, re-offer, or quarantine; it may not approve the scientific exception |

## 3. Time and escalation

The values below are fictional scenario fixtures in UTC, not observed staffing
or approved operational thresholds.

| Stage | Maximum wait | Reminder or signal | Escalation target | Authority gained or changed | Context transferred | Workflow action |
| --- | --- | --- | --- | --- | --- | --- |
| Initial assignment | Thirty minutes | Unclaimed-task signal | Queue owner | None | Change identity, remaining window, eligibility requirements | Re-offer or assign under policy |
| First escalation | One hour total | Claim or review overdue | Program Operations duty owner | May authorize reassignment; no exception authority inferred | Prior owner, evidence versions, remaining time | Recheck and reassign or request information |
| Final escalation | Four hours or one hour before window, whichever is earlier | Decision absent | Named program exception authority | Only documented current authority | Full minimized decision record | Decide, abstain, keep original plan, or enter manual resolution |
| Deadline exhaustion | Observation window can no longer support a governed command | Window-expiry signal | Program Operations | No automatic expansion | State, schedule, command/effect evidence, unknowns | Stop new command; choose reschedule or non-execution disposition |

A late decision is retained as superseded and cannot change an already executed
command or terminal disposition without a new authorized correction.

## 4. Delegation, substitution, and conflict

| Condition | Authorized substitute | Scope and duration | Conflict check | Approval evidence | Revocation path |
| --- | --- | --- | --- | --- | --- |
| Absence | Another eligible duty astronomer | This exception until decision/lease expiry | Proposal participation and organizational conflict | Eligibility/delegation record | Queue owner releases and records reason |
| Capacity overflow | Secondary roster only if current competence/scope checks pass | Declared instrument/target classes for bounded shift | Recheck conflicts and separation | Roster/policy version and allocation | Program Operations disables roster and reassigns |
| Emergency | Named emergency authority if policy explicitly grants it | Narrow stop/change authority and time window | Current conflict checks remain | Emergency policy, actor, start/end, rationale | Automatic expiry and task re-evaluation |
| Organizational change | Newly assigned role after authority update | Only after fresh identity/competence/delegation checks | Former/new role relationships | Change record and current authorization | Administrator revokes stale role mappings |

## 5. Decision evidence

| Required record | Scenario value or rule |
| --- | --- |
| Task/workflow/decision identity | `AVO-CAMPAIGN-01`, stable task ID, `AVO-HUMAN-01` |
| Actor and delegated authority | Actor, represented program, role, competence/scope, delegation source, and expiry |
| Evidence version presented | Approved proposal and exact change bundle references; lifecycle remains `unknown` |
| Decision, rationale, and policy version | Structured outcome, criterion, concise reason, abstention/escalation if used |
| Assigned/viewed/claimed/decided/escalated times | UTC instants plus window/deadline rule |
| Conflicting or superseded decisions | Preserve all; only one current authorized transition may take effect |
| Downstream effect identity/outcome | Link to `AVO-RETRY-01` command and authoritative instrument/capture evidence |
| Appeal/override/correction path | New authorized decision linked to original and any executed effect |

No claim is made that the proposed context is scientifically sufficient,
privacy-complete, accessible, usable, legally sufficient, or appropriately
retained.

## 6. Human-centered failure tests

| Planned challenge | Expected governed response | Evidence needed | Result |
| --- | --- | --- | --- |
| No qualified reviewer available | Stop or preserve original plan; name escalation owner | Eligibility and state/owner trace | `planned` / `unrun` |
| Assigned reviewer loses authority | Expire claim and recheck substitute | Authority mutation | `planned` / `unrun` |
| Workload exceeds assumption | Surface aging; invoke governed overflow or stop | Queue/claim/age trace | `planned` / `unrun` |
| Two reviewers disagree | Preserve both; accept one current authorized transition | Concurrent-decision history | `planned` / `unrun` |
| Late decision arrives after command | Mark superseded; use correction path | Controlled-time/effect trace | `planned` / `unrun` |
| Context missing, stale, or prohibited | Request information, abstain, or stop | Evidence-version/access trace | `planned` / `unrun` |
| Reviewer acts outside scope | Reject transition and escalate | Authorization mutation | `planned` / `unrun` |
| AI recommendation anchors reviewer | Present provenance/limits or remove input; observe only under protocol | Blinded protocol/consent boundary | `planned` / `unrun` |
| Correction follows executed observation | Preserve original and govern new disposition | Decision/command/correction chain | `planned` / `unrun` |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Map field | Decision ID | Applicable blank worksheet and chapter | State |
| --- | --- | --- | --- |
| Command/capture evidence shown to reviewer | `AVO-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md); Chapter 5 in the book's source record | `scenario`; effect test `unrun` |
| Window deadline and exhaustion | `AVO-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md); Chapter 6 in the book's source record | `scenario`; clock test `unrun` |
| Replacement-slot authority and residue | `AVO-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md); Chapter 7 in the book's source record | `scenario`; eligibility `unrun` |
| Eligible population, claim, scope, and late decision | `AVO-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md); Chapter 8 in the book's source record | `scenario`; practitioner test `unrun` |

The map demonstrates field completion only. The linked blanks are not populated
source records, and the example cannot establish that a human decision is
correct, independent, fair, safe, usable, or scientifically valid.
