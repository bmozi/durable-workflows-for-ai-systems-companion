# One-Screen Decision Handoff

**Packet:** WF-RV-PILOT-001 version 1.2.5
**Status:** Blank Stage A transfer; complete only after the live update

Keep this to one declared US Letter portrait page. Do not open or complete it until
`WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt` verifies. Export the completed handoff as the exact literal local
filename `WF-A-ONE-SCREEN-HANDOFF-v1.md`. Link detailed artifacts instead of
copying them. `UNASSIGNED` and `UNKNOWN` are valid and preferable to invention.

## Immutable provenance metadata — excluded from the reader-facing word count

| Provenance field | Exact value |
| --- | --- |
| Handoff artifact ID/version | |
| Handoff completion timestamp/timezone | |
| Handoff state before hashing | `HANDOFF COMPLETE` / invalid |
| Detached revised freeze-verification record exact local filename/hash | `WF-A-REVISED-FREEZE-RECORD-v1.md` / |
| Governing revised-artifact manifest exact local filename/hash | `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` / |
| Verified handoff-input manifest | `WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt` |

## Reader-facing handoff — maximum 450 words

| Decision field | Stage A entry |
| --- | --- |
| Evidence class and current state | |
| Beneficiary; promised outcome; every supplied service commitment affecting this decision (Meadowline: **initial human contact within 30 minutes and on-site response within 4 hours**) | |
| Present open promise | |
| Recommended decision | `EXPLORE` / `PROCEED BOUNDED` / `INVEST` / `HOLD` / `STOP` |
| Allowed now | |
| Withheld | |
| Assigned owner | Name role or write `UNASSIGNED` |
| Assigning/acting authority | Name source/trigger or write `UNKNOWN` |
| Known evidence | |
| Material unknowns | |
| Largest unacceptable outcome | |
| Immediate next action | |
| Reconsideration | Date **or** evidence-based trigger |

Reader-facing transition guard — included in the 450-word count: an API
receipt/acceptance or contractor job acceptance is not evidence of a
reconciled appointment. Record the present open promise until verified
restoration or another authorized terminal outcome is evidenced.

## Immutable revised-detail provenance — excluded from the reader-facing word count

Every row is required. Stage B receives each file under this exact local
filename; no rename, generated copy, summary, or substitution is permitted.

| Exact literal local filename | Artifact ID/version | SHA-256 value |
| --- | --- | --- |
| `WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md` | | |
| `WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md` | | |
| `WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md` | | |
| `WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md` | | |

The generated proof must preserve this exact Markdown, the PDF, literal
rendering command, tool versions, page count, and PDF SHA-256. `PASS` requires
US Letter portrait, exactly one page, every margin at least 0.5 inch, body and
table text at least 9 points, no more than 450 words across the completed
Markdown excluding only the two sections explicitly labeled immutable
provenance metadata, and no clipping, overlap, hidden overflow, or
unreadable shrinking. Any missing or failed condition yields layout `HOLD`.
This local proof does not establish human comprehension or scanability.

Do not put this handoff's own hash, a future verification timestamp, or a
claim that it is frozen inside this file. After `HANDOFF COMPLETE` bytes exist,
the facilitator creates `WF-A-HANDOFF-SHA256SUMS-v1.txt`, verifies it, and then
creates `WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md`. Stage B Phase 1
receives and hashes that completed triple.
