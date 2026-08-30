# Meadowline Scenario: Restore Heat and Keep the Promise

**Packet:** WF-RV-PILOT-001 version 1.0.0
**Status:** Fictional, prepared, and unrun

Meadowline Housing manages apartment repairs. A tenant reports that the heat is
not working during cold weather. The business asks for “one automated flow that
gets a contractor there quickly and keeps the tenant informed.” The proposed
design is:

> Accept the repair request, let an AI assistant select and book a contractor,
> publish `HeatRestorationScheduled`, close the service case, and reopen it if
> someone later reports a problem.

You are reviewing who remains responsible from request through verified heat
restoration before workflow steps or agent prompts are generated.

## Known facts

1. The tenant needs safe heat restored, not merely a ticket, dispatch request,
   appointment, or notification.
2. Meadowline promises an initial human contact within thirty minutes and an
   on-site response within four hours for the fictional priority assigned here.
3. The AI assistant may rank approved contractors. Meadowline has not decided
   whether it may commit an appointment or approve an emergency premium.
4. The contractor API may return `accepted` before a contractor accepts the
   job. A timeout may occur after the contractor system records the request.
5. Retrying with a new request ID can dispatch a second contractor for the same
   repair.
6. A contractor can arrive but fail to gain access, lack a required part, make
   a temporary repair, or report completion while the tenant still has no heat.
7. Cancelling a duplicate dispatch does not erase a call-out charge or travel
   already begun. That residue requires an owner and evidence.
8. The proposed `HeatRestorationScheduled` event is emitted after API
   acceptance. Customer messaging currently translates it as “Your repair is
   confirmed.”
9. The service desk plans to close the case after sending that message. No
   named role then owns timeout, access, duplicate dispatch, contractor
   disagreement, or tenant follow-up.
10. A supervisor must approve premiums over the normal limit. The current
    proposal has no durable approval task, expiry rule, backup approver, or late
    decision behavior.
11. No authoritative progress model distinguishes received, triaged,
    dispatch-unknown, scheduled, on-site, repair-pending, restored, failed,
    compensated, or manually resolved.
12. No implementation, time/failure test, practitioner session, cost
    measurement, or business-result evidence exists.

## Stage A task

Without discussing the intended answer with a facilitator:

1. Explain in plain language what the tenant and Meadowline are promising each
   other.
2. Complete the first pass and relevant portions of the supplied Workflow
   Responsibility-and-Progress Brief.
3. Name the durable owner at each transfer and the evidence required before
   moving to the next meaningful state.
4. Use the Compensation and Failure Matrix for duplicate dispatch, charge
   residue, no access, and reported-but-unverified completion.
5. Specify one timeout, ambiguity, approval-expiry, and recovery test.
6. Leave missing authority or evidence unknown. Do not invent it.
7. Complete the handoff in the practitioner workbook.

## Live update

The facilitator will provide one update after the initial artifact is frozen.
Revise only after hearing it. Record the original and revised answer.

## Boundary

This exercise asks for a reviewable durable-work decision. It does not ask you
to select a workflow engine, write code, approve production, or estimate
savings.
