# Aster Vale Compensation-and-Failure Matrix

**Example state:** `scenario`

**Validation state:** `unrun`

**Scenario identity:** `AVO-CAMPAIGN-01`; decision `AVO-COMP-01`

**Disclosure:** Aster Vale Observatory is an unrelated fictional scenario. This
completed example demonstrates use of the
[blank matrix](../compensation-and-failure-matrix.md). It does not establish
that an observation, loss, replacement, scientific outcome, or repair occurred.
Completion does not validate the workflow or establish any usability,
technical, scientific, business, privacy, accessibility, or safety result.

## Workflow context

| Field | Scenario decision |
| --- | --- |
| Workflow and version | `AVO-OBSERVING-CAMPAIGN/v0-proposed` |
| Business promise | Reach an authorized campaign disposition while preserving proposal, schedule, command, capture, and package history |
| Business owner | Program Operations |
| Compensation authority | Program Operations may consider a replacement slot; Instrument Operations controls execution; exact policy remains `unknown` |
| Maximum recovery window | Remaining campaign window up to the fictional thirty-day deadline; exception policy `unknown` |
| Residual harm owner | Program Operations owns unresolved campaign obligation; Instrument Operations owns command/capture discrepancy |

## Effect classification

| Step or external effect | Business effect | Confirmation evidence | Response eligibility or inverse preconditions | Conditions or deadline | Duplicate risk | Ambiguous-outcome probe | Compensation, semantic undo, or reconciliation | Authority | Residue or residual harm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reserve telescope window | Consumes schedulable capacity | Reservation identity | Release or reschedule is conditional on the current schedule policy and the reservation still being changeable | Release before window; policy `unknown` | Duplicate reservation | Query schedule by campaign identity | Release duplicate, reconcile, or reschedule under policy; semantic undo is not assumed | Program Operations | Lost opportunity for another campaign |
| Execute observation command | Consumes elapsed sky/instrument time and may create raw captures | Instrument command log plus raw-capture manifest | Semantic undo is ineligible for elapsed time; replacement eligibility and inverse conditions remain `unknown` | Current proposal, window, instrument authority | Repeated command may create extra capture or consume another window | Query command and raw-store authorities | Reconcile; an authorized replacement may compensate but cannot restore the prior world | Instrument Operations plus campaign authority | Sky conditions and time cannot be recreated exactly |
| Publish package manifest | Makes a data package discoverable to the scenario beneficiary | Versioned manifest and object references | Correction is conditional on a version guard, retained raw objects, and current steward authority | Raw objects and provenance must remain linked | Duplicate/conflicting manifest | Compare raw store and manifest versions | Semantic undo may apply only if exact manifest inverse conditions hold; retain the superseded version | Data steward | Delay or interpretive uncertainty |
| Grant replacement slot | Creates a new capacity commitment | New schedule and authorization identity | Conditional on eligibility, capacity, current proposal, and current authority | Eligibility, capacity, current proposal | Duplicate replacement | Query schedule and authorization | Reconcile or release duplicate slot; original missed conditions remain | Program Operations | Replacement conditions differ from original |

## Failure-response decisions

| Failure or ambiguity | Known state | Unknown state | Safe immediate action | Retry rule | Stop condition | Compensation trigger | Escalation owner | Required evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Observation acknowledgement lost | Command was sent | Capture may be absent, partial, or present | Enter `OBSERVATION_OUTCOME_UNKNOWN`; query instrument/raw store | No blind repeat | Query unavailable, window closes, or evidence conflicts | None until effect state known | Instrument Operations | Command, instrument, and raw-store records |
| Capture confirmed unusable for declared package rule | Capture exists | Replacement eligibility and scientific value | Preserve package and reason; evaluate disposition | No automatic repeated observation | No authority/capacity or deadline exhausted | Current policy authorizes replacement | Program Operations | Manifest, rule version, authority, schedule |
| Replacement command acknowledgement lost | Replacement request sent | Second capture may be absent or present | Query new effect identity | No blind repeat | Conflicting evidence or budget exhausted | Already an open repair promise | Instrument Operations | Replacement operation/attempt/effect ledger |
| Manifest correction fails | Raw objects remain | Published package consistency | Quarantine package publication; reconcile | Repeat only under version guard | Source/manifest conflict | Correction is already the repair | Data steward | Raw object and manifest version comparison |
| No replacement is permitted | Original disposition remains | Accepted residue | Seek non-execution/manual-resolution decision | None | No eligible repair | Not applicable | Program Operations | Policy, capacity, beneficiary notice, rationale |

## Response vocabulary

| Response | Scenario use |
| --- | --- |
| Retry | Repeat a proven-safe technical attempt under stable identity, not the observation blindly |
| Compensate | Authorize a new replacement-slot action with its own promise and evidence |
| Semantic undo | Assert a domain inverse only when exact current conditions can be checked; never claim that elapsed sky time or prior observation disappeared |
| Reconcile | Compare workflow, instrument, raw-store, schedule, and manifest authorities |
| Escalate | Transfer a bounded decision to Program or Instrument Operations |
| Accept loss | Record non-recoverable window/condition residue under named authority |
| Stop | Prevent new commands while effect or authority is unknown |
| Manual resolution | Create owned exception work with deadline and record |

## Compensation invariants

- Original command and capture history is never erased by a replacement.
- A replacement slot and command have new identities, authority, failure modes,
  and evidence.
- The workflow does not claim that a later observation recreates the original
  sky conditions or scientific value.
- Ambiguous replacement execution remains owned until reconciled.
- A terminal disposition preserves remaining uncertainty and beneficiary
  communication obligations.

## Failure tests

| Planned challenge | Expected governed response | Required artifact | Result |
| --- | --- | --- | --- |
| Failure before observation command | Preserve known absence if supported | Command trace | `planned` / `unrun` |
| Command commits; acknowledgement is lost | Enter unknown and query authorities | Lost-ack and raw-store trace | `planned` / `unrun` |
| Duplicate observation command | Prevent or expose additional execution | Attempt/effect ledgers | `planned` / `unrun` |
| Replacement commits; acknowledgement is lost | Query replacement identity | Replacement ledger | `planned` / `unrun` |
| Replacement fails transiently then terminally | Exhaust finite policy and transfer owner | Failure/exhaustion record | `planned` / `unrun` |
| Replacement window expires | Stop automation; obtain disposition | Clock/authority record | `planned` / `unrun` |
| Authority or proposal changes | Recheck eligibility | Version/authority mutation | `planned` / `unrun` |
| Instrument and raw-store evidence disagree | Quarantine and reconcile | Conflict bundle | `planned` / `unrun` |

## Decision record

| Decision | Rationale | Evidence | Remaining uncertainty | Owner | Revisit trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| Reconcile an unknown observation before another command | Caller timeout cannot establish capture absence | Scenario `AVO-STATE-01` and `AVO-RETRY-01` reasoning | Instrument query contract remains unknown | Instrument Operations; Program Operations keeps promise | Query cannot correlate stable command/capture identities | `scenario`; test `unrun` |
| Treat an eligible replacement as semantic repair | Time and conditions cannot be rolled back | Scenario effect classification | Eligibility, capacity, and beneficiary acceptance remain unknown | Program Operations | Proposal, policy, or capacity changes | `scenario`; eligibility `unrun` |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Matrix field | Decision ID | Applicable blank worksheet and chapter | State |
| --- | --- | --- | --- |
| Command/capture ambiguity | `AVO-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md); [Chapter 5](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch05-durable-execution-and-checkpointing.md) | `scenario`; experiment `unrun` |
| Query-before-repeat and budgets | `AVO-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md); [Chapter 6](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch06-retries-timeouts-and-backoff.md) | `scenario`; policy test `unrun` |
| Replacement eligibility, residue, and failure | `AVO-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md); [Chapter 7](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch07-compensation-rather-than-rollback.md) | `scenario`; tests `unrun` |
| Exception authority and no-repair disposition | `AVO-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md); [Chapter 8](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch08-human-approval-and-escalation.md) | `scenario`; authority test `unrun` |

The linked blanks are illustrative only; no response is shown to work or to
produce an acceptable scientific or business outcome.
