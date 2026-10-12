# REC-012 — Offline topology baseline

**Status: EXECUTED / PARTIAL EVIDENCE / NON-CERTIFYING**  
**Scope: one deterministic policy actor versus a manager plus two policy specialists. No LLM was used.**

## Hypothesis and task

Two independently observable incident attributes might benefit from specialist concurrency, but coordination overhead can dominate trivial CPU-fast tools.

The task: triage immutable logs and impact metadata into incident category, responsible team and severity, compared with **16 manually labeled fixtures**. These include user-count boundary cases, security, DB, payment, frontend, integration and unknown scenarios.

## Topology and parity

| Attribute | Baseline | Multi-actor |
|---|---|---|
| Actors | 1 deterministic policy actor | 1 manager + 2 specialist policy actors |
| Tools | `analyze_logs` then `analyze_impact` | same two functions, run in two Python threads |
| Input/evaluator | identical fixtures + expected labels | identical |
| Final synthesis | same merge function | same merge function |
| State | per-run ephemeral, no persistence | immutable shared inputs, manager single writer |
| Termination | 10ms budget checked between stages | 10ms budget; cooperative future cancellation; worker shutdown may overrun |
| Model | NONE | NONE |
| Side effects | read-only local work | read-only local work |

Fresh worker thread pools are created for every multi-actor invocation, so timing measures **this cold-start configuration only**. No artificial tool delay in nominal runs; a 25ms delay exists only in explicitly injected faults.

## Reproduce locally

Requires Python **3.10+** and standard library only; no API keys, Docker, CI, network or paid infrastructure.

```bash
cd agent-engineering/experiments/rec-012
python -m unittest -v
python benchmark.py --trials 30 --timeout-ms 10 --output results.json
```

`results.json` is the preserved, locally executed receipt. Timings will change by host/scheduler load; this benchmark cannot be used for generalized latency rankings.

## Actual run (2026-10-12)

- **16 cases × 30 trials × 2 topologies = 960 executions**.
- Correct outcomes: **480/480 per topology** for these predetermined labels.
- Median wall-time: **0.005468ms single / 0.148609ms multi** in preserved second run.
- Tool calls: **960 per topology**. Explicit multi handoffs: **960**.
- Six `unittest` methods passed locally (includes parity, schema, type guards, timeout and fault paths).
- Six distinct fault modes tested in both topologies: tool exceptions, malformed outputs and stalls. All report failure rather than a successful result.
- Injected stall overruns 10ms budget because threads cannot be force-stopped: **hard cancellation is not proven**.
- Tokens, model inference cost, model calls, stochastic model quality, real-world critical path and true multi-LLM routing are **NOT_APPLICABLE / NOT_TESTED**, not zeros that demonstrate efficiency.

## Evidence custody

- [Measured results](./results.json)
- [Executable benchmark](./benchmark.py)
- [Hand-labelled fixtures](./fixtures.json)
- [Automated tests](./test_benchmark.py)
- [Research receipt and hashes](../../quarries/rec-012-offline-topology-baseline.md)

## Real-model preflight (2026-10-12)

[Hardware/network feasibility receipt](./LLM_FEASIBILITY_2026-10-12.md) + [machine-readable snapshot](./preflight-2026-10-12.json): the ChatGPT execution container has CPU and RAM, but **no model weights, no inference runner and no working model download route**. The **real-model** comparison remains **NOT RUN / BLOCKED_ENVIRONMENT**. This does not invalidate the deterministic fixture or pass G7.

## Gate

**REC-012 remains OPEN_MK1 / PARTIAL EVIDENCE.** A deterministic actor-topology stress test exercises coordination and termination, **not** model-driven agent autonomy. A real model-based same-task single-vs-manager+specialists comparison is still needed to satisfy the representative gate. No MK1 freeze, MK2 activation or production certification follows from these results.
