# Durable Workflows for AI Systems — Companion

**Series:** *AI Systems Architecture Field Guides*
Make one long-running promise retain its owner, state, deadlines, recovery, and
proof after the initiating request, worker, or AI session ends.

## The problem you may recognize first

You may have arrived because you need better retries, a queue, an orchestrator,
a scheduled job, or an agent that keeps working. If the request succeeded but a
person is still waiting, a partial effect may already have occurred, or nobody
owns the next move, the problem is durable workflow architecture before it is
engine selection.

This companion helps you produce a first reviewable result. It does not certify
a workflow, compensation, human review, organization, or AI participant as
safe, complete, or ready for production.

## The book-and-companion contract

- **The book teaches the judgment:** what promise remains open, who owns it,
  how work may advance, which effects can be repaired, and what completion
  means across time and failure.
- **The companion provides the moves:** responsibility briefs, failure and
  compensation matrices, time-controlled test plans, approval maps, migration
  plans, and worked examples.
- **The book stands alone:** this repository extends *Durable Workflows for AI
  Systems* without replacing its reasoning or story.

For the full intended learning path, use the book as the required source for
the judgment behind each exercise and this companion as the editable practice
resource.
The companion is useful on its own for a first bounded artifact, but it does
not contain the book's complete reasoning or story.

## Start here

Use [START-HERE.md](START-HERE.md) to take one long-running process through a
thirty-minute first pass. You will name the promise, beneficiary, durable owner,
deadline, allowed endings, authority, and closure evidence.

## Core assets

| Need | Start with |
| --- | --- |
| Define the promise and progress | [Workflow Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md) |
| Decide responses to partial effects | [Compensation-and-Failure Matrix](compensation-and-failure-matrix.md) |
| Exercise time, ambiguity, and recovery | [Time-and-Failure Test Plan](time-and-failure-test-plan.md) |
| Govern human decisions and escalation | [Human Approval-and-Escalation Map](human-approval-and-escalation-map.md) |
| Protect running obligations during change | [Workflow Version-and-Migration Plan](workflow-version-and-migration-plan.md) |
| Bound an AI participant | [Governed Agent Participation Record](governed-agent-participation-record.md) |
| Recover queued work after worker failure | [Northbridge Data-Structures Architecture Bridge](examples/northbridge-data-structures-architecture-bridge.md) |

Use [INDEX.md](INDEX.md) for role- and outcome-based routes and
[BOOK-TO-COMPANION-MAP.md](BOOK-TO-COMPANION-MAP.md) to reconnect each tool to
the book's reasoning.

## Use it across roles

[Role-Based Paths](ROLE-BASED-PATHS.md), the [Team Workshop](TEAM-WORKSHOP.md),
and the [Executive Decision Brief](EXECUTIVE-DECISION-BRIEF.md) turn one
technical design into a cross-role decision. Use the
[Value and Evidence Ledger](VALUE-AND-EVIDENCE-LEDGER.md) to connect the design
to an observed outcome without inventing benefits, then exercise it with the
[Failure Lab](FAILURE-LAB.md) and [Pilot Route](PILOT-AND-USABILITY.md).

The current checksum-locked reader-value packet is version 1.2.5. It preserves
six immutable scored freeze chains while separately enforcing the complete
route: an exclusive human-consent or synthetic-context entry branch, exact
stage boundaries, post-scoring debrief, immutable results before log close,
external closeout binding, and literal one-page handoff proof. Its first
semantic log event is branch selection, immediately followed by run-log start.
It remains
**PREPARED/UNRUN** for humans; real-world evidence remains **UNRUN**.

## Imagine and shape what comes next

Use the [Responsible Amplification and Possible Futures
Card](examples/responsible-amplification-and-possible-futures-card.md) to begin
with a beneficial possibility, trace bias and consequences through the whole
system, compare three plausible futures, and turn one future signal into a
reversible present decision. It is `PLANNED/UNRUN` and does not prove a
forecast, fairness, safety, legality, effectiveness, or reader learning.

## Evidence and use boundary

This is the public reader companion to *Durable Workflows for AI Systems*. It provides
editable tools and constructed examples; it does not certify a design,
implementation, organization, or AI system as safe, lawful, effective, or
production-ready. Preserve every `constructed`, `scenario`, `planned`,
`unrun`, `observed`, `tested`, `reported`, `inferred`, and `unknown`
label when adapting the material.

Written content is available under
[CC BY 4.0](LICENSE-CONTENT), and executable code is available under the
[Apache License 2.0](LICENSE-CODE). Source lineage is recorded in
[PROVENANCE.md](PROVENANCE.md); local integrity checks are documented in
[VALIDATION.md](VALIDATION.md). Human learner and practitioner validation
remains a separate evidence gate.

## Continue through the series

The five public companions follow the same evidence-bounded field-guide model:

1. [API Architecture for AI Systems](https://github.com/bmozi/api-architecture-for-ai-systems-companion)
2. [Event-Driven Architecture for AI Systems](https://github.com/bmozi/event-driven-architecture-for-ai-systems-companion)
3. [Durable Workflows for AI Systems](https://github.com/bmozi/durable-workflows-for-ai-systems-companion)
4. [Data Platform Architecture for AI Systems](https://github.com/bmozi/data-platform-architecture-for-ai-systems-companion)
5. [Agentic Systems Architecture](https://github.com/bmozi/agentic-systems-architecture-companion)
