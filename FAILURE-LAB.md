# Failure Lab: The Completed Process That Still Owes a Customer

**Status:** Constructed exercise; prepared and unrun. It is not evidence of a
real defect, control effectiveness, or practitioner usability.

## Scenario

A credit workflow records its final step as successful. The call to the ledger
timed out, an automatic retry ran, and the customer portal now says “complete.”
Operations cannot tell whether the credit was committed once, twice, or not at
all. The approval that authorized the amount has also expired.

## Attractive shortcut

Treat the successful workflow step as proof of the business outcome and replay
the ledger call if the customer complains.

## Find the hidden decisions

1. What is the open promise: finish steps, or issue exactly one authorized
   credit and communicate the outcome?
2. Which system can prove whether the effect committed?
3. Does the idempotency identity survive the timeout and retry?
4. May an expired approval authorize a replay?
5. Who owns reconciliation while the result is unknown?

## Produce

- one row in the [Compensation Matrix](compensation-and-failure-matrix.md);
- the uncertain state and owner in the
  [Responsibility Brief](workflow-responsibility-and-progress-brief.md);
- a timeout and delayed-callback case in the
  [Time-and-Failure Test Plan](time-and-failure-test-plan.md);
- the closure evidence required before telling the customer “complete.”

## Evidence that would change the design

Observe whether the effect identity is stable, whether the ledger can answer
authoritatively, whether reconciliation detects the unknown state, and whether
expired authority blocks unsafe replay. Record what remains unknown.

## Outside-team test

Ask someone outside engineering, “Has the customer received the promised
outcome?” If the artifacts cannot support a clear **yes**, **no**, or **still
unknown and owned by this person**, the workflow is not yet accountable.

## Supplied practice for the current edition

Begin with [Did the credit happen?](examples/lost-reply-lab/README.md) if you do
not yet have a process of your own. Predict the effect count, run the optional
Python fixture, then explain the changed-amount and expired-authority results.
This connects Chapters 5, 6, 12, and 15 without requiring the other volumes.
Ten local fixture tests are distinct from human learning or production evidence.
