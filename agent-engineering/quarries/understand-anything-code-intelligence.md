# Understand Anything — Code Intelligence as an Agentic System

Status: **QUARRY — NON-CANONICAL**

Source receipt: [`S-113`](../mining-site/S-113-understand-anything.md)  
Pinned upstream: `Egonex-AI/Understand-Anything@6df3065f1d8ddc2ce3615314d1d493f36d6b1c80`

## Question

What does this repository teach us about building agentic systems that must understand a large software/knowledge environment without turning every run into an unbounded LLM crawl?

## Core finding

The strongest pattern is not “multi-agent code review.” It is a **hybrid evidence pipeline**:

```text
deterministic scan
      ↓
stable structural evidence
      ↓
topology-aware partitioning
      ↓
bounded semantic agents
      ↓
merge + schema/integrity checks
      ↓
versioned knowledge artifact
      ↓
derived tasks: explain / diff / onboard / search / learn
```

This is a useful pressure test for the agent-engineering distinction between:

- tool/runtime capability;
- model inference;
- durable state;
- verification;
- publication authority.

## 1. Deterministic facts should not consume model authority

The source pre-resolves imports and extracts syntax structure mechanically, then injects that evidence into file-analyzer prompts.

Candidate rule:

```text
mechanically knowable fact
        → deterministic extractor
semantic interpretation
        → model
```

Benefits:
- lower token duplication;
- reproducibility;
- fewer hallucinated structural edges;
- simpler downstream verification;
- clearer provenance of each graph field.

Anti-pattern:

```text
give raw repository to model
→ ask it to discover files/imports/symbols/architecture simultaneously
→ treat output as one undifferentiated truth layer
```

## 2. Agent specialization is valuable only when contracts are explicit

The upstream pipeline separates scanning, file analysis, architecture analysis, tours, graph review and domain analysis.

The reusable idea is not the number of agents. It is that each role has:
- bounded input;
- a declared artifact/output;
- a schema or merge contract;
- a known place in the pipeline;
- retry/failure behavior.

This aligns with the existing agent-engineering rule that multi-agent decomposition should be justified by boundaries and verification, not by role names.

## 3. Semantic batching is part of reasoning quality

The move from count-based batching to Louvain communities exposes an important agentic design principle:

```text
partition strategy
      affects
context coherence
      affects
semantic edge quality
```

Batching is therefore not merely a performance knob.

The source preserves:
- within-community locality;
- one-hop cross-batch neighbors;
- exported symbols;
- deterministic fallback behavior.

Candidate classification dimension for future use:

`context_partitioning = arbitrary | topology_aware | semantic | hierarchical`

Not promoted to MK1 schema yet.

## 4. Incremental agents need a source-of-truth reconciliation layer

The source does not trust an incremental analyzer to perfectly reproduce all prior symbols.

It keeps a baseline, checks the candidate against current source evidence and prevents publication when a missing symbol is ambiguous.

Important distinction:

```text
model omission        ≠ source deletion
parse success         ≠ complete evidence
valid JSON            ≠ semantically complete artifact
```

This is a strong reusable pattern for any agent that incrementally maintains durable knowledge, code indexes, documentation or inventories.

## 5. Retry budgets should be bounded and stateful

The symbol-loss path allows a targeted repair attempt, preserves diagnostics and stops publication if the repair still fails.

The deeper lesson is:

```text
retry
≠ repeat blindly

retry =
  new bounded evidence/context
  + explicit attempt budget
  + preserved failure state
  + no silent publication on exhaustion
```

This fits the existing agent-engineering termination/budget discipline.

## 6. Durable semantic artifacts need freshness semantics

The graph carries `gitCommitHash` and analysis time, and consumers such as diff/onboard/explain inspect freshness before trusting graph-derived context.

Candidate invariant:

> An agent-maintained knowledge artifact without a freshness relation to its source should be treated as potentially stale, not implicitly current.

Useful status shape:

```text
FRESH
STALE
UNKNOWN
```

`UNKNOWN` matters when Git metadata cannot be resolved; it must not collapse to fresh.

## 7. One substrate can support many agents/tools

Once the graph exists, multiple tasks query a reduced structured representation instead of re-ingesting the full project.

This suggests a pattern for agent platforms:

```text
expensive ingestion
      ↓
validated shared substrate
      ↓
many narrow read/query workflows
```

Potential applications in our ecosystem:
- project recovery before implementation;
- onboarding;
- impact analysis before changing code;
- reviewer context packs;
- architectural drift detection;
- targeted agent context generation.

## 8. Ontology scope must be controlled

The source expands from codebase nodes into domain, wiki-knowledge and design graph kinds, while keeping graph kind and alias behavior explicit.

Useful principle:

> Extending one schema is acceptable only while semantic collisions remain controlled and graph kind determines interpretation.

The source itself had to make aliases kind-sensitive (for example terms meaningful in design vs knowledge). This is evidence that a universal ontology accumulates collision risk.

## 9. Validation should distinguish repairable degradation from fatal corruption

The graph validation pipeline uses multiple severity levels rather than all-or-nothing parsing.

Reusable shape:

```text
sanitize
→ normalize aliases
→ bounded auto-fix
→ drop invalid local elements
→ fatal on broken global contract
```

This pattern is appropriate when partial output still has value, provided degraded state is observable and referential integrity is preserved.

## 10. Prompt-injection boundary in knowledge ingestion

The `understand-knowledge` skill explicitly treats article contents as untrusted data and instructs analysis agents not to obey embedded instructions.

This is directly relevant to agent systems that ingest:
- repositories;
- docs;
- tickets;
- emails;
- web pages;
- wikis.

The security boundary belongs at ingestion/orchestration, not only in a generic system prompt.

## Candidate additions to future agent-engineering normalization

Not promoted yet:

| Candidate dimension | Values / question |
|---|---|
| evidence substrate | raw-only / deterministic / hybrid |
| context partitioning | arbitrary / topology-aware / semantic / hierarchical |
| durable artifact freshness | absent / timestamp-only / revision-bound / verified-diff |
| incremental publication gate | none / best-effort / fail-closed |
| omission semantics | deletion / unknown / source-verified |
| retry discipline | unbounded / bounded-repeat / bounded-evidence-changing |
| graph/knowledge authority | advisory / derived / operational dependency |

## Non-transferable implementation details

Do not promote as general rules:
- Louvain specifically;
- 5 concurrent analyzers;
- exact file-count thresholds;
- 60-node / 120-edge chunk thresholds;
- JSON as the only persistence format;
- the exact node/edge taxonomy.

Those are local design choices.

## Current conclusion

`SUPPORTED AS A PATTERN SOURCE`.

The repository materially strengthens existing agent-engineering ideas around:
- bounded orchestration;
- deterministic vs stochastic responsibility;
- state/freshness;
- retry/termination;
- fail-closed publication;
- untrusted-context handling.

It does not currently justify an MK1 schema revision by itself.
