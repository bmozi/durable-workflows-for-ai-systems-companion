# Human Approval, Escalation, Authority, and Evidence Record

**Status:** Working-draft companion tool; not author approved, practitioner
tested, technically validated, or publication ready

**Primary chapter:** Chapter 8, *Human Approval and Escalation*

**Research basis:** WF-R008 is `sourced` in the research register; the
[dated research note](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/research/2026-08-29-part-ii-pattern-foundation-wf-r005-r008.md)
supports the bounded propositions used here. Named experiments and applications
remain `unrun`; completing this asset changes no evidence state.

**Validation state:** `unrun`. No queue, workload, approval, delegation,
substitution, escalation, privacy, accessibility, or usability result is
recorded here.

**Nonclaim:** A human step does not by itself establish safety, fairness,
correctness, accountability, independence, legal sufficiency, or business
authority. Completing this record does not establish compliance with any law,
regulation, accessibility standard, labor policy, or professional duty.

## What this tool helps you decide

“Send it to manual review” is not an operating model. A governable human task
needs a visible queue, an eligible population, an actual owner, bounded
authority, adequate but minimized context, allowed outcomes, deadlines,
substitution rules, escalation, recovery, and evidence.

Use this record for one human decision at a time:

1. name the exact decision and why it needs judgment;
2. distinguish who can see, claim, decide, approve, and remain accountable;
3. make waiting, workload, delegation, and absence visible;
4. define what happens when no qualified decision arrives;
5. minimize and govern the evidence shown and retained; and
6. plan negative cases that challenge assignment and authority.

Use the governed evidence vocabulary. A planned human or usability exercise
remains `unrun` until the session, inputs, consent boundary, observations, and
limitations are retained.

## 1. Decision and promise

| Field | Decision |
| --- | --- |
| Decision record ID | |
| Workflow and definition version | |
| Open business promise | |
| Business-promise owner | |
| Human decision, fact, or transition | |
| Why automation may not decide | |
| Beneficiary or affected party | |
| Allowed outcomes | approve / reject / request information / abstain / escalate / other: |
| Prohibited outcomes | |
| Consequence of no decision | |
| Appeal, correction, or override path | |
| Decision policy and version | |

## 2. Participation and authority map

Authentication, assignment, operation authorization, business authority,
provenance, and accountability belong on separate lines.

| Participant or role | Actor identity | Subject represented | Tenant or domain | Task relation | Decision authority and limit | Delegation source | Accountability retained by | Evidence required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Business-promise owner | | | | accountable owner | | | | |
| Potential reviewer | | | | eligible / offered | | | | |
| Actual task owner | | | | claimed / allocated | | | | |
| Decision approver | | | | authorized decision | | | | |
| Business administrator | | | | recover / reassign | | | | |
| Escalation recipient | | | | notify / reassign / add review / stop | | | | |
| Evidence custodian | | | | retain / redact / correct | | | | |

State amount, purpose, region, policy version, state transition, competence,
conflict, and time limits wherever they narrow authority.

## 3. Queue, offer, claim, and workload

| Field | Decision | Evidence | Unknown | Recovery owner |
| --- | --- | --- | --- | --- |
| Queue and named queue owner | | | | |
| Eligible population and source | | | | |
| Excluded or conflicted population | | | | |
| Offer and prioritization rule | | | | |
| Claim or allocation mechanism | | | | |
| Actual-owner lease or expiry | | | | |
| Capacity assumption | | | | |
| Workload and aging signal | | | | |
| Duplicate-task handling | | | | |
| Abandoned-claim detection | | | | |
| No-eligible-owner response | | | | |
| Operator support and correction path | | | | |

A queue is an access path, not an owner. Work is not assigned merely because an
eligible group can see it.

## 4. Context and decision evidence

| Information or evidence | Why needed | Source and version | Freshness rule | Access rule | Withheld or redacted content | Correction path | Retention or deletion rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

### Minimum decision record

| Field | Required value |
| --- | --- |
| Workflow, task, and decision identity | |
| Actor, subject, tenant, and delegated authority | |
| Eligibility and conflict check | |
| Policy and evidence versions presented | |
| Decision or abstention | |
| Reason appropriate to the domain | |
| Assigned, viewed, claimed, decided, and escalated times | |
| Downstream transition or effect identity | |
| Superseded, conflicting, or late decision handling | |
| Appeal, override, or correction evidence | |

More context can increase privacy exposure, retention obligations, cognitive
load, and anchoring risk. “Show everything” is not an evidence policy.

## 5. Timing and escalation

| Stage | Maximum wait and calendar | Trigger | State change | Next owner | Authority gained, narrowed, or unchanged | Context transferred | Workflow action | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Offered but unclaimed | | | | | | | | |
| Claimed but not started | | | | | | | | |
| In progress | | | | | | | | |
| First escalation | | | notify / reassign / add review / stop | | | | | |
| Final escalation | | | | | | | | |
| Decision deadline exhausted | | | | | | | | |
| Late decision arrives | | | | | | | | |

An alert or reassignment is an action, not resolution. State who now owns the
business promise and what the workflow may do next.

## 6. Delegation, substitution, and separation of duties

| Condition | Transfer type | Proposed recipient | Eligibility recheck | Conflict and separation check | Scope and duration | Authority retained or transferred | Revocation | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Planned absence | delegate / forward / substitute / reassign | | | | | | | |
| Capacity overflow | | | | | | | | |
| Emergency | | | | | | | | |
| Organizational change | | | | | | | | |
| Original owner loses authority | | | | | | | | |

Two separate clicks do not prove independent judgment. Define the organizational
duties that must be separated and how current policy will enforce them across
systems and roles.

## 7. Negative and boundary cases

Challenge the design when:

- no eligible owner exists or every candidate is excluded;
- work remains offered but nobody claims it;
- a claimed task is abandoned, its lease expires, or its owner leaves;
- the queue exceeds the capacity assumption;
- an automatic substitute is absent, conflicted, underqualified, or outside the
  amount, tenant, region, purpose, or policy scope;
- two reviewers return conflicting decisions;
- two nominal approvers share the same disqualifying conflict or upstream error;
- required evidence is missing, stale, excessive, contradictory, or prohibited;
- a reminder or escalation increases alerts without reducing unresolved work;
- a late decision arrives after reassignment or a downstream effect;
- the reviewer is authenticated and assigned but unauthorized for the decision;
- an AI recommendation anchors the reviewer without adequate provenance; or
- appeal or correction is required after the original effect occurred.

Preserve cases in which abstention, request for more information, stop, or
reassignment is the correct response.

## 8. Planned human-work challenges

| Challenge | Expected governed response | Business invariant | Evidence required | Privacy or consent boundary | Result |
| --- | --- | --- | --- | --- | --- |
| No eligible reviewer | | | | | `unrun` |
| Multiple potential owners; nobody claims | | | | | `unrun` |
| Actual owner abandons task | | | | | `unrun` |
| Queue exceeds assumed capacity | | | | | `unrun` |
| Delegation after policy or conflict change | | | | | `unrun` |
| Late decision after escalation | | | | | `unrun` |
| Missing, stale, excessive, or conflicting context | | | | | `unrun` |
| Decision attempted outside authority scope | | | | | `unrun` |
| Evidence must be corrected, redacted, or deleted | | | | | `unrun` |
| Practitioner interprets the blank tool without chapter context | | | No employer secrets or real sensitive cases | Informed participation; collect only task responses | `unrun` |

## 9. AI implementation brief boundary

### AI may draft candidate machinery from completed decisions

- task, queue, claim, release, and reassignment states;
- eligibility and authorization checks;
- reminders, deadlines, and evidence-bearing escalation transitions;
- context views with declared redaction and access rules;
- orphan, conflict, late-decision, and stale-context test cases; and
- operator views for ownership, aging, evidence, and recovery.

### AI must not invent

- why judgment is required or what decision is acceptable;
- a person's eligibility, competence, availability, independence, or authority;
- an amount, purpose, tenant, region, policy, or delegation scope;
- evidence that a reviewer understood the context;
- queue capacity, deadline, substitution, or escalation policy;
- privacy, accessibility, retention, labor, or legal requirements; or
- proof that a human decision is correct, fair, safe, or accountable.

### Required generation stop conditions

Stop and request a human decision when no eligible owner exists, actual
ownership is absent, authority or conflict status is unknown, context is missing
or prohibited, policies disagree, the deadline is exhausted, substitution would
break separation of duties, or evidence and privacy lifecycles are undefined.

No claim is made here about AI-generated artifact speed, quality, reliability,
or benefit.

## 10. Evidence gate

| Claim to challenge | Supporting evidence required | Disproving or boundary evidence | Owner | State |
| --- | --- | --- | --- | --- |
| Every open human task has an actionable owner | Queue, claim, aging, and orphan-recovery reconstruction | Offered or claimed work without a recoverable owner | | `planned` / `unrun` |
| Only currently authorized people can decide | Subject, tenant, delegation, conflict, and policy mutations | Accepted decision outside current scope | | `planned` / `unrun` |
| Escalation changes responsibility visibly | State, owner, authority, and context transfer | Alert sent while ownership remains ambiguous | | `planned` / `unrun` |
| Decision evidence is sufficient and minimized | Independent reconstruction plus privacy/retention review | Missing basis, excessive exposure, or unrecoverable correction | | `planned` / `unrun` |
| Late and conflicting decisions are governed | Controlled-time and concurrency cases | Two effective outcomes or silent overwrite | | `planned` / `unrun` |

## 11. Constructed Northbridge application

**Continuity mode:** Independent constructed review fixture; not continuity
evidence.

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
section is constructed design material, not an incident, observed queue, or
practitioner result.

| Decision | Offer and actual owner | Authority | Timing and escalation | Evidence and privacy | Result |
| --- | --- | --- | --- | --- | --- |
| Review a dispute credit that exceeds the ordinary automated path under the applicable policy | Offer to a currently eligible approval population; a shared queue is not an actual owner. Exact allocation and capacity remain `unknown`. | Reviewer authority must be checked for actor, subject, tenant, amount, purpose, policy version, delegation, and conflict. Assignment alone is insufficient. | The constructed ten-business-day partner promise continues. Unclaimed or abandoned work must move through an evidence-bearing escalation without transferring decision authority by accident. | Present only necessary dispute evidence and retain identity, policy/evidence versions, rationale, times, downstream effect, and correction path under a still-undefined lifecycle. | `constructed`; queue, deadline, authorization, privacy, and usability exercises `unrun` |

Partner Operations retains the partner promise. Service Operations may own queue
recovery without gaining authority to approve the credit. The row does not
prove that the queue, eligible population, capacity, amount rule, evidence view,
or escalation policy exists or has been approved.

## 12. Decision and reversal record

| Decision | Reason | Evidence used | Unknown or residual risk | Owner | Revisit or reversal trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | `proposed` |

Transfer completed queue, authority, timing, substitution, and evidence fields
into the existing
[Human Approval-and-Escalation Map](human-approval-and-escalation-map.md).
Transfer planned clock and failure cases into the existing
[Time-and-Failure Test Plan](time-and-failure-test-plan.md). These transfers do
not change an `unrun` result into evidence.
