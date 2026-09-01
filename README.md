# Durable Workflows for AI Systems — Companion

**Series:** *AI Systems Architecture Field Guides*
**Previous working title:** *Architecting Durable Workflows in the Age of AI*.

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
the judgment behind each exercise and this companion as the working resource.
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

## Development boundary

This is an owner-approved release candidate. Northbridge and Aster Vale are
constructed transfer fixtures, not evidence that the assets work in a real
organization. Human learner and practitioner validation remains pending. See
[LICENSE-STATUS.md](LICENSE-STATUS.md). Source lineage is recorded in
[PROVENANCE.md](PROVENANCE.md), and local validation is described in
[VALIDATION.md](VALIDATION.md).
