# S-110 — LangGraph runtime semantics

Status: **REGISTERED / OFFICIAL + OBSERVED**  
Observed: **2026-09-16**

## Source identity

| Field | Value |
|---|---|
| ID | `S-110` |
| System | LangGraph |
| Type | open-source graph/agent runtime + official documentation |
| Documentation | https://docs.langchain.com/oss/python/langgraph/ |
| Repository | https://github.com/langchain-ai/langgraph |
| Snapshot | `230927fb3a9ac9b2893a30322b4dfea7cdea9a8f` |
| Snapshot observed | 2026-09-16 |
| License | MIT |
| Use here | independent MK1 pressure test for concurrency, termination budgets, replay and HITL enforcement boundaries |
| Authority | official for LangGraph behavior; not normative for general agent engineering |
| Confidence | HIGH for documented/runtime-specific facts |

## Primary evidence inspected

- `Interrupts` official documentation;
- `Persistence` official documentation;
- `GRAPH_RECURSION_LIMIT` official error documentation;
- `INVALID_CONCURRENT_GRAPH_UPDATE` official error documentation;
- current public repository metadata and pinned `main` snapshot.

## Material observations

### Concurrency is a state contract

LangGraph permits parallel graph execution, but concurrent updates to the same state key are not automatically safe. If multiple parallel nodes write a state property without an explicit reducer, the runtime raises `INVALID_CONCURRENT_GRAPH_UPDATE`. Reducers define how concurrent values are merged.

This independently supports classifying:

- whether concurrent writers are allowed;
- how writes merge;
- what conflict semantics apply.

A generic `checkpointing: durable` field does not capture these semantics.

### Interrupt/replay semantics affect side effects

When execution resumes from an `interrupt()`, the node restarts from the beginning. Code executed before the interrupt can therefore execute again. Official documentation explicitly warns that pre-interrupt side effects must be designed with replay in mind.

This strengthens the existing requirement for idempotency/revalidation around consequential actions.

### Recursion limit is a kill switch, not a success predicate

`GRAPH_RECURSION_LIMIT` fires when a graph reaches the configured step limit without reaching a stop condition. The limit can be increased per invocation.

This independently confirms that a numeric step/turn cap and semantic completion are separate contracts.

### HITL placement determines enforcement strength

LangGraph interrupts can live directly inside a tool before a consequential dispatcher executes. They can support approve/edit/reject flows, but the safety guarantee depends on placing the interrupt before the actual side effect and revalidating edited values.

## Promotion boundary

Use this source to pressure-test framework-independent dimensions. Do not infer that every LangGraph application is concurrency-safe, idempotent, human-gated or production-ready merely because the runtime exposes the relevant primitives.

Cross-source synthesis: [`../quarries/runtime-semantics-strands-langgraph-openai.md`](../quarries/runtime-semantics-strands-langgraph-openai.md)
