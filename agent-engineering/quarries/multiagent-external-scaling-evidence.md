# REC-012 — Real-model external controlled comparison (revised 2026 study)

**Evidence:** `S-118` primary paper + released code/data; source-reported real LLM runs; summary CSV independently re-aggregated; **no local LLM rerun**.  
**Scope:** multi-agent *admission evidence* for MK1 only; not an operational benchmark certificate or universal ranking.  
**Date/versions:** 2026-10-12 observation; paper [arXiv v3](https://arxiv.org/html/2512.08296v3); code [`v2.2.2@072276fd`](https://github.com/ybkim95/agent-scaling/tree/072276fd3ae71cf095587f1232e8eefc17a21898). Source receipt: [S-118](../mining-site/S-118-agent-scaling-research.md).

## Question and admission hypotheses

**Question:** Does an independently measured real-LLM multi-agent design justify its overhead relative to the *same-model, same-task, same-tool* single-agent baseline?

Hypothesis families: decomposition/parallelism and independent verification could help; sequential-dependency and information-transfer costs could hurt. Do not assume any architecture is superior without its task-specific outcome and resource budget.

## Observed experiment contract (authors, primary paper)

| Axis | Evidence |
|---|---|
| Baseline | Single LLM agent with tools; unified interaction stream |
| Alternatives | Independent parallel (3 agents), centralized manager + 3 workers, decentralized peer debate, hybrid |
| Control | Model-directed bounded tool interactions; different orchestrator/handoff semantics |
| Model comparability | Three provider/model families; matched model within comparable benchmark/configuration cells; no inference performed by us |
| Tasks | Six tested benchmarks (Finance Agent, PlanCraft, BrowseComp-Plus, Workbench, SWE-bench Verified, Terminal-Bench) |
| Equality pressure | Authors report matched per-system compute ceilings and tools/prompts; **architecture-specific prompts/coordination necessarily differ** |
| Success | Benchmark-specific ground truth, environment outcomes and in some cases model judges |
| Cost | Token-overhead/coordination metrics; model-dependent dollar cost estimates from article (not independently validated) |
| Latency | Article discusses latency/turn/communication cost; **numeric per-topology wall-clock distribution NOT independently available in checked summary CSV** |
| Failures | Logical contradiction, numerical drift, context omission and coordination failure (author-reported trace taxonomy) |
| Termination | Iteration/round limits and explicit coordinator vs worker timeouts in pinned YAML; hard cancellation, idempotency, external effects **NOT ESTABLISHED** |
| Repetition | Many task instances/model cells; independent stochastic rerun by us **NOT RUN** |
| Code/data | Main results, scripts, configs, and source CSV exist in pinned release; original cited release has documented script-population drift |

## Independently re-aggregated results from released CSV

The checked release's `data/Source_Data_Fig1_Fig2.csv` contains **260 rows**, each with a dataset, architecture, family, model and performance. Simple arithmetic means computed from these rows:

| Dataset | Single-agent | Centralized | Independent | Decentralized | Hybrid | Models per architecture |
|---|---:|---:|---:|---:|---:|---:|
| Finance Agent | 0.34889 | 0.63111 | 0.54667 | 0.60889 | 0.60444 | 9 |
| PlanCraft | 0.56782 | 0.28173 | 0.17028 | 0.33275 | 0.34614 | 9 |
| BrowseComp-Plus | 0.31767 | 0.31836 | 0.20604 | 0.34678 | 0.33572 | 9 |
| Workbench | 0.62889 | 0.62111 | 0.55667 | 0.66444 | 0.62111 | 9 |
| SWE-bench Verified | 0.48750 | 0.47500 | 0.42500 | 0.45625 | 0.48125 | 8 |
| Terminal-Bench | 0.31250 | 0.25000 | 0.33125 | 0.29375 | 0.27500 | 8 |

**Computation method:** group `performance` by exact `dataset,architecture` and compute arithmetic mean over available models, with no weighting by dataset sample sizes and no additional statistical significance inference. Results are author-deposited *already measured scores*; this check confirms arithmetic aggregation, **not** original model execution.

**Consequence:** evidence points in opposite directions depending on task; do not collapse to a single best topology.

## Trace-level cost/failure signals — reported, not locally reconstructed

The manuscript reports approximate inter-agent overhead `+58%` independent, `+285%` centralized, `+263%` decentralized and `+515%` hybrid relative to single-agent under the paper's own definition. Its trace-level error amplification metric is reported as **17.2 for independent**, **4.4 for centralized**; these are *not* probabilities of an incorrect user result. Its discussion states latency/token cost grows with more agents, but the inspected per-configuration public CSV lacks per-run wall-time, so **our latency comparison remains DIRECTIONAL / NOT INDEPENDENTLY MEASURED**.

The paper discusses `~45%` single-agent capability saturation and `87%` within-domain architecture selection. The MIT authors' page explicitly warns that the threshold is empirical, that some tool-heavy interactions lose clustered statistical significance, and that leave-one-domain-out absolute prediction is poor. These are **bounded observations**, not portable constants or product deployment limits.

## Termination, trust, and evidence separation

- Code `run_conf/agent/multi-agent-centralized.yaml`: `max_rounds:10`, `max_execution_time:600`, `worker_timeout:300` at pinned v2.2.2. **Config-present ≠ independently tested effective enforcement**, and a worker timeout does not prove remotely dispatched effects stopped.
- The source spans three model families, but no per-task production sandbox, full authorization-boundary proof or idempotent mutation path was validated by us.
- Our [local rule-based fixture](../experiments/rec-012/README.md) measures **different** dynamics (Python worker startup, synthetic log tools); never join its 960 runs to external model outcomes or pool their latency ratios.

## Decision for MK1

This is a **real-model, empirical, source-reported multi-agent-vs-single comparison with a public 260-row outcome dataset**, sufficient to classify architecture topology separately from observed benefit in a **QUALIFIED** MK1 record without any local model install. It also exposes meaningful limits and failures, but does **not** independently certify latency, reliability, paper rerun, future model families or real-product advantage.

**Candidate G7 resolution:** `PASS / QUALIFIED_UPSTREAM` under the original MK1 admission spec, provided final registry/gate crosscheck accepts source-reported execution and explicitly records unverified latency. **This is not the full C5/C6 freeze audit.**

Exact next work: final representative/COVERED_BY review, UNKNOWN routing, PA-01 comparison-contract disposition, cross-dimension schema audit. No software adoption.
