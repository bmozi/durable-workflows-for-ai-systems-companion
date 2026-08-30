# Exact Packet Route

**Packet:** WF-RV-PILOT-001 version 1.2.2
**Status:** Prepared and unrun; this route records no human result

## Before either stage

The facilitator must complete the execution-owner, storage, access, retention,
deletion, withdrawal, and recording fields in the consent notice. The human
participant must review and affirm that notice before scored work begins. A
blank prerequisite or missing consent means **do not start**.

Use only the exact local filenames named below in the sealed flat run input.
Do not follow a link unless this route names the linked file. Do not omit,
replace, rename, summarize, or add a file. Record any access problem, question,
pause, or facilitator intervention; do not silently repair the route. The
run-specific manifest must hash every supplied file before scored work begins.
A governing manifest hashes only already-completed governed artifacts; it does
not hash itself or the later detached record that describes its verification.
The next phase-input manifest hashes the completed artifacts, prior governing
manifest, detached verification record, and any newly released inputs.

## Stage A — exact read and work order

1. Complete [Consent and Privacy](01-consent-and-privacy.md) before scored work.
2. Immediately before first reading this route, record the exact Stage A start
   timestamp and timezone in the practitioner workbook and facilitator log.
3. Read this route, then [Scenario and Task](02-scenario-and-task.md).
4. Open the [Practitioner Workbook](03-practitioner-workbook.md) and complete
   Section 1, **Recognition before terminology**, without companion assets.
5. Open only these assets, in order:
   `START-HERE.md`,
   `workflow-responsibility-and-progress-brief.md`,
   `compensation-and-failure-matrix.md`,
   and `time-and-failure-test-plan.md`.
6. Complete the detailed workbook and relevant portions of the supplied blank
   assets. Do not open linked completed examples, the Failure Lab, executive
   files, or facilitator files.
   A miniature example embedded inside a supplied asset may be read because it
   is part of the supplied file; a linked full worked example is withheld.
7. Complete the initial workbook and detailed artifacts with IDs, versions,
   exact completion timestamps/timezones, and `INITIAL COMPLETE` state. Create
   and verify `WF-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`, then create the
   detached `WF-A-INITIAL-FREEZE-VERIFICATION-RECORD-v1.md` from that observed
   verification event. Do not add the later record to the earlier manifest.
8. The facilitator exports the exact authorized update as
   `WF-A-LIVE-UPDATE-v1.md` and creates
   `WF-A-LIVE-UPDATE-INPUT-SHA256SUMS-v1.txt`, hashing the initial artifacts,
   their governing manifest and detached record, and the update file. Verify
   that phase-input manifest before opening or reading the update. Then receive
   the update and record it exactly; revise only after the initial freeze.
9. Export the revised detail set under these exact immutable local filenames:
   `WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md`,
   `WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md`,
   `WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md`, and
   `WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md`. Create
   an artifact header in each file with its ID/version, exact completion timestamp
   and timezone, and state `REVISED COMPLETE`; complete that header before hashing. Then create
   `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, listing each of those four
   filenames and hashes but not the manifest itself or any later verification
   record. Verify the manifest from the sealed directory and capture the exact
   verification timestamp and timezone.
10. Complete [Revised Artifact Freeze Record](06-revised-artifact-freeze-record.md)
    and export it as `WF-A-REVISED-FREEZE-RECORD-v1.md`. It must record the
    exact observed manifest-verification timestamp and timezone; every revised artifact's exact local
    filename, ID/version, artifact-stated completion timestamp/timezone, and
    SHA-256 value; and the governing manifest's exact filename and SHA-256
    value. This record is written only after successful manifest verification
    and is not listed in that earlier manifest. Confirm every revised
    artifact's own state is `REVISED COMPLETE`. If any
    listed artifact still says `PENDING`, `AWAITING FREEZE`, or anything other
    than `REVISED COMPLETE`, do not open the handoff.
11. Create and verify `WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt`, hashing the four
    completed revised artifacts, `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`,
    `WF-A-REVISED-FREEZE-RECORD-v1.md`, and the blank handoff input. Only then
    open and complete the
    blank [One-Screen Decision Handoff](05-one-screen-handoff.md). Export it as
    `WF-A-ONE-SCREEN-HANDOFF-v1.md`, link every revised detail by the same exact
    literal filename, ID/version, and hash, and name the governing manifest and
    detached freeze record. Add the handoff's ID/version, exact completion
    timestamp/timezone, and `HANDOFF COMPLETE` state before hashing. Create
    `WF-A-HANDOFF-SHA256SUMS-v1.txt`, which hashes only the completed handoff;
    verify it and capture the exact timestamp/timezone; then create
    `WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md`. Include the
    beneficiary, promised outcome, and every supplied service commitment that
    affects the bounded decision, including Meadowline's exact **initial human
    contact within 30 minutes and on-site response within 4 hours**. Do not invent an
    owner, authority, date, number, or evidence source: use `UNASSIGNED` or
    `UNKNOWN` where appropriate and an evidence-based trigger when no honest
    date exists.
12. Complete material feedback and record the exact Stage A end timestamp.

## Stage B — exact read and work order

1. Complete [Consent and Privacy](01-consent-and-privacy.md) before scored work.
2. Immediately before first reading this route, record the exact Stage B start
   timestamp and timezone in the decision-owner workbook and facilitator log.
3. Read this route. Before the handoff is opened, verify
   `WF-B-PHASE-1-INPUT-SHA256SUMS-v1.txt`, which hashes the completed handoff,
   its governing manifest and detached verification record, this route, and
   the blank workbook. Then receive `WF-A-ONE-SCREEN-HANDOFF-v1.md` as the
   first scored content. Do not receive the scenario, revised-detail detached
   record, revised-detail governing manifest, or detailed artifacts yet.
4. Open the [Decision-Owner Workbook](04-decision-owner-workbook.md). Complete
   Section 1, the handoff-only read-back and
   scanability finding, without Stage A explanation or repair. Export it as
   `WF-B-SECTION-1-v1.md` with ID/version, completion timestamp/timezone, and
   `SECTION 1 COMPLETE`. Create `WF-B-SECTION-1-SHA256SUMS-v1.txt`, verify it,
   capture the verification timestamp/timezone, and then create
   `WF-B-SECTION-1-FREEZE-VERIFICATION-RECORD-v1.md`.
5. Receive `02-scenario-and-task.md`,
   `WF-A-REVISED-FREEZE-RECORD-v1.md`,
   `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and every unchanged revised
   Stage A detail named in the handoff. Each detail must arrive under the exact
   literal local filename recorded in the handoff. Verify filename,
   artifact ID/version, and SHA-256 value against both the detached freeze
   record and governing manifest. No renamed, regenerated, summarized, or
   substituted copy is permitted. A missing or mismatched file is a route
   deviation: stop the detailed read-back and retain the evidence.
6. Before reading detail, verify `WF-B-PHASE-2-INPUT-SHA256SUMS-v1.txt`. It must
   hash the Section 1 artifact, its governing manifest and detached record,
   plus the scenario, all four revised artifacts, their governing manifest,
   and their detached record. Complete Section 2, the detailed read-back.
   Export it as `WF-B-SECTION-2-v1.md` with ID/version, completion
   timestamp/timezone, and `SECTION 2 COMPLETE`. Create and verify
   `WF-B-SECTION-2-SHA256SUMS-v1.txt`; then create
   `WF-B-SECTION-2-FREEZE-VERIFICATION-RECORD-v1.md` from the observed
   verification event before receiving or opening either executive file.
7. Receive `EXECUTIVE-DECISION-BRIEF.md` and
   `VALUE-AND-EVIDENCE-LEDGER.md`. Verify
   `WF-B-PHASE-3-INPUT-SHA256SUMS-v1.txt`, which hashes the Section 2 artifact,
   its governing manifest and detached record, and both executive inputs.
   Only then open the two executive files in that order and complete Sections
   3-5. Export them as `WF-B-SECTIONS-3-5-v1.md`. Add ID/version, completion
   timestamp/timezone, and `SECTIONS 3-5 COMPLETE` to
   the exported artifact. Create and verify
   `WF-B-SECTIONS-3-5-SHA256SUMS-v1.txt`, then create
   `WF-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD-v1.md` before debrief.
8. Only after scoring ends may the Stage A practitioner explain anything.
   Complete Section 6 as debrief and record the exact Stage B end time.

The revision after the planned live update creates the first revised detail
set; it is not a correction to already frozen revised bytes. Every claimed
freeze is immutable. If already frozen revised bytes require correction,
retain every old file and create a new immutable filename and version. Record
the exact old and new filenames, artifact IDs/versions, old and new SHA-256
values, governing manifests, reason, and correction timestamp/timezone. A
post-freeze correction stops this attempt; do not proceed to Stage B. Start a
fresh attempt from a newly sealed input after authorized review. Never silently
replace frozen bytes, and never require a manifest to hash itself or its later
detached verification record. A replacement uses a new immutable artifact
set, governing manifest, verification event, and detached record.

Synthetic route preflight may identify wording or routing defects, but it is
not human consent, practitioner validation, or evidence that the packet is
usable, safe, effective, or valuable.
