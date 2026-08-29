# Workflow Version-and-Migration Plan

**Status:** Working-draft companion tool; not author approved, practitioner
tested, technically validated, or publication ready

**Validation state:** `unrun`. Completing this plan does not prove that running
instances can migrate, historical meaning remains intact, interrupted change is
recoverable, or the resulting business outcomes are acceptable.

Use the evidence states `constructed`, `scenario`, `planned`, `unrun`,
`observed`, `tested`, `reported`, `sourced`, `bounded`, `inferred`, `proposed`,
and `unknown` exactly. A planned case remains `planned` / `unrun` until its
inputs, execution, result, limits, and artifact location are retained. `Blocked`
below is a gate disposition, not an evidence state.

Use this plan before changing process definitions, code, state schema, policy,
dependencies, or authorization while workflow instances remain open.

## 1. Change identity

| Field | Decision |
| --- | --- |
| Workflow | |
| Current and target versions | |
| Change owner | |
| Business reason | |
| Changed meaning, policy, code, schema, timing, or dependency | |
| Effective date and business calendar | |
| Reversal deadline | |
| Approving authorities | |

## 2. Semantic compatibility

| Dimension | Current meaning | Target meaning | Compatible for running work? | Evidence | Decision owner |
| --- | --- | --- | --- | --- | --- |
| Promise and terminal outcomes | | | | | |
| State and transition meaning | | | | | |
| Authority and approval | | | | | |
| Deadlines and escalation | | | | | |
| Retry and idempotency | | | | | |
| Compensation and recovery | | | | | |
| Evidence and retention | | | | | |

## 3. Instance cohorts

| Cohort | Identification rule | Count/evidence | Treatment | Reason | Owner | Reversibility | Completion evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not started | | | | | | | |
| Open before changed state | | | | | | | |
| Waiting on external party | | | | | | | |
| Waiting on human decision | | | | | | | |
| Partially effected | | | | | | | |
| Compensating or recovering | | | | | | | |
| Poisoned or incompatible | | | | | | | |

Choose an explicit treatment:

- continue under old definition;
- compatible evolution in place;
- start new work on target version only;
- controlled cutover at a safe state;
- replay or reconstruct under bounded rules;
- migrate state with verification;
- compensate and restart;
- quarantine for repair;
- manual resolution; or
- governed cancellation or accepted closure.

## 4. Migration mechanics and authority

| Step | Preconditions | Authorized actor | State/effect change | Idempotency identity | Failure response | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 5. Validation and release

| Gate | Test or evidence | Negative case | State | Approver |
| --- | --- | --- | --- | --- |
| Cohorts completely identified | | | blocked | |
| Historical meaning preserved | | | blocked | |
| State transformation verified | | | blocked | |
| External effects reconciled | | | blocked | |
| Interrupted migration recoverable | | | blocked | |
| Monitoring distinguishes versions | | | blocked | |
| Rollback limits understood | | | blocked | |
| Business owner accepts residual risk | | | blocked | |

## 6. Recovery and audit

- How will a partially migrated instance be detected?
- Which source of state is authoritative during interruption?
- Who may repair, resume, reverse, compensate, or close it?
- Which history remains immutable?
- How will operators distinguish an old-definition obligation from a migration
  defect?
- What evidence would trigger a halt or rollback?

## Final decision record

| Decision | Supported scope | Evidence | Residual uncertainty | Owner | Revisit trigger |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
