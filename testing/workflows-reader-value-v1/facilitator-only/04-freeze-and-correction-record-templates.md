# Detached Freeze-Verification and Correction Record Templates

**Packet:** WF-RV-PILOT-001 version 1.2.2
**Status:** Facilitator-only blank records; prepared and unrun

These schemas create run evidence. Never supply this template during a scored
stage. A freeze-verification record describes an event that already occurred;
it must not predict a future hash or verification time.

## Output completion header

Before hashing a governed output, place these values in that output:

- exact immutable local filename;
- artifact ID and version;
- exact completion timestamp and timezone; and
- the phase's required state: `INITIAL COMPLETE`, `REVISED COMPLETE`,
  `HANDOFF COMPLETE`, `SECTION 1 COMPLETE`, `SECTION 2 COMPLETE`, or
  `SECTIONS 3-5 COMPLETE`.

Do not place the artifact's own hash, a future verification timestamp, or a
claim that verification has occurred inside the governed output.

## Governing manifest and detached record

Create the governing manifest only after all governed outputs are complete.
It lists only those outputs. It never lists itself or the later detached
record. Verify it from the sealed directory, capture the exact timestamp and
timezone, and only then create the detached record:

- attempt ID and phase;
- detached record completion timestamp/timezone;
- manifest verification timestamp/timezone, method, and pass/fail result;
- governing manifest exact filename and SHA-256;
- for every governed output: exact filename, ID/version, completion
  timestamp/timezone, required completion state, and SHA-256; and
- facilitator code.

Use these exact output pairs:

| Phase | Governing manifest | Detached freeze-verification record |
| --- | --- | --- |
| Stage A initial | `WF-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` | `WF-A-INITIAL-FREEZE-VERIFICATION-RECORD-v1.md` |
| Stage A revised | `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` | `WF-A-REVISED-FREEZE-RECORD-v1.md` |
| Stage A handoff | `WF-A-HANDOFF-SHA256SUMS-v1.txt` | `WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md` |
| Stage B Section 1 | `WF-B-SECTION-1-SHA256SUMS-v1.txt` | `WF-B-SECTION-1-FREEZE-VERIFICATION-RECORD-v1.md` |
| Stage B Section 2 | `WF-B-SECTION-2-SHA256SUMS-v1.txt` | `WF-B-SECTION-2-FREEZE-VERIFICATION-RECORD-v1.md` |
| Stage B Sections 3-5 | `WF-B-SECTIONS-3-5-SHA256SUMS-v1.txt` | `WF-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD-v1.md` |

## Next phase-input manifests

The next phase-input manifest hashes the prior completed output, its governing
manifest, its completed detached record, and the new phase inputs:

| Release | Exact phase-input manifest |
| --- | --- |
| Initial set to live update | `WF-A-LIVE-UPDATE-INPUT-SHA256SUMS-v1.txt` |
| Revised set to blank handoff | `WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt` |
| Handoff to Stage B Section 1 | `WF-B-PHASE-1-INPUT-SHA256SUMS-v1.txt` |
| Section 1 to detailed read-back | `WF-B-PHASE-2-INPUT-SHA256SUMS-v1.txt` |
| Section 2 to executive decision | `WF-B-PHASE-3-INPUT-SHA256SUMS-v1.txt` |

Record each phase-input manifest's exact filename, SHA-256, verification
method, result, and timestamp/timezone in the results log.

## Correction of already verified bytes

The planned live-update revision is not a correction. For a later byte change,
stop the attempt and retain the full prior chain. Create:

- a new immutable artifact filename, ID, and version;
- a new completion timestamp/timezone and completion state;
- a replacement governing manifest;
- a new observed manifest-verification event and timestamp/timezone;
- a replacement detached freeze-verification record; and
- a replacement next phase-input manifest when another phase follows.

Record the reason, exact old/new filenames, IDs/versions, completion times,
hashes, manifest filenames/hashes, detached record filenames/hashes, and
effect on routing and interpretation. Never overwrite, rename, or relabel the
prior chain.
