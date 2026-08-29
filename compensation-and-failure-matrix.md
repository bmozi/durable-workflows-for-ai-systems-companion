# Compensation-and-Failure Matrix

**Status:** Working-draft companion tool; not author approved, practitioner
tested, technically validated, or publication ready

**Validation state:** `unrun`. Completing this matrix does not prove that an
effect occurred, a response is authorized or effective, residue is acceptable,
or the business promise can close.

Use the evidence states `constructed`, `scenario`, `planned`, `unrun`,
`observed`, `tested`, `reported`, `sourced`, `bounded`, `inferred`, `proposed`,
and `unknown` exactly. A planned case remains `planned` / `unrun` until its
inputs, execution, result, limits, and artifact location are retained.

Use this matrix to replace vague “rollback” language with explicit choices
after partial success, ambiguity, or irreversible effects.

## Workflow context

| Field | Decision |
| --- | --- |
| Workflow and version | |
| Business promise | |
| Business owner | |
| Compensation authority | |
| Maximum recovery window | |
| Residual harm owner | |

## Effect classification

| Step or external effect | Business effect | Confirmation evidence | Response eligibility or inverse preconditions | Conditions or deadline | Duplicate risk | Ambiguous-outcome probe | Compensation, semantic undo, or reconciliation | Authority | Residue or residual harm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | eligible / conditional / ineligible / unknown | | | | | | |

## Failure-response decisions

| Failure or ambiguity | Known state | Unknown state | Safe immediate action | Retry rule | Stop condition | Compensation trigger | Escalation owner | Required evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | |

## Response vocabulary

Use one explicit response for each effect:

- **retry** - repeat an attempt under an established identity and safety rule;
- **compensate** - perform a new business action that addresses an earlier
  effect without pretending history was erased;
- **semantic undo** - assert that exact domain inverse conditions now hold while
  preserving the original effect, observations, and any remaining residue;
- **reconcile** - compare authorities and records, then establish the accepted
  state;
- **escalate** - transfer decision authority and context to a named owner;
- **accept loss** - record a bounded residual outcome authorized by policy;
- **stop** - prevent further effects while preserving evidence; or
- **manual resolution** - assign governed human work with deadline and audit.

## Compensation invariants

- Compensation never silently deletes the original effect or its evidence.
- A compensation attempt has its own identity, authority, failure modes, and
  evidence.
- Repeating compensation cannot create an additional prohibited outcome.
- Partial compensation has a named owner and escalation path.
- An irreversible effect is not mislabeled reversible because an offsetting
  action exists.

## Failure tests

For each material effect, test at minimum:

1. failure before the effect;
2. effect succeeds but acknowledgement is lost;
3. duplicate request or delivery;
4. compensation succeeds but acknowledgement is lost;
5. compensation fails transiently and then terminally;
6. the compensation window expires;
7. policy or authority changes during recovery; and
8. evidence sources disagree.

## Decision record

| Decision | Rationale | Evidence | Remaining uncertainty | Owner | Revisit trigger |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
