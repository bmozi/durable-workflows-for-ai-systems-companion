# Workflow Evidence Portfolio

**Use boundary:** Illustrative field tool; not a maturity model, certification,
or proof of production fitness

**Validation state:** `unrun`. A filled portfolio does not make its evidence
complete or prove production safety, causal improvement, current authority, or
an acceptable business outcome.

Use this worksheet to state exactly what each retained result concerns, what
it may support, and what it cannot establish alone. Plan time and failure cases
in the canonical Time-and-Failure Test Plan. Store actual artifacts separately
and link them here by immutable identity.

## 1. Portfolio identity

| Field | Record |
| --- | --- |
| Stable portfolio ID | |
| Workflow and business promise | |
| Decision or release under review | |
| Definition/code/configuration manifest hash | |
| Evidence owner | |
| Business-invariant owner | |
| Review window and environment scope | |
| Known excluded populations, paths, or effects | |

## 2. Evidence-layer inventory

| Layer | Exact subject exercised or observed | Version/configuration/environment | Result and evidence state | Retained artifact and hash | What it may support | What it cannot prove alone | Gap/negative result | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Static/schema check | | | | | | Runtime, time, failure, effect, or business meaning | | |
| Unit/state test | | | | | | Durable runtime, real participant, credential, queue, or effect behavior | | |
| Deterministic replay | | | | | | New paths, semantic correctness, current policy, external effects, or full coverage | | |
| Controlled/virtual time | | | | | | Wall-clock behavior, civil-time change, contention, or host skew | | |
| Failure injection | | | | | | Unknown faults, other topologies, universal resilience, or absence of harm | | |
| Integration | | | | | | Other modes, versions, permissions, regions, load, effects, or business acceptance | | |
| Model/simulation | | | | | | Real behavior without validation, empirical fit, or bounded uncertainty | | |
| Production observation | | | | | | Unobserved paths, missing telemetry, causality, authority, or safety | | |
| Business reconciliation | | | | | | Future safety, all populations, or cause of improvement | | |

## 3. Corpus and evidence provenance

| Artifact class | Selection rule | Source and authority | Privacy/security treatment | Sampling or survivorship limit | Version/retention limit |
| --- | --- | --- | --- | --- | --- |
| Histories and fixtures | | | | | |
| Clock/calendar inputs | | | | | |
| Fault plan and topology | | | | | |
| Participant records | | | | | |
| Telemetry | | | | | |
| Business records | | | | | |

## 4. Safety and execution authority

| Field | Decision |
| --- | --- |
| Authorized environments and participants | |
| Credential/data class | |
| Fault targets, order, duration, and blast radius | |
| Stop signals and operator | |
| Restoration and cleanup owner | |
| Escaped-effect and residual-harm owner | |
| Prohibited tests or environments | |

## 5. Cross-layer contradictions

Retain contradictions. A green technical layer must not overwrite a failed
business invariant, and a failed technical step may coexist with an acceptable
business outcome.

| Evidence A | Evidence B | Contradiction or missing link | Authority needed | Disposition | Revisit trigger |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## 6. Bounded decision

| Decision | Supported scope | Negative and boundary evidence | Residual uncertainty | Owner | Expiry/revisit trigger |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
