# REC-012 — Executed actor-topology comparison (partial receipt)

**Status:** EXECUTED / QUALIFIED DETERMINISTIC OBSERVATION / **G7 AT EXECUTION TIME OPEN**  
**Date:** 2026-10-12  
**Fixture and source:** [rec-012](../experiments/rec-012/README.md)  
**Target gate:** [MULTI_AGENT_BASELINE_SPEC](../mk/MK1/MULTI_AGENT_BASELINE_SPEC.md)

## Predeclared admission hypothesis

Parallel specialists observing independent tool surfaces could shorten completion, **but** orchestration overhead may exceed savings for fast tasks. Compare this with a one-actor sequential baseline under identical tasks, tools, combining rule and quality rubric. Negative, neutral or inconclusive outcomes are valid.

## Experimental identity

**Task:** deterministic incident triage from logs + impact metadata. `fixtures.json` has **16 manually labelled** cases. `benchmark.py` executes **30 repetitions per task per topology**, recording wall-time, outcome, tool calls, handoffs and six injected failure modes.

| Category | Single baseline | Manager + two specialists |
|---|---|---|
| Agent classification | deterministic policy actor | manager_workers topology, deterministic policy actors |
| Control authority | deterministic | deterministic; termination owned by manager |
| Delegation | none | two independent specialists (logs, impact) |
| Model count | 0 | 0 |
| Concurrency | serial-only | local 2-thread pool per call; one manager writer |
| Shared state | immutable input | immutable input, typed handoffs to coordinator |
| Persistence / memory | none | none |
| Tools and side effects | two local read-only tools, S0 | same tools, same S0 |
| Time budget | 10ms checked at boundaries | 10ms coordinator deadline + cooperative cancellation |
| External protocols/auth | none | none |

No external side effects, persistent agents, cross-model communication, tokens or inference. **This is a topology exercise, not a true LLM multi-agent benchmark.** Thread-pool cold-start cost is included in the multi-actor timing.

## Executed outcome (preserved reproducible receipt)

| Metric | Single | Multi | Scope |
|---|---:|---:|---|
| Nominal task attempts | 480 | 480 | 16 fixtures × 30 |
| Correct according to labels | 480 | 480 | fixed handcrafted rubric |
| Wrong / terminated | 0 | 0 | nominal path only |
| Median wall-time | 0.005468ms | 0.148609ms | local short CPU-bound tools |
| p95 wall-time | 0.008613ms | 0.339741ms | scheduler dependent |
| Total observed tool invocations | 960 | 960 | identical tool count |
| Handoffs | 0 | 960 | two per multi invocation |
| Model calls | 0 | 0 | no LLM present |
| Tokens / model bill | NOT_APPLICABLE | NOT_APPLICABLE | **not** financial evidence |
| External API calls | 0 | 0 | isolated fixture |

The observed multi median was approximately **27.2× the baseline** in the preserved second run. An earlier local run on the same date measured medians 0.004156ms and 0.086831ms (~20.9×). Such microbenchmarks are **unstable** and dominated by per-run worker/thread startup. Neither ratio describes real LLM agent cost or latency.

## Fault, containment and termination observations

Fault injection was actually executed against both topologies:
- `logs:raise`, `impact:raise` → structured tool errors;
- `logs:malformed`, `impact:malformed` → validation rejects the handoff/output;
- `logs:stall`, `impact:stall` → `time-budget-exceeded` status.

All 12 fault/topology combinations were explicitly recorded as **failed**, never a false successful output. Six `unittest` test cases passed locally; these are method counts, not the case-set size.

In-flight Python threads cannot be forcibly stopped by `future.cancel()`; injected 25ms stalls had elapsed times around 25–26ms even with a 10ms deadline. **Timeout request ≠ hard cancellation ≠ rollback**. No mutating operations existed, so side-effect/idempotency guarantees were not tested. Critical-path coordination waiting and resource contention are NOT_MEASURED.

## Local command and custody

```bash
python -m unittest -q
python benchmark.py --trials 30 --timeout-ms 10
sha256sum benchmark.py fixtures.json test_benchmark.py results.json
```

Observed: `Ran 6 tests ... OK`, 960 nominal executions (all expectations matched), six fault types. Python 3.13.5, Linux x86_64. Files were read back from GitHub and match the local Git blob hashes.

| Artifact | SHA-256 at execution |
|---|---|
| `benchmark.py` | `ac0449a2001039b3a30b637bd3529e724b267fce557fea5e8c3536255bd17098` |
| `fixtures.json` | `1242efb8b852de7a3e18dcb6f1018e97120766409da622ac42122cd614241b5b` |
| `test_benchmark.py` | `78d1e2bafc57a4420e3374d79469f6dd6196b34de8debc5a7b1a6e1f83ec8198` |
| `results.json` | `565a972b65957d9f766feb13381c7e1a0b0bd9be0462f8d818ee06123b01dea3` |

## G7 interpretation and decision

**What this proves (scoped):** under a shared task/evaluation contract, an added coordinator and specialist handoffs can preserve quality while adding measurable coordination overhead; tool errors, malformed transfers and timeouts are independently observable from topology.

**What remains unknown:** real model-directed planning quality, model-provider/config parity, independent live evaluator, tokens and billing, stochastic variance, agent conversation dynamics, useful parallel external tools, session/checkpoint durability, concurrency beyond process, safe external side effects and production viability.

**Historical decision for this fixture: G7 OPEN / EVIDENCE_PARTIAL**, because it had no LLM inference. A subsequent separate [real-model external evidence receipt](./multiagent-external-scaling-evidence.md) leads to [REC-012 MATERIALIZED / QUALIFIED_UPSTREAM](../mk/MK1/records/REC-012-external-agent-scaling.md). The local trial remains non-LLM. MK1 still IN PROGRESS; MK2 still BLOCKED.

**Exact remaining experiment:** same held-out tasks; same accessible tools; a bounded tool-using single *real-model* agent vs manager + 2 real-model specialist agents; pinned provider/model/revision, decoding, explicit token/cost/time budgets, held-out grader, multiple stochastic trials, handoff failure and termination observations. Local inference or explicitly authorized credits only. If not available, retain OPEN state.

No new features, product integrations, model subscriptions, GitHub Actions or production deployments are authorized.
