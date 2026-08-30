# Temporal Freeze Protocol Static Validation

**Packet:** WF-RV-PILOT-001 version 1.2.3
**Validation type:** Static source review; not a human run
**Validation date:** 2026-08-29
**Result:** PASS for the reviewed prepared source protocol; executable
mutation regression is required after any protocol change

## Required ordering checked

For initial and revised Stage A, the handoff, and each Stage B output, the instructions now
require this irreversible order:

1. complete the governed bytes, including ID, version, completion timestamp
   and timezone, and the phase's required `COMPLETE` state;
2. create a governing manifest that hashes only those completed artifacts;
3. verify that manifest from sealed storage and capture the exact verification
   timestamp and timezone; and
4. create a detached freeze-verification record describing that already-
   observed verification event.

The governing manifest cannot hash itself or the later record. A next-phase
input manifest hashes the completed governed artifacts, prior governing
manifest, completed detached record, and new phase inputs.

Each detached record now requires attempt ID, canonical phase,
facilitator/actor code, literal verification command, observed standard output
and standard error, integer exit status, exact verification timestamp and
timezone, and an explicitly later record-completion timestamp and timezone.
The record cannot reuse or predict the verification event.

## Input isolation and run continuity checked

- Each staged participant release has exact canonical membership. An
  undeclared orchestration note, hidden prompt, facilitator file, renamed
  substitute, or execution/access log fails the release.
- The facilitator-only JSONL execution/access log stays outside participant
  input and separately records manifest gates, file releases, opens, completed
  reads, artifact completions, manifest creation/verification, and detached-
  record completion.
- Each JSONL event carries actor, exact filename, timestamp/timezone, unique
  event ID, contiguous sequence, and the preceding event's ID and SHA-256.
  The final closed log is bound by a later external manifest rather than by a
  self-hash.

## Self-reference checks

- The revised practitioner workbook no longer requests its own SHA-256 or a
  future freeze timestamp inside its governed bytes.
- The handoff no longer requests its own hash or future freeze timestamp.
- Stage B workbook freeze fields name the exported output, governing manifest,
  detached verification record, and next phase input rather than embedding the
  output's own hash or future verification time.
- The revised Stage A record is explicitly created after, and excluded from,
  the manifest whose verification it describes.
- A post-freeze correction requires a new immutable artifact set, manifest,
  observed verification event, and detached record; it cannot overwrite the
  prior chain.

## Evidence boundary

The canonical inventory is
[`TEMPORAL-FREEZE-PROTOCOL.json`](TEMPORAL-FREEZE-PROTOCOL.json). Run both
`python3 scripts/validate_repository.py` and
`python3 scripts/test_temporal_freeze_protocol.py` from the repository root.
The latter uses disposable copies, refreshes ordinary packet checksums, and
requires one positive control plus rejection of fifteen structural mutations,
including missing record completion, an undeclared participant-input
orchestration file, an omitted access-log event, and a log admitted as
participant input.

This PASS means only that the reviewed prepared source and executable mutation
checks agree on the stated temporal invariants. It does not establish that a
human followed the route, understood it, found it usable, or produced a
correct or safe workflow decision. Packet state remains **PREPARED/UNRUN**.
