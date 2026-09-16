# Strands Agents — Engineering Quarry

Status: **PROCESSED EVIDENCE / NOT CANON**  
Observed: **2026-09-16**

## Research snapshot

| Field | Value |
|---|---|
| System | Strands Agents |
| Canonical docs | https://strandsagents.com |
| Canonical source repository | https://github.com/strands-agents/harness-sdk |
| Repository snapshot | `a9361c54ca190117d5801dd09a1ab8d6d3d9bf20` |
| Snapshot observed | 2026-09-16 |
| Python release observed | `python/v1.56.0` — 2026-09-15 |
| TypeScript release observed | `typescript/v1.18.0` — 2026-09-15 |
| License | Apache-2.0 |
| Primary provenance | `OFFICIAL` + `OBSERVED` |
| Use in this domain | MK1 framework pressure test / runtime architecture quarry |

Strands is treated here as a **framework implementation to classify**, not as an authority that can redefine the framework-independent taxonomy.

## Source set inspected

Primary sources:

- root monorepo README at the pinned snapshot;
- Agent Loop;
- Tools Overview / custom tools;
- Hooks and plugins;
- Steering / interventions;
- State Management;
- Session Management;
- Conversation Management;
- Memory;
- Structured Output;
- Multi-agent Graph, Swarm, Workflow and Agents-as-Tools;
- MCP integration and A2A integration;
- Observability / traces / metrics;
- Strands Evals SDK;
- Responsible AI / Guardrails;
- Operating Agents in Production;
- model-provider matrix;
- repository releases and repository-consolidation history.

Secondary official context:

- AWS Open Source posts describing the model-driven approach;
- AWS posts covering production architecture, Strands 1.0, open protocols and Strands Labs.

## 1. Identity and platform shape

**OBSERVED** — Strands is an open-source **library / SDK**, not a hosted agent platform. The agent runs inside the application process; the SDK does not require a hosted control plane, scheduler or database as a prerequisite.

**SUPPORTED** — This makes the host process itself a primary trust boundary. Strands can simplify the agent loop while leaving deployment topology, process isolation, secrets, network access, tenancy and infrastructure policy under the application owner.

**OBSERVED** — The source project was consolidated into `strands-agents/harness-sdk`, which now contains the Python SDK, TypeScript SDK, documentation site and supporting packages. Older standalone repositories such as `sdk-typescript` were archived during this migration.

### Engineering implication

`framework = Strands` does **not** imply a deployment architecture. The same SDK can run in a local process, container, serverless function or managed runtime. Deployment and containment therefore remain separate classification dimensions.

## 2. Core control model

**SOURCE CLAIM / OBSERVED** — Strands describes itself as model-driven. The core agent loop repeatedly:

1. sends current context to a model;
2. receives text, reasoning metadata and/or tool requests;
3. executes requested tools;
4. appends tool results;
5. invokes the model again until a terminal stop reason occurs.

This is a genuine model-directed control loop: the model chooses whether to answer or request tools.

**OBSERVED** — The runtime still owns important control mechanics:

- per-invocation turn limits;
- cumulative output-token limits;
- cumulative total-token limits;
- cancellation;
- stop reasons;
- concurrent-invocation protection;
- hook events around model and tool lifecycle boundaries.

### Important budget semantics

**OBSERVED** — invocation limits are **soft boundary checks**, not hard preemption. Limits are checked at the top of loop iterations. A model response can overshoot a token cap by one turn, and tools requested by the prior turn are allowed to complete before the next limit check.

**SUPPORTED** — A field such as `turn_budget: 5` is therefore incomplete evidence unless the classification also records **where the budget is enforced** and what work can still complete after the nominal threshold is reached.

### Cancellation semantics

**OBSERVED** — cancellation is cooperative. Strands checks cancellation at defined safe points. A non-MCP tool already executing can finish unless the tool itself observes the cancellation signal. MCP cancellation can be forwarded, but remote cancellation is best-effort.

**SUPPORTED** — `cancellation: yes` is insufficient as a reliability claim. Cancellation needs an enforcement-boundary qualifier: model stream, before-tool, in-tool cooperative cancellation, remote best-effort, or hard external process termination.

## 3. Multi-agent control topologies

Strands exposes several materially different orchestration forms. They must not collapse into one `multi_agent=true` label.

### Agents as tools

**OBSERVED** — a parent/orchestrator agent can expose specialist agents as tools. This is a hierarchical manager/specialist topology. The parent model decides when to delegate unless application code preselects the specialist.

### Graph

**OBSERVED** — Graph is developer-defined topology. Nodes may be agents, custom deterministic nodes, nested Graphs or Swarms. Edges establish dependency and information flow. Graphs can be acyclic or cyclic and can include conditional traversal.

**SUPPORTED** — Graph is usually **mixed control**: structure is developer-defined, while agent nodes can still use model-directed behavior and conditional decisions may introduce runtime routing.

### Swarm

**OBSERVED** — Swarm provides peer-style autonomous handoffs with shared working context. Agents decide when and where to hand off.

**SUPPORTED** — this is closer to `model_directed / peers` than to a deterministic workflow.

### Workflow

**OBSERVED** — Workflow is a pre-defined task dependency graph. Independent tasks can execute in parallel and dependency structure determines order. It is the most deterministic orchestration pattern in the Strands family.

### Qualification

**QUALIFIED** — the existence of Graph/Swarm/Workflow does not prove any one is better. Strands itself provides multiple control structures. Selection remains task-specific, and multi-agent complexity still requires outcome/cost/latency evidence against a simpler baseline.

## 4. State, context, session and memory

Strands strongly validates the domain's existing separation among state concepts.

### Runtime/context layers

**OBSERVED** — the SDK distinguishes:

- conversation history — model-visible messages and tool results;
- agent state — application state that can survive invocations when persisted;
- invocation state — ephemeral request-scoped data that need not enter model context;
- conversation management — strategies for fitting active context inside the model window;
- session management — persistence needed to resume a conversation / orchestrator state;
- long-term memory — knowledge recalled across sessions.

### Session persistence

**OBSERVED** — session managers can persist messages, agent state and related execution state. Single-agent snapshot managers support storage backends such as local files, S3 and custom storage; Graph/Swarm use repository-style session management.

**OBSERVED / IMPORTANT LIMIT** — session management is designed around a **single live writer per conversation**. The documented managers do not provide distributed locking and are not thread-safe for concurrent writers.

**SUPPORTED** — concurrency semantics are material enough to pressure-test MK1. Durability alone does not imply safe multi-writer semantics.

### Memory

**OBSERVED** — `MemoryManager` is cross-session knowledge, separate from session persistence. It supports:

- model-invoked recall/search;
- pre-model context injection;
- extraction of durable memories;
- configurable stores and tenant/user scopes.

**SUPPORTED** — this directly reinforces the invariant `persistence is not memory`. Conversation replay, session durability, context reduction and cross-session semantic memory are separate contracts.

## 5. Tools and capability boundary

**OBSERVED** — tools are the mechanism through which an agent can read data, mutate systems, execute code or call external services.

**OFFICIAL SECURITY STATEMENT** — Strands documents that tools execute with the permissions of the host process. The framework recommends auditing tool behavior and applying least privilege.

### Engineering implications

1. `tool schema valid` does not imply `tool safe`.
2. process credentials, filesystem access, network reachability and shell permissions remain part of the effective capability set.
3. a Strands deployment without external sandboxing can have a blast radius equal to the host process.
4. community tools must be audited separately from the core SDK.

**SUPPORTED** — this validates the existing `least privilege is an agent invariant` rule.

## 6. Hooks, plugins, interventions and steering

**OBSERVED** — hooks expose typed lifecycle callbacks around model calls, tool calls and orchestration events. They can observe or modify behavior.

**OBSERVED** — plugins build higher-level behavior on top of those primitives, including Skills, context injection/offloading and steering.

**OBSERVED** — steering can:

- allow a pending tool call;
- cancel it and feed guidance back to the agent;
- pause for human confirmation;
- inspect a model response and accept or guide a retry.

### Hard policy vs probabilistic steering

**IMPORTANT QUALIFICATION** — Strands also supports LLM-driven steering handlers, where another model evaluates whether an action should proceed, be guided or require confirmation.

**SUPPORTED** — this is useful for adaptive guidance, but it must not be conflated with a deterministic authorization boundary. A critical invariant that must never be bypassed still belongs in enforceable code, tool permissions, infrastructure or a deterministic dispatcher check.

This pressure test strengthens the distinction:

```text
behavior guidance != authorization enforcement
```

## 7. Structured output

**OBSERVED** — structured output is supported through Pydantic in Python and Zod in TypeScript. The SDK converts the schema to model-facing structure and validates the returned object.

**SUPPORTED** — schema validation improves interface reliability but does not certify semantic correctness. A well-typed wrong answer is still wrong.

## 8. Observability

**OBSERVED** — Strands includes agent-oriented observability primitives and OpenTelemetry tracing. Traces can include model calls, tool execution, latency and token usage.

The documented metric families include:

- tool invocation counts / duration / errors;
- loop-cycle counts;
- token usage;
- model latency and provider errors;
- system resource metrics;
- product/user-feedback signals.

**SUPPORTED** — this matches the domain principle that production agent observability must span both ordinary software telemetry and AI-specific execution telemetry.

## 9. Evaluation

**OBSERVED** — Strands Evals supports multiple evaluation levels and mechanisms:

- output-level evaluation;
- trace / trajectory evaluation;
- session-level evaluation;
- deterministic evaluators;
- LLM-as-a-judge evaluators;
- tool-use checks;
- simulated multi-turn users/tools;
- trace-based evaluation from observability backends;
- experiment serialization/versioning.

**SUPPORTED** — Strands is strong evidence that `outcome`, `trajectory`, `tool behavior` and `session success` are distinct evaluation surfaces.

**QUALIFIED** — built-in evaluator availability is not evidence that a specific deployed agent has adequate eval coverage. Repeated trials, held-out cases and project-specific outcome graders remain application responsibilities.

## 10. Protocols and interoperability

### MCP

**OBSERVED** — the SDK natively connects to MCP servers as a source of external tools.

### A2A

**OBSERVED** — Strands can consume and expose A2A-compatible agents. Remote agents can participate as explicit remote agents, graph nodes in supported configurations, or model-selected tools.

### Other protocol boundaries

Official Strands material also discusses AG-UI and x402 as integration boundaries in the wider ecosystem.

**SUPPORTED** — protocols move responsibilities across boundaries; they do not replace runtime authorization, persistence, evaluation or deployment policy.

**IMPORTANT** — protocol presence must remain revision-aware. `MCP=true` or `A2A=true` is incomplete evidence without version / implementation / transport / auth receipts.

## 11. Model-provider portability

**OBSERVED** — Strands is provider-agnostic and offers first-party or integrated support across multiple model providers. Current documentation shows broader Python coverage than TypeScript for some providers.

**SUPPORTED** — model portability is useful, but provider parity must be treated as a per-language/per-feature compatibility matrix, not as a blanket property.

## 12. Deployment and production posture

**OBSERVED** — Strands provides deployment guidance for Docker and infrastructure patterns including serverless and container targets. The production guide recommends explicit model configuration, explicit tool lists, least privilege, input validation, output sanitization, execution limits, error handling and observability.

**SUPPORTED** — these are production-oriented controls, but the SDK being production-capable does not make every Strands application production-ready.

A production-readiness claim still requires project-specific evidence for:

- isolation and secrets;
- authentication/authorization;
- tenancy;
- availability / SLOs;
- replay / retry safety;
- idempotency;
- data retention;
- incident response;
- rollback;
- eval/regression gates;
- threat model and abuse testing.

## 13. Ecosystem maturity and experimental boundary

**OBSERVED** — Strands has a fast-moving ecosystem with stable SDK releases plus separate experimental work such as Strands Labs and Agent SOPs.

**SUPPORTED** — experimental patterns should stay outside canon until independently validated. Repository/source consolidation also means old links and old standalone-repository assumptions can drift quickly; exact snapshot receipts matter.

## 14. Pressure test against current agent-engineering invariants

| Existing candidate invariant | Strands pressure-test result |
|---|---|
| simplest sufficient architecture | **SUPPORTED** — SDK includes deterministic Workflow and structured Graph in addition to model-driven loops; architecture remains a choice |
| policy belongs in enforceable code | **SUPPORTED / STRENGTHENED** — deterministic hooks/tool boundaries can enforce; LLM steering is adaptive guidance, not automatically hard authorization |
| every loop is bounded | **SUPPORTED WITH QUALIFICATION** — limits exist, but are opt-in and soft at loop boundaries |
| tools are typed contracts | **SUPPORTED** — typed/schema tooling exists; permissions and side effects still require separate control |
| side effects cross a policy boundary | **SUPPORTED AS REQUIREMENT, NOT AUTOMATIC** — framework exposes interception points but does not infer business risk for each action |
| context is curated state | **STRONGLY SUPPORTED** — explicit conversation, agent state, invocation state, context management, session and memory separation |
| persistence is not memory | **STRONGLY SUPPORTED** — session and MemoryManager are distinct mechanisms |
| agent says DONE != task is DONE | **SUPPORTED** — `end_turn` is a loop stop reason, not external-world outcome proof |
| evaluate outcomes and trajectories | **SUPPORTED** — Evals SDK explicitly separates evaluation surfaces |
| multi-agent must earn complexity | **NOT CONTRADICTED** — multiple topologies exist; no general benchmark guarantee makes complexity free |
| least privilege is an agent invariant | **STRONGLY SUPPORTED** — official tool security guidance states host-process permission inheritance |
| frameworks are adapters, not truth | **SUPPORTED** — Strands exposes several architectures and providers rather than one universal topology |
| version compatibility is evidence | **STRENGTHENED** — 2026 monorepo consolidation and uneven Python/TS support make snapshot/version receipts important |

## 15. New candidate dimensions surfaced by Strands

These are **not promoted to schema yet**. They are pressure-test findings that need independent confirmation.

### A. Concurrency semantics

Candidate placement: under `state` or `reproducibility`.

Questions:

- one invocation per agent instance or concurrent?
- single writer or multi-writer state?
- local mutex / distributed lock / optimistic concurrency / none?
- what happens on duplicate concurrent invocation?

Reason: Strands explicitly documents one-live-writer assumptions and default rejection of overlapping calls on an agent instance.

### B. Budget enforcement boundary

Candidate placement: under `termination`.

Questions:

- hard pre-call vs soft turn-boundary cap?
- can an in-flight model/tool exceed the nominal budget?
- can a running external side effect continue after cancellation?

Reason: Strands demonstrates that `budget value` and `enforcement semantics` are separate engineering facts.

### C. Intervention enforcement owner

Candidate placement: under `human_control` / `security`.

Questions:

- deterministic code/policy engine?
- model judge / LLM steering?
- human approval?
- provider guardrail?
- external infrastructure gate?

Reason: two systems can both claim “guarded tool calls” while one is hard policy and another is probabilistic guidance.

## 16. Material UNKNOWNs / open validation debt

1. Exact current compatibility evidence between Strands MCP integrations and the domain-pinned MCP `2026-07-28` contract needs a dedicated protocol-level execution pass.
2. A2A version/auth/interoperability should be pinned before treating it as reproducible evidence.
3. Generic exactly-once / transactional semantics are not guaranteed by the SDK; consequential tools require project-specific idempotency and receipt design.
4. Durable session storage does not imply safe distributed multi-writer execution.
5. Cooperative cancellation is not equivalent to hard termination of arbitrary in-process tools.
6. Provider feature parity differs between Python and TypeScript and can drift by release.
7. Built-in/community tool packages must be audited independently from the core SDK.
8. Production-readiness remains workload-specific despite production deployment guides.
9. Multi-agent benefit requires benchmark evidence per task/topology/model/toolset.
10. LLM-based steering needs adversarial and repeated evaluation before use as a reliability mechanism.

## 17. Reusable engineering takeaways

**SUPPORTED candidate rules from this quarry:**

1. **Budget value and budget enforcement semantics are separate contracts.**
2. **Concurrency belongs in agent state architecture, not only infrastructure notes.**
3. **Cancellation must name the cancellation-safe boundary.**
4. **Adaptive steering is not automatically authorization.**
5. **In-process agent libraries inherit the host process blast radius unless externally contained.**
6. **Session durability, context management and long-term memory require separate schemas.**
7. **Multi-agent topology must record who chooses the next actor: code, graph condition, manager model or peer model.**
8. **Protocol adapters require version/auth/transport receipts; protocol support is not a security guarantee.**
9. **Structured output validates shape, not truth.**
10. **A framework's production features are capabilities, not a production-readiness certificate for applications built with it.**

## Promotion decision

Strands Agents is a **high-value MK1 pressure-test source** because it exposes a broad, modern agent runtime while making several operational constraints explicit.

It should be retained as:

- a reference implementation quarry;
- a model-driven agent-loop example;
- a multi-agent topology comparison source;
- an evidence source for state/session/memory separation;
- an observability/evaluation implementation example;
- a counterexample showing why budget, cancellation and concurrency semantics need more detail than boolean support flags.

It should **not** become:

- the taxonomy itself;
- a universal architecture recommendation;
- proof that model-driven orchestration is superior for every workload;
- proof that applications using Strands are secure or production-ready.
