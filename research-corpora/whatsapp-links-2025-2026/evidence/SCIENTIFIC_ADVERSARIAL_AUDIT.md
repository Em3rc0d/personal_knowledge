# Scientific Adversarial Audit

**Date:** 2026-09-06  
**Purpose:** attempt to falsify the promoted B11 claims using peer-reviewed counterevidence before conformity.

## Evidence policy

- `PEER_REVIEWED_EMPIRICAL` supports empirical claims.
- `STANDARD_NORMATIVE` supports conformity/contracts, not empirical truth.
- `OFFICIAL_IMPLEMENTATION` supports concrete implementation behavior, not universal science.
- Preprints may triangulate hypotheses but do not alone certify them.

## Six material repairs

### K-006 — Benchmark comparability

**Counterevidence:**
- Northcutt, Athalye & Mueller (NeurIPS Datasets & Benchmarks 2021) show pervasive label errors can destabilize benchmark rankings.
- D’Amour et al. (JMLR 2022) show underspecified models with similar held-out performance can behave differently under deployment-relevant conditions.

**Repair:** benchmark metadata/reproducibility are necessary but insufficient. Deployment decisions also require evidence about benchmark validity, representativeness, metric quality and relevant stress/generalization behavior.

**Final:** `REUSABLE_PATTERN B`.

### K-007 — Agent architecture

**Counterevidence:**
- Xia et al., *Demystifying LLM-based Software Engineering Agents* (ACM FSE 2025, DOI 10.1145/3715754), show that a simpler structured non-autonomous pipeline can outperform more complex autonomous agents on the studied SWE-bench Lite setting.

**Repair:** begin with the minimum capability architecture justified by the workload. Add memory, planning, autonomy, tools or multi-agent coordination only when evaluation demonstrates sufficient value for their additional cost/complexity/failure surface.

**Final:** `REUSABLE_RULE B`.

### K-010 — Context engineering

**Conflicting peer-reviewed evidence:**
- Shi et al. (ICML 2023): irrelevant context can materially hurt reasoning.
- Cuconasu et al. (SIGIR 2024, DOI 10.1145/3626772.3657834): in their RAG experiments, some random/noisy documents improved performance while high-scoring non-answer passages could hurt.
- Li et al. (EMNLP Industry 2024, DOI 10.18653/v1/2024.emnlp-industry.66): when sufficient compute was available, long-context processing outperformed RAG on average in the studied setups, while RAG retained cost advantages.

**Repair:** no universal `less context`, `more context` or `highest retriever similarity` rule survives. Context policy is an empirical system parameter and must be evaluated for model + task + retrieval policy + cost/latency constraints.

**Final:** `REUSABLE_PATTERN B`.

### K-016 — AI/Agent Bill of Materials

**Counterevidence:**
- Nocera et al. (Journal of Systems and Software 2025, DOI 10.1016/j.jss.2025.112540) report incomplete/non-conformant SBOMs and missing recommended information in studied OSS projects.
- Bifolco et al. (EASE 2024, DOI 10.1145/3661167.3661175) report inaccuracies in GitHub dependency-graph data, relevant to dependency/SBOM tooling.

**Repair:** standards such as SPDX/CycloneDX provide interoperability, not truth. Certification separates schema conformance from inventory completeness/accuracy/provenance verification.

**Final:** `REUSABLE_RULE A/B`.

### K-022 — Microdata + aggregate evidence

**Counterevidence:**
- Riley & Steyerberg (Research Synthesis Methods 2010, DOI 10.1002/jrsm.4) explicitly model joint synthesis of individual participant data and aggregate data while accounting for different evidence levels and ecological-bias/confounding concerns.

**Repair:** prohibit naïve pooling, not heterogeneous synthesis. Harmonize when defensible; otherwise use explicit hierarchical/meta-analytic evidence-synthesis models; do not combine when assumptions or provenance cannot be defended.

**Final:** `REUSABLE_RULE B`.

### K-025 — Local-first / WebAssembly

**Counterevidence:**
- Jangda et al. (USENIX ATC 2019) report material WebAssembly-vs-native performance overhead in their browser/SPEC experiments.
- Narayan et al. (USENIX Security 2021), *Swivel*, demonstrate Spectre-style attacks can bypass WebAssembly isolation assumptions without hardening.

**Repair:** local/WASM is not evidence of privacy, security, near-native performance or universal portability. Every proposal needs independent workload benchmarking and threat-model/security review.

**Final:** `REUSABLE_PATTERN C`.

## Rejected stronger claims

1. `reproducible benchmark ⇒ valid deployment evidence` — rejected.
2. `more agentic capabilities ⇒ better agent` — rejected.
3. `less/more relevant context ⇒ universally better` — rejected.
4. `standard-compliant BOM ⇒ trustworthy inventory` — rejected.
5. `non-harmonizable micro/aggregate data must always remain separate` — rejected.
6. `local/WASM ⇒ near-native performance/privacy/strong isolation` — rejected.

## Gate result

Scientific adversarial pass: **PASS AFTER REPAIR**.

The repaired wording is canonical in `../mk/MK2/FINAL_KNOWLEDGE.md`. This file preserves the falsification history; it is not itself the canonical rule catalog.
