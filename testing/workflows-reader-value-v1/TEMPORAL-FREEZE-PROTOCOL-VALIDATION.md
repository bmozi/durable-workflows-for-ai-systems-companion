# Temporal Freeze Protocol Static Validation

**Packet:** WF-RV-PILOT-001 version 1.2.4
**Validation type:** Static source review; not a human run
**Validation date:** 2026-08-30
**Result:** Prepared validation specification; PASS is claimed only when the
repository validator, mutation suite, and packet checksum verification pass

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

## Full-route closure checked

- Exactly one human-consent or synthetic-context branch is selected before
  scored input. Synthetic context carries the exact nonhuman identity and
  cannot be mixed with consent or upgraded into a human result.
- The log must contain Stage A and Stage B starts, Stage A material-feedback
  completion/end, Stage B scoring end, post-scoring Section 6 debrief, and
  Stage B end. The six scored freeze chains remain immutable but do not alone
  mean the full route closed.
- Immutable run-specific results complete after Stage B end and before log
  close. They cannot predict the future closed-log hash or closeout time.
- A later external closeout record binds the actual results hash, closed-log
  hash, byte-identical closeout copy, and external checksum manifest.

## Layout and semantic-transfer checks

- A favorable one-page claim requires a preserved PDF and proof record showing
  exactly one US Letter portrait page, margins of at least 0.5 inch, text of
  at least 9 points, at most 450 reader-facing words excluding labeled
  provenance, and no clipping, overlap, hidden overflow, or unreadable
  shrinking. This is layout evidence, not comprehension evidence.
- Stage B Section 1 must preserve or attribute handoff business/domain nouns.
  The permanent negative fixture rejects changing `contractor request` into
  unsupported `billing request`; the retained frozen replay is not rewritten.

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
requires one positive control plus rejection of all declared structural
mutations, including branch omission/mixing, synthetic human-result claims,
missing boundaries/debrief/results, premature close, predicted future hashes,
missing external closeout, unsupported favorable layout claims, semantic noun
invention, missing record completion, undeclared participant-input
orchestration, and access-log defects.

This PASS means only that the reviewed prepared source and executable mutation
checks agree on the stated temporal invariants. It does not establish that a
human followed the route, understood it, found it usable, or produced a
correct or safe workflow decision. Packet state remains **PREPARED/UNRUN**.
