# Facilitator Guide

**Packet:** WF-RV-PILOT-001 version 1.2.3
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

## Stage A sequence

1. Complete the consent prerequisites and obtain human consent. A blank field
   means do not start.
2. Record exact Stage A start, timezone, and supplied-file route immediately
   before the participant's first packet read.
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
8. Record exact Stage A end.

## Stage B sequence

1. Use a participant who did not create the Stage A artifact. Complete consent
   before beginning.
2. Record exact Stage B start, timezone, and route immediately before first
   packet read.
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
   End scoring before allowing explanation or repair. Section 6 is debrief.
7. Record exact Stage B end. A post-freeze correction must preserve the prior
   artifact and record exact old/new immutable filenames and versions, reason,
   timestamp/timezone, old/new SHA-256 values, and old/new manifests. It is
   distinct from the planned live-update revision and stops the current
   attempt. The replacement is an immutable replacement artifact set,
   governing manifest, observed verification event, and detached record.

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
