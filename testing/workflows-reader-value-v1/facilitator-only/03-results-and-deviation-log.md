# Results and Deviation Log

**Packet:** WF-RV-PILOT-001 version 1.2.5
**Status:** Blank controlled source template; no run result exists

Export the immutable run result as
`WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md`. Complete its final bytes
after Stage B end and before `run_results_completed` and `run_log_closed`.
This record may bind the final pre-results log checkpoint; it must not predict
the future final closed-log hash or a future external closeout timestamp.

## Run identity

- Attempt ID:
- Exact filename:
  `WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md`
- Artifact ID/version: `WF-RUN-RESULTS-AND-DEVIATIONS/v1`
- Packet ID/version: `WF-RV-PILOT-001` / `1.2.5`
- Entry branch: human / synthetic
- Execution owner and authorization:
- Stage A participant code:
- Stage B reviewer code:
- Facilitator:
- Evaluator and independence disclosure:
- Date, mode, and timezone:
- Record completion timestamp/timezone:
- State: `RUN RESULTS COMPLETE` / invalid

## Entry context, privacy, and freeze

- Branch-selection event ID and exact line-byte SHA-256:
- Human Stage A/Stage B consent filenames/hashes, or `NOT APPLICABLE`:
- Synthetic context filename/hash, or `NOT APPLICABLE`:
- Branches mutually exclusive and stage context gates matched: yes / no / deviation
- Synthetic context contains no human-consent or human-result claim: yes / no / not synthetic
- Storage/access/retention authority:
- Run-specific SHA-256 manifest:
- Prepared-source manifest match:
- Supplied and withheld materials correct: yes / no / deviation
- Every sealed phase input contains only canonical declared files: yes / no / deviation
- Undeclared orchestration, hidden instruction, or facilitator file found:
- Confidentiality or privacy concern:

## Facilitator execution/access log identity

- JSONL exact filename: `WF-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl`
- Kept outside every participant-input directory: yes / no / deviation
- Attempt ID constant and event IDs unique: yes / no / deviation
- Sequence contiguous from 1 and each event binds the prior ID/hash: yes / no / deviation
- First two semantic events are `entry_branch_selected` -> `run_log_started`: yes / no / deviation
- Branch-selection event is sequence 1 with `GENESIS` prior bindings: yes / no / deviation
- Each file separately logged as released, opened, and read: yes / no / deviation
- Ordered manifest and freeze gates complete: yes / no / deviation
- Final pre-results log checkpoint event ID and exact line-byte SHA-256:
- Final pre-results checkpoint timestamp/timezone:

Do not place the final closed-log hash, external checksum-manifest hash, or a
future closeout timestamp in this record. Those later facts belong only in
`WF-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md`.

## Exact starts, file route, questions, pauses, and interventions

- Exact Stage A start before first scored read of the packet route, with timezone:
- Stage A start event ID/line hash:
- Stage A material-feedback completion event ID/line hash:
- Exact Stage A end and end event ID/line hash:
- Exact Stage B start before first scored read of the packet route, with timezone:
- Stage B start event ID/line hash:
- Exact scoring end and event ID/line hash:
- Debrief-input manifest verification event ID/line hash:
- Section 6 debrief completion event ID/line hash:
- Exact Stage B end and end event ID/line hash:

| Time | Stage | File opened or activity | Route position | Question/pause/access issue | Intervention and level | Interpretation effect |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

No coaching is allowed. Repeating text or resolving access is still logged.
Supplying an owner, authority, approval field, number, date, evidence source,
state interpretation, or answer contaminates the affected gate. This readable
table does not replace the item-by-item JSONL execution/access log.

## Timing and freezes

| Stage/activity | Exact start | Exact end | Elapsed | Artifact IDs/manifest or notes |
| --- | --- | --- | ---: | --- |
| A recognition before assets | | | | |
| A detailed work | | | | |
| A initial completion / manifest verification / detached record | | | | |
| A live update | | | | |
| A revised completion / manifest verification / detached record | | | | |
| A handoff-input manifest verification | | | | |
| A one-screen handoff completion / manifest verification / detached record | | | | |
| B Phase 1 input verification; Section 1 completion / manifest verification / detached record | | | | |
| B Phase 2 input verification; Section 2 completion / manifest verification / detached record | | | | |
| B executive files opened | | | | |
| B Phase 3 input verification; Sections 3-5 completion / manifest verification / detached record | | | | |
| B scoring end | | | | |
| B debrief-input manifest verification | | | | |
| B Section 6 debrief | | | | |
| B stage end | | | | |
| Run-results completion | | | | |

The live-update revision is planned and must be logged separately from any
later correction of already frozen revised bytes. For every post-freeze
correction, retain the prior artifact and record the reason,
timestamp/timezone, exact old/new immutable filenames, artifact IDs/versions,
old/new SHA-256 values, and old/new manifests in Deviations and stops. A
post-freeze correction stops the current attempt. A governing manifest hashes
only completed governed artifacts, never itself or its later detached record.
The replacement must be a new immutable set, manifest, verification event, and
detached record.

## Revised-detail and Stage B transfer verification

- Revised governing artifacts completed before hashing: yes / no / deviation
- Revised manifest verification timestamp and timezone:
- Revised governing manifest exact filename and SHA-256:
- Detached freeze-verification record completion timestamp/timezone and SHA-256:
- Handoff-input manifest exact filename/hash and verification time/timezone:
- Every revised detail state before hashing is `REVISED COMPLETE`: yes / no / deviation
- Any `PENDING` or `AWAITING FREEZE` state retained after freeze:

| Handoff-linked exact local filename | Artifact ID/version | Artifact-stated completion timestamp/timezone and `REVISED COMPLETE` state | SHA-256 | Matched detached record | Matched manifest | Supplied to Stage B under same filename |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

A rename, regenerated copy, summary, substitution, missing governing manifest,
or mismatch stops the detailed Stage B read-back and is recorded below.

## Temporal freeze chain

| Output phase | Completed artifact filename + ID/version + completion time/state | Governing manifest filename/hash | Literal manifest-verification command + observed stdout/stderr + exit status + exact timestamp/timezone | Detached record filename/hash + attempt/phase/actor + later completion timestamp/timezone | Next phase-input manifest filename/hash + verification time |
| --- | --- | --- | --- | --- | --- |
| Initial Stage A | | | | | |
| Revised Stage A | | | | | |
| Handoff | | | | | |
| Stage B Section 1 | | | | | |
| Stage B Section 2 | | | | | |
| Stage B Sections 3-5 | | | | | `WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt` |

The detached record must be created after the manifest verification it
describes. A row is invalid if the record omits attempt ID, canonical phase,
facilitator/actor code, literal command, observed standard output and standard
error, integer exit status, verification timestamp/timezone, or its own later
completion timestamp/timezone. A row is also invalid if a governed manifest
lists itself or the later record, or if a governed artifact embeds its own
hash or future verification time.

## Route counts and full-closure checkpoints

- Declared participant-input file count:
- Released/opened/completed-read counts:
- Governed artifact count:
- Manifest-verification count:
- Detached-record count:
- Six scored freeze chains complete: yes / no / stopped
- Stage A start/feedback/end complete: yes / no / deviation
- Stage B start/scoring-end/debrief/end complete: yes / no / deviation
- Run results completed before log close: yes / no / deviation
- External closeout state at this earlier result time:
  `PENDING — MUST BE COMPLETED AFTER LOG CLOSE`

## Handoff layout proof

- Markdown filename/hash:
- PDF filename/hash:
- Layout-proof record filename/hash:
- Rendering command and tool versions:
- US Letter portrait: yes / no
- Page count:
- Margins all >=0.5 inch: yes / no
- Body/table text >=9 points: yes / no
- Reader-facing words excluding labeled immutable provenance:
- No clipping/overlap/hidden overflow/unreadable shrinking: yes / no
- Literal one-page state: `PASS` / `FAIL` / `UNRUN`
- Human comprehension state: separately `UNRUN` unless a consented human route
  actually supplied evidence

## Separate evidence states

| Dimension | State | Exact evidence | Limits |
| --- | --- | --- | --- |
| Protocol integrity | | | |
| Synthetic behavior | `UNRUN` unless synthetic branch completed | | Not human evidence |
| Layout | `PASS` / `FAIL` / `UNRUN` | | Not comprehension evidence |
| Human comprehension/usability | `PREPARED/UNRUN` unless human branch completed | | No synthetic promotion |
| Real-world evidence | `UNRUN` | | No implementation, safety, cost, value, or outcome inference |

## Gate results

| Gate | Score/state | Exact evidence | Negative or boundary finding |
| --- | --- | --- | --- |
| RV-1 | | | |
| RV-2 | | | |
| RV-3 | | | |
| RV-4 | | | |
| RV-5 | | | |
| RV-6 | | | |
| RV-7 | | | |

## Deviations and stops

| ID | Condition/reason and correction timestamp/timezone | Prior immutable artifact set + manifest + detached record | Replacement artifact set + manifest + observed verification event + detached record + next-phase manifest | Action and interpretation effect |
| --- | --- | --- | --- | --- |
| | | | | |

Record every rejected entry branch, branch mix, synthetic human-result claim,
missing boundary, premature debrief, semantic invention, layout failure,
premature close attempt, and unexplained variance. An unsupported
handoff-to-Section-1 business/domain noun is a retained semantic invention and
scores zero for the affected behavior; do not rewrite the frozen output.

## Findings and disposition

| ID | Finding | Source | Severity | Revise / retest / hold / remove | Owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Truthful state statement

- Six freeze chains state: complete / incomplete / stopped
- Full selected route before close: complete / incomplete / stopped
- Synthetic behavior state: passed / partial / failed / unrun / not applicable
- Layout state: passed / failed / unrun
- Human evidence state: passed / partial / failed / `PREPARED/UNRUN`
- Real-world evidence state: `UNRUN`
- What this exact pair establishes:
- What it does not establish:
- Packet state after authorized review:
- Files changed only after raw evidence was preserved:
- Next attempt and version:

`RUN RESULTS COMPLETE` is permitted only when all required fields above are
present and the record contains no predicted final closed-log hash or future
closeout time. The facilitator logs `run_results_completed` with this exact
file's hash, then closes the log. The later external closeout record binds the
actual closed-log, closeout-manifest, and results hashes.
