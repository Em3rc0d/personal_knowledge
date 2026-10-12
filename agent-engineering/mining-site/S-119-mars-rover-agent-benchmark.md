# S-119 — Single vs prompt-orchestrated multi-LLM on synthetic rover decisions

**Status:** EXTERNAL COMPARATIVE STUDY / SOURCE-REPORTED EXECUTION / QUALIFIED  
**Observed:** 2026-10-12; no paid/local rerun by this repository.

## Source receipt

- Study: Dan Sanabria (2026), *OpenAI single-agent LLM architecture reduces computational overhead relative to multi-agent orchestration in a simulated mars rover decision-support benchmark*, **Frontiers in Robotics and AI**, 13:1877762 (published **2026-07-06**).
- Primary full text: https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1877762/full
- Exact DOI: `10.3389/frobt.2026.1877762`; secondary indexing https://pubmed.ncbi.nlm.nih.gov/42518364/
- Data archive stated by authors: https://doi.org/10.5281/zenodo.20563739 . Existence cited in article; **not downloaded/independently rerun**.
- Source authority: published article primary for **its reported experimental setup and numbers**, not for real Mars safety or external correctness.
- Scope: 100 synthetically labelled scenarios, 5 repeated runs per scenario and architecture, GPT-4o and GPT-5.5, single-agent vs *prompt-defined* specialists plus orchestrator, tool-less compact decision task.
- Version evidence: publication DOI and date, not dynamically reinterpreted using later model names. Model identifiers are those reported in paper.

## Source-reported outcome and resource evidence

| Model / architecture | Decision accuracy | Mean latency | Mean tokens |
|---|---:|---:|---:|
| GPT-4o single | 0.810 | 2.32 s | 458 |
| GPT-4o orchestrated | 0.734 | 11.83 s | 2,273 |
| GPT-5.5 single | 0.974 | 6.06 s | 548 |
| GPT-5.5 orchestrated | 0.934 | 35.59 s | 3,160 |

The study uses scenario-level paired comparisons and Holm corrections. **Most decision-quality differences were not significant after correction**, while latency/token differences were; no claim that orchestration always reduces decision accuracy. Hazard identification had weak F1 and different failure patterns; several extra hazards may be plausible, not intrinsically hallucinations. Labels are synthetic and **not independent operational ground truth**.

## Limits important to REC-012

- This benchmark uses **prompt-defined specialist model calls, without external tools or autonomous long-horizon action**. It is a **different regime** than the tool-using multi-agent 260-configuration [S-118](./S-118-agent-scaling-research.md).
- Architecture necessarily adds model calls; latency/token effects show the expected cost of the tested design, not a theorem that all multiagent implementations are slower.
- No independent check of raw run-level traces, external action outcomes, hard cancellation or deployment security by us.
- Use as **separate within-study quantitative latency/token contrast** complementing S-118's tool-using benchmark; never merge the two datasets or imply the same task/model was used across studies.

## Route

[Combined evidence quarry](../quarries/multiagent-external-scaling-evidence.md) → [REC-012](../mk/MK1/records/REC-012-external-agent-scaling.md).
