# Book-to-Companion Map

The artifact does not replace the chapter. Use the chapter to understand the
decision and this repository to make the decision inspectable.

| Book reasoning | Companion practice |
| --- | --- |
| Chapters 1–4: promise, progress, state, ownership, and authority | [Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Chapter 5: durable state and checkpoint claims | [Durable State Decision Record](durable-state-and-checkpoint-decision-record.md) |
| Chapter 6: retries, timeouts, backoff, and exhaustion | [Retry and Exhaustion Record](retry-timeout-backoff-and-exhaustion-safety-record.md) |
| Chapter 7: compensation and residual harm | [Compensation Matrix](compensation-and-failure-matrix.md) and [Eligibility Record](compensation-eligibility-and-failure-record.md) |
| Chapter 8: human approval and escalation | [Human Approval Map](human-approval-and-escalation-map.md) and [Authority and Evidence Record](human-approval-escalation-authority-and-evidence-record.md) |
| Chapters 9–11: time, parallelism, and child responsibility | [Time-and-Failure Test Plan](time-and-failure-test-plan.md) |
| Chapter 12: business idempotency | [Recovery Authority and Evidence Record](recovery-authority-and-evidence-record.md) |
| Chapter 13: versioning and running obligations | [Version-and-Migration Plan](workflow-version-and-migration-plan.md) |
| Chapters 14–15: stuck work, recovery, and testing | [Workflow Evidence Portfolio](workflow-evidence-portfolio.md) and [Time-and-Failure Test Plan](time-and-failure-test-plan.md) |
| Chapter 16: agents inside durable work | [Governed Agent Participation Record](governed-agent-participation-record.md) |

Use [Northbridge and Aster Vale](examples/README.md) to compare one method across
two constructed domains.

## Supplied practice for the current edition

Begin with [Did the credit happen?](examples/lost-reply-lab/README.md) if you do
not yet have a process of your own. Predict the effect count, run the optional
Python fixture, then explain the changed-amount and expired-authority results.
This connects Chapters 5, 6, 12, and 15 without requiring the other volumes.
Ten local fixture tests are distinct from human learning or production evidence.
