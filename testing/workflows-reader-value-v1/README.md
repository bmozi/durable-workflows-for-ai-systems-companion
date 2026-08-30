# Durable Workflows Reader-Value Pilot Packet

**Packet ID:** WF-RV-PILOT-001
**Version:** 1.2.2
**Status:** Prepared and unrun; no participant recruited or consented
**Scenario:** Meadowline Housing, entirely fictional

## Version and evidence note

Version 1.2.2 repairs a temporal self-reference defect in version 1.2.1's
freeze procedure. A governed artifact now records only its completion state
and completion time. A governing manifest then hashes those completed bytes,
is verified at an exact timestamp and timezone, and only afterward is a
detached freeze-verification record written to describe the observed
verification event. The governing manifest never hashes itself or that later
record. The next sealed phase-input manifest hashes the completed artifacts,
their governing manifest, and the detached record. The same sequence now
governs initial and revised Stage A details, the handoff, and all three Stage B output
freezes. The audit and synthetic regressions were defect-finding only: none
was a human or practitioner session, and none establishes usability, safety,
effectiveness, value, or an actual-system result. Version 1.2.2 remains
**PREPARED/UNRUN** for people.

## Sealed flat run input

Before either stage, copy the exact authorized source bytes into a new sealed,
flat run-input directory. Keep every delivery filename exactly as named below;
do not substitute a shortcut, repository path, generated copy, or renamed
file. Hash every supplied file in a run-specific SHA-256 manifest before the
participant begins. The facilitator records the manifest and supplies files
only in the route's order. A byte change requires a new immutable filename,
completion timestamp, version, manifest, verification event, and detached
record; a meaning change also requires a new packet version. A manifest hashes
only already-completed governed files and never itself or a later record.

## What this packet tests

This packet tests whether the Workflows companion helps a reader move through
the complete value chain:

`RECOGNIZE A PROMISE OVER TIME -> NAME THE OWNER -> RECORD PROGRESS ->`
`HANDLE AMBIGUITY AND FAILURE -> PROVE THE OUTCOME -> HAND OFF A DECISION`

It does not convert the existing Northbridge or Aster Vale examples into
practitioner evidence. This is a separate, checksum-locked protocol for the
reader routes, gateway brief, failure tools, value ledger, and executive
decision language.

## Two stages

### Stage A — practitioner

Supply only these exact local filenames from the sealed flat run input:

1. `01-consent-and-privacy.md`
2. `00-packet-route.md`
3. `02-scenario-and-task.md`
4. `03-practitioner-workbook.md`
5. `START-HERE.md`
6. `workflow-responsibility-and-progress-brief.md`
7. `compensation-and-failure-matrix.md`
8. `time-and-failure-test-plan.md`
9. `06-revised-artifact-freeze-record.md`
10. `05-one-screen-handoff.md`

Follow the route exactly: recognition comes before companion assets; the
initial detailed artifact is frozen before the live update; the live update
creates the planned revised detail set; and a detached revised-detail freeze
record is completed before the one-screen handoff is opened. The required
revised-detail output names are:

1. `WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md`;
2. `WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md`;
3. `WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md`; and
4. `WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md`.

The governing manifest is
`WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and the detached record is
`WF-A-REVISED-FREEZE-RECORD-v1.md`. The manifest hashes the four revised
details, not itself or the later record. Verify the manifest and capture the
exact verification timestamp/timezone before writing the detached record.
Then create `WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt`, which hashes the four
artifacts, their governing manifest, the detached record, and the blank
handoff input. Do not supply completed examples, follow omitted links,
or supply the repository Failure Lab, facilitator materials, executive brief,
or value ledger during Stage A. Miniature examples embedded inside an
authorized asset remain part of that asset; full worked examples linked from
it are withheld.

### Stage B — independent decision owner

Supply these exact local filenames from a separately frozen Stage B flat run
input:

1. `01-consent-and-privacy.md`;
2. `00-packet-route.md`;
3. the frozen `WF-A-ONE-SCREEN-HANDOFF-v1.md` as the first scored content;
4. `WF-A-HANDOFF-SHA256SUMS-v1.txt`,
   `WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md`, and
   `04-decision-owner-workbook.md`;
5. `02-scenario-and-task.md`, every frozen, unchanged revised Stage A detail
   under the exact literal local filename recorded in the handoff,
   `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and
   `WF-A-REVISED-FREEZE-RECORD-v1.md`;
6. `EXECUTIVE-DECISION-BRIEF.md`; and
7. `VALUE-AND-EVIDENCE-LEDGER.md`.

Use a different person for Stage B during the first calibration round. Do not
let the Stage A participant explain or repair the artifact during the initial
read-back. Freeze the handoff-only read-back before supplying the scenario or
detailed artifacts. At the detailed release, verify that every handoff-linked
filename, artifact ID/version, and SHA-256 value matches the detached freeze
record and governing manifest. Do not rename, regenerate, summarize, or
substitute an artifact. Each freeze exports the completed section or section
set as its own immutable artifact. Complete Section 2 and finish its
manifest-verification/detached-record sequence before
supplying `EXECUTIVE-DECISION-BRIEF.md` or `VALUE-AND-EVIDENCE-LEDGER.md`. Open
those two files in that order, complete Sections 3-5, and freeze the bounded
decision before debrief. Each Stage B output records completion before its
governing manifest is created. The manifest is verified with an exact
timestamp/timezone, and a detached freeze-verification record is then created.
The next phase-input manifest hashes the completed output, governing manifest,
detached record, and newly released inputs. Any correction after a claimed freeze receives a new
immutable filename, artifact version, timestamp with timezone, SHA-256 value,
manifest, and reason; retain the old file and record, stop the attempt, and do
not proceed to Stage B. The planned live-update revision is not a correction to
frozen revised bytes. Supply no other files or omitted links.

## Facilitator only

- [Facilitator guide](facilitator-only/01-facilitator-guide.md)
- [Observation and scoring rubric](facilitator-only/02-observation-and-scoring-rubric.md)
- [Results and deviation log](facilitator-only/03-results-and-deviation-log.md)
- [Freeze-verification and correction record templates](facilitator-only/04-freeze-and-correction-record-templates.md)

Never supply these files before either scored stage ends.

## Execution prerequisites

Before recruitment:

1. assign an accountable execution owner;
2. approve storage, access, retention, redaction, and deletion;
3. decide whether further ethics, legal, privacy, or organizational review is
   required;
4. copy each exact named file into a sealed flat run-input directory without
   changing its bytes or filename;
5. record every supplied file's SHA-256 value in a run-specific evidence
   manifest that does not list itself;
6. keep scheduling identity separate from participant codes; and
7. assign a facilitator and evaluator with disclosed relationships.

The checked-in `SHA256SUMS` records the prepared source packet. A run-specific
copy must also hash every supplied referenced asset. Any byte change requires a
new manifest and, when meaning changes, a new packet version.

## Temporal sealing rule

[`TEMPORAL-FREEZE-PROTOCOL.json`](TEMPORAL-FREEZE-PROTOCOL.json) is the
machine-readable canonical inventory for the six output freezes, five
next-release triples, completion states, correction rules, artifact bindings,
and results rows. Reader-facing instructions must agree with that inventory;
the repository validator also checks reviewed protocol-document hashes so a
prose change cannot silently bypass structural review.

For every initial-detail, revised-detail, handoff, or Stage B section freeze,
use this order:

1. finish the governed artifact and record its ID, version, exact completion
   timestamp/timezone, and `COMPLETE` state inside its own bytes;
2. create a governing SHA-256 manifest that lists only those completed
   governed artifacts;
3. verify that manifest from the sealed directory and capture the exact
   verification timestamp/timezone; and
4. create a detached freeze-verification record describing that observed
   event, including literal filenames, IDs, versions, artifact hashes, and the
   governing manifest's filename and hash.

The governing manifest cannot include the later detached record. The next
sealed phase-input manifest must include the governed artifacts, the governing
manifest, and the detached record. See
[`TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md`](TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md)
for the static protocol check and
[`facilitator-only/04-freeze-and-correction-record-templates.md`](facilitator-only/04-freeze-and-correction-record-templates.md)
for run-record schemas.

## Evidence boundary

A completed pair can reveal wording defects, unsafe interpretations, transfer
failures, and useful behavior for the exact participants and materials. It
cannot prove workflow correctness, reliable recovery, business value, broad
usability, or publication readiness.
