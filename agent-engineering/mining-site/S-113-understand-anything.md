# S-113 — Egonex-AI / Understand-Anything

Status: **SOURCE RECEIPT — NON-CANONICAL**

## Identity

| Field | Value |
|---|---|
| ID | `S-113` |
| Type | public GitHub repository / code-intelligence + knowledge-graph system |
| Repository | https://github.com/Egonex-AI/Understand-Anything |
| Pinned snapshot | `6df3065f1d8ddc2ce3615314d1d493f36d6b1c80` |
| Snapshot observed | 2026-09-25 |
| Upstream commit date | 2026-09-12 |
| License | MIT |
| Primary implementation | TypeScript + Node.js, Python helper scripts, React dashboard |
| Authority | primary for behavior implemented in this repository; README/spec prose is source-owned design/claim and may drift from code |
| Use here | pressure-test agentic codebase understanding, deterministic/LLM boundaries, incremental verification, semantic batching and knowledge-artifact freshness |

## Why collected

The repository is useful because it treats codebase understanding as a durable engineering artifact rather than a one-shot chat response.

Its current design combines:

1. deterministic structural extraction;
2. bounded semantic analysis by specialized agents;
3. a typed knowledge-graph interchange format;
4. incremental refresh tied to Git state;
5. explicit freshness/staleness semantics;
6. downstream explain/onboard/diff/chat views derived from the persisted graph;
7. validation and fail-before-publication behavior for ambiguous incremental symbol loss.

This makes it relevant to both `agent-engineering` and Jett Engineering Method without implying that its implementation should be copied wholesale.

## High-value upstream evidence inspected

Current implementation / contracts:

- `README.md`
- `understand-anything-plugin/skills/understand/SKILL.md`
- `understand-anything-plugin/skills/understand-diff/SKILL.md`
- `understand-anything-plugin/skills/understand-explain/SKILL.md`
- `understand-anything-plugin/skills/understand-onboard/SKILL.md`
- `understand-anything-plugin/skills/understand-knowledge/SKILL.md`
- `understand-anything-plugin/packages/core/src/schema.ts`
- `understand-anything-plugin/packages/core/src/change-classifier.ts`
- `understand-anything-plugin/packages/core/src/fingerprint.ts`
- `understand-anything-plugin/packages/core/src/staleness.ts`
- `understand-anything-plugin/packages/core/src/analyzer/graph-builder.ts`
- `understand-anything-plugin/skills/understand/compute-batches.mjs`
- `understand-anything-plugin/skills/understand/prepare-incremental.mjs`

Design / audit evidence:

- `docs/superpowers/specs/2026-03-14-understand-anything-design.md`
- `docs/superpowers/specs/2026-04-01-business-domain-knowledge-design.md`
- `docs/superpowers/specs/2026-05-24-semantic-batching-and-output-chunking-design.md`
- `docs/incremental/source-evidence-audit.md`
- `docs/benchmarks/large-monorepo.md`

Repository tests were also inspected through the repository tree to confirm dedicated coverage exists for batching, incremental preparation, symbol preservation, graph freshness, merge behavior, schema validation and dashboard freshness.

## Observed architecture

### Deterministic substrate

Tree-sitter-backed parsers and deterministic scripts are used for structural facts such as files, declarations, imports, call-like relationships where supported, fingerprints and scan inventories.

The current code explicitly distinguishes structural fingerprint support from unsupported languages. When structural coverage is unavailable, a content change is treated conservatively rather than silently classified as cosmetic.

### Semantic layer

LLM agents add information that static analysis cannot reliably determine from syntax alone: summaries, tags, architectural interpretation, business-domain mapping, guided learning material and implicit knowledge relationships.

The source deliberately separates these roles instead of asking the LLM to rediscover every import/declaration from raw source.

### Semantic batching

`compute-batches.mjs` builds an import graph and uses Louvain community detection to group related files. It preserves one-hop cross-batch neighbors and exported symbols as context. If Louvain fails, it falls back to deterministic count-based batching and emits a warning.

This converts batching from an arbitrary token-management mechanism into a topology-aware orchestration decision.

### Typed graph contract

The graph schema distinguishes code, infrastructure, domain, knowledge and design node families and a typed edge vocabulary. Validation is multi-stage: sanitize → normalize aliases → auto-fix bounded defects → validate/drop malformed elements → fail on unrecoverable top-level/project errors.

### Incremental model

A prior analyzed Git commit plus per-file fingerprints form the baseline.

Change classification distinguishes:
- no structural change / cosmetic;
- localized structural change;
- architecture-level change;
- full rebuild threshold.

Incremental preparation rescans inventory, refreshes relevant import context, prunes replaced graph slices, and emits a bounded plan rather than letting an agent decide ad hoc what to recompute.

### Symbol-loss publication gate

Incremental merge does not treat analyzer omission as proof of deletion.

The source's audit explicitly records the invariant:

> evidence is not completeness.

Current behavior uses scoped source evidence and blocks publication when a previously known symbol cannot be proven deleted. A targeted retry is bounded; unresolved repair stops before advancing durable graph/fingerprint/meta artifacts.

### Freshness model

Persisted graph metadata carries the analyzed Git commit. Freshness evaluation is project-scoped and explicitly distinguishes `fresh`, `stale` and `unknown`.

A hash mismatch alone is not necessarily project drift in a monorepo; the source checks project-scoped diffs.

### Multiple derived views, one substrate

The same graph supports:
- interactive structural exploration;
- explanation of a file/function;
- impact analysis of current diffs;
- onboarding generation;
- guided tours;
- natural-language querying;
- optional business-domain and wiki knowledge views.

This reduces repeated full-source ingestion for every downstream question.

## Important limitations / boundaries

- A graph is a model of the repository, not the repository itself.
- Static parser success is not proof of declaration completeness.
- Semantic edges produced by an LLM remain inference and require integrity checks.
- Historical design specs are useful intent evidence but current source/tests outrank them when they disagree.
- Thresholds such as batch sizes or rebuild cutoffs are implementation choices, not universal laws.
- The dashboard is a delivery surface; the reusable engineering value is primarily in the evidence model, freshness contract and orchestration boundaries.
- Large-repo benchmark documentation explicitly separates deterministic-stage performance evidence from end-to-end LLM/token/cost claims.

## Candidate reusable lessons

These are `INSPIRED` / `INFERRED` until independently normalized:

1. Build deterministic evidence first; ask models to add semantics, not reconstruct facts already available mechanically.
2. Persist understanding as a versioned artifact with source revision identity.
3. Treat freshness as a first-class state, including `UNKNOWN`.
4. Incremental understanding needs a publication gate, not only a cache.
5. Absence from a best-effort analyzer is not evidence of deletion.
6. Batch by dependency topology when semantic locality matters.
7. Preserve cross-batch context explicitly rather than assuming independent shards.
8. Separate structural, domain and knowledge views when combining them would overload one ontology.
9. Reuse one validated substrate for explain/onboard/diff/search instead of repeatedly rereading the entire codebase.
10. Benchmark deterministic and stochastic stages separately; do not infer end-to-end claims from a partial harness.

## Promotion boundary

This receipt establishes what was inspected at the pinned snapshot.

It does **not** establish:
- that Understand-Anything is the best code-intelligence architecture;
- that its thresholds generalize to our projects;
- that every language/parser has equal completeness;
- that its graph should become our repository's canonical representation;
- that an LLM-generated semantic graph is ground truth.

Processed synthesis:
- `../quarries/understand-anything-code-intelligence.md`
- `../../jett-engineering-method/quarries/understand-anything-codebase-intelligence.md`
