# Strands Agents — Canonical Engineering View

Status: **CURRENT SYSTEM SYNTHESIS / QUALIFIED**  
Observed baseline: **2026-09-16**  
Pinned source: `strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20`  
Observed releases: Python `v1.56.0`, TypeScript `v1.18.0`  
MK1 schema: `mk1-draft-2026-09-16.1`

This package is the preferred entrypoint for the **current understanding of Strands Agents** inside `personal_knowledge`.

Raw observations/history remain in `mining-site/`, `quarries/` and `mk/`. This package consolidates current conclusions without deleting that evidence trail.

## Core thesis

**Strands is best understood as an in-process agent harness/SDK with a model-directed core loop plus several developer-selectable orchestration topologies. It is not a hosted control plane, security sandbox, production-readiness certificate or taxonomy of agent systems.**

Its engineering value is high because one framework exposes materially different control models—single-agent model-directed execution, deterministic Workflow, structured Graph, peer Swarm and manager/specialist agents-as-tools.

> **Framework identity is not architecture. Classify the control, capabilities, state, enforcement and failure semantics that actually execute.**

## What Strands supplies — and what the application still owns

At the pinned snapshot, Strands supplies agent-loop mechanics, model/tool integration, state/session abstractions, hooks, orchestration primitives, observability/evaluation surfaces and protocol adapters.

The application/deployment still owns major system responsibilities such as:

- deployment topology and process/container isolation;
- credentials, secrets, network and filesystem authority;
- tenant boundaries and data governance;
- tool/business authorization;
- idempotency, rollback and unknown-outcome handling;
- storage policy and concurrency semantics of concrete backends;
- SLOs, incident response and workload-specific certification.

Therefore `uses Strands` is never a complete system classification.

## Non-inferences

```text
Strands used                 != production ready
MCP connected                != authorized/safe execution
A2A supported                != A2A 1.0 compatible
structured output            != semantically correct output
session persistence          != safe multi-writer shared state
memory enabled               != trustworthy/isolated knowledge
HITL/steering available      != every side effect gated
cancellation supported       != remote effects rolled back
Graph/Swarm available        != multi-agent performs better
OpenTelemetry available      != production observability complete
```

## Core runtime mental model

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

The model proposes/selects actions; runtime/application/infrastructure boundaries determine what can actually execute.

## Control topologies inside one SDK

| Surface | Normalized interpretation | Main authority |
|---|---|---|
| Core `Agent` | bounded multi-step agent loop | model-directed inside runtime limits |
| Workflow | predefined tasks/dependencies | deterministic/developer-defined |
| Graph | developer topology with deterministic/model nodes | mixed |
| Swarm | peer agents handing work among themselves | model-directed / peers |
| Agents as tools | parent delegates to specialists | manager/specialist, often model-routed |

A single framework therefore cannot be one `agent_type`.

## State model

Keep these separate:

```text
conversation history
≠ invocation state
≠ agent/application state
≠ session persistence
≠ context-window management
≠ long-term memory
```

The strongest reusable conclusion is:

> **Persistence is not memory, and durability is not concurrency safety.**

Documented session handling assumes one live writer per conversation; that does not imply distributed locking for arbitrary backends/shared state.

## Effective capability boundary

Tool execution inherits authority available to the application/host unless separately constrained.

Effective capability is closer to:

```text
registered tools
+ host filesystem permissions
+ network reachability
+ credentials/secrets
+ subprocess/shell access
+ remote protocol endpoints
+ application policy wrappers
```

This is why least privilege belongs to the agent-system architecture rather than the prompt.

## Hooks, HITL and steering

Strands exposes multiple intervention mechanisms with different guarantees:

- deterministic hooks/application policy can block a dispatcher;
- human confirmation can authorize/reject an action;
- infrastructure/provider boundaries may enforce policy externally;
- LLM steering/model judges provide probabilistic guidance unless backed by deterministic enforcement.

> **Record enforcement owner and enforcement boundary. Behavior guidance is not authorization enforcement.**

## Budgets, termination and cancellation

Observed semantics show why numeric budgets alone are insufficient:

- checks occur at particular runtime boundaries;
- in-flight work may overshoot nominal values;
- cancellation is cooperative/boundary-dependent;
- arbitrary tools may continue unless they observe cancellation;
- remote protocol cancellation is not transactional rollback.

> **A budget value is incomplete without enforcement boundary and overshoot semantics.**

This distinction survived independent comparison with LangGraph and OpenAI Agents SDK and is now normalized in MK1.

## Concurrency

The Strands pass helped surface that:

- overlapping invocation/session usage has explicit constraints;
- persistence does not imply multi-writer safety;
- external/shared application state requires its own conflict/locking semantics.

Cross-runtime pressure confirmed concurrency belongs under normalized state semantics rather than a framework-specific category.

## Observability and evaluation

Strands exposes primitives for traces, model/tool metrics, token use, output evaluation, trajectory evaluation, session evaluation, deterministic evaluators, model judges and experiments.

Keep these evidence surfaces distinct:

```text
output correctness
trajectory correctness
side-effect verification
session/task outcome
production telemetry
```

Framework support does not imply a project has configured adequate graders, repeated trials or regression gates.

## MCP `2026-07-28`

For the pinned Python snapshot, modern MCP interoperability is **SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED**.

Current evidence covers modern negotiation/lifecycle, Streamable HTTP, tools, structured results/errors, multi-round-trip input, prompts/resources, list-change behavior and trace continuity, with explicit qualifications for deployment authorization, remote rollback and universal compatibility.

See [`PROTOCOLS.md`](./PROTOCOLS.md) and [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

## A2A — current qualified state

A2A is now revision-aware rather than `supported=true`.

Pinned dependency evidence:

```text
Python      a2a-sdk >=0.3.0,<0.4.0
TypeScript  @a2a-js/sdk ^0.3.10
```

The pinned source contains:

- `A2AAgent` client surfaces;
- Agent Card discovery;
- server/executor surfaces;
- sync/async invocation;
- streaming/task events;
- per-context server state patterns;
- an integration fixture that combines a remote `A2AAgent` node with a local Strands Graph node;
- integration workflow scope covering `tests_integ`.

But the current official A2A protocol line is **1.0**, which introduced breaking changes from 0.3.

Therefore the correct state is:

```text
Strands A2A 0.3 implementation       SUPPORTED / QUALIFIED
integration fixture source           PRESENT
specific successful fixture CI run   NOT VERIFIED
independent reproduction             NOT RUN
current A2A line                     1.0
Strands A2A 1.0 compatibility        NOT ESTABLISHED
MK1 classification-shape gate        PASS / QUALIFIED
```

The gate passes at MK1 because the schema can express revision, role, transport/task shape, auth/state boundaries and evidence strength without pretending current-version compatibility.

Also preserve the documented security distinction:

> `context_id` is a conversation/isolation key, **not an authentication boundary**.

See [`PROTOCOLS.md`](./PROTOCOLS.md) and [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md).

## What Strands changed in the general taxonomy

Strands initially surfaced three distinctions the earlier MK1 draft represented poorly:

```text
concurrency semantics
budget enforcement boundary / overshoot
intervention enforcement owner/boundary
```

They were not promoted from Strands alone. LangGraph and OpenAI Agents SDK independently confirmed them.

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

The framework was used as a **pressure instrument**, not as the taxonomy.

## Current Strands-specific unknowns / routed debts

- A2A `1.0` migration/interoperability at a newer/pinned implementation;
- specific successful A2A CI execution receipt for the studied fixture and/or independent rerun;
- application-specific idempotency and unknown-outcome handling for consequential tools;
- hard containment for arbitrary host-process tools;
- distributed concurrency behavior of each chosen persistence backend;
- Python/TypeScript feature parity as releases evolve;
- measured benefit of Graph/Swarm/agents-as-tools against simpler baselines;
- repeated/adversarial reliability of LLM-mediated steering;
- protected external MCP OAuth behavior for a concrete deployment;
- remote side-effect state after cancellation when work may already have begun.

These remain explicit because missing evidence must not be replaced by framework reputation.

## Recommended reading order

Human:

```text
README.md
→ ENGINEERING_RULES.md
→ CLASSIFICATION.md
→ PROTOCOLS.md when interoperability matters
→ EVIDENCE.md for audit
```

LLM/agent: start at [`LLM_CONTEXT.md`](./LLM_CONTEXT.md).

## Evidence chain

- source receipt: [`../../mining-site/S-109-strands-agents.md`](../../mining-site/S-109-strands-agents.md)
- detailed framework quarry: [`../../quarries/strands-agents.md`](../../quarries/strands-agents.md)
- runtime crosscheck: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md)
- MCP receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md)
- A2A receipt: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md)
- historical MK1 pressure test: [`../../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](../../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)
- current schema: [`../../mk/MK1/CLASSIFICATION_SCHEMA.md`](../../mk/MK1/CLASSIFICATION_SCHEMA.md)
- current gates: [`../../mk/MK1/GATES.md`](../../mk/MK1/GATES.md)
- domain status: [`../../STATUS.md`](../../STATUS.md)
