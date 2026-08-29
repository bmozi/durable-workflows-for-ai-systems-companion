# Role-Based Paths

The same workflow looks different depending on what you are accountable for.
Choose one path, produce one artifact, then bring the result to another role.

## Developer or workflow designer

**What this unlocks:** work that can survive restarts, delays, retries, and
releases without losing the customer promise.

1. Complete the [thirty-minute start](START-HERE.md).
2. Name durable state and checkpoints in the
   [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md).
3. Exercise one timeout and one retry with the
   [Time-and-Failure Test Plan](time-and-failure-test-plan.md).

Leave with: a state model, an idempotency boundary, and evidence of one safe
recovery—not merely a diagram of steps.

## Architect or operations lead

**What this unlocks:** visible ownership where a process crosses services,
teams, time, and failure.

1. Map transfers and terminal outcomes in the responsibility brief.
2. Classify partial effects in the
   [Compensation Matrix](compensation-and-failure-matrix.md).
3. Define detection, recovery, and reconciliation evidence.

Leave with: a promise ledger that distinguishes step health from business
completion.

## Product or service manager

**What this unlocks:** a process whose delays and failures can be managed as
customer outcomes instead of hidden technical incidents.

1. Name the beneficiary and acceptable endings.
2. Put deadlines, escalation, and human decisions on the
   [Approval Map](human-approval-and-escalation-map.md).
3. Use the [Value and Evidence Ledger](VALUE-AND-EVIDENCE-LEDGER.md) to connect
   reliability work to delay, rework, abandonment, and trust.

Leave with: a decision about what the service promises and when intervention
is required.

## Executive or decision owner

**What this unlocks:** a defensible view of obligations, operational exposure,
and investment—not a dashboard of successful jobs.

1. Read the [Executive Decision Brief](EXECUTIVE-DECISION-BRIEF.md).
2. Ask which open promises can outlive the team or system that started them.
3. Require closure evidence, named residual exposure, and a reconsideration
   trigger before funding broader automation.

Leave with: a bounded continue, constrain, redesign, or stop decision.

## Cross-role handoff

Ask someone outside the implementation team to explain: who is still owed an
outcome, who owns the next move, what happens after a timeout, and what proves
the promise is closed. If they describe only the happy-path steps, the design
is not yet transferable.
