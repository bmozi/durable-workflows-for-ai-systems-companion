# Northbridge Data-Structures Architecture Bridge

**Status:** Constructed teaching example; `PLANNED/UNRUN`

**Disclosure:** Northbridge Exchange, its warehouse, records, quantities,
workload, and outcomes are fictional composite teaching material. They are not
production measurements or John Briggs project history.

## Structures are workers' tools, not durable responsibility

Northbridge can place routine picking in a deque and urgent or perishable
orders in a heap. That makes selection efficient, but neither structure owns
the promise. A worker crash, duplicate delivery, stale priority, or route
change must leave a durable record of what was accepted, attempted, completed,
or left unresolved.

The workflow therefore records operation identity, responsibility owner,
deadline, attempt history, external effect evidence, and recovery authority.
The deque or heap can be rebuilt from that durable state. Rebuilding the
structure is not the same as replaying an irreversible shipment.

## Plain-language model: the dispatch board and the case file

A dispatch board shows which job should be taken next. It cannot be the only
record that the job exists. The durable workflow is the case file: it preserves
ownership, attempts, evidence, custody changes, and recovery decisions.

A queue can hold the next task, but it cannot decide who is responsible for
completing that task, whether the task is still authorized, or what happens
when the worker fails.

```text
durable work -> queue -> time-limited worker lease -> attempt -> effect receipt
worker loss -> visibility timeout -> inspect state -> retry/escalate/stop
```

| Runtime structure | Durable workflow question |
| --- | --- |
| FIFO deque | Who owns work removed from the queue when the worker disappears? |
| Priority heap | What evidence justifies changing priority, and how are stale entries ignored? |
| Route graph | Which route version was attempted, and who decides whether to replan? |

## Transfer artifact: worker-failure recovery card

| Decision | Your answer |
| --- | --- |
| Durable operation and attempt identity | |
| Owner before, during, and after an attempt | |
| Queue eligibility, priority, and lease rule | |
| Checkpoint and external-effect receipt | |
| Retry-safe and irreversible steps | |
| Exhaustion and escalation path | |
| Recovery authority after an unknown outcome | |

Inject the hard failure: the worker loses contact one millisecond after the
external system accepts the action. What prevents both lost work and a
duplicated effect?

## AI-amplified transfer to other systems

AI tools can generate candidate structures, implementation code, tests, and
diagrams for many domains. The architect supplies the governing decisions the
generated machinery must preserve.

| Transfer case | AI can accelerate | Decision the structure cannot settle |
| --- | --- | --- |
| Search-engine indexing | Crawlers, inverted indexes, ranking code, query tests | Content authority, freshness, deletion, ranking policy, and evidence |
| Social-media platforms | Social graphs, feeds, queues, moderation classifiers | Consent, identity, amplification limits, appeal, and causal responsibility |
| Blockchain systems | Transaction parsing, Merkle proofs, graph analysis, contract tests | Signing authority, finality assumptions, off-chain governance, and reversal limits |
| Recommendation systems | Feature pipelines, candidate retrieval, ranking, evaluation | Permitted inputs, objective, fairness, explanation, and user control |
| Online food delivery | Route graphs, order queues, dispatch heaps, ETA models | Order and payment authority, worker custody, retry safety, refunds, and recovery |

The lesson is not that AI removes architecture work. It moves practitioners up
a level: generated machinery arrives sooner, so meaning, authority, failure,
and evidence must become explicit sooner.

> **Why we did not choose every structure**
>
> Autocomplete systems help predict partial search terms, but they are not
> needed for core inventory and order work. Huffman coding compresses data, but
> it does not solve ownership, scheduling, routing, retries, or recovery. Choose
> a structure because the problem requires it.
