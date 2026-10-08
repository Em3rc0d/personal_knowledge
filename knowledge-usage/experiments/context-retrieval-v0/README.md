# Context Retrieval v0 — Offline Cost / Evidence Pilot

Status: **PILOT / MEASUREMENT ONLY — NOT CERTIFIED TOKEN SAVINGS**  
Date: 2026-10-08  
Owner: `knowledge-usage/` (transversal experiment, **not** a new domain or MK)  
Reference revision: `4e7b7dff5ffdb8eaa4a8232423a037b21d55f065`

## Why this exists

`personal_knowledge` is intended to reduce rediscovery, unnecessary reading, repeated reasoning and eventually token consumption. More Markdown or even a shorter context window does **not** independently prove cheaper agent operation.

Experiment question:

> For a fixed repository revision and the same information question, how much document payload can an **oracle-curated minimal evidence route** omit versus a **manually scoped broader exploratory read**, without losing the required evidence paths?

This is a **first structural experiment**, not a comparison of working search engines, paid API usage or generated-answer correctness.

## Scope

- Four real questions from `agent-engineering` and `knowledge-usage`.
- Broad and selective document lists pinned in [`cases.json`](./cases.json).
- Per-document Git blob hashes pin content independent of later changes to unrelated files.
- Selected lists conservatively include the relevant router/index when applicable.
- Fail closed on missing, changed, escaped or unsupported files, or on omitted required evidence/anchor text.
- Measure **UTF-8 bytes** and whitespace words with standard Python. Optionally measure **local tokenizer counts** only if the matching offline tokenizer is available.
- Zero model calls, zero remote CI, zero API fees or backend dependencies in the default path.

Not in scope: automatic routing/search, paragraph-level retrieval, actual model responses, tool-call wrappers, LLM input/output totals, caching, latency, human review effort and paid-token accounting.

## First source-pinned observation

[Static measurement receipt](./static-receipt-2026-10-08.json) was derived from the pinned GitHub tree's blob byte sizes, with the required evidence anchors checked against source file contents. This **did not execute the Python harness over a complete local checkout**.

| Case | Broad reading | Selective reading | Input bytes reduced |
|---|---:|---:|---:|
| Current MK1 blockers | 67,196 B (8 files) | 24,554 B (3 files) | **63.46%** |
| Collaborator source/evidence | 66,337 B (6 files) | 26,729 B (3 files) | **59.71%** |
| Strands and A2A 1.0 | 89,242 B (8 files) | 22,175 B (2 files) | **75.15%** |
| Portfolio compact re-entry | 34,918 B (8 files) | 4,321 B (2 files) | **87.63%** |

All four selected routes cover the **predeclared file/anchor presence checks** at the source snapshot. That gate is deliberately weak: an answer could still be wrong or omit an important counterclaim.

Interpretation: **these four hand-picked tasks have a smaller available source-text footprint** under curated reading. The percentages above are **not** model-token reductions, savings on invoices or measured gains in answer quality.

## Reproduce locally

With a checkout of `personal_knowledge` containing the pinned source blobs:

```bash
python -m unittest discover -s knowledge-usage/experiments/context-retrieval-v0 -p 'test_*.py' -v
python knowledge-usage/experiments/context-retrieval-v0/measure.py
```

To write an untracked JSON receipt:

```bash
python knowledge-usage/experiments/context-retrieval-v0/measure.py \
  --json-out /tmp/context-retrieval-result.json
```

**Optional** — only if a compatible `tiktoken` encoding is *already installed and available locally*:

```bash
python knowledge-usage/experiments/context-retrieval-v0/measure.py \
  --encoding o200k_base \
  --json-out /tmp/context-retrieval-tokenizer-result.json
```

The `--encoding` option requires the package and tokenizer vocabulary to be locally accessible. If unavailable, this explicit request **fails** rather than guessing token counts. Different models/providers may tokenize differently; even accurate local source-text token counts are **not provider-billed tokens**.

The harness detects changed pinned files and stops with `STALE_SOURCE`. If documents change, create a deliberate new manifest revision and comparison; do not rewrite historical receipts.

## Minimum-context operating hypothesis (candidate)

```text
user's intent
→ smallest existing domain router / index
→ current authoritative answer file
→ needed evidence slice / source receipt
→ expand only for contradiction, provenance, freshness or uncertainty
→ stop when claims are supported; keep UNKNOWN explicit
```

Anti-pattern: opening every source in a domain, carrying entire raw quarries or using a source registry as default answer context.

**Do not mistake** a shorter input for correct retrieval. Before leaving a required file unread, the agent must be able to justify why its claims still have adequate evidence.

## Gates

### Gate A — fixed document-footprint pilot

- [x] Existing routing infrastructure inventoried rather than rebuilt.
- [x] Four non-synthetic questions scoped to real repo evidence.
- [x] Pinned revision and blob hashes captured.
- [x] Selected routes are subsets of broad routes.
- [x] Required evidence paths and scoped anchor strings present.
- [x] Static input-byte comparisons recorded, including non-rounded source measurements.
- [x] Six offline fail-closed unit tests pass with synthetic files.
- [ ] Whole-repository local CLI run on a checkout of the pinned corpus.

**Status: PASS / QUALIFIED for static document footprint; complete corpus CLI rerun pending.**

### Gate B — actual tokenizer/context accounting

- [ ] Pin encoding appropriate to the actual chosen model.
- [ ] Count routed query, context assembly and tool-result overhead (not just Markdown).
- [ ] Measure total input/output/cache usage using provider usage metadata **only when already available**, or obtain explicit authorization before paid runs.
- [ ] Calculate cache-adjusted cost where pricing/usage data permit it.
- [ ] Record repeat-run distribution rather than a single cherry-picked run.

**Status: NOT EXECUTED. No monetary or billed-token saving is claimed.**

### Gate C — non-regression of evidence and answers

- [ ] Run both variants on a broader task set not used to curate routes.
- [ ] Compare factual coverage, citations, false claims, contradictions and explicit UNKNOWNs.
- [ ] Include hard questions that require deep source reopening; record false negatives.
- [ ] Blindly review quality against the same acceptance contract.
- [ ] Only recommend default selective routing when savings survive quality controls.

**Status: NOT EXECUTED. Evidence-anchor presence != answer-quality verification.**

## Decision

`KEEP EXPERIMENT` — the bounded, dependency-free technique appears promising enough to evaluate further, but **NO-GO** for any broad claim that `personal_knowledge` has already saved a quantified percentage of billed tokens.

Do not purchase embeddings, deploy a vector DB, change every domain router, or launch recurring paid workflows as a consequence of these four cases. Future knowledge-use receipts can cite this experiment once a **real consumption decision** occurs.
