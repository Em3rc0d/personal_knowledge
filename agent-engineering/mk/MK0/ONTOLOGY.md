# MK0 — Ontology & Critical Distinctions

Status: **HISTORICAL FRAME / CLOSED MK0**

This file preserves the vocabulary established during Mine & Frame. MK1 may refine or decompose these concepts, but it must not silently erase their provenance.

## Initial system classes

```text
LLM CALL
single inference; no autonomous iteration

LLM WORKFLOW
multi-step system whose main control flow is predetermined by code

MODEL-ROUTED WORKFLOW
code defines a bounded set of branches; the model selects among them

TOOL-USING AGENT
model repeatedly selects actions/tools and adapts from observations within runtime limits

MULTI-AGENT SYSTEM
multiple model-directed execution loops coordinate, delegate, critique or partition work
```

### MK0 conclusion

The hierarchy is useful as orientation but insufficient as a final taxonomy. A real system can be deterministic in one stage, model-routed in another, model-directed for tools and human-gated for writes.

MK1 therefore classifies systems through orthogonal dimensions rather than one `agent_type` label.

## Core components established

```text
OBJECTIVE
POLICY
HARNESS / RUNTIME
MODEL
CONTEXT BUILDER
STATE
CHECKPOINTER / PERSISTENCE
MEMORY
TOOLS / ENVIRONMENT
HUMAN CONTROL
TRACE / RECEIPTS
EVALUATOR
BUDGET / TERMINATION
```

## Workflow vs agent

The primary discriminator is **control authority**, not framework identity.

A LangGraph application can be mostly deterministic. A raw Python loop can be model-directed. `LangGraph`, `LangChain`, `CrewAI`, `AutoGen`, MCP or any provider name is therefore implementation metadata, not a sufficient architectural class.

## Prompt vs invariant

```text
PROMPT RULE
asks the model to behave in a certain way

RUNTIME INVARIANT
makes forbidden behavior impossible or intercepts it before execution
```

Prompts can shape behavior. Security, authorization, side-effect control, hard budgets and other critical constraints require enforceable boundaries outside model compliance alone.

## Context vs state vs checkpoint vs persistence vs memory

```text
STATE
facts the runtime currently knows or needs for execution

CHECKPOINT
serialized state captured at an execution boundary

PERSISTENCE
durability mechanism that lets state/checkpoints survive process/session loss

CONTEXT
information projected into a specific model invocation

MEMORY
information intentionally retained and recalled under a lifecycle/retrieval policy

KNOWLEDGE / RAG
external source material retrieved because it may answer or ground a task
```

A transcript is only one possible context source. A framework class named `MemorySaver` does not prove semantic long-term memory.

## Model claim vs trace vs outcome vs evidence

```text
MODEL CLAIM
generated assertion, explanation or completion text

TRACE
record of calls/actions that occurred

OUTCOME
external state or result actually produced

EVIDENCE
observation supporting a success/failure claim
```

A model cannot certify its own external effect merely by saying `done`.

## Control / capability separation

Control authority and capability are independent.

Examples:

- a deterministic workflow may execute a high-impact financial mutation;
- an autonomous research loop may only read public documents;
- a model may generate code without being allowed to execute it;
- a browser may be used read-only even though the underlying session could support transactions.

MK1 preserves these axes separately.
