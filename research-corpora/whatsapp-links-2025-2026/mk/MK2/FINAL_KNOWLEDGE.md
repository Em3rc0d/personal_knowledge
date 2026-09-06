# MK2 — Operationalize

# WhatsApp Links Corpus — B11 v5 FINAL

**Date:** 2026-09-06  
**Scope:** 89 unique URLs + 1 attached image from the WhatsApp ZIP research corpus.  
**Status:** CROSS-CONSISTENCY CLOSED / READY FOR CONFORMITY.

## 1. Evidence model

`confidence` and `evidence_class` are independent.

### Confidence
- `A` — verified/high confidence inside the declared scope.
- `B` — strongly supported; material limits remain.
- `C` — supported pattern/case-dependent.
- `D` — hypothesis only.

### Evidence class
- `PEER_REVIEWED_EMPIRICAL`
- `STANDARD_NORMATIVE`
- `OFFICIAL_IMPLEMENTATION`
- `LEGAL_PLATFORM_TERMS`
- `DERIVED_POLICY`
- `MIXED`

A claim supported by an official specification is not called “scientific” unless it also has peer-reviewed empirical support.

## 2. Corpus accounting — corrected

The 89 source rows were re-parsed directly from the B11 disposition table.

### Access state — mutually exclusive, total 89
- `INACCESIBLE`: 32
- `DIRECTO_VERIFICADO`: 27
- `PARCIAL`: 10
- `INDEXADO_ORIGINAL`: 10
- `FUENTE_PRIMARIA_ALTERNATIVA`: 4
- `INDEXADO_REPOST`: 4
- `REDIRECT_NO_RESUELTO`: 1
- `DUPLICADO_CANONICO`: 1

**Total: 89**

### Knowledge disposition — total 89
- `GAP`: 37
- `DISCOVERY_ONLY`: 21
- `PRIMARY_REFERENCE`: 4
- `SECONDARY_REFERENCE`: 4
- `IMPLEMENTATION_CASE_STUDY`: 4
- `QUARRY`: 3
- `SENSITIVE_PROVENANCE`: 3
- `QUARRY_WITH_PROVENANCE_CHECK`: 2
- `PRIMARY_DATASET_REFERENCE`: 1
- `HISTORICAL_REFERENCE`: 1
- `VOLATILE_VENDOR_REFERENCE`: 1
- `VOLATILE_QUARRY`: 1
- `PATTERN_SOURCE`: 1
- `STALE_REFERENCE`: 1
- `QUARRY_CASE_STUDY`: 1
- `PRIMARY_PATTERN_SOURCE`: 1
- `DUPLICATE_CANONICAL`: 1
- `ECOSYSTEM_REFERENCE`: 1
- `VENDOR_CLAIM_REFERENCE`: 1

**Total: 89**

The previous manually typed summary omitted one single-count disposition; the source rows were not missing.

## 3. Cross-consistency repairs

### X-001 — Evidence class vs confidence
Repaired. Confidence no longer implies scientific evidence.

### X-002 — K-006 ↔ K-020
Hardware-aware model selection must inherit the benchmark-validity constraints of K-006. Estimates may screen candidates; deployment choice must use target-hardware measurements with workload validity.

### X-003 — K-007 ↔ K-009
Evaluation is a lifecycle/system requirement, not necessarily a runtime module. Agent capabilities follow minimality: add complexity only when evaluation demonstrates value.

### X-004 — K-010 ↔ K-011
Knowledge-as-code remains a curation pattern. It does not inherit the false universal claim that less context is always better. Retrieval/full-context/hybrid policies are evaluated per workload.

### X-005 — K-012 / K-013 / K-014
These are implementation/concurrency rules, not scientific laws.
- K-012 remains a framework/server-isolation rule.
- K-013 becomes a pattern: send only data needed across the boundary, without premature micro-optimization.
- K-014 becomes a pattern: parallelize only after dependency, failure, cancellation, rate and bounded-concurrency analysis.

### X-006 — K-015 ↔ K-016
The security inventory records **credential references/boundaries and privilege**, never secret values. Representation should map to SPDX/CycloneDX/compatible standards before proprietary extension.

### X-007 — K-017 ↔ K-018 ↔ K-025
`local`, `self-hosted`, `private`, `secure`, `offline`, and `WASM` are separate properties.
No one property is evidence of another. Local-first proposals require workload benchmark and threat model.

### X-008 — K-003 ↔ K-023
K-023 is explicitly a specialization of K-003:
popularity/curation lists are discovery surfaces, not claim authority.

### X-009 — K-005 ↔ K-026 ↔ K-027
K-026 and K-027 are specializations of temporal provenance:
expired jobs, screenshots, versions, quotas, prices and model availability are time-scoped evidence.

### X-010 — K-024 ↔ K-001
A crawl record stores observed URL, declared canonical where present, retrieval method, representation hash and timestamp. A canonical tag is evidence supplied by a publisher, not unquestionable identity truth.

## 4. Final promoted catalog

| ID | Final class | Confidence | Evidence class | Final claim |
|---|---|---:|---|---|
| K-001 | REUSABLE_RULE | A | DERIVED_POLICY + STANDARD_NORMATIVE | Promoted knowledge preserves source/provenance, verification date/version and evidence linkage. |
| K-002 | REUSABLE_RULE | A | STANDARD_NORMATIVE | Requirements should be uniquely identifiable, verifiable and traceable; quantitative NFRs must be measurable. |
| K-003 | REUSABLE_RULE | A | DERIVED_POLICY | Popularity, views or stars do not establish authority or truth. |
| K-004 | REUSABLE_RULE | A | LEGAL_PLATFORM_TERMS | Public GitHub visibility/platform permissions do not equal general open-source reuse rights; license/upstream/provenance remain a gate. |
| K-005 | REUSABLE_RULE | A | DERIVED_POLICY | Mutable service facts require `verified_at` and version/time scope. |
| K-006 | REUSABLE_PATTERN | B | PEER_REVIEWED_EMPIRICAL + STANDARD | Benchmark comparison requires reproducibility **and validity**: workload/version/system/conditions/metrics plus benchmark quality, representativeness and relevant stress/generalization evidence. |
| K-007 | REUSABLE_RULE | B | PEER_REVIEWED_EMPIRICAL | Start with the minimum capability architecture justified by the task; add agentic capabilities only when evaluation justifies complexity/cost/failure surface. |
| K-008 | REUSABLE_RULE | A | STANDARD_NORMATIVE | For protected remote MCP, follow the current specification’s authorization model, least privilege, issuer/audience validation and prohibition of unsafe token forwarding; version-scope the rule. |
| K-009 | REUSABLE_PATTERN | B | MIXED | Agent quality should use repeatable eval datasets/cases, traces and metrics in an eval-fix loop rather than demos alone. |
| K-010 | REUSABLE_PATTERN | B | PEER_REVIEWED_EMPIRICAL | Context policy is an empirical system parameter: compare selective retrieval, long-context, hybrid/progressive-disclosure strategies on the actual model/task/cost surface. |
| K-011 | REUSABLE_PATTERN | C | DERIVED_POLICY | Knowledge-as-code is a traceability structure: source → atomic claim → scope/rationale → examples/counterexamples → eval/test → version/certification. No superiority claim is certified. |
| K-012 | REUSABLE_RULE | A | OFFICIAL_IMPLEMENTATION | Request-scoped mutable server state must not be stored in shared module state when it can leak/race across requests. |
| K-013 | REUSABLE_PATTERN | B | OFFICIAL_IMPLEMENTATION | Across Server→Client serialization boundaries, pass the data required by the client contract; avoid unnecessary exposure/serialization while preserving a coherent API. |
| K-014 | REUSABLE_PATTERN | B | LANGUAGE_SEMANTICS + DERIVED_POLICY | Concurrent async execution is appropriate only after checking dependency/order, failure semantics, cancellation, rate/resource limits and bounded concurrency. |
| K-015 | REUSABLE_PATTERN | B | MIXED | Agent/workflow security review inventories agents, models, tools/MCP, privilege, credential **references/boundaries**, webhooks and egress—not credential secret values. |
| K-016 | REUSABLE_RULE | A/B | STANDARD_NORMATIVE + PEER_REVIEWED_EMPIRICAL | Use interoperable BOM standards as the schema base; separately verify inventory completeness/accuracy/provenance. Schema conformance is not content truth. |
| K-017 | REUSABLE_PATTERN | B | DERIVED_ARCHITECTURE | Analyze local-first/private claims by separating compute location, state location, egress, offline behavior, secret handling and backups. |
| K-018 | REUSABLE_RULE | B | SECURITY_ENGINEERING | Self-hosting does not itself prove privacy, security or zero cost; it shifts operational/security responsibilities to the operator/stack. |
| K-019 | REUSABLE_PATTERN | B | OFFICIAL_IMPLEMENTATION | Protocol/API compatibility can reduce provider coupling but does not prove semantic, quality or feature equivalence. |
| K-020 | REUSABLE_PATTERN | B | MIXED | Local-model placement is hardware/workload-aware; heuristics screen candidates, target-hardware benchmarks decide. Inherits K-006. |
| K-021 | REUSABLE_PATTERN | B | DERIVED_POLICY | Evaluate mature OSS using README + releases/changelog + advisories + failure/issue history where available, weighting authoritative/current artifacts over arbitrary issues. |
| K-022 | REUSABLE_RULE | B | PEER_REVIEWED_EMPIRICAL | Naïve pooling of microdata and aggregates is prohibited; harmonize when defensible or use explicit hierarchical/meta-analytic evidence-synthesis models; do not combine when assumptions/provenance are indefensible. |
| K-023 | REUSABLE_RULE | A | DERIVED_POLICY | Awesome-lists/toolkits/galleries are quarries/discovery surfaces; individual claims require upstream verification. |
| K-024 | REUSABLE_PATTERN | B | RESEARCH_METHOD | Research retrieval records observed URL, declared canonical, method/render mode, timestamp and representation hash; provider-specific usage signals are conditional metadata. |
| K-025 | REUSABLE_PATTERN | C | PEER_REVIEWED_EMPIRICAL + OFFICIAL_IMPLEMENTATION | Local-first/WASM is a context-dependent architecture option; validate performance/resource fit and security/isolation independently with benchmark + threat model. |
| K-026 | REUSABLE_RULE | A | DERIVED_POLICY | Expired job postings are historical evidence, not current company/market requirements. |
| K-027 | REUSABLE_RULE | A | DERIVED_POLICY | Versioned posts/screenshots are historical snapshots; current knowledge must be revalidated against current primary sources. |

## 5. Hypotheses kept outside canon

- `H-001`: knowledge-as-code reduces drift vs monolithic prompts — **UNPROVEN**.
- `H-002`: separate tool registry vs knowledge/skill registry reduces capability-assumption failures — **UNPROVEN**.
- `H-004`: local-first/WASM capability cores reduce backend dependence — **CASE-DEPENDENT / UNPROVEN AS GENERAL CLAIM**.
- `H-010B`: smaller composable skills reduce long-term drift/coupling — **UNPROVEN**.
- `H-003`: need to invent a proprietary AI-BOM — **SUPERSEDED/REJECTED** by standards-first mapping.

## 6. Cross-consistency verdict

No material contradiction remains among K-001..K-027 after the repairs above.

Open hypotheses are not promoted knowledge and therefore do not block conformity.

`GAP` does not mean false; it means insufficiently verified.  
`INACCESSIBLE` remains inaccessible.  
No inaccessible URL is represented as directly studied.

## 7. Scientific / normative anchors

- Northcutt, Athalye & Mueller (NeurIPS Datasets & Benchmarks 2021), *Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks*.
- D’Amour et al. (JMLR 2022), *Underspecification Presents Challenges for Credibility in Modern Machine Learning*.
- Xia et al. (ACM FSE 2025), *Demystifying LLM-based Software Engineering Agents*, DOI 10.1145/3715754.
- Shi et al. (ICML 2023), *Large Language Models Can Be Easily Distracted by Irrelevant Context*.
- Cuconasu et al. (SIGIR 2024), *The Power of Noise: Redefining Retrieval for RAG Systems*, DOI 10.1145/3626772.3657834.
- Li et al. (EMNLP Industry 2024), *Retrieval Augmented Generation or Long-Context LLMs?*, DOI 10.18653/v1/2024.emnlp-industry.66.
- Nocera et al. (Journal of Systems and Software 2025), SBOM adoption/completeness study, DOI 10.1016/j.jss.2025.112540.
- Bifolco et al. (EASE 2024), *On the Accuracy of GitHub's Dependency Graph*, DOI 10.1145/3661167.3661175.
- Riley & Steyerberg (Research Synthesis Methods 2010), mixed IPD/aggregate meta-analysis, DOI 10.1002/jrsm.4.
- Jangda et al. (USENIX ATC 2019), *Not So Fast: Analyzing the Performance of WebAssembly vs. Native Code*.
- Narayan et al. (USENIX Security 2021), *Swivel: Hardening WebAssembly against Spectre*.
- ISO/IEC/IEEE 29148:2018 — current published requirements-engineering standard as of 2026-09-06; Edition 3 remains DIS under development.
- Model Context Protocol specification 2026-07-28.
- SPDX 3.0.1 AI/Dataset profiles.
- CycloneDX AI/ML-BOM / current specification family.

## 8. Promotion gate

This v5 supersedes the wording of K-006, K-007, K-010, K-016, K-022 and K-025 from v3/v4, and refines K-011, K-013, K-014, K-015, K-018, K-020, K-021 and K-024.

**Result: PASS FOR CONFORMITY ACT.**
