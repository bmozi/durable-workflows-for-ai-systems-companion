# Durable Workflows Reader-Value Pilot Packet

**Packet ID:** WF-RV-PILOT-001
**Version:** 1.2.5
**Status:** Prepared and unrun; no participant recruited or consented
**Scenario:** Meadowline Housing, entirely fictional

## Version and evidence note

Version 1.2.5 is a separate, non-amended successor to version 1.2.4. It retains
version 1.2.3's six non-self-referential scored freeze
chains and repairs full-route closure gaps found by an independent synthetic
replay. Every detached record
must now identify the attempt, phase, and facilitator/actor; preserve the
literal manifest-verification command, observed standard output and standard
error, exit status, timestamp, and timezone; and record its own later
completion timestamp and timezone. A separate facilitator-only, item-by-item
execution/access log binds each event to the preceding event. It records the
ordered manifest gates, releases, opens, completed reads, artifact
completions, manifest creation and verification, and detached-record
completion. It is evidence about the route, not an instruction supplied to a
participant.

The retained synthetic replay was defect-finding only. Its frozen Stage B
Section 1 introduced the unsupported business/domain noun `billing`; that
defect remains frozen evidence and is not rewritten. Version 1.2.4 turned the
lesson into a permanent semantic-transfer rejection rule. The replay was not
a human or practitioner session and establishes no usability, safety,
effectiveness, value, or actual-system result. Human testing remains
**PREPARED/UNRUN**, human comprehension remains **UNRUN**, and real-world
evidence remains **UNRUN**.

## Mutually exclusive entry branch

Before starting the run log or opening scored input, select exactly one branch.
The first two semantic log events are exactly
`entry_branch_selected` -> `run_log_started`, in that order:

1. **Human:** complete the human-branch consent record from
   `participant/01-consent-and-privacy.md`; or
2. **Synthetic:** complete and verify
   `WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md` from the facilitator-only
   synthetic template, including the exact statement
   `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`.

Never mix the branches. A synthetic run must not complete a human consent
record or claim human consent, comprehension, usability, practitioner
behavior, or a human result. Verify the selected entry-context bytes before
both `stage_a_started` and `stage_b_started`.

## Sealed flat run input

Before each staged release, copy only the exact authorized source bytes for
that release into a new sealed, flat phase-input directory. Keep every
delivery filename exactly as declared by the canonical protocol; do not
substitute a shortcut, repository path, generated copy, renamed file, hidden
prompt, or orchestration note. An undeclared file fails the release. In
particular, `ORCHESTRATION.md`, facilitator instructions, and the
facilitator-only execution/access log must never enter sealed participant
input. Hash every declared file in the phase's run-specific SHA-256 manifest,
verify it, and log the gate before any file is released, opened, or read. A
byte change requires a new immutable filename, completion timestamp, version,
manifest, verification event, and detached record; a meaning change also
requires a new packet version. A governing manifest hashes only already-
completed governed files and never itself or a later record.

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

1. the selected, verified entry-context record;
2. `00-packet-route.md`;
3. `02-scenario-and-task.md`;
4. `03-practitioner-workbook.md`;
5. `START-HERE.md`;
6. `workflow-responsibility-and-progress-brief.md`;
7. `compensation-and-failure-matrix.md`;
8. `time-and-failure-test-plan.md`;
9. `06-revised-artifact-freeze-record.md`; and
10. `05-one-screen-handoff.md`.

Follow the route exactly: recognition comes before companion assets; the
initial detailed artifact is frozen before the live update; the live update
creates the planned revised detail set; and a detached revised-detail freeze
record is completed before the one-screen handoff is opened. The required
initial-detail output names are
`WF-A-INITIAL-PRACTITIONER-WORKBOOK-v1.md`,
`WF-A-INITIAL-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md`,
`WF-A-INITIAL-COMPENSATION-AND-FAILURE-MATRIX-v1.md`, and
`WF-A-INITIAL-TIME-AND-FAILURE-TEST-PLAN-v1.md`. The required
revised-detail output names are:

1. `WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md`;
2. `WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md`;
3. `WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md`; and
4. `WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md`.

The governing manifest is
`WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and the detached record is
`WF-A-REVISED-FREEZE-RECORD-v1.md`. The manifest hashes the four revised
details, not itself or the later record. Verify the manifest and capture the
literal command, observed standard output and standard error, exit status,
exact verification timestamp, and timezone before writing the detached
record. Complete that record at a later exact timestamp/timezone; a record
without both events is incomplete.
Then create `WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt`, which hashes the four
artifacts, their governing manifest, the detached record, and the blank
handoff input. Do not supply completed examples, follow omitted links,
or supply the repository Failure Lab, facilitator materials, executive brief,
or value ledger during Stage A. Miniature examples embedded inside an
authorized asset remain part of that asset; full worked examples linked from
it are withheld.

After the handoff freeze, render the exact Markdown to
`WF-A-ONE-SCREEN-HANDOFF-v1.pdf` and complete the layout proof record. A
favorable one-page claim requires exactly one US Letter portrait page, every
margin at least 0.5 inch, all body and table text at least 9 points, at most
450 reader-facing words excluding only labeled immutable provenance, and no
clipping, overlap, hidden overflow, or unreadable shrinking. Layout PASS is
not human comprehension evidence. Log Stage A material-feedback completion
and `stage_a_ended`; the three Stage A freezes alone do not close Stage A.

### Stage B — independent decision owner

Supply these exact local filenames from a separately frozen Stage B flat run
input:

1. the matching selected, verified entry-context record;
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
decision before debrief. Section 1 must preserve or explicitly attribute the
handoff's business/domain nouns; an unsupported noun invention is a retained
deviation and scores zero on the affected semantic item. Each Stage B output
records completion before its
governing manifest is created. The manifest is verified with an exact
timestamp/timezone, and a detached freeze-verification record is then created.
The next phase-input manifest hashes the completed output, governing manifest,
detached record, and newly released inputs. Any correction after a claimed freeze receives a new
immutable filename, artifact version, timestamp with timezone, SHA-256 value,
manifest, and reason; retain the old file and record, stop the attempt, and do
not proceed to Stage B. The planned live-update revision is not a correction to
frozen revised bytes. Supply no other files or omitted links.

After the sixth scored freeze, log `stage_b_scoring_ended`, create and verify
`WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt`, complete
`WF-B-SECTION-6-DEBRIEF-v1.md`, and log `stage_b_ended`. Debrief cannot change
the six frozen scores or outputs. Complete the immutable run-specific results
as `WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md` before
`run_log_closed`; it may record the final pre-results log checkpoint but must
not predict the future closed-log hash or closeout time. After log close, bind
the actual results hash, closed-log hash, byte-identical external copy, and
external checksum-manifest hash in
`WF-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md`.

## Facilitator only

- [Facilitator guide](facilitator-only/01-facilitator-guide.md)
- [Observation and scoring rubric](facilitator-only/02-observation-and-scoring-rubric.md)
- [Results and deviation log](facilitator-only/03-results-and-deviation-log.md)
- [Freeze-verification and correction record templates](facilitator-only/04-freeze-and-correction-record-templates.md)
- [Run execution and access log schema](facilitator-only/05-run-execution-and-access-log-schema.md)
- [Synthetic context record template](facilitator-only/06-synthetic-context-record-template.md)
- [Handoff layout proof record template](facilitator-only/07-handoff-layout-proof-record-template.md)
- [External closeout record template](facilitator-only/08-external-closeout-record-template.md)

Keep these files outside every sealed participant-input directory. Never
supply them during either scored stage.

## Execution prerequisites

Before recruitment:

1. assign an accountable execution owner;
2. approve storage, access, retention, redaction, and deletion;
3. decide whether further ethics, legal, privacy, or organizational review is
   required;
4. create a new sealed flat phase-input directory for each staged release,
   containing every and only the canonical inventory's declared files;
5. record every supplied file's SHA-256 value in a run-specific evidence
   manifest that does not list itself, and reject an undeclared file;
6. select exactly one entry branch and append `entry_branch_selected` as the
   genesis semantic event;
7. append `run_log_started` immediately afterward, keep the facilitator-only
   execution/access log outside participant input, and bind every later event
   to the preceding event;
8. keep scheduling identity separate from participant codes; and
9. assign a facilitator and evaluator with disclosed relationships.

The checked-in `SHA256SUMS` records the prepared source packet. A run-specific
copy must also hash every supplied referenced asset. Any byte change requires a
new manifest and, when meaning changes, a new packet version.

## Temporal sealing rule

[`TEMPORAL-FREEZE-PROTOCOL.json`](TEMPORAL-FREEZE-PROTOCOL.json) is the
machine-readable canonical inventory for the six scored freeze chains, six
next-release triples, mutually exclusive entry branches, full-route
boundaries, completion states, detached-record schema, sealed
participant inputs, facilitator execution/access events, correction rules,
layout proof, debrief, immutable results, external closeout, semantic transfer,
artifact bindings, and results rows. Reader-facing instructions must agree
with that inventory;
the repository validator also checks reviewed protocol-document hashes so a
prose change cannot silently bypass structural review.

For every initial-detail, revised-detail, handoff, or Stage B section freeze,
use this order:

1. finish the governed artifact and record its ID, version, exact completion
   timestamp/timezone, and `COMPLETE` state inside its own bytes;
2. create a governing SHA-256 manifest that lists only those completed
   governed artifacts;
3. verify that manifest from the sealed directory and capture the literal
   command, observed standard output and standard error, exit status, exact
   verification timestamp, and timezone; and
4. create a detached freeze-verification record describing that observed
   event, including attempt ID, phase, facilitator/actor code, literal
   filenames, IDs, versions, artifact hashes, the governing manifest's
   filename and hash, and its own later exact completion timestamp/timezone.

The governing manifest cannot include the later detached record. The next
sealed phase-input manifest must include the governed artifacts, the governing
manifest, and the completed detached record. The facilitator-only event log
must show the same order, include every release/open/completed read, and remain
outside participant input. See
[`TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md`](TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md)
for the static protocol check and
[`facilitator-only/04-freeze-and-correction-record-templates.md`](facilitator-only/04-freeze-and-correction-record-templates.md)
for run-record schemas.

## Evidence boundary

A completed pair can reveal wording defects, unsafe interpretations, transfer
failures, and useful behavior for the exact participants and materials. It
cannot prove workflow correctness, reliable recovery, business value, broad
usability, or publication readiness.
