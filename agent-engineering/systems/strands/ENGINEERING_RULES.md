# Strands Agents — Reusable Engineering Rules

Status: **CURRENT SYNTHESIS / NOT UNIVERSAL CERTIFICATION**  
Purpose: extract reusable engineering lessons from the Strands study without turning framework behavior into framework-independent truth by assertion.

Every rule below is either already supported by cross-source evidence or explicitly qualified.

## 1. Framework identity is not architecture

**State: STRONGLY SUPPORTED**

Strands contains model-directed `Agent`, deterministic Workflow, mixed Graph, peer Swarm and manager/specialist agents-as-tools inside one SDK.

Therefore:

```text
framework_name → implementation identity
control/topology/state/capabilities → architecture
```

Do not classify a system as simply `Strands agent`. Record the execution authority and topology actually used.

## 2. The model operates inside a runtime envelope

**State: SUPPORTED**

The model can choose tools and continuation in the core loop, while the runtime owns loop mechanics such as limits, cancellation checks, hooks, state transitions and tracing.

Engineering consequence:

> Model autonomy and runtime authority are separate dimensions.

A model deciding *what it wants to do* does not mean the model should decide *what it is allowed to do*.

## 3. Critical policy belongs on an enforceable boundary

**State: CROSS-RUNTIME SUPPORTED**

Strands supports deterministic hooks, human confirmation, provider/infrastructure controls and LLM-mediated steering. These mechanisms are not equivalent.

Use model steering for adaptive guidance, not as the only enforcement mechanism for invariants that must never be bypassed.

For consequential actions, record:

```text
enforcement owner
→ enforcement boundary
→ dispatcher coverage
→ approval binding
→ revalidation after edit
```

## 4. Tool schema is not tool security

**State: STRONGLY SUPPORTED**

Typed inputs/outputs improve the agent-computer interface. They do not constrain filesystem, network, secrets or subprocess permissions available to the underlying implementation.

Effective authority is determined by reachable capabilities plus the host environment.

A valid schema can still wrap a dangerous dispatcher.

## 5. Least privilege must be designed outside the prompt

**State: STRONGLY SUPPORTED**

Because tools execute within the host application's authority unless separately constrained, sandboxing and least privilege are deployment/application responsibilities.

Prefer capability-specific isolation over broad process authority:

```text
narrow tool
+ narrow credential
+ narrow network scope
+ narrow filesystem scope
+ explicit policy
> prompt instruction saying "be careful"
```

## 6. Persistence is not memory

**State: CROSS-SOURCE SUPPORTED**

Strands distinguishes active conversation, invocation state, agent state, session persistence, context management and long-term memory.

Do not collapse these into `memory=true`.

Each has a different contract for:

- lifetime;
- visibility to the model;
- retrieval;
- mutation;
- isolation;
- retention;
- replay;
- provenance.

## 7. Durability is not concurrency safety

**State: CROSS-RUNTIME SUPPORTED / PROMOTED TO MK1**

The Strands session model exposed the danger of inferring safe shared-state concurrency from durable storage. LangGraph and OpenAI Agents SDK supplied independent pressure evidence for concurrency as a distinct state concern.

Record:

```text
invocation concurrency
writer model
locking model
conflict semantics
```

Do not infer them from the storage backend name.

## 8. A budget value is incomplete without enforcement semantics

**State: CROSS-RUNTIME SUPPORTED / PROMOTED TO MK1**

Strands showed that turn/token limits can be checked at loop boundaries, allowing in-flight work or one response to exceed the nominal threshold before the next check.

A useful budget record needs:

```text
budget type/value
+ check boundary
+ overshoot behavior
+ in-flight work behavior
+ cancellation boundary
```

`max_turns=10` and another runtime's `10`-step limit are not automatically equivalent.

## 9. Cancellation is not rollback

**State: SUPPORTED**

Stopping future runtime progress does not prove that an already-dispatched tool or remote service reverted its external effects.

For mutating operations, cancellation must be paired with independent reasoning about:

- idempotency;
- request identity;
- unknown outcome after timeout;
- server-side cancellation semantics;
- compensating actions;
- external verification.

## 10. Protocol compatibility is a vector, not a boolean

**State: STRONGLY SUPPORTED BY MCP PASS**

The Strands MCP study demonstrates why `MCP=true` is low-quality evidence.

A protocol receipt should identify at least:

```text
revision
negotiation/lifecycle
transport
core request behavior
extensions
authentication/authorization
cancellation semantics
observability continuity
execution evidence
```

The pinned Strands Python MCP path passes modern `2026-07-28` core interoperability evidence upstream, while deployment-specific OAuth authorization and remote rollback remain separate questions.

## 11. Runtime completion is not task completion

**State: SUPPORTED**

An `end_turn`/terminal model response proves that the loop stopped. It does not prove that a business objective is true in the external world.

Use outcome evidence such as:

- state readback;
- deterministic assertions;
- receipts;
- integration checks;
- domain graders;
- human verification where required.

## 12. Output, trajectory and session success are different evaluation surfaces

**State: SUPPORTED**

Strands Evals/observability surfaces reinforce that a good final response can hide a bad trajectory, and a reasonable trajectory can still fail the intended outcome.

Evaluate separately when material:

```text
static/schema correctness
trajectory/tool behavior
external outcome
session/task success
cost/latency
production telemetry
```

Repeated trials remain necessary for stochastic behavior; framework evaluator availability does not make them automatic.

## 13. Structured output improves contract reliability, not truth

**State: SUPPORTED**

Pydantic/Zod validation can prove shape compatibility. It cannot prove that the generated values are factually or semantically correct.

Treat structured output as an interface contract, not an outcome verifier.

## 14. Multi-agent topology must earn its complexity

**State: QUALIFIED / STILL REQUIRES BENCHMARK EVIDENCE**

Strands makes several multi-agent shapes easy to express. That is an implementation capability, not proof of better performance.

A Graph, Swarm or agents-as-tools design should be compared against a simpler baseline on task-relevant metrics such as:

- success rate;
- latency;
- token/cost usage;
- failure containment;
- coordination overhead;
- reproducibility.

No general performance rule is promoted until this evidence exists.

## 15. Production readiness is a vector of project evidence

**State: SUPPORTED**

Strands provides production-oriented guidance and deployment patterns, but a concrete application still needs its own evidence for:

- authn/authz;
- tenant and secret isolation;
- least privilege;
- idempotency/retry safety;
- data retention;
- observability/SLOs;
- eval/regression gates;
- rollback/incident response;
- threat/abuse testing.

Therefore:

```text
production-capable SDK != production-ready application
```

## 16. Use frameworks as pressure tests, not sources of taxonomy

**State: METHOD RULE / VALIDATED BY THIS STUDY**

The most important methodological result is how Strands was used.

Strands surfaced three missing distinctions. They were not immediately promoted. They were tested against LangGraph and OpenAI Agents SDK, and only the reusable semantics survived into MK1.

Preferred knowledge workflow:

```text
framework observation
→ candidate distinction
→ independent pressure test
→ normalized semantics
→ schema promotion
→ later operational contract/test
```

This prevents the knowledge base from becoming a catalog of framework vocabulary.

## Current non-rules / claims we deliberately do not make

The Strands study does **not** establish that:

- Strands is the best framework;
- model-driven orchestration is generally superior;
- Swarm is superior to Graph or Workflow;
- built-in memory is trustworthy by default;
- MCP use is safe by default;
- steering by an LLM is deterministic authorization;
- all provider integrations have feature parity;
- cancellation guarantees remote effect reversal;
- every Strands application is production-ready.

Those would require evidence outside what this package proves.
