# Synthetic Reader Walkthrough: Durable Workflows

**Attempt:** WF-SYNTH-2026-08-30-01
**Packet:** WF-RV-PILOT-001 v1.2.5
**Scenario:** Meadowline Housing, fictional heat-restoration request
**Reader mode:** Synthetic cold-reader walkthrough; no human participant or human data
**Status:** COMPLETE for the representative exercise path; not practitioner evidence

## Scope and evidence boundary

I read the companion `START-HERE.md`, the packet route and scenario, and the
workflow responsibility brief. The manuscript's stated promise was used as
context: preserve ownership, progress, compensation, deadlines, and closure
evidence across time and failure. I did not use linked completed examples,
facilitator scoring material, or an answer key while forming the initial answer.

This record demonstrates what a synthetic reader can produce from the supplied
materials. It does not establish human comprehension, usability, safety,
effectiveness, business value, or production readiness. The packet's complete
sealed-input, manifest, detached-record, execution-log, Stage B, and external
closeout protocol was not claimed as executed here.

## Reader path and retained output

### Recognition before terminology

- **Beneficiary:** the tenant whose heat is not working.
- **Promise:** Meadowline owes safe heat restoration, not merely a ticket,
  dispatch, appointment, event, or reassuring message.
- **Service commitments:** initial human contact within 30 minutes and on-site
  response within 4 hours for the stated fictional priority.
- **Durable owner:** a Meadowline service role must own the open promise through
  dispatch uncertainty, access failure, repair pending, and verification. The
  scenario names no such assigned role, so current owner is `UNASSIGNED`.
- **Closure:** only verified restoration, with authoritative evidence and an
  accepting Meadowline owner, closes the promise. A repair report alone is not
  enough.

### Initial workflow decision

The smallest useful design is a durable repair case with a stable repair ID and
one owner. It records distinct states: received, triaged, dispatch-unknown,
contractor-accepted, appointment-reconciled, on-site, repair-pending,
restored-pending-verification, verified-restored, failed/compensated, or
manually resolved. Each state requires its own evidence and owner.

The contractor API receipt or `accepted` response means only that the provider
received or accepted the request for processing. Contractor job acceptance,
reconciled appointment, arrival, repair report, and verified restoration are
separate transitions. A timeout after a possible effect triggers a status query
using the same repair and attempt identity before any repeat request.

### Failure and recovery decisions

- **Duplicate dispatch:** stop further retries, query both provider records,
  retain the contractor that can meet the promise if authorized, and assign a
  decision owner for the other. Cancellation is a request, not proof of
  cancellation; fee, travel, shipment, and tenant delay remain open residue.
- **No access or missing part:** keep the case open, record the authoritative
  visit result, assign the next move, and do not close from a contractor
  completion report.
- **Unsafe customer message:** replace “repair confirmed” with the strongest
  claim supported by evidence, such as request received or contractor job
  accepted. Correct the event consumer and reopen the case if it was closed.
- **Premium approval:** no premium may proceed until a durable approval task,
  exact scope/amount, policy version, linked repair, absolute expiry,
  fallback approver, and late-decision rule are present. Missing fields remain
  `UNKNOWN` and the approval remains incomplete.

### Live update response

The supplied update was treated as fictional reported effects, not real-world
execution evidence: the first request timed out after API receipt/acceptance;
status showed contractor acceptance and travel begun; a second contractor was
dispatched by retry; the original contractor then reported no access; and no
durable owner was assigned.

The revised decision is to stop new dispatches, reconcile both contractor
records, preserve the tenant promise as open, correct the overstrong event and
message, assign or escalate ownership, and record all residue. The revised
handoff must state:

> FICTIONAL REPORTED EFFECTS EXIST; REAL-WORLD EXECUTION EVIDENCE DOES NOT.

### One-screen handoff content

- **Decision:** HOLD autonomous dispatch and case closure.
- **Candidate scope:** evaluate ranking approved contractors and drafting a
  dispatch recommendation.
- **Present authorization:** `NOT AUTHORIZED` for committing appointments,
  emergency premiums, retries, cancellation, or closure because the scenario
  supplies no current authority source.
- **Recommended containment:** stop new dispatches; query both attempts; retain
  the open repair case; correct the customer message and event interpretation.
- **Actual containment execution:** `UNKNOWN`.
- **Largest unacceptable outcome:** tenant remains without safe heat while the
  system reports a false completion, duplicates contractor effects, or loses
  responsibility for fees and follow-up.
- **Next trigger:** resume only after authority, owner, state evidence,
  duplicate handling, approval expiry, and closure proof are assigned and
  tested.

## Cold-reader findings

| Gate | Result | Evidence and object lesson |
| --- | --- | --- |
| RV-1 recognition | Complete | The tenant outcome was identifiable before workflow terminology. |
| RV-2 plain understanding | Complete | The distinction between receipt, appointment, and restoration was usable. |
| RV-3 first artifact | Complete | The brief produced explicit owner and evidence unknowns. |
| RV-4 outside read-back | Not run | No independent human decision owner was present. |
| RV-5 failure discovery | Complete | Duplicate dispatch, false closure, residue, approval expiry, and lost ownership were found. |
| RV-6 team transfer | Partial | Handoff content was complete conceptually; literal frozen packet transfer was not executed. |
| RV-7 decision-owner legibility | Partial | HOLD was clear, but independent decision-owner behavior was not observed. |

Critical gates: promise `clear`; durable ownership `clear with explicit
UNASSIGNED gap`; progress evidence `clear`; ambiguity/duplication `clear`;
compensation/residue `clear`; completion evidence `clear`; incident authority
`partial` because the scenario intentionally omits assignment; approval
completeness `clear`; handoff scanability `partial` pending a literal one-page
proof and independent read-back.

## Friction and retained lessons

1. The route says “thirty minutes,” but the full packet route is materially
   longer once manifests, detached records, staged freezes, rendering, and
   closeout are included. Preserve the distinction between the reader's first
   pass and the formal pilot protocol.
2. `Owner` is easy to confuse with technical operating ownership. The template's
   explicit separation helped; the handoff should repeat that distinction.
3. The state vocabulary is strong but dense. A first reader benefits from one
   compact transition strip showing what each provider response permits the team
   to say.

## Disposition

The representative synthetic exercise is **complete and bounded** for this
scenario. It supports retaining the current exercises and their negative
lessons. It does not support labels `Piloted`, `Practitioner-tested`,
`Reader-validated`, or `Release-ready`. A recruited human Stage A and
independent Stage B remain required.
