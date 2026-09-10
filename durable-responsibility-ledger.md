# Durable Responsibility Ledger

Use this front sheet when several workflow decisions must stay joined around
one unresolved outcome. It does not replace the canonical workflow tools. It
helps a reviewer see, in one place, what is owed, who owns it, what may happen
next, and what counts as an acceptable ending.

**Use boundary:** Illustrative field tool; not certification or proof of
production fitness. A completed Ledger is a design record, not proof that the
workflow is correct or that an outcome occurred.

## Ten-minute first pass

Create one row for one open promise. Before discussing an engine, worker, or
agent, name:

1. the beneficiary and promised outcome;
2. the accountable business owner and technical operating owner;
3. the authoritative state and next permitted transition;
4. the deadline and escalation owner; and
5. the evidence required for an acceptable ending.

If any answer is unknown, record the unknown and its decision owner. Do not
let a workflow diagram, queue, tool result, or AI-generated definition supply
the missing decision.

## Ledger row

| Field | Current decision or evidence | Resolver record |
| --- | --- | --- |
| Promise ID, beneficiary, and opening condition | | [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Authoritative state and definition/policy version | | [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Business owner and technical operating owner | | [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Current state and next authorized transition | | [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Clock, deadline, queue, and escalation owner | | [Human Approval-and-Escalation Map](human-approval-and-escalation-map.md) |
| Effect, ambiguity, repeat rule, compensation, reconciliation, and residue | | [Compensation-and-Failure Matrix](compensation-and-failure-matrix.md) |
| Definition or policy change and treatment of open work | | [Workflow Version-and-Migration Plan](workflow-version-and-migration-plan.md) |
| Time, failure, duplicate, and recovery challenge | | [Time-and-Failure Test Plan](time-and-failure-test-plan.md) |
| Agent participation and its withheld authority, if relevant | | [Governed Agent Participation Record](governed-agent-participation-record.md) |
| Permitted terminal outcome and closure evidence | | [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Uncertainty, evidence state, and reconsideration trigger | | Evidence package and applicable canonical record |

## Non-negotiable review gates

- No nonterminal promise is reviewable without an owner, deadline, permitted
  next action, and progress evidence.
- Approval, timeout, compensation, escalation, migration, recovery, and
  accepted abandonment are state transitions with authority; they are not
  annotations beside a happy-path diagram.
- No row may claim completion without evidence of the authority, effect, and
  reconciliation required by its defined terminal outcome.
- An AI system may make a bounded contribution inside the workflow. It never
  becomes the durable owner of the promise merely by planning or calling a
  tool.

## Falsifiable forecast

**Prediction:** As AI makes it cheaper to generate workflow steps and expand
fan-out, organizations will increasingly review responsibility through open
promises and closure evidence rather than through diagrams and successful task
counts alone.

**Leading indicators:** open work without a named business owner; approvals
without expiry or escalation; retries without stable business-operation
identity; and releases without an inventory of running obligations.

**Disconfirming condition:** high-volume, AI-mediated work repeatedly retains
reconstructable ownership, bounded recovery, and acceptable closure without
recording an equivalent responsibility model. Treat that result as a reason to
reconsider the Ledger, not as a failure to be hidden.
