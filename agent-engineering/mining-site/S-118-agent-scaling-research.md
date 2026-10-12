# S-118 — Controlled single-agent vs multi-agent scaling evidence

Status: **SOURCE RECEIPT / EXTERNAL EXECUTION EVIDENCE / QUALIFIED**  
Observed: **2026-10-12**  
Source is **primary for authors' study**, not independent validation or a deployment certificate.

## Identity, version, and custody

| Field | Pinned observation |
|---|---|
| ID | `S-118` |
| Study | *Capable language models can outgrow the benefits of collaboration* (Nature Machine Intelligence, 2026), DOI `10.1038/s42256-026-01268-y` |
| Manuscript available | [arXiv 2512.08296v3 — 2026-04-08](https://arxiv.org/html/2512.08296v3), titled *Towards a Science of Scaling Agent Systems* |
| Institution explanation | [MIT Media Lab](https://www.media.mit.edu/projects/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/overview/) — reflects the later 260-configuration study |
| Research code | [ybkim95/agent-scaling](https://github.com/ybkim95/agent-scaling), MIT license |
| Pinned analysis release | [`v2.2.2`](https://github.com/ybkim95/agent-scaling/tree/072276fd3ae71cf095587f1232e8eefc17a21898) → Git commit `072276fd3ae71cf095587f1232e8eefc17a21898` |
| Data receipt | [`data/Source_Data_Fig1_Fig2.csv`](https://github.com/ybkim95/agent-scaling/blob/072276fd3ae71cf095587f1232e8eefc17a21898/data/Source_Data_Fig1_Fig2.csv), Git blob `18607b8802ee02cf540329f996b7b3e8d47a4298` |
| Data checked | **260 data rows**, six benchmarks, five topologies, three model families (nine model identifiers overall; eight for two newer benchmarks) |
| Capture scope | arXiv full text HTML, MIT authors' summary, GitHub pinned README, CHANGELOG, REPRODUCTION, dataset provenance, single and centralized YAML configs, published CSV |
| Direct execution | **NONE by this project**; no provider API calls, no full paper rerun |
| Independent check | Recomputed simple per-dataset/architecture arithmetic means from the 260 deposited CSV rows through the GitHub connector; not a rerun of authors' traces, hypothesis tests, regression or judge evaluations |
| Confidence | High: stated version/code/data presence and checked row counts/means. Qualified: underlying model-run outcomes, judge validity, cross-domain transfer and reported significance |
| Canon | **REC-012 evidence input only**; not a universal multiagent design law |

## Version reconciliation — material

Do not combine incompatible numbers from revisions:

- `arXiv v1` and the [January 2026 Google Research article](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/) discuss **180 configurations / 4 benchmarks**.
- `arXiv v3` (2026-04-08), the authors' MIT synopsis and Nature-linked published work cover **260 configurations / 6 benchmarks**.
- The public repository's [CHANGELOG at pinned release](https://github.com/ybkim95/agent-scaling/blob/072276fd3ae71cf095587f1232e8eefc17a21898/CHANGELOG.md) records that `v2.1.3` analysis scripts sometimes included ten out-of-sample Gemini-3 preview configurations (**270**, rather than the paper's **260**) and did **not** reproduce some published regression values; the `v2.2.0–v2.2.2` line corrects the default analysis population and adds published-analysis scripts.
- [Pinned README](https://github.com/ybkim95/agent-scaling/blob/072276fd3ae71cf095587f1232e8eefc17a21898/README.md) recommends `v2.2.2` for corrected analysis, while [REPRODUCTION.md](https://github.com/ybkim95/agent-scaling/blob/072276fd3ae71cf095587f1232e8eefc17a21898/REPRODUCTION.md) still says `v2.1.3` when describing the originally manuscript-cited release. **This is a real document inconsistency**, not our verified successful rerun.

## Published evidence and boundaries

The revised authors' study describes five architectures (single, independent, centralized, decentralized, hybrid), standardized prompts/tools/compute ceilings, three model families and six benchmarks: BrowseComp-Plus, Finance-Agent, PlanCraft, Workbench, SWE-bench Verified and Terminal-Bench. The last two use 20-instance subsets and have wide per-cell uncertainty.

The authors report, *within these test configurations*:
- Finance-Agent single-agent mean **34.9%** vs centralized **63.1%** (relative **+80.8%**), and substantial decline across multiagent PlanCraft alternatives;
- response/coordination trace analysis, turn growth, extra token overhead, tool access parity and a coordination-failure taxonomy;
- capability saturation near **45%** baseline as an *empirical fitted threshold*, **not** a production rule;
- within-domain held-out architecture-choice agreement of **87%**, **not** reliable unseen-domain prediction;
- some tool-coordination relationships lost statistical support with benchmark-clustered inference; not a universal law.

**Data provenance of independent arithmetic check:** the repository CSV has columns `dataset,architecture,family,model,performance`; grouping all model rows for each (dataset, architecture) reproduced Finance mean single `0.34889` and centralized `0.63111`, PlanCraft single `0.56782` and centralized `0.28173`. This is evidence that deposited aggregate *quality* data align with cited headline numbers, not evidence that provider traces, costs, latency, errors or regression analyses reproduced independently.

## Inspection limitations

- The deposited summary CSV provides **performance**, not per-run latency, actual model tokens, raw failure histories or hard-cancellation proofs.
- Manuscript/code expose budgets, architecture configuration, error taxonomy and qualitative cost/latency patterns; **per-cell latency validation NOT REPRODUCED**.
- Some benchmark evaluation uses LLM-as-judge, others structural/outcome labels; do not claim uniformly independent judges.
- Full rerun requires third-party model keys/paid inference, datasets, environment setup, and sometimes Docker/search credentials; not authorized or executed here.
- Source is not permission to install multiagent frameworks, copy raw code/data into our repo, alter any product topology or freeze MK1 schema.

## Routing

- [Processed quarry](../quarries/multiagent-external-scaling-evidence.md)
- [Normalized REC-012](../mk/MK1/records/REC-012-external-agent-scaling.md)
- [Complementary S-119 latency/token contrast](./S-119-mars-rover-agent-benchmark.md) — separate study, no data pooling.
- [Evidence gate](../mk/MK1/MULTI_AGENT_BASELINE_SPEC.md)
