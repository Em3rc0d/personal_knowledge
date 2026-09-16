# Strands Agents — Canonical Engineering View

Status: **CURRENT SYSTEM SYNTHESIS / QUALIFIED**  
Observed baseline: **2026-09-16**  
Pinned source: `strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20`  
Observed releases: Python `v1.56.0`, TypeScript `v1.18.0`  
MK1 schema: `mk1-draft-2026-09-16.1`

This package is the preferred entrypoint for the **current understanding of Strands Agents** inside `personal_knowledge`.

Raw observations and historical reasoning remain in `mining-site/`, `quarries/` and `mk/`. This layer consolidates their current conclusions without deleting the evidence trail.

## Core thesis

**Strands is best understood as an in-process agent harness/SDK with a model-directed core loop plus several developer-selectable orchestration topologies. It is not a hosted control plane, not a security sandbox, not a production-readiness certificate and not a taxonomy of agent systems.**

Its engineering value to this knowledge base is unusually high because one framework exposes materially different control models—single-agent model-directed execution, deterministic Workflow, structured Graph, peer Swarm and manager/specialist agents-as-tools. That makes Strands strong evidence for a central rule:

> **Framework identity is not architecture. Classify the control, capabilities, state, enforcement and failure semantics that actually execute.**

## What Strands is

At the pinned snapshot, Strands is an open-source SDK/library that runs inside the application process. The framework supplies agent-loop mechanics, model/tool integration, state/session abstractions, hooks, orchestration primitives, observability/evaluation surfaces and protocol adapters.

The application owner still owns major system responsibilities such as:

- deployment topology;
- process/container isolation;
- credentials and secrets;
- network and filesystem permissions;
- tenant boundaries;
- tool authorization;
- idempotency and rollback design;
- storage policy;
- SLOs and incident response;
- workload-specific evaluation and certification.

Therefore `uses Strands` tells us much less than a complete system classification.

## What Strands is not

Do **not** infer any of the following merely from framework use:

```text
Strands used                 != production ready
MCP connected                != authorized/safe tool execution
structured output            != semantically correct output
session persistence          != concurrency-safe shared state
memory enabled               != trustworthy/isolated knowledge
HITL/steering available      != every side effect is gated
cancellation supported       != running remote effects are rolled back
Graph/Swarm available        != multi-agent is better
OpenTelemetry available      != production observability is complete
```

## Mental model

The core single-agent path is a **model-directed loop inside a runtime-owned envelope**.

```text
request / invocation
        │
        ▼
┌──────────────────────────┐
│ Strands runtime envelope │
│ limits / cancellation    │
│ hooks / state / tracing  │
└────────────┬─────────────┘
             │
             ▼
      ┌──────────────┐
      │ model call   │
      └──────┬───────┘
             │
      text/end│tool request
             │
       ┌─────▼──────┐
       │ tool layer │──────► host / network / filesystem / remote services
       └─────┬──────┘
             │ tool result
             └──────────────► next model cycle
```

The model chooses whether to answer or request tools. The runtime owns the loop mechanics and interception points. The application/infrastructure must still enforce any policy that cannot be delegated to probabilistic model behavior.

## Control topologies inside one SDK

Strands is especially useful because its orchestration surfaces are **not equivalent**.

| Surface | Normalized interpretation | Main authority |
|---|---|---|
| Core `Agent` loop | bounded multi-step agent loop | model-directed inside runtime limits |
| Workflow | predefined task/dependency execution | deterministic/developer-defined |
| Graph | developer-defined topology with dynamic/model nodes possible | mixed |
| Swarm | peer agents handing work among themselves | model-directed / peers |
| Agents as tools | parent delegates to specialist agents | manager/specialist, usually model-routed |

This directly rejects `multi_agent=true` or `agent_type=Strands` as sufficient architecture descriptions.

## State model: keep the layers separate

Strands reinforces a distinction already central to this repository:

```text
conversation history
≠ invocation state
≠ agent/application state
≠ session persistence
≠ context-window management
≠ long-term memory
```

### Conversation history

Model-visible messages, tool requests and results participating in the active context.

### Invocation state

Request-scoped data useful to tools/runtime behavior without necessarily entering model context.

### Agent/application state

Structured application data associated with the agent/system.

### Session persistence

Durable state used to resume a conversation/orchestration execution.

### Context management

Policies for retaining, trimming, summarizing or otherwise fitting active information into a finite model context.

### Long-term memory

Cross-session knowledge that can be stored, retrieved, injected and extracted independently from session replay.

The strongest reusable conclusion is:

> **Persistence is not memory, and durability is not concurrency safety.**

Documented session managers assume a single live writer per conversation and do not, by themselves, provide distributed multi-writer locking.

## Tools define the effective capability boundary

A Strands agent can only affect the world through capabilities reachable from its tools and process environment. Tool schemas improve interface structure, but tool execution inherits the permissions available to the host process unless separately constrained.

For security analysis, the effective capability set is therefore closer to:

```text
registered tools
+ host filesystem permissions
+ network reachability
+ credentials/secrets
+ subprocess/shell access
+ remote protocol endpoints
+ application-specific wrappers/policy
```

rather than merely the names shown to the model.

This is why Strands strongly supports the domain invariant **least privilege is an agent invariant**.

## Hooks, HITL and steering

Strands exposes several intervention mechanisms, but they have different guarantees.

- deterministic runtime/application hooks can block a dispatcher;
- a human can approve/reject a pending action;
- provider/infrastructure policy may enforce an external boundary;
- LLM steering/model judges can guide or challenge behavior probabilistically.

These must never collapse into one `guardrail=true` field.

Current normalized rule:

> **Record enforcement owner and enforcement boundary. Behavior guidance is not authorization enforcement.**

A side effect that requires approval is only truly protected when the approval/policy gate sits on the consequential dispatch path and any edited action is revalidated before execution.

## Budgets and termination

Strands exposes turn/token limits and cancellation, but the semantics are boundary-sensitive.

Important observed behavior:

- turn/token limits are checked at loop boundaries;
- an in-flight model response can exceed the nominal token threshold;
- tool work requested by the preceding turn may finish before the next budget check;
- cancellation is cooperative at defined safe points;
- an arbitrary in-process tool may continue unless it observes cancellation;
- remote MCP cancellation cannot be equated with transactional rollback.

Therefore:

> **A budget value is incomplete without its enforcement boundary and overshoot semantics.**

This distinction survived comparison against LangGraph and OpenAI Agents SDK and is now part of the general MK1 schema.

## Concurrency

Strands originally surfaced the concurrency problem strongly enough to force a schema pressure test.

Current normalized interpretation:

- overlapping invocation on one agent instance is restricted by the runtime behavior inspected;
- documented session persistence assumes one live writer per conversation;
- durability does not imply distributed locking;
- application-level external/shared-state concurrency remains independent.

Cross-runtime comparison confirmed that concurrency belongs under the normalized `state` dimension using invocation mode, writer model, locking and conflict semantics—not framework-specific fields.

## Observability and evaluation

Strands provides useful primitives for:

- OpenTelemetry traces;
- model/tool latency and error signals;
- token usage;
- loop-cycle/tool metrics;
- output evaluation;
- trace/trajectory evaluation;
- session evaluation;
- deterministic evaluators;
- model-judge evaluators;
- simulated tools/users and experiment artifacts.

This supports another key separation:

```text
output correctness
trajectory correctness
side-effect verification
session/task success
production telemetry
```

are related but distinct evidence surfaces.

Framework support does not mean a deployed system has configured adequate graders, repeated trials or regression gates.

## MCP `2026-07-28`

For the pinned Python snapshot, modern MCP interoperability is no longer merely a source claim.

Current evidence supports:

- declared MCP 2.x dependency range;
- modern `server/discover` negotiation;
- Streamable HTTP fixture using MCP 2.x's real `MCPServer`;
- explicit rejection of the legacy `initialize` path inside the fixture;
- tools list/call;
- structured results/errors;
- multi-round-trip input-required behavior;
- prompts/resources;
- tool-list change subscription;
- task-extension handling;
- end-to-end trace continuity in a separate upstream test;
- successful upstream CI execution receipts.

Classification: **`SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED`**.

Still not implied:

- universal server interoperability;
- external protected-server OAuth correctness for every deployment;
- transactional rollback after remote cancellation;
- compatibility beyond the pinned dependency range.

See [`PROTOCOLS.md`](./PROTOCOLS.md).

## A2A

Strands supports A2A-oriented remote-agent integration surfaces, but this knowledge base has **not yet closed the same revision/auth/transport execution receipt** that now exists for MCP.

Treat A2A as supported framework capability with reproducibility debt, not as a fully certified current integration contract.

## What Strands changed in the general taxonomy

Strands initially surfaced three distinctions that the old MK1 draft represented poorly:

1. concurrency semantics;
2. budget enforcement boundary / overshoot semantics;
3. intervention enforcement owner/boundary.

They were deliberately **not** promoted from Strands alone. Independent pressure tests with LangGraph and OpenAI Agents SDK confirmed all three as framework-independent engineering distinctions.

Final promotion:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

This is one of the most important outcomes of the Strands study: the framework was used as a **pressure instrument**, not as the taxonomy itself.

## Current unknowns that matter

The main unresolved Strands-specific questions are now narrower:

- A2A exact revision/auth/transport execution receipt;
- application-specific idempotency and unknown-outcome handling for consequential tools;
- hard containment for arbitrary host-process tools;
- distributed concurrency behavior of each chosen persistence backend;
- Python/TypeScript provider/feature parity over time;
- benchmarked benefit of Graph/Swarm/agents-as-tools versus simpler baselines;
- repeated/adversarial reliability of LLM-mediated steering;
- external protected-server OAuth behavior for a concrete MCP deployment;
- remote side-effect state after cancellation when execution may already have begun.

Unknowns remain explicit because absence of evidence must not be replaced with framework reputation.

## Recommended reading order

### Human — 10 minute path

1. this file;
2. [`ENGINEERING_RULES.md`](./ENGINEERING_RULES.md);
3. [`CLASSIFICATION.md`](./CLASSIFICATION.md);
4. [`PROTOCOLS.md`](./PROTOCOLS.md) when interoperability matters;
5. [`EVIDENCE.md`](./EVIDENCE.md) when auditing a claim.

### LLM / agent

Start at [`LLM_CONTEXT.md`](./LLM_CONTEXT.md). It defines canonical facts, precedence, prohibited inferences and source routing.

## Evidence chain

- source receipt: [`../../mining-site/S-109-strands-agents.md`](../../mining-site/S-109-strands-agents.md)
- detailed framework quarry: [`../../quarries/strands-agents.md`](../../quarries/strands-agents.md)
- runtime crosscheck: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md)
- MCP receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md)
- historical MK1 pressure test: [`../../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](../../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)
- current schema: [`../../mk/MK1/CLASSIFICATION_SCHEMA.md`](../../mk/MK1/CLASSIFICATION_SCHEMA.md)
- current gates: [`../../mk/MK1/GATES.md`](../../mk/MK1/GATES.md)
- domain status: [`../../STATUS.md`](../../STATUS.md)
