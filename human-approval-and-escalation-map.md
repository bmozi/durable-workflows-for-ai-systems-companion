# Human Approval-and-Escalation Map

**Use boundary:** Illustrative field tool; not certification or proof of
production fitness

**Validation state:** `unrun`. Completing this map does not prove that a person
is eligible, authorized, independent, informed, accessible, timely, or correct,
or that the business promise can close.

Use the evidence states `constructed`, `scenario`, `planned`, `unrun`,
`observed`, `tested`, `reported`, `sourced`, `bounded`, `inferred`, `proposed`,
and `unknown` exactly. A planned case remains `planned` / `unrun` until its
inputs, execution, result, limits, and artifact location are retained.

Use this map when a workflow waits for human judgment, correction, confirmation,
or exception handling. “Manual step” is not an operational design.

## 1. Decision definition

| Field | Decision |
| --- | --- |
| Human decision or task | |
| Why automation may not decide | |
| Business-promise owner | |
| Authorized role or individual | |
| Subject, tenant, amount, geography, or policy scope | |
| Required context and evidence | |
| Allowed decisions | |
| Prohibited decisions | |
| Required rationale | |
| Effect of no decision | |

## 2. Queue and workload

| Field | Decision |
| --- | --- |
| Assignment mechanism | |
| Offered population and eligibility rule | |
| Actual owner | |
| Claim or lease expiry | |
| Named queue owner | |
| Capacity assumption and evidence | |
| Prioritization rule | |
| Duplicate-task handling | |
| Reassignment rule | |
| Late or superseded decision handling | |
| Abandonment detection | |
| Privacy/classification constraints | |
| Operator support and recovery path | |

## 3. Time and escalation

| Stage | Maximum wait | Reminder or signal | Escalation target | Authority gained or changed | Context transferred | Workflow action |
| --- | --- | --- | --- | --- | --- | --- |
| Initial assignment | | | | | | |
| First escalation | | | | | | |
| Final escalation | | | | | | |
| Deadline exhaustion | | | | | | |

State the business calendar, time zone, holiday rule, and what happens when a
late answer arrives after reassignment or escalation.

## 4. Delegation, substitution, and conflict

| Condition | Authorized substitute | Scope and duration | Conflict check | Approval evidence | Revocation path |
| --- | --- | --- | --- | --- | --- |
| Absence | | | | | |
| Capacity overflow | | | | | |
| Emergency | | | | | |
| Organizational change | | | | | |

## 5. Decision evidence

Capture without exposing prohibited data:

- task and workflow instance identity;
- actor identity and delegated authority;
- evidence version presented;
- decision, rationale, and policy version;
- time assigned, viewed, decided, and escalated;
- conflicting or superseded decisions;
- downstream effect identity and outcome; and
- appeal, override, or correction path.

## 6. Human-centered failure tests

Test:

1. no qualified reviewer is available;
2. the assigned reviewer leaves or loses authority;
3. workload exceeds the assumed capacity;
4. two reviewers answer differently;
5. a late decision arrives after escalation;
6. required context is missing, stale, or prohibited;
7. a reviewer approves outside delegated scope;
8. an agent recommendation anchors or misleads the reviewer; and
9. correction or appeal is required after the effect occurs.

## Review test

At any moment, an operator should be able to answer who owns the task, why it is
waiting, what authority the assignee has, when responsibility moves, what the
workflow will do next, and how the decision can be explained later.
