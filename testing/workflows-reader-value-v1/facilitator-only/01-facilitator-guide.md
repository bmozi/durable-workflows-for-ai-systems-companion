# Facilitator Guide

**Packet:** WF-RV-PILOT-001 version 1.2.4
**Status:** Facilitator-only; prepared and unrun

## Purpose

Test the materials, not the participants. Observe whether the reader-value
layer supports a practitioner workflow decision and an independent decision-
owner read-back.

## Recommended timing

### Stage A — 70 to 85 minutes

- consent and setup: 5 minutes;
- scenario and recognition questions: 10 minutes;
- responsibility-and-progress brief: 30 minutes;
- compensation and time/failure plan: 15 minutes;
- live update and revision: 10 minutes; and
- handoff and feedback: 10 minutes.

### Stage B — 35 to 50 minutes

- independent read-back: 15 minutes;
- executive brief and value ledger review: 10 minutes;
- bounded decision: 10 minutes; and
- debrief: 5 to 15 minutes.

Time is evidence, not a speed target.

## No-coaching rule

During scored work, the facilitator may repeat written text or resolve file
access. Do not supply the state model, name the durable owner, interpret
`accepted`, select compensation, define completion, or confirm an answer.
Do not supply missing approval fields, authority, an owner, a number, a date,
or an evidence source. Record every question, pause, access problem, and
intervention with exact time and level.

## Prepare each sealed delivery and separate execution log

Before each staged release, copy every and only the canonical protocol's
declared files into a new flat phase-input directory. Preserve the exact
filenames and bytes named in `00-packet-route.md`. An undeclared file fails the
release. Never add `ORCHESTRATION.md`, a hidden prompt, this guide, or any
facilitator note to sealed participant input.

Create the separate facilitator-only JSONL execution/access log defined in
`05-run-execution-and-access-log-schema.md` outside every participant-input
directory. Bind each event to the preceding event. Log manifest creation and
verification, each file's separate release/open/completed-read events,
artifact completion, manifest creation/verification, detached-record
completion, deviations, and stops with actor, exact filename, timestamp, and
timezone. The log records the route; it must never become an instruction the
participant can read.

Create a run-specific SHA-256 manifest that covers every supplied participant
file, companion asset, and frozen artifact. Seal that manifest before scored
work begins and record each later staged release. A
governing manifest hashes only artifacts whose completion state and completion
timestamp/timezone are already in their final bytes. It never hashes itself or
the later detached record describing its verification. Verify it from the
sealed directory, capture the literal command, observed standard output and
standard error, integer exit status, exact verification timestamp, and
timezone, and then create the detached freeze-verification record. Every
detached record requires attempt ID, canonical phase, facilitator/actor code,
those observed verification fields, and its own later exact completion
timestamp and timezone. Each next phase-input manifest
hashes the prior artifacts, governing manifest, detached record, and newly
released files. Do not rely on
repository-relative paths. If any claimed-frozen artifact requires correction,
retain it and create a new immutable filename and version. Record the exact
old/new filenames and versions, reason, correction timestamp/timezone,
old/new SHA-256 values, governing manifests, observed verification events,
detached records, and next-phase manifests.

## Select exactly one entry branch

Before scored input opens, log `entry_branch_selected` with `human` or
`synthetic`. Never infer the branch from a blank consent form.

- Human: complete every prerequisite and affirmation in
  `participant/01-consent-and-privacy.md`; export distinct immutable Stage A
  and Stage B human-consent records. Verify them under
  `WF-A-HUMAN-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt` and
  `WF-B-HUMAN-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt`, respectively. A blank
  or nonaffirmative required field stops the run.
- Synthetic: create
  `WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md` from
  `06-synthetic-context-record-template.md`, including the exact statement
  `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`, both actor codes,
  facilitator, orchestration-manifest identity, evidence/retention/access
  boundaries, start/checkpoint, and human/real-world `UNRUN` limits. Do not
  fill a human consent form or claim human consent, comprehension, usability,
  practitioner behavior, or result.

Missing selection, branch mixing, or a synthetic human-result claim stops the
attempt. Complete and verify the selected stage-context manifest before each
`stage_a_started` or `stage_b_started` event and before scored input opens.

## Stage A sequence

1. Verify the selected Stage A entry-context record. Human consent and the
   synthetic context are mutually exclusive.
2. Record exact Stage A start, timezone, and supplied-file route immediately
   before the participant's first packet read, then append
   `stage_a_started` to the execution/access log.
3. Follow `participant/00-packet-route.md` exactly. Let the participant
   complete recognition before opening companion assets. Do not follow omitted
   links or supply full worked examples.
4. Complete the initial workbook and detailed artifacts before the update,
   including IDs, versions, completion timestamp/timezone, and `INITIAL
   COMPLETE` state. Create and verify
   `WF-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`, capture the literal command,
   observed output, exit status, exact verification time, and timezone, and
   only then create
   `WF-A-INITIAL-FREEZE-VERIFICATION-RECORD-v1.md`. Export the exact quote in
   Step 5 as `WF-A-LIVE-UPDATE-v1.md`. Create and verify
   `WF-A-LIVE-UPDATE-INPUT-SHA256SUMS-v1.txt`, covering the initial artifacts,
   their manifest and detached record, and that update file. Do not read the
   update until this phase-input manifest passes.
5. Read the live update:

> Meadowline's first contractor request timed out after API receipt/acceptance.
> A provider status query now shows a contractor job-acceptance record and
> travel begun. The assistant retried with a new request ID, and a second
> contractor recorded contractor job acceptance. A call-out fee may remain.
> `HeatRestorationScheduled` was published after the first API
> acceptance, so the tenant was told the repair was confirmed and the service
> case was closed. No reconciled appointment evidence exists, no technician
> has arrived, the premium approval expires in twelve minutes, and no named
> role currently
> owns the open promise.

6. Ask only: “What can each party safely say or do now, and what changes in
   your artifacts?”
7. Treat the live-update revision as a planned new set, not as correction of
   the initial frozen set. Export the four revised details under the exact v1
   filenames required by the route. Create
   each revised file's artifact header with ID/version, exact completion
   timestamp/timezone, and state `REVISED COMPLETE` before hashing. Then create
   `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`; it lists and hashes those four
   files, not itself or a later record. Verify it from the sealed directory
   and capture the literal command, observed output, exit status, exact
   verification timestamp, and timezone. Only then complete the detached
   `WF-A-REVISED-FREEZE-RECORD-v1.md` with the attempt ID, phase,
   facilitator/actor code, that observed verification event, artifact
   IDs/versions, filenames, hashes, manifest filename/hash, and its own later
   record-completion timestamp/timezone.
   Confirm every revised detail's own state is `REVISED COMPLETE`, with no `PENDING` or
   `AWAITING FREEZE` state. Create and verify
   `WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt`, covering the four revised artifacts,
   governing manifest, detached record, and blank handoff. Only then let Stage
   A open and complete `WF-A-ONE-SCREEN-HANDOFF-v1.md`, including its
   ID/version, completion timestamp/timezone, and `HANDOFF COMPLETE` state.
   Create `WF-A-HANDOFF-SHA256SUMS-v1.txt`, verify it, capture the verification
   time/timezone, and only then create
   `WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md` with every required field
   and its own later record-completion event. Confirm that the blank field was
   completed with the beneficiary, promised outcome, and every supplied
   service commitment affecting the bounded decision, including the exact
   **initial human contact within 30 minutes and on-site response within 4
   hours** commitments. Confirm the handoff lists every revised detail's exact
   literal filename, ID/version, and hash, plus the detached record and
   governing manifest filenames/hashes. Record initial, revised, and one-screen
   completion and verification timestamps, manifests, and detached records; do not let
   the handoff erase earlier evidence. This is a completeness check, not
   coaching about the failure decision.
8. Render the exact handoff Markdown to
   `WF-A-ONE-SCREEN-HANDOFF-v1.pdf` and complete
   `WF-A-HANDOFF-LAYOUT-PROOF-<attempt-id>-v1.md` from
   `07-handoff-layout-proof-record-template.md`. Preserve the command, tool
   versions, PDF, page count, and PDF hash. A favorable literal one-page result
   requires US Letter portrait, one page, margins >=0.5 inch, body/table text
   >=9 points, <=450 reader-facing words excluding only labeled immutable
   provenance, and no clipping, overlap, hidden overflow, or unreadable
   shrinking. Otherwise record layout `FAIL` and `HOLD`. Do not call this human
   comprehension evidence.
9. Complete material feedback, log
   `stage_a_material_feedback_completed`, then record exact Stage A end and
   append `stage_a_ended`. Do not treat the six scored freezes as full-route
   completion.

## Stage B sequence

1. Use a participant who did not create the Stage A artifact in a human run,
   or the separately declared Stage B synthetic actor in a synthetic run.
   Verify the selected Stage B context record; it must match the Stage A
   branch.
2. Record exact Stage B start, timezone, and route immediately before first
   packet read, then append `stage_b_started`.
3. Create and verify `WF-B-PHASE-1-INPUT-SHA256SUMS-v1.txt`, covering the
   completed handoff, its governing manifest and detached record, the route,
   and the blank workbook. Only then supply and open the handoff as the first
   scored content; its provenance files are unscored inputs. Export the
   completed handoff-only read-back as `WF-B-SECTION-1-v1.md` with its
   ID/version, completion
   timestamp/timezone, and `SECTION 1 COMPLETE` state. Create and verify
   `WF-B-SECTION-1-SHA256SUMS-v1.txt`; only afterward create
   `WF-B-SECTION-1-FREEZE-VERIFICATION-RECORD-v1.md` with the required
   identity, observed command/output/exit/timestamp/timezone, and later record-
   completion timestamp/timezone. Do this before supplying
   the scenario or detailed artifacts.
   Reject any unsupported business/domain noun or qualifier in Section 1.
   The reviewer may shorten or reorder the handoff, but must preserve or
   attribute its nouns. Freeze and retain any semantic invention as a scored
   deviation; never repair it silently.
4. Supply `02-scenario-and-task.md`, the detached revised freeze record, its
   governing revised-artifact manifest, and every handoff-linked revised detail
   under the exact literal local filename recorded by Stage A. Cross-check each
   filename, artifact ID/version, and SHA-256 value against both records. Do
   not rename, regenerate, summarize, or substitute any file. A missing or
   mismatched file stops the detailed read-back and is retained as a route
   deviation. Create and verify `WF-B-PHASE-2-INPUT-SHA256SUMS-v1.txt`, covering
   the Section 1 artifact, its manifest and detached record, and every newly
   released detailed input. After a complete match, have the participant
   complete Section 2 and export `WF-B-SECTION-2-v1.md` with its ID/version,
   completion timestamp/timezone, and `SECTION 2 COMPLETE` state. Create and
   verify `WF-B-SECTION-2-SHA256SUMS-v1.txt`; only afterward create
   `WF-B-SECTION-2-FREEZE-VERIFICATION-RECORD-v1.md` with every required field
   and its own later completion event. Finish this before either
   executive file is supplied or opened.
5. Only after the Section 2 freeze, supply `EXECUTIVE-DECISION-BRIEF.md` and
   then `VALUE-AND-EVIDENCE-LEDGER.md`. Create and verify
   `WF-B-PHASE-3-INPUT-SHA256SUMS-v1.txt`, covering the Section 2 artifact,
   manifest, detached record, and the two executive inputs. Have the
   participant complete Sections 3-5 and export `WF-B-SECTIONS-3-5-v1.md` with
   its ID/version, completion timestamp/timezone, and `SECTIONS 3-5 COMPLETE`
   state. Create and verify `WF-B-SECTIONS-3-5-SHA256SUMS-v1.txt`; only
   afterward create `WF-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD-v1.md`.
   Require every detached-record field and a record-completion time later than
   the observed manifest verification.
   Record each open time, pause, question, access issue, and intervention.
6. Keep the Stage A participant unavailable through the Sections 3-5 freeze.
   Score the frozen artifacts and append `stage_b_scoring_ended` before
   allowing explanation or repair.
7. Create and verify `WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt` over the Sections
   3–5 artifact, its governing manifest, its detached record, and
   `participant/07-stage-b-section-6-debrief.md`. Only after that gate complete
   Section 6, export `WF-B-SECTION-6-DEBRIEF-v1.md`, and append
   `stage_b_section_6_debrief_completed`. Debrief cannot rewrite or upgrade a
   frozen artifact or score.
8. Record exact Stage B end and append `stage_b_ended`. A post-freeze correction must preserve the prior
   artifact and record exact old/new immutable filenames and versions, reason,
   timestamp/timezone, old/new SHA-256 values, and old/new manifests. It is
   distinct from the planned live-update revision and stops the current
   attempt. The replacement is an immutable replacement artifact set,
   governing manifest, observed verification event, and detached record.

## Results, log close, and later external closeout

After `stage_b_ended`, complete the immutable run-specific
`WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md` from
`03-results-and-deviation-log.md`. Include the final pre-results log
checkpoint, six freeze chains, input/access/output counts, all boundaries and
debrief, interventions/deviations/stops/semantic inventions/layout failures,
scores, separate protocol/synthetic/layout/human/real-world states, decision,
and evidence limits. Do not predict the final closed-log hash or a future
closeout timestamp. Append `run_results_completed`; only then append
`run_log_closed`.

After close, validate the log, copy it without byte change into a dedicated
closeout input, create and verify
`WF-RUN-EXECUTION-ACCESS-LOG-SHA256SUMS-<attempt-id>.txt`, and complete
`WF-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md` from
`08-external-closeout-record-template.md`. The later record binds the actual
closed-log hash, external checksum-manifest hash, and run-results hash. Missing
external binding means the full route is not complete.

## Intervention levels

- **L0:** silence or think-aloud reminder;
- **L1:** repeat written text;
- **L2:** neutral probe such as “Who owns the tenant's unfinished outcome?”;
- **L3:** define a term without applying it; and
- **L4:** recommend or supply the decision.

L3 is aided. L4 contaminates the affected gate. Preserve the result.

## Stop conditions

Stop and retain partial evidence on consent withdrawal, confidential-data
disclosure, material unblinding, changed frozen bytes, distress, material tool
failure, or coaching that makes the central result uninterpretable.
