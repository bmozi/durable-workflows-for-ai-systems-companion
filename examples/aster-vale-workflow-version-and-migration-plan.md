# Aster Vale Workflow Version-and-Migration Plan

**Example state:** `scenario`

**Validation state:** `unrun`

**Scenario identity:** `AVO-CAMPAIGN-01`

**Disclosure:** Aster Vale Observatory is an unrelated fictional scenario. This
completed example demonstrates use of the
[blank plan](../workflow-version-and-migration-plan.md). It does not show that
an inventory, migration, replay, data transformation, or recovery worked.
Completion does not validate the workflow or establish any usability,
technical, scientific, business, privacy, accessibility, or safety result.

## 1. Change identity

| Field | Scenario decision |
| --- | --- |
| Workflow | `AVO-OBSERVING-CAMPAIGN` |
| Current and target versions | `v0-proposed` to `v1-proposed` |
| Change owner | Proposed joint owner: Platform Operations change lead and Program Operations business owner |
| Business reason | Add explicit unknown-capture state, command/attempt identity, claimed human-task ownership, and versioned package provenance |
| Changed meaning, policy, code, schema, timing, or dependency | New `OBSERVATION_OUTCOME_UNKNOWN`; separate command/attempt/capture IDs; exception-task lease; calibration-manifest version; candidate instrument/raw-store query |
| Effective date and business calendar | `unknown`; no cutover authorized |
| Reversal deadline | `unknown`; must be chosen before release |
| Approving authorities | Program Operations for campaign meaning; Instrument Operations for command/effect contract; Data steward for manifest meaning; Platform Operations for execution |

## 2. Semantic compatibility

| Dimension | Current meaning | Target meaning | Compatible for running work? | Evidence | Decision owner |
| --- | --- | --- | --- | --- | --- |
| Promise and terminal outcomes | Existing mapping not retained in fixture | Explicit package, reschedule, non-execution, or manual-resolution disposition | `unknown` | Terminal comparison `planned` / `unrun` | Program Operations |
| State and transition meaning | Timeout may follow generic technical failure | Timeout becomes unknown/reconciliation when capture may exist | No automatic mapping | State-history fixtures `planned` / `unrun` | Program and Platform Operations |
| Authority and approval | Task assignment and scope may be incomplete | Actual owner, competence/scope, delegation, conflict, policy version | `unknown` | Authority mutation `planned` / `unrun` | Program Operations |
| Deadlines and escalation | Window/deadline relation `unknown` | Versioned UTC window and evidence-bearing escalation | `unknown` | Controlled-time comparison `planned` / `unrun` | Program Operations |
| Retry and idempotency | Command/attempt identity may not be separate | Stable command operation plus unique attempts and query-before-repeat | No unless identities reconstruct | Instrument reconciliation `planned` / `unrun` | Instrument Operations |
| Compensation and recovery | Reschedule may be labeled generic retry | Replacement is a new governed promise with residue | No automatic mapping | Response classification `planned` / `unrun` | Program Operations |
| Evidence and retention | Calibration/manifest/lifecycle `unknown` | Versioned proposal, command, capture, calibration, manifest, migration links | `unknown` | Records/lifecycle review `planned` / `unrun` | Data owner `unknown` |

## 3. Instance cohorts

No cohort count has been observed. Identification, treatment, and completion
evidence remain `scenario` and `planned` / `unrun`.

| Cohort | Identification rule | Count/evidence | Treatment | Reason | Owner | Reversibility | Completion evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not started | No campaign identity before cutover | `unknown`; inventory unrun | Start on target only after approval | Avoid migration | Platform Operations | Stop admissions before effect | Admission/version report |
| Open before changed state | `v0` and no command/human claim | `unknown` | Controlled cutover only if proposal/state mapping passes | Meaning still needs proof | Program Operations | Return to `v0` before target-only transition if supported | Before/after state/owner |
| Waiting on external party | Awaiting investigator clarification | `unknown` | Continue old version unless policy/timing compatibility approved | Preserve communication promise | Program Operations | Old-version continuation | Response/terminal evidence |
| Waiting on human decision | Active `v0` exception task | `unknown` | Continue old or reissue under target with supersession | Avoid duplicate/late decision | Program Operations | Reissue may leave residue | Claim/decision/supersession trace |
| Partially effected | Instrument command sent or capture possible | `unknown` | Quarantine and reconcile before migration | Capture ambiguity cannot become failure | Instrument Operations | State repair may be irreversible | Command/capture/reconciliation bundle |
| Compensating or recovering | Replacement/reschedule open | `unknown` | Continue original recovery unless mapping approved | Repair is a new promise | Program Operations | `unknown` | Replacement identity/outcome |
| Poisoned or incompatible | Missing ID, corrupt history, unmappable proposal/calibration | `unknown` | Quarantine for repair/manual resolution | Speculation could alter meaning/provenance | Named recovery owner | `unknown`; decide per instance | Authorized disposition |

## 4. Migration mechanics and authority

| Step | Preconditions | Authorized actor | State/effect change | Idempotency identity | Failure response | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Freeze inventory | Queries defined; no migration started | Platform Operations change role | None | Migration run ID | Stop if inventory cannot reconcile | Frozen cohort report/hash |
| Classify cohort | Source state/history and effect links available | Platform Operations plus domain owner | Classification only | Campaign plus migration run | Quarantine ambiguity | Classification rationale |
| Transform eligible state | Approved state/proposal/calibration mapping | Migration operator under approval | Add target fields; no instrument command | Campaign/source/target versions | Record partial status; use planned resume/reverse | Before/after state and mapping version |
| Reconcile captures/packages | Stable instrument/raw-store/manifest queries | Instrument Operations and Data steward | Add evidence links; do not infer capture/package | Command/capture/manifest identities | Quarantine conflicts | Query/result bundle |
| Release cohort | Gates pass for cohort | Change owner and Program Operations | Allow target execution | Cohort release ID | Reblock on negative result | Approval, monitor, reversal limits |

## 5. Validation and release

| Gate | Test or evidence | Negative case | Disposition | Evidence state | Approver |
| --- | --- | --- | --- | --- | --- |
| Cohorts completely identified | Frozen inventory/reconciliation | Campaign missing version/cohort | `blocked` | `planned` / `unrun` | Change owner |
| Historical meaning preserved | Independent proposal/state reconstruction | Unknown capture becomes false non-execution | `blocked` | `planned` / `unrun` | Program Operations |
| State transformation verified | Before/after schema/transition fixtures | Partial or repeated transform | `blocked` | `planned` / `unrun` | Platform Operations |
| External effects reconciled | Command/capture/manifest comparison | Unlinked or contradictory capture | `blocked` | `planned` / `unrun` | Instrument Operations and Data steward |
| Interrupted migration recoverable | Fail every mechanics step | Ownerless/double-transformed campaign | `blocked` | `planned` / `unrun` | Change owner |
| Monitoring distinguishes versions | Version/cohort views and alerts | Mixed versions appear identical | `blocked` | `planned` / `unrun` | Platform Operations |
| Rollback limits understood | Reversal matrix by cohort | Target-only command or manifest blocks reversal | `blocked` | `planned` / `unrun` | Program and Instrument Operations |
| Business owner accepts residual risk | Named residue/unknown decision | Generic acceptance without scope | `blocked` | `planned` / `unrun` | Program Operations |

## 6. Recovery and audit

- Detect partial migration through per-campaign migration state linked to the
  frozen run and source/target versions.
- During interruption, source workflow state, instrument records, raw captures,
  and package manifest remain distinct authorities.
- Platform Operations executes repair/resume/reversal only after appropriate
  Program, Instrument, or Data disposition.
- Proposal, command, capture, decision, package, and migration history remains
  immutable; corrections append.
- Operators distinguish old obligations from migration defects using source
  version, last authorized transition, effect links, cohort, and failure step.
- Halt on incomplete inventory, unmappable proposal meaning, capture conflict,
  stale authority, missing owner, or failed interruption fixture.

## Final decision record

| Decision | Supported scope | Evidence | Residual uncertainty | Owner | Revisit trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| Do not bulk-migrate partially effected or recovering campaigns | Scenario `v0` cohorts with possible captures/replacements | Chapter 5–7 reasoning only; no execution evidence | Counts, runtime semantics, instrument queries, package lifecycle unknown | Program and Instrument Operations | Frozen cohort experiment supports narrower treatment | `scenario`; `unrun` |
| Start target-only admissions before eligible cutover | Not-started campaigns after approval | Proposed isolation rule | Effective date, controls, reversal unapproved | Change owner | Admission/version gate fails | `scenario`; `unrun` |

## Chapter 5–8 field trace

No populated worksheet-source record exists for these values. Each link below
identifies the applicable blank worksheet only.

| Version-plan field | Decision ID | Applicable blank worksheet | Transfer boundary |
| --- | --- | --- | --- |
| Checkpoint/replay compatibility and capture ambiguity | `AVO-STATE-01` | [Chapter 5 blank worksheet](../durable-state-and-checkpoint-decision-record.md) | `scenario`; replay/migration `unrun` |
| Command/attempt identity and authority recheck | `AVO-RETRY-01` | [Chapter 6 blank worksheet](../retry-timeout-backoff-and-exhaustion-safety-record.md) | `scenario`; identity reconstruction `unrun` |
| Replacement/recovery cohort and residue | `AVO-COMP-01` | [Chapter 7 blank worksheet](../compensation-eligibility-and-failure-record.md) | `scenario`; eligibility `unrun` |
| Human-task claim, supersession, policy version | `AVO-HUMAN-01` | [Chapter 8 blank worksheet](../human-approval-escalation-authority-and-evidence-record.md) | `scenario`; late-decision test `unrun` |

The plan demonstrates field completion only. The linked blanks are not
populated source records, and the example cannot establish migration
feasibility, scientific validity, recoverability, or acceptable outcomes.
