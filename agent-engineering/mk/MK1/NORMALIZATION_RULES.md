# MK1 — Normalization Rules

Status: **OPEN / IN PROGRESS**  
Aligned schema: **`mk1-draft-2026-09-16.1`**

## Core rule

> Classify what the system can actually decide and do, not what its repository, framework or marketing copy calls it.

## NR-01 — Prefer orthogonal dimensions

A single `agent_type` field is insufficient because one system can combine deterministic stages, model routing, model-directed tools, human-gated writes and durable runtime state.

Separate at minimum:

- control authority;
- capability;
- side-effect class;
- state/checkpoint/persistence/concurrency semantics;
- memory lifecycle;
- human control and enforcement ownership;
- retry/error ownership;
- termination and budget enforcement;
- evaluation;
- protocol revision;
- security/reproducibility.

## NR-02 — Framework identity is metadata

`LangGraph`, `LangChain`, `CrewAI`, `AutoGen`, PydanticAI, MCP or a model vendor may matter for implementation and reproducibility, but none is sufficient as an architecture class.

## NR-03 — Authority outranks intent labels

Words such as `scraper`, `tester`, `assistant`, `converter`, `researcher` or `publisher` do not determine risk.

Classify reachable authority:

- can it read?
- can it write?
- can it execute code?
- can it access shell/browser/database?
- can it communicate externally?
- can it publish or move data across a trust boundary?

## NR-04 — Generation and execution are separate privileges

Model output remains data until a trusted execution boundary promotes it to action.

Generated code, SQL, shell commands, emails or social posts must not be treated as executed merely because they were generated.

## NR-05 — Side effects are independent from autonomy

Do not equate `more agentic` with `more dangerous`, or deterministic with safe. Side-effect class is its own axis.

## NR-06 — Preserve lifecycle semantics

Do not collapse state, checkpointing, persistence, context, memory and knowledge/RAG into one `memory` field.

Memory classification must expose:

- semantic role;
- scope;
- persistence;
- retrieval/write policies;
- isolation;
- retention;
- provenance.

## NR-07 — Human control is only as strong as enforcement

A UI approval, reviewer node or interrupt does not prove a consequential action is gated.

Classify whether the actual dispatcher independently enforces authorization and whether edited arguments invalidate prior approval/validation.

## NR-08 — Retry semantics belong to the system

A model should not infer retry policy solely from prose errors.

Classify:

- error type;
- retry owner;
- retry budget;
- idempotency/verification;
- unknown-outcome behavior.

## NR-09 — Termination has multiple budgets

Do not reduce termination to one recursion/turn limit. Separate semantic success from kill switches and resource budgets.

## NR-10 — Evaluation must distinguish trajectory and outcome

A trace can be policy-correct while the real outcome is wrong; an outcome can be correct through an unexpected but valid trajectory.

Record both when material.

## NR-11 — Stochastic evidence requires repeated trials

A single successful run demonstrates possibility, not stable behavior.

## NR-12 — Reflection is not automatically learning

Use:

```text
reflection
revision loop
feedback-driven adaptation
persistent learning
```

as distinct concepts.

Claims of `self-improvement` require measured improvement across an evaluation distribution and a defined persistence mechanism.

## NR-13 — Multi-agent must carry an admission hypothesis

Record why multiple agents exist and what baseline they outperform.

Without measured benefit, classify topology but do not promote it as a best practice.

## NR-14 — Protocols are revisioned contracts

`MCP` or another protocol flag must include revision/role/capabilities/transport/auth assumptions when those details affect behavior.

Protocol discovery does not imply authorization.

## NR-15 — UNKNOWN is first-class

If a material fact is not supported, record `UNKNOWN`.

Do not infer approval coverage, sandboxing, idempotency, persistence or production readiness from adjacent features.

## NR-16 — Classification is not certification

A complete record describes architecture and evidence state. It does not prove the system is secure, reliable or production-ready.

Operational claims belong to MK2+ evidence gates.

## NR-17 — Persistence does not imply concurrency safety

A durable checkpoint/session store does not reveal whether concurrent invocations or writers are safe.

When shared state or parallel execution is reachable, classify:

- invocation concurrency;
- writer model;
- conflict/merge semantics;
- locking/serialization mechanism.

A reducer-based merge, a single-writer session, an optimistic version check and distributed locking are materially different contracts.

This rule is supported independently by Strands Agents, LangGraph and OpenAI Agents SDK runtime behavior.

## NR-18 — Budget values require enforcement semantics

`max_turns=10`, `recursion_limit=25`, a wall-clock timeout and a token cap are not interchangeable evidence.

Record where a budget becomes effective and whether work already in flight may complete or overshoot the nominal limit.

For consequential work, also record whether cancellation is hard, cooperative, boundary-based or best-effort remote.

A kill switch is still not a semantic success predicate.

## NR-19 — Intervention mechanism is not enforcement strength

`guardrail`, `interrupt`, `approval`, `steering` and `judge` are implementation labels, not equivalent policy guarantees.

Classify:

- enforcement owner;
- enforcement boundary;
- dispatcher binding;
- approval binding/revalidation when arguments change.

Deterministic pre-dispatch policy, human approval, model-mediated judging, provider guardrails and infrastructure policy may all coexist, but their guarantees differ. Parallel validation that can trip after model/tool work begins must not be described as equivalent to blocking pre-effect authorization.
