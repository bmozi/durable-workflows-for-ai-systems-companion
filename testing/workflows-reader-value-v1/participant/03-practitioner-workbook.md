# Stage A Practitioner Workbook

**Packet:** WF-RV-PILOT-001 version 1.2.1
**Status:** Blank participant record

- Participant code:
- Broad role and experience band, optional:
- Exact Stage A start before first scored read of the packet route, with timezone:
- Exact Stage A end, with timezone:
- Frozen supplied-file manifest and route record:

## 1. Recognition before terminology

Complete this section before opening companion assets.

- Who needs what outcome?
- What promise must survive time, handoffs, and failure?
- What becomes possible if progress and ownership are dependable?
- What can go wrong if API receipt/acceptance, contractor job acceptance,
  reconciled appointment, arrival, repair report, and verified restoration are
  treated as the same ending?
- Present open promise right now:

## 2. Explain it to someone outside the team

In no more than five sentences, explain what Meadowline has promised, who owns
unfinished work, what can remain uncertain, and how the tenant will know the
promise was fulfilled.

## 3. Workflow record

- Business start and promised outcome:
- Meaningful progress states, authoritative evidence source, and permitted
  claim for each:
- Owner before and after each transfer:
- Accepted terminal outcomes:
- Authority left `UNKNOWN` or owner left `UNASSIGNED`:
- Business identity that survives retries and tool calls:
- Unknown-outcome and query-before-repeat rule:
- Compensation, residue, and owner:
- Deadline, escalation, and approval-expiry rule:
- Final verified-restoration evidence and accepting owner:

Record transition evidence separately. API receipt/acceptance or contractor
job acceptance is not evidence of a reconciled appointment. Arrival is not a
repair report. A repair report is not verified restoration.

## 4. Practitioner incident-authority block

Do not infer authority from job title, system access, or availability. Use
`UNASSIGNED` when no person or role has been assigned. Use `UNKNOWN` when the
assigning authority, permission, source, or trigger is not supplied.

| Incident responsibility | Current factual owner | Proposed durable role | Assigning authority or trigger | Authority limit or evidence |
| --- | --- | --- | --- | --- |
| Own the still-open tenant promise | | | | |
| Emergency containment | | | | |
| Status query and reconciliation | | | | |
| Correct message, reopen case, or correct state | | | | |
| Retain or cancel either contractor | | | | |
| Approval and late-decision fallback | | | | |
| Financial residue, fee, or call-out charge | | | | |

### Approval evidence completeness

If any field below is absent, record the omission explicitly. Do not treat the
premium as approved unless all are supplied and linked:

- durable approval task ID:
- exact scope and amount:
- applicable policy and immutable version:
- link to the exact dispatch/business repair:
- absolute expiry timestamp and timezone:
- backup approver; if absent, record `UNASSIGNED` and keep approval incomplete:
- late-decision rule and owner/assigning authority; if absent, record `UNKNOWN`
  and keep approval incomplete:

## 5. Monday-morning decision

- Smallest useful design or policy change:
- First time, failure, approval, or compensation behavior to test:
- Assigned test owner or `UNASSIGNED`:
- Assigning authority or evidence-based assignment trigger:
- Result that would block or reverse the design:

## 6. Live update and detailed-artifact freezes

Record the update exactly as supplied. The initial artifacts must already be
frozen before revising them. The update-driven revision is planned: it creates
new revised artifacts from the retained initial artifacts. It is not a
correction to already frozen revised bytes.

- Initial artifact IDs/versions:
- Initial freeze timestamp, timezone, and manifest reference:
- Exact live update:
- Initial answer now challenged:
- Present open promise after update:
- Work that remains open:
- Current durable owner or `UNASSIGNED`:
- Assigning authority or trigger, or `UNKNOWN`:
- Duplicate effect or residue to reconcile:
- Unsafe message or closure to correct:
- Artifact fields revised:
- Evidence still missing:
- Revised artifact inventory (use the required literal v1 filenames):

| Exact local filename | Artifact ID/version | Artifact-stated completion timestamp/timezone | SHA-256 value | Artifact's pre-hash state |
| --- | --- | --- | --- | --- |
| `WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md` | | | | `REVISED COMPLETE` / invalid |
| `WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md` | | | | `REVISED COMPLETE` / invalid |
| `WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md` | | | | `REVISED COMPLETE` / invalid |
| `WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md` | | | | `REVISED COMPLETE` / invalid |

- Revised freeze timestamp and timezone:
- Governing manifest exact filename:
  `WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`
- Governing manifest SHA-256 value:
- Detached freeze record exact filename:
  `WF-A-REVISED-FREEZE-RECORD-v1.md`
- Detached freeze record completed before handoff opened: yes / no

Put the artifact ID/version, exact completion timestamp/timezone, and `REVISED COMPLETE`
state inside each revised file before hashing it. The detached record supplies
the later exact freeze timestamp/timezone. The governing manifest lists
the revised artifacts, not itself. Complete the
detached record from `06-revised-artifact-freeze-record.md`. If any revised
artifact still says `PENDING`, `AWAITING FREEZE`, or anything other than
`REVISED COMPLETE`, do not open the handoff.

### Post-freeze correction record, only if required

Do not use this block for the planned live-update revision. Use it only if
bytes already recorded as frozen must later be corrected. Never overwrite the
old file or reuse its filename. A post-freeze correction stops this attempt;
do not open the handoff or proceed to Stage B.

| Reason | Correction timestamp/timezone | Exact old filename | Old artifact ID/version | Old SHA-256 | Old manifest filename/hash | Exact new immutable filename | New artifact ID/version | New SHA-256 | New manifest filename/hash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |

## 7. One-screen transfer preparation

Only after `WF-A-REVISED-FREEZE-RECORD-v1.md` is complete and every revised
artifact is `REVISED COMPLETE` and the detached freeze record is complete,
complete and freeze the separate
[One-Screen Decision Handoff](05-one-screen-handoff.md) after the live update.
Export it as `WF-A-ONE-SCREEN-HANDOFF-v1.md`. Link every revised detail by its
exact literal local filename, artifact ID/version, and SHA-256 value rather
than copying every implementation detail. Name and hash the governing manifest
and detached freeze record.
Use a date **or** an evidence-based reconsideration trigger. Never invent an
owner, assigning authority, date, or evidence to make the handoff look full.
The handoff must state the beneficiary, promised outcome, and every supplied
service commitment that affects the bounded decision: for Meadowline,
**initial human contact within 30 minutes and on-site response within 4
hours**.

- Handoff artifact ID/version:
- Handoff freeze timestamp, timezone, and manifest reference:

## 8. Material feedback

- Prompt that changed your thinking:
- Term or field that was unclear:
- Important decision the materials missed:
- Any prompt that pushed you toward an unsupported answer:
- Question, pause, or access problem and exact time:
- What this exercise cannot establish:
