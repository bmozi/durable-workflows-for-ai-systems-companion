# Compensation Eligibility-and-Failure Record

**Status:** Working-draft companion tool; not author approved, practitioner
tested, technically validated, or publication ready

**Primary chapter:** Chapter 7, *Compensation Rather Than Rollback*

**Research basis:** WF-R007 is `sourced` in the research register; the
dated research note cited in the book
supports the bounded propositions used here. Named experiments and applications
remain `unrun`; completing this asset changes no evidence state.

**Validation state:** `unrun`. No forward effect, compensation, semantic undo,
reconciliation, accepted-loss decision, failure, or acknowledgement-loss result
is recorded here.

**Nonclaim:** This record does not allocate legal liability, establish that an
effect is reversible, prove policy or regulatory sufficiency, or guarantee that
compensation restores the prior world. Compensation is additional forward work
and can fail, duplicate, conflict, or leave residue.

## What this tool helps you decide

After partial success, “roll it back” is often too vague to be safe. The earlier
effect may already be visible, another party may have acted on it, or time and
cost may be impossible to restore.

Use this record before generating a compensation handler:

1. establish what effect is known to have happened;
2. decide whether an atomic transaction is still open;
3. choose compensation, semantic undo, reconciliation, accepted loss, another
   governed response, or stop;
4. state who may authorize that response;
5. define repeat safety, prerequisites, residue, and failure ownership; and
6. plan cases in which the response itself fails or becomes ambiguous.

Use `rollback` only for a still-open atomic transaction with the exact applicable
guarantee. Use `compensation` for a new domain action after a prior commit.

## 1. Promise, effect, and authority

| Field | Decision |
| --- | --- |
| Decision record ID | |
| Workflow and definition version | |
| Open business promise | |
| Business-promise owner | |
| Prior action and effect identity | |
| Authority that can confirm the prior effect | |
| Evidence that the prior effect is absent, present, or unknown | |
| Beneficiary or affected party | |
| Compensation or recovery authority | |
| Maximum response window | |
| Residual-harm owner | |
| Applicable policy version and approval scope | |
| Privacy, notice, retention, or access boundary | |

## 2. Response selection gate

| Question | Decision | Evidence | Unknown | Stop or escalation condition |
| --- | --- | --- | --- | --- |
| Is one atomic transaction still open? | | | | |
| Has the original effect committed? | absent / present / unknown | | | |
| Has another party observed or relied on it? | | | | |
| Can an inverse condition be defined and verified? | | | | |
| Could concurrent change make the inverse unsafe? | | | | |
| Can a compensating action itself repeat safely? | | | | |
| Is reconciliation required before action? | | | | |
| Who may accept remaining loss or inconsistency? | | | | |
| Which beneficiary obligations remain after response? | | | | |

Choose one response explicitly:

| Response | Use only when | Evidence required | What it does not mean |
| --- | --- | --- | --- |
| Atomic rollback | The transaction is still open and the named atomicity guarantee applies | Transaction identity, scope, abort result | Erasure of external observations outside that transaction |
| Compensation | An authorized new action can offset, amend, or contain a committed effect | Original effect, authority, new action, result, residue | Rewinding time or restoring an identical world |
| Semantic undo | Defined inverse conditions can be checked and satisfied | Before/after facts and inverse-condition proof | Removal of messages, observation, delay, fees, or third-party consequences |
| Reconciliation | Authorities or records must be compared before repair or declaration | Compared sources, discrepancies, decision and repair result | Automatic repair or certainty |
| Accepted loss | A named authority may end further repair under explicit policy | Authority, threshold, known residue, beneficiary obligations, revisit trigger | Success, harmlessness, or permission to hide uncertainty |
| Stop or quarantine | Further action could increase harm or lacks authority/evidence | Stop record, current state, owner, next review condition | Closure of the business promise |
| Governed human resolution | A person must make a bounded domain decision | Assignment, context, authority, deadline, decision evidence | An indefinite manual queue |

## 3. Effect eligibility matrix

| Effect | Known state | Observers or dependencies | Candidate response | Eligibility preconditions | Authority | Repeat-safety rule | Deadline | Expected residue | State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | absent / present / unknown | | | | | | | | `proposed` |

Do not classify an effect as reversible merely because an offsetting action
exists. State what the offset cannot restore.

## 4. Compensation contract

| Field | Decision |
| --- | --- |
| Compensation action and business meaning | |
| Stable compensation operation identity | |
| Original effect linked to compensation | |
| Current authorization and policy check | |
| Required preconditions and evidence version | |
| Concurrent-change guard | |
| Duplicate-prevention or query rule | |
| Allowed attempts and total time budget | |
| Effect-confirmation source | |
| Success meaning | |
| Partial or ambiguous meaning | |
| Failure state and new owner | |
| Notice, appeal, correction, or beneficiary obligation | |
| Evidence and retention boundary | |

## 5. Compensation failure paths

Every compensating action creates its own open responsibility until its outcome
is known and accepted.

| Failure or ambiguity | Known state | Unknown state | Safe immediate action | Prohibited action | Owner | Required evidence | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Compensation fails before effect | | | | | | | `unrun` |
| Compensation commits; acknowledgement is lost | | | Query or reconcile | Blind repeat | | | `unrun` |
| Compensation repeats | | | | | | | `unrun` |
| Compensation window expires | | | | | | | `unrun` |
| Authorization changes before compensation | | | Re-evaluate authority | Use stale approval | | | `unrun` |
| Concurrent third-party change breaks inverse condition | | | Stop or reconcile | Force stale inverse | | | `unrun` |
| Original-effect and compensation records disagree | | | | | | | `unrun` |
| Compensation succeeds but beneficiary obligation remains | | | | | | | `unrun` |
| No allowed repair exists | | | Governed loss or escalation decision | Relabel as success | | | `unrun` |

## 6. Residue and accepted-loss record

| Residue, harm, cost, delay, or inconsistency | Who is affected | Known quantity or `unknown` | Repair attempted | Why further repair stops | Accepting authority | Required notice or appeal | Revisit trigger | State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | `proposed` |

Accepted loss must preserve the original effect, attempted repair, uncertainty,
authority, and beneficiary obligations. It must not be hidden inside a generic
`COMPLETE` state.

## 7. Negative and boundary cases

Challenge the response when:

- restocking cannot restore item condition, delivery timing, or a customer's
  observation;
- a refund adds fees, exchange-rate differences, delay, or provider failure;
- a notification, disclosure, physical shipment, or reputation effect cannot be
  unsent;
- reverse-order compensation conflicts with a concurrent domain change;
- the coordinator knows it requested compensation but not whether it happened;
- compensation becomes unauthorized after policy or amount limits change;
- the compensation succeeds technically but the beneficiary remains owed
  notice, appeal, or another outcome;
- compensation itself exhausts retries and becomes a new ownerless promise; or
- the only honest response is reconciliation, mitigation, or accepted loss.

Preserve examples in which compensation is ineligible or makes the outcome
worse.

## 8. AI implementation brief boundary

### AI may draft candidate machinery from completed decisions

- compensation commands, handlers, and state transitions;
- linkage between original and compensating identities;
- inverse-precondition and concurrent-change guards;
- query, reconciliation, stop, and quarantine paths;
- compensation-failure and lost-acknowledgement tests; and
- operator evidence views that retain original effect and residue.

### AI must not invent

- whether an effect committed or can be reversed;
- the semantic meaning of repair;
- authority to compensate or accept loss;
- eligibility preconditions, amount thresholds, or beneficiary obligations;
- repeat safety or an inverse condition;
- the acceptability of remaining harm; or
- evidence that compensation succeeded.

### Required generation stop conditions

Stop and request a human decision when prior-effect state is unknown, response
eligibility is unspecified, authority is missing or stale, concurrent change
invalidates the inverse, effect evidence conflicts, compensation becomes
ambiguous, or residue lacks an accepting owner and policy.

No claim is made here about AI-generated artifact speed, quality, reliability,
or benefit.

## 9. Evidence gate

| Claim to challenge | Supporting evidence required | Disproving or boundary evidence | Owner | State |
| --- | --- | --- | --- | --- |
| The chosen response is eligible under current facts | Effect, policy, authority, and prerequisite record | Unknown effect, stale policy, or failed inverse condition | | `planned` / `unrun` |
| Compensation cannot repeat a prohibited outcome | Attempt and effect ledgers with duplicate mutation | Duplicate or unlinked compensation effect | | `planned` / `unrun` |
| Compensation failure remains owned | Failure-state and escalation reconstruction | Ownerless retry or manual queue | | `planned` / `unrun` |
| Residue and beneficiary obligations remain visible | Closure and notice evidence | Generic success hiding unresolved harm | | `planned` / `unrun` |
| Accepted loss requires named authority | Policy and authorization mutation | Unapproved or technically inferred acceptance | | `planned` / `unrun` |

## 10. Constructed Northbridge application

**Continuity mode:** Independent constructed review fixture; not continuity
evidence.

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
row is constructed design material, not an incident, observed failure, or
experiment result.

| Prior effect | Known state | Candidate response | Eligibility and authority | Residue | Failure owner | Result |
| --- | --- | --- | --- | --- | --- | --- |
| A second finance credit may have been created after acknowledgement loss and a repeated request | `unknown` until finance evidence is reconciled | Reconcile first; if two credits are confirmed, consider one authorized offsetting finance action rather than fictional rollback | Finance must confirm both effects and authorize any offset under current policy; exact authority and inverse conditions remain `unknown` | Partner observation, timing, accounting entries, fees, notice, or appeal may remain even if an offset succeeds | Partner Operations retains the partner promise; Finance reconciliation owns effect confirmation and any authorized repair | `constructed`; eligibility review and failure tests `unrun` |

The row does not prove that a duplicate credit occurred, that an offset is
legal, permitted, technically available, or semantically sufficient, or that
the named roles approved this response.

## 11. Decision and reversal record

| Decision | Reason | Evidence used | Unknown or residual risk | Owner | Revisit or reversal trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | `proposed` |

Transfer the completed effect and response rows into the existing
[Compensation-and-Failure Matrix](compensation-and-failure-matrix.md). Transfer
planned time and failure cases into the existing
[Time-and-Failure Test Plan](time-and-failure-test-plan.md). These records do not
change state until retained evidence warrants it.
