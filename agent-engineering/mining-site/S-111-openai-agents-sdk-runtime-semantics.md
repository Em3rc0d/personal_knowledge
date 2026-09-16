# S-111 — OpenAI Agents SDK runtime semantics

Status: **REGISTERED / OFFICIAL + OBSERVED**  
Observed: **2026-09-16**

## Source identity

| Field | Value |
|---|---|
| ID | `S-111` |
| System | OpenAI Agents SDK (Python) |
| Type | open-source agent runtime + official documentation |
| Documentation | https://openai.github.io/openai-agents-python/ |
| Repository | https://github.com/openai/openai-agents-python |
| Snapshot | `5f9899d584c5cfc879d3579352eb929fd4b34756` |
| Snapshot observed | 2026-09-16 |
| Latest release observed | `v0.22.2` — 2026-09-09 |
| License | MIT |
| Use here | independent MK1 pressure test for budget enforcement, intervention ownership, concurrency and guardrail timing |
| Authority | official for OpenAI Agents SDK behavior; not normative for all runtimes |
| Confidence | HIGH for documented/source-specific behavior |

## Primary evidence inspected

- `Running agents` official documentation;
- `Guardrails` official documentation;
- `Handoffs` official documentation;
- `Sessions` official documentation;
- multi-agent orchestration guidance;
- current repository source around `max_turns` enforcement;
- current public repository/release metadata.

## Material observations

### Budget value and enforcement boundary are distinct

The runner exposes `max_turns`; exceeding it raises `MaxTurnsExceeded`. Source inspection at the pinned snapshot shows the runtime tracks `current_turn` and checks the configured turn limit inside the run loop.

The broader runtime also exposes tool timeouts and cancellation primitives. These controls operate at different boundaries and should not collapse into one generic `bounded=true` field.

### Guardrail timing changes safety semantics

Input guardrails can run in two modes:

- **blocking** — guardrail completes before model/tool execution begins;
- **parallel** — guardrail and agent execution start concurrently.

The official documentation explicitly warns that with parallel execution the model may already have consumed tokens or executed tools before the guardrail trips.

This independently proves that `guardrail present` is insufficient. Classification must record the **enforcement owner and boundary**.

### Tool-level and agent-level controls have different coverage

Agent input/output guardrails apply at workflow boundaries. Tool guardrails apply to guarded function-tool calls, but not every hosted/built-in tool or handoff path shares the same pipeline. Authorization that depends on handoff arguments belongs at the start of the handoff callback, before application side effects.

This reinforces the domain rule that enforcement coverage must be tied to the actual dispatcher/call path.

### Tool concurrency is separately configurable

The runner can bound SDK-side local function-tool concurrency per turn. Provider-side parallel tool calls remain a separate mechanism.

This supports representing concurrency semantics explicitly instead of inferring them from `async`, `parallel tools`, or session persistence.

## Promotion boundary

Use this source to normalize enforcement timing and concurrency/budget semantics. Do not infer that guardrails automatically cover every tool path or that a configured turn limit proves semantic completion.

Cross-source synthesis: [`../quarries/runtime-semantics-strands-langgraph-openai.md`](../quarries/runtime-semantics-strands-langgraph-openai.md)
