# Aster Vale Workflow Responsibility-and-Progress Brief

**Example state:** `scenario`

**Validation state:** `unrun`

**Scenario identity:** `AVO-CAMPAIGN-01`

**Disclosure:** Aster Vale Observatory is an unrelated fictional scenario, not
a real organization or experience report. This completed example demonstrates
use of the [blank brief](../workflow-responsibility-and-progress-brief.md). It
does not validate the workflow or establish any usability, technical,
scientific, business, privacy, accessibility, or safety result.

## 1. Business promise

| Field | Scenario decision |
| --- | --- |
| Workflow name and version | `AVO-OBSERVING-CAMPAIGN/v0-proposed` |
| Initiating business condition | Program Operations accepts an approved observing proposal into a schedulable campaign |
| Promise made | Produce a governed observation disposition: recorded capture package, authorized reschedule, reasoned non-execution closure, or named manual resolution |
| Promise made to whom | The proposal's principal investigator |
| Business owner until closure | Program Operations |
| Technical operating owner | Observatory Platform Operations |
| Maximum acceptable duration | Thirty calendar days from first assigned window, a fictional scenario value |
| Business deadline and calendar | Observatory UTC calendar; weather and instrument windows are inputs, not automatic outcomes |
| Acceptable terminal outcomes | `PACKAGE_RECORDED`, `RESCHEDULE_AUTHORIZED`, `NON_EXECUTION_ACCEPTED`, or `MANUAL_RESOLUTION_ACCEPTED` |
| Unacceptable or prohibited outcomes | Ownerless campaign; repeated observation command without effect check; data package without provenance; silent target change |
| Cancellation meaning | Release future resources, preserve executed-observation history, and record authorized disposition; elapsed sky time is not undone |
| Evidence required at closure | Proposal/version, schedule identity, observation command/effect identity, raw-package manifest or non-execution reason, authority, and terminal record |

## 2. Participation and authority

| Participant | Role in promise | May start | May advance | May approve | May compensate | May cancel | May recover or migrate | Evidence required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal investigator | Beneficiary and proposal owner | Submit approved proposal | Supply clarification | Approve scientific preference only, not instrument operation | No | Request cancellation | No | Proposal and request identity |
| Program Operations | Business-promise owner | Admit approved campaign | Schedule, reschedule, close under policy | Approve campaign disposition within policy | Authorize replacement-slot consideration | Cancel under policy | Authorize business recovery/migration | Actor, rationale, policy/version |
| Instrument Operations | Physical-operation authority | No | Execute or stop approved instrument command | Approve operational execution within current constraints | No | Stop unsafe or invalid operation; no claim of safety is made here | Confirm effect and reconcile command | Command, instrument state, result manifest |
| Platform Operations | Technical workflow operator | No | Resume, query, or quarantine under runbook | No scientific or operational authority | No | No | Execute approved recovery/migration | Trace, version, runbook authority |
| Duty astronomer | Human exception reviewer | No | Approve, reject, abstain, or request information for target/window change within scope | Scoped exception only | No | No | No | Eligibility, conflict, evidence version, rationale |
| Data steward | Package and lifecycle custodian | No | Verify manifest completeness | No campaign outcome authority | Correct manifest only under policy | No | Reconcile package history | Manifest/version and correction evidence |

## 3. Authoritative state and progress

| State | Business meaning | Entry evidence | Owner while here | Allowed next actions | Timing policy | Failure or ambiguity response | Exit evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ACCEPTED` | Campaign promise is open | Approved proposal identity | Program Operations | Schedule or request clarification | Thirty-day scenario clock begins | Escalate if unscheduled | Schedule record |
| `WINDOW_ASSIGNED` | A future observation window is reserved | Window and instrument identity | Program Operations | Prepare, change under authority, or cancel | Window in UTC | Reassign only with evidence | Prepared-command record |
| `EXCEPTION_REVIEW` | Target/window change requires judgment | Exception task identity | Program Operations; duty astronomer owns claimed task | Approve, reject, abstain, request information | Constructed four-hour window | Transfer visibly; ignore late superseded decision | Decision record |
| `OBSERVATION_REQUESTED` | One governed command was sent | `AVO-RETRY-01` operation/attempt identity | Program Operations; Instrument Operations owns effect confirmation | Await receipt or query status | Bounded by observing window | Do not infer non-execution from caller timeout | Instrument receipt or unknown state |
| `OBSERVATION_OUTCOME_UNKNOWN` | Capture may be absent or present | Missing/conflicting acknowledgement | Program Operations; Instrument Operations reconciles | Query, quarantine, reconcile, or separately authorize action | Immediate escalation inside remaining window | Preserve `unknown` | Authoritative command and capture evidence |
| `PACKAGE_REVIEW` | A candidate data package exists | Raw manifest identity | Program Operations; Data steward owns manifest check | Record package or correct manifest | Before campaign deadline | Preserve raw history if correction occurs | Versioned package manifest |
| `CLOSED` | One authorized disposition ended the promise | Terminal record and evidence package | Program Operations for correction/appeal | Correction path only | Lifecycle policy `unknown` | Preserve original record | Reconstructable closure package |
| `QUARANTINED` | Work is stopped for governed recovery | Stop reason and owner | Named recovery owner; Program Operations retains promise | Repair, reconcile, reschedule, migrate, or close by authority | Recovery deadline `unknown` | Escalate if no permitted path | Recovery disposition |

## 4. Effects and dependencies

| Action or effect | Owning system or party | Invocation path | Outcome evidence | Ambiguous-outcome test | Repeat rule | Compensation or reconciliation |
| --- | --- | --- | --- | --- | --- | --- |
| Reserve window | Scheduling service | Scheduling capability | Reservation identity | Reservation persisted; acknowledgement lost | Query before repeat | Release duplicate reservation if authorized |
| Execute observation | Instrument Operations | Governed instrument command | Command log plus raw-capture manifest | Capture begins; response is lost | Query command/capture state; never blind repeat | `AVO-COMP-01`: replacement slot may be semantic repair, not rollback |
| Record package | Data stewardship service | Manifest capability | Versioned manifest | Raw files exist; manifest write fails | Reconcile raw store and manifest | Correct manifest without deleting original history |
| Notify investigator | Communications service | Closure action | Message attempt/content version | Delivery unknown | Repeat only under communication policy | Corrective notice; original cannot be unsent |

## 5. Invariants

- Exactly one acceptable business outcome means one authorized campaign
  disposition, not one execution attempt.
- The workflow must never infer that no observation occurred merely because a
  caller stopped waiting.
- A terminal package state is invalid without a proposal, command, raw-manifest
  or explicit absence evidence, provenance, and authorized disposition.
- A repeated instrument attempt requires authoritative knowledge of the first
  effect and current operational authority.
- A replacement window does not erase lost time, changed conditions, or the
  original observation record.
- Human or agent action is valid only under current scoped authority; generated
  recommendations are inputs, not decision authority or evidence.

## 6. Version and recovery obligations

| Question | Scenario decision |
| --- | --- |
| How is definition/version identity recorded? | Definition, proposal, policy, calibration-manifest, and command versions on the instance |
| What happens to open instances after change? | Identify cohorts; default to old version unless compatibility is decided |
| How are incompatible states quarantined? | Enter `QUARANTINED` with source version, state, owner, and allowed disposition |
| Who may repair, resume, cancel, or migrate? | Platform Operations executes only after Program, Instrument, or Data authority appropriate to the effect |
| What history must remain immutable? | Proposal, schedule, command attempts, capture manifests, decisions, corrections, and migration transitions |
| What recovery evidence is retained? | Before/after versioned state, command/capture query, authority record, and terminal reconciliation |

## 7. Evidence gate

| Claim to challenge | Evidence that could support it | Evidence that could disprove it | Owner | State |
| --- | --- | --- | --- | --- |
| Promise always has an owner | State/owner reconstruction | Any ownerless open state | Program Operations | `planned` / `unrun` |
| Every open state can progress or escalate | Controlled-time fixtures | Indefinite or alert-only wait | Platform Operations | `planned` / `unrun` |
| Repetition cannot create prohibited extra command | Attempt and instrument ledgers | Duplicate or unexplained execution | Instrument Operations | `planned` / `unrun` |
| Running campaigns survive approved change | Cohort/migration fixtures | Lost proposal meaning, owner, or command link | Change owner | `planned` / `unrun` |
| Closure is reconstructable and authorized | Independent closure reconstruction | Missing provenance or authority | Program Operations | `planned` / `unrun` |

## 8. Unknowns and stop conditions

- Unknowns generation must not invent: instrument guarantees, query semantics,
  scientific acceptance, authority scope, data lifecycle, capacity, or
  migration support.
- Human decision required: terminal policy, repeat eligibility, replacement
  eligibility, exception authority, and accepted residue.
- Stop when capture state is unknown, authority is stale, evidence conflicts,
  or definition compatibility is unverified.
- Escalate when the observing window or campaign deadline expires without an
  authorized disposition.
- Redesign if tests reveal ownerless campaigns, blind command repeats, missing
  provenance, or changed proposal meaning.

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Brief field | Decision ID | Applicable blank worksheet and chapter section | Transfer state |
| --- | --- | --- | --- |
| Durable state and capture ambiguity | `AVO-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md); [Chapter 5](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch05-durable-execution-and-checkpointing.md) | `scenario`; test `unrun` |
| Command attempts and timeout | `AVO-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md); [Chapter 6](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch06-retries-timeouts-and-backoff.md) | `scenario`; test `unrun` |
| Replacement window and residue | `AVO-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md); [Chapter 7](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch07-compensation-rather-than-rollback.md) | `scenario`; eligibility `unrun` |
| Exception-task authority | `AVO-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md); [Chapter 8](https://github.com/bmozi/architecting-durable-workflows-in-the-age-of-ai/blob/main/chapters/ch08-human-approval-and-escalation.md) | `scenario`; usability `unrun` |

This field trace identifies blank forms available for future reasoning. It does
not validate any decision or scenario behavior.
