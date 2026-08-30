# External Closeout Record Template

**Packet:** WF-RV-PILOT-001 version 1.2.4
**Status:** Facilitator-only blank template; no closeout result exists

Complete this record only after the immutable run-results record is complete,
the execution/access log is closed and validated, and its byte-identical copy
has been bound by an external checksum manifest. Export the exact run-specific
filename `WF-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md`.

## Run and results binding

- Packet ID/version: `WF-RV-PILOT-001` / `1.2.4`
- Attempt ID:
- Run-results exact filename:
  `WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md`
- Run-results SHA-256:
- Run-results completion event ID:
- Run-results completion timestamp/timezone:

## Closed-log binding

- Active closed-log exact filename:
  `WF-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl`
- Active closed-log SHA-256:
- Closed-log validation command:
- Observed standard output:
- Observed standard error; write `(empty)` when empty:
- Integer exit status:
- Validation timestamp/timezone:
- Closeout-copy exact filename:
  `WF-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl`
- Copy is byte-identical to active closed log: yes / no
- Closeout-copy SHA-256:
- External checksum-manifest exact filename:
  `WF-RUN-EXECUTION-ACCESS-LOG-SHA256SUMS-<attempt-id>.txt`
- External checksum-manifest SHA-256:
- External manifest verification command:
- External manifest observed stdout/stderr and integer exit status:
- External manifest verification timestamp/timezone:

## Closeout completion

- Final event in closed log: `run_log_closed` / invalid
- Closed-log hash was absent from the earlier run-results bytes: yes / no
- Future closeout timestamp was absent from the earlier run-results bytes:
  yes / no
- Record completion timestamp/timezone:
- Record state: `EXTERNAL CLOSEOUT COMPLETE` / invalid

This record binds the actual closed-log hash, external manifest hash, and
run-results hash after those bytes exist. It does not embed its own hash or
pretend that the earlier closed log predicted this later external evidence.
