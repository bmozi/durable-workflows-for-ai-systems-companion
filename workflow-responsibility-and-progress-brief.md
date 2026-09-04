# Workflow Responsibility-and-Progress Brief

Use this when work will outlive one request, wait for a person or another
system, or leave partial effects behind. The brief helps a team keep one answer
visible: what is still owed, who owns it now, and what will prove that it ended
acceptably.

## Ten-minute first pass

Complete these seven lines before choosing or generating workflow machinery:

1. **We owe this outcome to:** name the beneficiary.
2. **The promise opens when:** name the business condition, not merely the API
   call or first message.
3. **The owner while work is unfinished is:** name a durable role.
4. **The deadline is:** include the business calendar or policy.
5. **The acceptable ways this promise may end are:** include rejection,
   cancellation, compensation, expiration, or accepted abandonment when they
   are legitimate.
6. **Only these roles may close or change the promise:** name their authority.
7. **Closure is proved by:** name the authoritative outcome and evidence.

If any line is unanswered, record the unknown and its decision owner. Do not let
a workflow engine or generator supply the missing business decision.

### Miniature example

| First-pass line | Northbridge dispute answer |
| --- | --- |
| Beneficiary and promise | A distribution partner is owed an eligibility decision and any authorized account correction. |
| Promise opens | Northbridge accepts the dispute for investigation. |
| Durable owner | Partner service operations owns the open case even while carrier evidence, system work, or human approval is pending. |
| Deadline | The applicable partner policy supplies the business deadline and calendar. |
| Acceptable endings | Approved and corrected, denied with reasons, withdrawn, or another explicitly authorized terminal disposition. |
| Closure authority | The workflow may record progress; only the named business authorities may approve, deny, compensate, cancel, or accept an exception. |
| Closure evidence | The durable case record joins the decision, authority, effects, notifications, and unresolved exceptions. |

See the
[complete Northbridge Responsibility-and-Progress Brief](examples/northbridge-workflow-responsibility-and-progress-brief.md)
and the
[unrelated Aster Vale example](examples/aster-vale-workflow-responsibility-and-progress-brief.md)
for comprehensive applications and their evidence limits.

## Plain-language vocabulary

- **Promise:** the outcome the organization still owes while work is open.
- **Beneficiary:** the person, partner, team, or system waiting for that outcome.
- **Durable owner:** the role that remains accountable after the initiating
  request, worker, or AI session ends.
- **Authoritative state:** the record the organization trusts to say what is
  currently owed and what may happen next.
- **Terminal outcome:** an allowed ending that actually closes the promise.
- **Compensation:** a new authorized action that addresses an earlier effect; it
  is not time travel or a distributed rollback.
- **Invariant:** a business truth that must remain true through retries, delay,
  partial success, and change.
- **Closure evidence:** the record that connects the final outcome to the
  authority and effects that produced it.

**Use boundary:** Illustrative field tool; not certification or proof of
production fitness

**Validation state:** `unrun`. Completing this record does not validate a
workflow, authority model, failure response, or business outcome.

Use the evidence states `constructed`, `scenario`, `planned`, `unrun`,
`observed`, `tested`, `reported`, `sourced`, `bounded`, `inferred`, `proposed`,
and `unknown` exactly. A planned exercise remains `unrun` until a retained
result exists.

The full record below turns the first-pass promise into a reviewable state,
authority, failure, recovery, and evidence design.

## 1. Business promise

| Field | Decision |
| --- | --- |
| Workflow name and version | |
| Initiating business condition | |
| Promise made | |
| Promise made to whom | |
| Business owner until closure | |
| Technical operating owner | |
| Maximum acceptable duration | |
| Business deadline and calendar | |
| Acceptable terminal outcomes | |
| Unacceptable or prohibited outcomes | |
| Cancellation meaning | |
| Evidence required at closure | |

## 2. Participation and authority

| Participant | Role in the promise | May start | May advance | May approve | May compensate | May cancel | May recover or migrate | Evidence required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | |

Distinguish authenticated access from authority to change the business outcome.
Record tenant, subject, delegation, amount, policy, or other scope limits.

## 3. Authoritative state and progress

| State | Business meaning | Entry evidence | Owner while here | Allowed next actions | Timing policy | Failure or ambiguity response | Exit evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

For every nonterminal state, answer:

- How will lack of progress be detected?
- Who is paged, queued, or otherwise assigned?
- What may safely repeat?
- Which deadline is being consumed?
- What evidence lets an operator distinguish waiting from lost work?

## 4. Effects and dependencies

| Action or effect | Owning system or party | Invocation path | Outcome evidence | Ambiguous-outcome test | Repeat rule | Compensation or reconciliation |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 5. Invariants

State business truths independently of implementation:

- Exactly one acceptable business outcome means:
- The workflow must never:
- A terminal state is invalid unless:
- A repeated attempt is safe only when:
- A compensation is complete only when:
- Human or agent action is valid only when:

## 6. Version and recovery obligations

| Question | Decision |
| --- | --- |
| How is definition/version identity recorded? | |
| What happens to open instances after change? | |
| How are incompatible states quarantined? | |
| Who may repair, resume, cancel, or migrate? | |
| What history must remain immutable? | |
| What recovery evidence is retained? | |

## 7. Evidence gate

| Claim | Evidence that could support it | Evidence that could disprove it | Owner | State |
| --- | --- | --- | --- | --- |
| The promise always has an owner | | | | planned; unrun |
| Every nonterminal state can progress or escalate | | | | planned; unrun |
| Repeated execution cannot repeat the prohibited outcome | | | | planned; unrun |
| Running instances survive approved change | | | | planned; unrun |
| Closure is reconstructable and authorized | | | | planned; unrun |

## 8. Unknowns and stop conditions

- Unknowns that generation must not invent:
- Conditions requiring human architectural decision:
- Conditions that stop execution:
- Conditions that force escalation or manual resolution:
- Evidence that would require redesign:

## Review test

Give the seven first-pass lines and the completed record to someone outside the
implementing team. Without showing them the workflow diagram, they should be
able to answer:

1. What promise remains open?
2. Who owns it now?
3. What authoritative evidence shows progress?
4. What happens after delay, duplicate work, partial success, or ambiguity?
5. Who may close, compensate, cancel, recover, or migrate it?
6. What proves an acceptable business outcome?

Ask them what could still be owed after every visible step reports success. If
their answer differs from the design team's answer, the workflow is not ready
to automate the disagreement.
