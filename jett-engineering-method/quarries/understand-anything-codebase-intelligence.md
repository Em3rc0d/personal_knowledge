# Understand Anything — Codebase Understanding as Evidence Engineering

Status: **QUARRY — NON-CANONICAL**

Upstream: https://github.com/Egonex-AI/Understand-Anything  
Pinned snapshot: `6df3065f1d8ddc2ce3615314d1d493f36d6b1c80`  
Observed: 2026-09-25  
License: MIT  
Detailed source receipt: `../../agent-engineering/mining-site/S-113-understand-anything.md`

## Why this matters to JEM

Understand-Anything is relevant to JEM less as a product and more as an example of turning “I think I understand the codebase” into a **revision-bound, inspectable, refreshable artifact**.

That directly pressures the JEM phases:

```text
RECOVER
  ↓
evidence inventory
  ↓
structured model
  ↓
reasoning / explanation
  ↓
freshness + validation
  ↓
PROVE what can actually be claimed
```

## Findings

### 1. Recovery should create evidence, not only narrative

A recovery pass over an unfamiliar project should produce machine-checkable anchors where practical:
- current source revision;
- inventory;
- major dependency relationships;
- entry points;
- architectural clusters;
- unresolved coverage.

A prose architecture summary without source identity becomes stale silently.

Candidate JEM rule:

> Recovery artifacts that summarize a mutable system should identify the source revision they describe.

### 2. Evidence and completeness are different claims

The upstream source-evidence audit records a failure caused by confusing “valid evidence exists” with “the evidence inventory is complete.”

This maps directly to JEM claim discipline:

```text
parser succeeded
    ≠
all declarations were found

test passed
    ≠
all relevant behaviors were covered

artifact valid
    ≠
artifact complete
```

Candidate JEM invariant:

> Evidence can support a positive claim without proving coverage completeness. Completeness requires its own evidence.

### 3. UNKNOWN must survive incremental updates

When a prior symbol disappears from a new analyzer output, the source does not automatically call it deleted. It attempts to classify deletion from current source evidence and blocks publication when the result remains unknown.

This is JEM's `UNKNOWN remains UNKNOWN` expressed as a concrete incremental-state transition.

Candidate state rule:

```text
previously known
+ missing from new best-effort extraction
= UNKNOWN

until source evidence proves deletion
```

### 4. Publication needs a gate separate from generation

The pipeline can successfully produce intermediate output and still refuse to advance durable artifacts.

This is a strong example of:

```text
BUILD succeeded
      ≠
PROMOTION passed
```

Candidate JEM rule:

> A generated artifact may be internally valid yet still fail promotion because reconciliation, freshness or evidence coverage is unresolved.

### 5. Recompute scope should be proportional to evidence of change

The source classifies changes into skip, partial, architecture-level and full update paths using fingerprints, inventory and thresholds.

The universal lesson is not the thresholds. It is proportional recomputation:

> Revalidation scope should expand with the scope and uncertainty of the change.

This can reduce unnecessary work without weakening evidence when change classification is conservative.

### 6. Freshness should be explicit and three-valued

The source distinguishes fresh, stale and unknown.

JEM implication:

> An unverifiable freshness check is not equivalent to a fresh artifact.

This is especially relevant to:
- generated docs;
- architecture diagrams;
- knowledge graphs;
- benchmark reports;
- compliance inventories;
- agent-maintained context files.

### 7. Partial benchmarks must not be promoted into end-to-end claims

The large-monorepo benchmark explicitly limits itself to deterministic stages and rejects extrapolation into LLM/token/cost/end-to-end performance claims.

This is directly compatible with JEM evidence truth:

```text
measured stage A
    → claim about stage A

not:
measured stage A
    → product-wide performance claim
```

### 8. Context partitioning can be an evidence-quality decision

Semantic batching groups files by dependency topology rather than arbitrary count. That indicates an important planning lesson:

> Work decomposition can change evidence quality, not only throughput.

For JEM planning, slice boundaries should preserve the relationships needed to reason correctly.

### 9. Shared intermediate representations reduce repeated uncertainty

A persisted graph lets later explain/onboard/diff tasks reuse previously validated structure.

Candidate rule:

> When many workflows repeatedly need the same expensive understanding step, consider a versioned shared evidence substrate rather than repeated ad hoc reconstruction.

### 10. Donor/reference ≠ copy

The repository contains many product-specific choices:
- graph ontology;
- dashboard;
- Louvain batching;
- Tree-sitter plugin implementation;
- exact thresholds;
- agent roles.

JEM should extract invariants, not transplant architecture by resemblance.

## Candidate JEM additions for MK1 comparison

These are not canonical yet:

1. **Revision-bound recovery artifact** — summary/model records the source commit/revision.
2. **Completeness claim separation** — evidence validity and evidence coverage are separate fields.
3. **Freshness state** — `FRESH | STALE | UNKNOWN`.
4. **Promotion reconciliation** — generation success cannot bypass reconciliation gates.
5. **Incremental omission rule** — omission from best-effort extraction is `UNKNOWN`, not deletion.
6. **Proportional recomputation** — expand verification scope as structural uncertainty grows.
7. **Partial-benchmark boundary** — stage benchmark cannot silently become end-to-end claim.
8. **Topology-aware slicing** — planning/batching should preserve relationships material to the claim.

## Proposed applicability

High:
- recovering existing repositories before redesign;
- generated architecture/context artifacts;
- agent-maintained project knowledge;
- incremental documentation/indexes;
- codebase onboarding and review context.

Medium:
- non-code knowledge bases where source revision/freshness can be identified.

Low:
- static one-off artifacts with no continuing source relationship.

## Promotion boundary

This quarry is `INSPIRED` + `OBSERVED` evidence for future JEM MK1 normalization.

No constitutional JEM rule has been changed by this pass.
