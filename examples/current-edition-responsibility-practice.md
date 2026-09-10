# Current-edition practice: hand off an unresolved promise

**Status:** Fictional Northbridge teaching facts; design exercise, execution and
human learning unrun. This is the completed day-nine practicum branch, not a
retroactive completion of the older examples' deliberately unknown fields.

Use the [Responsibility Ledger](../durable-responsibility-ledger.md) and
[Durable-Responsibility Practicum](../durable-responsibility-practicum.md).

## Supply the next reader with an actionable handoff

Dispute `NB-8472` is `completion_unproven`. At 13:00 UTC on business day nine,
the `credit-outcome-8472` Finance receipt cannot be reconstructed after its
retention boundary. The partner deadline remains day ten, 17:00 UTC. The
following assignments and times are stipulated scenario facts.

| Responsibility | Accepted assignment and due point | Permitted next move |
| --- | --- | --- |
| Partner notice | Rosa accepted at 12:55; if unavailable, OPS-2 must accept within 15 minutes or escalate to Samir | Recover notice evidence; issue only a newly authorized, policy-bounded provisional notice |
| Finance evidence | FIN-17 accepted at 13:00; report by 13:45 | Supply available evidence or state the unrecoverable gap; no invented effect result |
| Recovery disposition | Nia reviews at 14:00 | Approve a bounded disposition before any state mutation |
| Unresolved gap or assignment | Samir receives escalation at 14:15 | Own the next decision while preserving the partner deadline |

**Try it:** Write a handoff a new reviewer can act on without asking who owns
the next step. Include the unknown, prohibited actions, and re-review trigger.

**Check your answer:** It must prohibit retry, offset, and closure while the
effect remains unproven; identify FIN-17 and 13:45; retain Rosa, Nia, Samir, and
their clocks; and preserve the day-ten deadline. New evidence, unavailable
assignees, or changed applicable authority require immediate re-review. An
agent may summarize frozen evidence; it cannot create effect or closure
permission. A passed deadline escalates responsibility, not certainty.

## Test the policy that actually applies

In the [Time-and-Failure Test Plan](../time-and-failure-test-plan.md), make
these separate cases before choosing the expected result:

| Changed condition | Expected decision boundary |
| --- | --- |
| New policy explicitly invalidates unused approvals for this waiting cohort | Retain the old decision as history; block advancement and obtain current approval |
| New policy explicitly preserves this cohort's earlier approvals | Check their remaining scope, expiry, actor authority, and other guards; a version change alone does not invalidate them |
| Applicability to this cohort is unknown | Hold advancement and assign the policy question to an authorized owner |

Neither a policy version string nor an engine replay result establishes which
case applies. Record the rule, cohort, effective time, and decision evidence.
