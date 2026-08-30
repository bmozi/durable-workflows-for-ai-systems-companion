# Stage B Decision-Owner Workbook

**Packet:** WF-RV-PILOT-001 version 1.2.5
**Status:** Blank independent read-back record

- Reviewer code:
- Broad role and experience band, optional:
- Entry branch: human / synthetic
- Exact selected Stage B context-record filename and manifest:
- Stage B context-gate verification event ID:
- Stage A artifact ID/version:
- Exact Stage B start before first scored read of the packet route, with timezone:
- `stage_b_started` event ID and exact line-byte SHA-256:
- Exact supplied-file route and manifest:
- Handoff exact local filename: `WF-A-ONE-SCREEN-HANDOFF-v1.md` / deviation
- Handoff governing manifest received:
  `WF-A-HANDOFF-SHA256SUMS-v1.txt` / deviation
- Handoff detached freeze-verification record received:
  `WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md` / deviation
- Prior involvement with Stage A: none required for first calibration

Do not ask the Stage A practitioner to explain or repair the artifact until
Sections 1–5 are complete.

## 1. Handoff-only read-back and scanability freeze

Complete this section from the verified one-screen handoff before receiving the
scenario or detailed Stage A artifacts.

Preserve the handoff's business and domain nouns. A paraphrase may reorder or
shorten supplied wording, but it must not introduce an unsupported noun or
domain qualifier. Attribute any genuinely new term to an exact later input;
no later input exists during Section 1. An unsupported invention is retained,
scores zero for the affected behavior, and is not silently repaired.

- Who receives value, what outcome is promised, and what supplied service
  commitments affect this decision?
- Present open promise:
- Recommended decision and what is allowed now:
- What is withheld?
- Assigned owner, or did the handoff honestly say `UNASSIGNED`?
- Assigning/acting authority, or did the handoff honestly say `UNKNOWN`?
- Known evidence, material unknowns, and largest unacceptable outcome:
- Immediate next action:
- Reconsideration date or evidence-based trigger:
- Could you find those fields on one screen without verbal repair? yes / partly / no
- Handoff layout-proof record received and result: exact filename / `PASS` /
  `FAIL` / missing. A favorable literal one-page finding requires the proof;
  layout proof is not human comprehension evidence.
- Phase-input manifest verified: `WF-B-PHASE-1-INPUT-SHA256SUMS-v1.txt` / deviation
- Section 1 output: `WF-B-SECTION-1-v1.md`; artifact ID/version:
- Section 1 completion timestamp/timezone and `SECTION 1 COMPLETE` state:
- Section 1 governing manifest: `WF-B-SECTION-1-SHA256SUMS-v1.txt`
- Section 1 detached freeze-verification record:
  `WF-B-SECTION-1-FREEZE-VERIFICATION-RECORD-v1.md`

Do not ask the Stage A practitioner to explain or repair the handoff. Do not
penalize an honest `UNASSIGNED`, `UNKNOWN`, or evidence-based trigger. Do flag
invented ownership, authority, dates, or evidence.

## 2. Detailed read-back and separate freeze

Complete this section after receiving the scenario and detailed Stage A
artifacts, but before receiving or opening `EXECUTIVE-DECISION-BRIEF.md` or
`VALUE-AND-EVIDENCE-LEDGER.md`.

- Detached revised freeze record exact local filename received:
- Governing revised-artifact manifest exact local filename received:
- Every handoff-linked revised detail received under its exact literal local
  filename: yes / no / deviation
- Filename, artifact ID/version, and SHA-256 cross-check against both freeze
  record and manifest: match / mismatch / incomplete
- Any renamed, regenerated, summarized, substituted, missing, or mismatched
  artifact (stop and record):
- Phase-input manifest verified: `WF-B-PHASE-2-INPUT-SHA256SUMS-v1.txt` / deviation

- Who receives value and what outcome is promised?
- What starts the durable obligation?
- Who owns unfinished work at each transfer?
- What may remain pending or unknown?
- What requires human authority?
- What evidence distinguishes API receipt/acceptance, contractor job
  acceptance, reconciled appointment, arrival, repair report, and verified
  restoration?
- What partial effects or residue can remain after repair?
- What proves the tenant received the final outcome?
- Section 2 output: `WF-B-SECTION-2-v1.md`; artifact ID/version:
- Section 2 completion timestamp/timezone and `SECTION 2 COMPLETE` state:
- Section 2 governing manifest: `WF-B-SECTION-2-SHA256SUMS-v1.txt`
- Section 2 detached freeze-verification record:
  `WF-B-SECTION-2-FREEZE-VERIFICATION-RECORD-v1.md`

Do not begin the detailed read-back when the exact-file cross-check fails. Do
not open the executive brief or value ledger until Section 2 is
completed, manifested, verified, and documented by its detached record. If any
Section 1 or 2 answer is corrected later, retain the
prior frozen artifact and record the exact old/new filenames and versions,
reason, correction timestamp/timezone, old/new SHA-256 values, and old/new
manifests. Never overwrite or rename a frozen artifact.

## 3. Decision legibility

Only now open `EXECUTIVE-DECISION-BRIEF.md`, followed by
`VALUE-AND-EVIDENCE-LEDGER.md`.

- Organizational capability unlocked:
- Operating or funding commitment required:
- Human or institutional authority that remains necessary:
- Largest visible risk or unacceptable outcome:
- Cost, delay, or burden that remains unknown:
- Evidence that would reveal a false assumption:

## 4. Bounded decision

Choose one: `EXPLORE` / `PROCEED BOUNDED` / `INVEST` / `HOLD` / `STOP`

- Scope and conditions:
- Withheld capability or authority:
- Evidence required before expansion:
- Assigned accountable owner or `UNASSIGNED`:
- Assigning authority or evidence-based assignment trigger, or `UNKNOWN`:
- Reconsideration date or evidence-based trigger:

## 5. Transfer finding

- Could you make the decision without verbal repair? yes / partly / no
- Missing or ambiguous information:
- Implementation detail that obscured the business decision:
- Unsupported benefit or certainty, if any:
- Smallest change that would improve the handoff:
- Detailed-artifact link that was missing or failed:
- Phase-input manifest verified: `WF-B-PHASE-3-INPUT-SHA256SUMS-v1.txt` / deviation
- Sections 3-5 output: `WF-B-SECTIONS-3-5-v1.md`; artifact ID/version:
- Sections 3-5 completion timestamp/timezone and `SECTIONS 3-5 COMPLETE` state:
- Sections 3-5 governing manifest: `WF-B-SECTIONS-3-5-SHA256SUMS-v1.txt`
- Sections 3-5 detached freeze-verification record:
  `WF-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD-v1.md`

Do not put a section's own hash or a future verification timestamp in the
section artifact. After each completed section export, the facilitator creates
and verifies its governing manifest and only then creates the named detached
freeze-verification record. The next phase-input manifest hashes the section,
its governing manifest, its detached record, and new inputs. Any correction
requires an immutable replacement set, manifest, verification event, and
detached record. Preserve the prior chain.

## 6. Debrief after scoring

Section 6 is a separate gated input. After Sections 3–5 freeze and scoring are
complete, the facilitator logs `stage_b_scoring_ended`, creates and verifies
`WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt`, and only then opens
`07-stage-b-section-6-debrief.md`. Export the completed record as
`WF-B-SECTION-6-DEBRIEF-v1.md` with `SECTION 6 DEBRIEF COMPLETE`, log its
completion, and then append the exact Stage B end event. Because each scored
workbook export completed earlier, do not add or predict the later scoring-end,
debrief-completion, or Stage B end events in those frozen bytes. Debrief cannot alter or upgrade
the frozen scored bytes or their retained scores.
