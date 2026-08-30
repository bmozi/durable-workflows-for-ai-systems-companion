# Run Execution and Access Log Schema

**Packet:** WF-RV-PILOT-001 version 1.2.3
**Status:** Facilitator-only blank schema; prepared and unrun

This log records what actually happened and when. It is not participant
instruction, participant context, or a substitute for an operating-system
audit log. Keep it outside every sealed participant-input directory. Never
copy it, an orchestration note, or any undeclared instruction into participant
input.

## Exact run file

Write one UTF-8 JSON object per line to
`WF-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl`. Use compact JSON on a single
line for each event. Do not edit or reorder an earlier line. If an entry is
wrong, append a `deviation_recorded` event describing the error and preserve
the original.

Every event contains every field below. Use an empty string only for `notes`
when there is nothing to add. Do not omit a field.

| Field | Plain-language meaning |
| --- | --- |
| `event_id` | Unique immutable ID for this event |
| `sequence` | Integer beginning at 1 and increasing by exactly 1 |
| `attempt_id` | One constant attempt ID for the whole log |
| `stage` | `A`, `B`, or `RUN` |
| `phase` | Canonical phase or release ID from the protocol |
| `event_type` | One exact event type from the inventory below |
| `actor_code` | Facilitator, participant, or tool code that performed or directly observed the event |
| `exact_filename` | Literal local filename acted on; use `N/A` only for `run_log_started`, `stop_recorded`, or `run_log_closed` |
| `timestamp` | Observed RFC 3339 timestamp including numeric UTC offset |
| `timezone` | IANA timezone name used by the run, such as `America/Denver` |
| `result` | `PASS`, `FAIL`, `COMPLETE`, `OPENED`, `READ`, `RELEASED`, `STOPPED`, or `RECORDED` as applicable |
| `prior_event_id` | Exact preceding event ID, or `GENESIS` for sequence 1 |
| `prior_event_sha256` | SHA-256 of the preceding exact JSONL line bytes excluding its newline, or `GENESIS` for sequence 1 |
| `notes` | Bounded detail; include the literal verification command, output, or deviation reference when the event type requires it |

## Event type inventory

- `run_log_started`;
- `sealed_input_manifest_created`;
- `sealed_input_manifest_verified`;
- `participant_file_released`;
- `participant_file_opened`;
- `participant_file_read_completed`;
- `governed_artifact_completed`;
- `governing_manifest_created`;
- `governing_manifest_verified`;
- `detached_record_completed`;
- `phase_input_manifest_created`;
- `phase_input_manifest_verified`;
- `deviation_recorded` when a deviation occurs;
- `stop_recorded` when a stop occurs; and
- `run_log_closed`.

An unstopped complete attempt contains every nonconditional type above.
`deviation_recorded` is required only when a deviation occurs, and
`stop_recorded` is required only when a stop occurs. A stopped attempt may end
without later phase types that it never reached; it still closes the log and
preserves the partial chain.

## Ordered gates and continuity

1. Start with `run_log_started`. Every later event binds the immediately
   preceding exact line by both `prior_event_id` and `prior_event_sha256`.
2. A sealed or phase-input manifest must be created and successfully verified
   before any newly governed file is released, opened, or read.
3. Log each file separately: release, then open, then completed read. Do not
   summarize a batch as one access event. The exact filename must be declared
   for that protocol release.
4. Log each governed artifact's completion before manifest creation. Log
   manifest creation before its successful verification. Log the detached
   record's later completion only after that verification event.
5. A next-phase input manifest is created only after the predecessor's
   detached record is complete. It must verify before the next phase's files
   are released, opened, or read.
6. Timestamps may be equal at the clock's precision except between
   `governing_manifest_verified` and its `detached_record_completed` event;
   that pair must be strictly increasing. Use sufficient clock precision to
   show the later completion. No timestamp may move backward. `attempt_id` is
   constant, `event_id` is unique, and `sequence` has no gap or duplicate.
7. Append `run_log_closed` as the final line. Create
   `WF-RUN-EXECUTION-ACCESS-LOG-SHA256SUMS-<attempt-id>.txt` afterward so the
   completed log is externally bound. Record that manifest's verification in
   the results-and-deviation log; do not mutate the closed JSONL file to
   describe its own later hash.

## Verification-event notes

For `sealed_input_manifest_verified`, `governing_manifest_verified`, and
`phase_input_manifest_verified`, `notes` must preserve the literal command,
observed standard output, observed standard error (write `(empty)` when it was
empty), and integer exit status. The event's `timestamp` and `timezone` state
when the result was observed. A command copied without its observed output and
exit status is not verification evidence.

## Evidence boundary

The log can show that the declared route was followed, deviated from, or
stopped according to recorded observations. It cannot prove participant
attention, correctness of an architectural decision, safety, broad usability,
or business value. Preserve missing or failed evidence; do not repair history
by rewriting the log.
