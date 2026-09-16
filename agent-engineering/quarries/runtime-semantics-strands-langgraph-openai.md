# Runtime Semantics — Strands × LangGraph × OpenAI Agents SDK

Status: **PROCESSED CROSS-SOURCE EVIDENCE / MK1 PROMOTION CANDIDATE**  
Observed: **2026-09-16**

## Sources

- `S-109` — Strands Agents `harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20`
- `S-110` — LangGraph `@230927fb3a9ac9b2893a30322b4dfea7cdea9a8f`
- `S-111` — OpenAI Agents SDK `@5f9899d584c5cfc879d3579352eb929fd4b34756`

Purpose: determine whether three distinctions surfaced by the Strands pressure test are framework-specific accidents or reusable agent-engineering dimensions.

## Promotion rule applied

MK1 permits a schema change only when:

1. existing fields materially distort the engineering difference;
2. the difference affects behavior, risk, reliability, evaluation or reproducibility;
3. at least two independent examples or one strong counterexample justify it;
4. the proposed field does not duplicate an existing dimension.

All three candidates below now have independent evidence across materially different runtimes.

---

## 1. Concurrency semantics

### Strands

**OBSERVED** — overlapping invocation on one agent instance is rejected by default, session managers assume one live writer per conversation, and documented session managers do not provide distributed locking.

### LangGraph

**OBSERVED** — parallel nodes may update graph state concurrently. If multiple nodes write the same state key without a reducer, the runtime raises `INVALID_CONCURRENT_GRAPH_UPDATE`. Explicit reducers define merge semantics.

### OpenAI Agents SDK

**OBSERVED** — local function-tool concurrency can be bounded independently from provider-side parallel tool calling. Session/context persistence and tool execution therefore have concurrency behavior that must be described separately.

### Cross-source conclusion

**SUPPORTED** — `persistence_backend` and `checkpointing` cannot represent concurrency safely. Two durable systems may differ materially in:

- whether invocations may overlap;
- whether one or many writers may update state;
- whether conflicts reject, serialize, reduce/merge or use another policy;
- whether locking is local, distributed, optimistic, custom or absent.

### Promotion

Promote concurrency as a **state subdimension**, not a new top-level axis.

---

## 2. Budget enforcement boundary

### Strands

**OBSERVED** — turn/token limits are checked at loop boundaries; an in-flight model response can overshoot token thresholds and tool work requested by the previous turn may complete before the next limit check. Cancellation is cooperative at documented safe points.

### LangGraph

**OBSERVED** — `recursion_limit` stops a graph after the configured number of steps if no stop condition was reached. It is a graph-execution kill switch, not semantic success evidence.

### OpenAI Agents SDK

**OBSERVED** — `max_turns` is enforced by the runner and raises `MaxTurnsExceeded`. Source inspection shows turn counting/checking inside the run loop. Tool timeouts and cancellation are separate mechanisms with their own boundaries.

### Cross-source conclusion

**SUPPORTED** — a budget value without an enforcement boundary is incomplete architecture evidence. `max_turns=10`, `recursion_limit=25` and `token_budget=N` do not imply the same semantics.

Classification must distinguish at least:

- budget value/type;
- where enforcement occurs;
- whether in-flight work may complete;
- overshoot semantics;
- cancellation boundary and whether termination is cooperative, hard or best-effort remote.

### Promotion

Promote budget-enforcement qualifiers inside **termination**.

---

## 3. Intervention enforcement owner

### Strands

**OBSERVED** — interventions may be deterministic hooks, human confirmation, provider/infrastructure controls or LLM-mediated steering. Model-based steering is probabilistic behavior guidance unless backed by a deterministic policy boundary.

### LangGraph

**OBSERVED** — `interrupt()` can be placed directly inside a tool before a side effect, allowing human approval/edit/reject before dispatcher execution. On resume, the node restarts from its beginning, making side-effect placement and replay safety material.

### OpenAI Agents SDK

**OBSERVED** — input guardrails can be blocking or parallel. In parallel mode, agent work may already have consumed tokens or executed tools before a tripwire stops subsequent processing. Tool guardrails cover a different call path from handoffs and some hosted/built-in tools; authorization for handoff arguments must be enforced before application side effects.

### Cross-source conclusion

**SUPPORTED** — `guardrail=true`, `HITL=true` or `approval_before=true` is insufficient. The classification must state **who/what owns enforcement** and whether that owner sits on the consequential dispatch path.

Relevant owners include:

- deterministic runtime/application code;
- human reviewer;
- model judge / LLM steering;
- provider guardrail;
- infrastructure/policy layer;
- mixed composition.

### Promotion

Promote `enforcement_owner` inside **human_control** and retain `dispatcher_enforcement` as the stronger call-path property.

---

## 4. Replay is adjacent but already represented

LangGraph adds strong evidence that resume semantics can replay node code before an interrupt. This does **not** require a new top-level field because `state.replay_semantics` already exists.

However, MK2 should eventually operationalize a rule:

> Consequential effects before replayable checkpoint/interrupt boundaries require idempotency, deduplication, verification or compensating behavior.

This remains a candidate operational contract, not MK1 certification.

## 5. Schema promotion decision

The three Strands candidates now satisfy the MK1 admission rule through independent evidence:

```text
concurrency semantics       → PROMOTE under state
budget enforcement boundary → PROMOTE under termination
intervention owner          → PROMOTE under human_control
```

Do **not** create framework-specific fields such as `langgraph_reducer`, `strands_session_lock` or `openai_guardrail_mode`. Normalize the engineering semantics instead.

## 6. Residual UNKNOWNs

Promotion of the dimensions does not close implementation-specific questions:

- exact distributed-lock/optimistic-concurrency behavior of each persistence backend;
- exact hard-vs-cooperative cancellation semantics for every tool/provider path;
- whether a specific application revalidates edited actions after approval;
- coverage gaps for hosted/built-in tool classes in individual runtimes;
- exact protocol cancellation behavior across MCP/A2A remote boundaries;
- project-specific idempotency and unknown-outcome recovery.

These remain explicit UNKNOWNs or MK2+ contract/evaluation debt.

## 7. Next gate

With these runtime semantics normalized, the next high-value gate is the executable **Strands ↔ MCP `2026-07-28`** compatibility fixture already identified by `S-109`.

That fixture should verify protocol version receipt, discovery/tool invocation, auth boundary, cancellation behavior and trace continuity without treating MCP interoperability as authorization.
