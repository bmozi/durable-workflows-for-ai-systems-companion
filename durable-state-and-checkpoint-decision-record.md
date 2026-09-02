# Durable State-and-Checkpoint Decision Record

**Status:** Working-draft companion tool; not author approved, practitioner
tested, technically validated, or publication ready

**Primary chapter:** Chapter 5, *Durable Execution and Checkpointing*

**Research basis:** WF-R005 is `sourced` in the research register; the
dated research note cited in the book
supports the bounded propositions used here. Named experiments and applications
remain `unrun`; completing this asset changes no evidence state.

**Validation state:** `unrun`. No runtime, provider, checkpoint, replay,
storage-failure, version-change, or lost-acknowledgement result is recorded here.

**Nonclaim:** Completing this record does not prove that execution will recover,
an external effect happened once, the history is a complete audit record, or the
business outcome is acceptable. Product guarantees remain product-, version-,
provider-, configuration-, and integration-specific.

## What this tool helps you decide

A checkpoint answers a narrow question: what will the runtime remember after a
failure? It does not automatically answer what happened in another system or
who owns the promise while the answer is unknown.

Use this record before placing or trusting a checkpoint. Work from one
consequential action at a time:

1. name the open business promise;
2. name the exact durable record and its authority;
3. separate runtime history from external-effect evidence;
4. inspect failure immediately before and after each boundary;
5. decide what recovery may do and when it must stop; and
6. define evidence that could support or disprove the decision.

Use the evidence states `constructed`, `scenario`, `planned`, `unrun`,
`observed`, `tested`, `reported`, `sourced`, `bounded`, `inferred`, `proposed`,
and `unknown` exactly. A planned test remains `unrun` until a retained result
exists.

## 1. Workflow and guarantee scope

| Field | Decision |
| --- | --- |
| Decision record ID | |
| Workflow name and definition version | |
| Open business promise | |
| Business-promise owner | |
| Consequential action being reviewed | |
| Runtime, version, and workflow type | |
| Persistence provider, version, and configuration | |
| Worker and deployment version | |
| External participant or system | |
| Business invariant that must survive recovery | |
| Privacy or classification boundary | |
| History retention and deletion policy | |
| Known product-scoped guarantee and source | |
| Guarantee subjects deliberately excluded | External effect; business outcome; authority; other: |

Write the guarantee with its subject. Prefer “the runtime records this state
transition” to “the workflow is exactly once.”

## 2. Checkpoint decision

Complete one row for every boundary on which recovery depends.

| Checkpoint ID | Trigger or location | Durable record | Persistence authority | Atomic scope | External effect: absent, present, or unknown | Independent effect evidence | Replay precondition | Recovery action | Promise owner while unknown | Retention or limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | replay / retry / query / compensate / quarantine / stop | | |

For each row, answer in plain language:

- What fact will still be available after the worker disappears?
- Which write or enqueue operation is outside the checkpoint's atomic scope?
- What could have happened in the external world without being recorded here?
- Which code and definition versions can replay this history?
- Who decides whether recovery may create another attempt?
- What will tell an operator that recovery is blocked rather than progressing?

## 3. External-effect evidence

| Effect identity | Authority that can confirm it | Query or receipt | Idempotency or compare key | Possible ambiguity | Reconciliation owner | Evidence retention | Current state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | `unknown` |

Do not copy a runtime completion flag into the effect-evidence column unless the
runtime and effect share the exact transaction being claimed. Name that
transaction and its limits if they do.

## 4. Failure-window plan

These are planned challenges, not results.

| Failure window or mutation | State expected to survive | External effect that may exist | Permitted recovery | Prohibited recovery | Required owner and evidence | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Worker stops immediately before checkpoint | | | | | | `unrun` |
| Checkpoint persists before work is dispatched | | | | | | `unrun` |
| External effect commits before acknowledgement | | | | | | `unrun` |
| Acknowledgement arrives before runtime records it | | | | | | `unrun` |
| Storage records history but work enqueue is delayed or lost | | | | | | `unrun` |
| Replay uses incompatible code or definition | | | | | | `unrun` |
| History reaches a size or retention limit | | | | | | `unrun` |
| Effect evidence and runtime history disagree | | | | | | `unrun` |

## 5. Recovery decision

| Condition after restart | Meaning | Next action | Action authority | New owner | Stop condition | Required evidence | Reversal trigger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Effect known absent | | | | | | | |
| Effect known present | | | | | | | |
| Effect unknown | | | | | | | |
| History missing or corrupted | | | | | | | |
| Definition incompatible with history | | | | | | | |
| Policy or authority changed while stopped | | | | | | | |

`Unknown` is a valid state. It must not silently become “failed” merely to make
a retry path convenient.

## 6. Negative and boundary cases

Record how the design responds when:

- the checkpoint is durable but its corresponding task was never dispatched;
- the external effect exists but its acknowledgement and runtime result do not;
- replay repeats logging, notification, metering, or another supposedly harmless
  side effect;
- the runtime reconstructs its state but the business deadline has expired;
- a provider offers different durability semantics under another workflow type;
- a history is intact but no longer compatible with the deployed definition;
- retained history exposes more personal or sensitive data than policy permits;
- an operator can resume execution but lacks authority to repeat the effect; or
- a technically consistent restart point violates a current business invariant.

## 7. AI implementation brief boundary

### AI may draft candidate machinery from completed decisions

- persistence adapters and checkpoint calls;
- replay-compatible state reconstruction code;
- queries and receipts for external effects;
- worker-loss and lost-acknowledgement test fixtures;
- telemetry that distinguishes replay from original execution; and
- operator views for blocked, ambiguous, or quarantined instances.

### AI must not invent

- the business promise or terminal outcome;
- the persistence guarantee, provider behavior, or atomic scope;
- evidence that an external effect occurred;
- replay compatibility across versions;
- permission to retry, compensate, discard, or migrate;
- retention, privacy, or deletion policy; or
- an owner for an unknown or corrupted state.

### Required generation stop conditions

Stop and request a human decision when the effect state is unknown, the
checkpoint's atomic scope is unspecified, replay compatibility is unverified,
authority is absent, evidence sources conflict, retention is undefined, or the
business invariant cannot be stated independently of the runtime.

No claim is made here about AI-generated artifact speed, quality, reliability,
or benefit.

## 8. Evidence gate

| Claim to challenge | Supporting evidence required | Disproving or boundary evidence | Owner | State |
| --- | --- | --- | --- | --- |
| Recorded state survives the named worker loss | Frozen topology, history, restart trace, and hash | Missing or contradictory record after restart | | `planned` / `unrun` |
| Replay does not repeat a prohibited effect | Effect ledger and before/after failure injections | Duplicate, missing, or unexplained effect | | `planned` / `unrun` |
| Unknown effects enter governed reconciliation | Lost-acknowledgement trace and recovery record | Blind retry or ownerless wait | | `planned` / `unrun` |
| Open responsibility survives recovery | State and owner reconstruction | State exists without an actionable owner | | `planned` / `unrun` |
| Retained history satisfies the declared lifecycle | Retention, access, deletion, and reconstruction checks | Excess retention or required evidence unavailable | | `planned` / `unrun` |

Record the runtime version, provider, configuration, inputs, failure injection,
clock control, retained outputs, and hashes before any row can move to `tested`.

## 9. Constructed Northbridge application

**Continuity mode:** Independent constructed review fixture; not continuity
evidence.

**Disclosure:** Northbridge Exchange is an authorized fictional composite. This
row is constructed design material, not an incident, observed failure, or
experiment result.

| Checkpoint ID | Durable record | External effect | Effect evidence | Recovery decision | Open owner | Result |
| --- | --- | --- | --- | --- | --- | --- |
| `NB-CREDIT-ACK-GAP` | Finance-credit request identity and workflow transition are intended to be durable; exact runtime/provider semantics remain `unknown` | One credit may be absent, present, or duplicated after acknowledgement loss | Query finance by stable request/effect identity; evidence contract remains `proposed` | Stop blind retry; query and reconcile before another authorized attempt | Partner Operations owns the partner promise; Finance reconciliation owns effect confirmation | `constructed`; experiment `unrun` |

This row does not establish that the proposed query exists, the identities are
stable, or the recovery decision works.

## 10. Decision and reversal record

| Decision | Reason | Evidence used | Unknown or residual risk | Owner | Revisit or reversal trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | `proposed` |

Transfer planned time and failure cases into the existing
[Time-and-Failure Test Plan](time-and-failure-test-plan.md). Transfer ownership
and terminal-outcome decisions into the
[Workflow Responsibility-and-Progress Brief](workflow-responsibility-and-progress-brief.md).
Those transfers do not change an `unrun` result into evidence.
