# Revised Artifact Freeze Record

**Packet:** WF-RV-PILOT-001 version 1.2.1
**Status:** Blank detached freeze record; complete after the planned live-update
revision and before opening the one-screen handoff

Export the completed record as the exact literal local filename
`WF-A-REVISED-FREEZE-RECORD-v1.md`.

## Freeze identity

- Freeze timestamp and timezone:
- Governing manifest exact local filename:
  `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`
- Governing manifest SHA-256 value:
- Planned live-update revision, not a correction of frozen revised bytes:
  yes / no

The governing manifest lists and hashes the four revised detail files. It does
not list or hash itself. This detached record repeats the exact values needed
to verify the freeze; it is not required to hash itself. A later staged-release
manifest may hash this completed record after its bytes are final.

## Exact revised-detail inventory

Every row must contain an artifact ID/version and SHA-256 value. Every pre-hash
state must be `REVISED COMPLETE`. `PENDING`, `AWAITING FREEZE`, a blank, or any other state
means this record is incomplete and the handoff must remain closed.

| Exact literal local filename | Artifact ID/version | Artifact-stated completion timestamp/timezone | SHA-256 value | Artifact's pre-hash state |
| --- | --- | --- | --- | --- |
| `WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md` | | | | `REVISED COMPLETE` / invalid |
| `WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md` | | | | `REVISED COMPLETE` / invalid |
| `WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md` | | | | `REVISED COMPLETE` / invalid |
| `WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md` | | | | `REVISED COMPLETE` / invalid |

## Release gate

- All four artifact bytes match the governing manifest: yes / no
- All four exact filenames match the governing manifest: yes / no
- All four artifacts contain their own `REVISED COMPLETE` state before hashing: yes / no
- Handoff remained unopened until this record was complete: yes / no
- Facilitator verification name/code:
- Verification timestamp and timezone:

Any `no`, blank, mismatch, or non-`REVISED COMPLETE` state means **do not open the
handoff**. Record the deviation without silently repairing it.

## Post-freeze correction, only if required

The planned live-update revision above is not a correction. Use this section
only if bytes already recorded as frozen later require correction. Retain the
old file and governing manifest. Give the corrected file a new immutable local
filename and version; never overwrite or rename the old file. The correction
stops this attempt. Retain the record and begin a fresh attempt only after
authorized review.

| Reason | Correction timestamp/timezone | Exact old filename | Old artifact ID/version | Old SHA-256 | Old manifest filename/hash | Exact new immutable filename | New artifact ID/version | New SHA-256 | New manifest filename/hash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |
