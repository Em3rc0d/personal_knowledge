# MK1 — Normalize & Classify

Status: **🟡 OPEN / IN PROGRESS**  
Precondition: **MK0 CLOSED**  
Current schema: **`mk1-draft-2026-09-16.1`**

## Purpose

MK1 turns mined evidence into a **framework-independent classification system**. It normalizes vocabulary and architecture descriptions before MK2 converts them into operational contracts.

This README is the **entrypoint/index** for MK1. The schema, dimensions, rules, queue, unknowns and gates live in dedicated files.

## Package map

| Artifact | Responsibility |
|---|---|
| [`CLASSIFICATION_SCHEMA.md`](./CLASSIFICATION_SCHEMA.md) | normalized machine/human-readable record shape |
| [`DIMENSIONS.md`](./DIMENSIONS.md) | control, capabilities, side effects, state/concurrency, memory, HITL, retry, termination, eval, protocol, multi-agent and evidence axes |
| [`NORMALIZATION_RULES.md`](./NORMALIZATION_RULES.md) | rules preventing framework labels, hidden assumptions and dimension collapse |
| [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md) | prioritized systems/families and classification workflow |
| [`STRANDS_AGENTS_PRESSURE_TEST.md`](./STRANDS_AGENTS_PRESSURE_TEST.md) | first explicit modern-framework pressure test across control, state, concurrency, budgets, interventions, eval and protocols |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | inherited and MK1-specific uncertainty register |
| [`GATES.md`](./GATES.md) | pressure tests and closure criteria |

## Mission

The classification model must be:

- orthogonal where possible;
- explicit about control authority;
- explicit about reachable capabilities and compositions;
- explicit about side effects independently of autonomy;
- explicit about state/checkpoint/persistence/memory lifecycle;
- explicit about concurrency/writer/conflict semantics when shared state or parallel work is reachable;
- explicit about human approval, enforcement owner and dispatcher binding;
- explicit about retries/errors/unknown outcomes;
- explicit about semantic termination, resource budgets and enforcement boundaries;
- explicit about evaluation evidence;
- revision-aware for protocols/integrations;
- capable of preserving `UNKNOWN` instead of forcing a label.

## Core principle

> Classify what the system can actually decide and do, not what the repository/framework calls it.

A single system may be deterministic in one stage, model-routed in another, model-directed for tools, human-gated for writes and durably checkpointed by the runtime. Therefore a single `agent_type` is insufficient.

## Primary dimensions

```text
CONTROL AUTHORITY
HORIZON / TOPOLOGY
CAPABILITIES + COMPOSITION
SIDE-EFFECT CLASS
STATE / CHECKPOINT / PERSISTENCE / CONCURRENCY
MEMORY LIFECYCLE
HUMAN CONTROL + ENFORCEMENT OWNER/BOUNDARY
ERROR / RETRY OWNERSHIP
TERMINATION + BUDGET ENFORCEMENT
EVALUATION
PROTOCOL REVISION
SECURITY / CONTAINMENT
REPRODUCIBILITY
EVIDENCE STATE
UNKNOWNs
```

Full definitions: [`DIMENSIONS.md`](./DIMENSIONS.md).

## First pressure-test set

MK1 begins with:

- minimal while-loop;
- HITL approval;
- trace-evaluation harness;
- E2E generated-code/browser execution;
- self-healing generated code;
- HR messaging;
- social publishing;
- document intake/data egress;
- DataScribe database authority;
- reflection/self-improvement claim;
- memory system;
- multi-agent system;
- legacy/current MCP comparison;
- Strands Agents as an explicit modern framework/runtime pressure test spanning model-directed loops, deterministic workflow, Graph, Swarm, state/session/memory, interventions, evals and protocol adapters.

Full queue: [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md).

## Runtime-semantics crosscheck

The Strands pass surfaced three schema questions:

1. concurrency semantics for agent/session state;
2. budget enforcement boundary / overshoot semantics;
3. intervention enforcement owner and boundary.

They were **not** promoted from Strands alone. MK1 then cross-checked them against LangGraph and OpenAI Agents SDK. All three survived as framework-independent engineering distinctions.

Promotion in `mk1-draft-2026-09-16.1`:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

No framework-specific top-level category was introduced.

## Strands × MCP `2026-07-28` protocol gate

The Strands MCP record has now been checked against a pinned protocol revision rather than represented as `MCP=true`.

Current evidence state:

```text
core interoperability       SUPPORTED / UPSTREAM-EXECUTED
modern lifecycle            REGRESSION-TESTED
Streamable HTTP             UPSTREAM-EXECUTED
MRTR / prompts / resources  SUPPORTED BY PINNED MODERN FIXTURE
list-changed subscription   UPSTREAM-EXECUTED
trace continuity            UPSTREAM E2E TESTED
auth adapter                SUPPORTED / deployment authorization separate
remote rollback on cancel   NOT IMPLIED
independent local rerun     BLOCKED BY CURRENT ENVIRONMENT NETWORK
```

The strongest fixture runs a real MCP 2.x server and explicitly rejects the legacy `initialize` handshake, so a successful connection proves the tested path uses the modern lifecycle rather than silently falling back to the legacy protocol.

Evidence: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

This closes the Strands-specific core compatibility unknown at the source-evidence level. It does **not** turn MCP interoperability into proof of authorization correctness, remote-effect rollback or universal server compatibility.

## State transition

```text
MK0 evidence/framing
        ↓
MK1 normalize/classify      ← current
        ↓
freeze classification schema revision
        ↓
MK2 operationalize contracts/tests
```

MK2 already contains **design scaffolding only** so the handoff shape is visible, but MK2 implementation remains blocked until MK1 closes.

## Current promotion state

```text
MK0 = CLOSED
MK1 = IN PROGRESS
RUNTIME SEMANTICS CROSSCHECK = PASS
STRANDS MCP 2026-07-28 = SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED
SCHEMA = mk1-draft-2026-09-16.1
MK2 = BLOCKED / DESIGN SEEDED
CANON OPERATIONAL RULES = NOT YET
```
