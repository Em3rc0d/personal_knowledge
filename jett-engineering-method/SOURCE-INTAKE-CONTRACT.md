# Source Intake Contract

## Purpose

This contract defines how an external source enters `personal_knowledge` before any claim derived from it can move from a pointer into mined evidence or canon.

The core rule is:

> **A source pointer is not the same thing as a verified source.**

A URL, short-link, screenshot, post, PDF, repository, video, message or search result may be enough to start research. It is not automatically enough to support a canonical claim.

## Why this exists

Without an intake boundary, the repository can silently collapse:

```text
link received
  → summary
  → interpretation
  → rule
  → canon
```

even when the destination was never resolved, the content was only partially visible, the source changed, or the claim came from a snippet rather than the source itself.

The required chain is:

```text
SOURCE POINTER
  ↓
IDENTITY / RESOLUTION
  ↓
ACCESS
  ↓
CAPTURE
  ↓
VERIFICATION
  ↓
MINING SITE / QUARRY
  ↓
SYNTHESIS
  ↓
MK GATE
  ↓
CANON
```

## Independent state dimensions

Do not model source maturity as one overloaded status. Track at least these independent dimensions.

### 1. Access state

```text
RECEIVED     pointer exists; destination/content not yet established
RESOLVED     final source identity/destination established
ACCESSIBLE   relevant source content can be inspected
BLOCKED      source is known but current environment cannot inspect it
DEAD         source no longer resolves or content is unavailable
```

### 2. Capture state

```text
NONE            no source content captured
METADATA_ONLY   title/author/date/URL or equivalent metadata only
PARTIAL         only a bounded fragment is captured
SNAPSHOT        sufficient source content is preserved for the current claim
REPRODUCIBLE    another reviewer can retrieve or reproduce the evidence path
```

### 3. Verification state

```text
UNVERIFIED
VERIFIED
CONTRADICTED
INCONCLUSIVE
```

### 4. Promotion state

```text
POINTER_ONLY
QUARRY_ONLY
ELIGIBLE_FOR_SYNTHESIS
PROMOTED
RETIRED
```

These dimensions must not be inferred from each other. For example, an `ACCESSIBLE` page may still be `UNVERIFIED`; a `SNAPSHOT` may preserve a claim that later becomes `CONTRADICTED`.

## Minimum source record

A source record should preserve, when applicable:

```text
source_id
received_at
input_pointer
resolved_identity
title
author / publisher
publication_or_version_date
observed_at
source_type
access_state
capture_state
verification_state
promotion_state
provenance
claims_supported
claims_not_supported
contradictions
confidence
notes
```

Unknown fields remain `UNKNOWN`. Do not manufacture metadata to complete the record.

## Short URLs and redirectors

Short-links require special handling.

Rules:

1. Preserve the original short-link as the received pointer.
2. Resolve and preserve the final destination when technically possible.
3. Preserve redirect-chain information when it materially affects identity or trust.
4. Prefer the final canonical URL as source identity when available.
5. If the short-link cannot be resolved, mark the source `BLOCKED` and keep it `POINTER_ONLY`.
6. Do not infer article/post content from the short code, surrounding platform UI, search snippets or an assumed destination.
7. A blocked short-link may generate a research task; it may not generate a canonical semantic claim.

## Dynamic and mutable sources

For content that can change without a stable version — social posts, dashboards, mutable docs, live pages, analytics, provider documentation — record an observation boundary:

```text
what was observed
where it was observed
when it was observed
which version / commit / release if available
what was not captured
```

If a future observation differs, preserve both observations and model the drift. Do not silently rewrite history.

## Snippets, previews and secondary surfaces

Search snippets, social previews and generated summaries are navigation aids, not substitutes for the underlying source.

They may support a claim only about the snippet/preview itself.

They must not be promoted as evidence for claims about source content that was not actually inspected.

## Claim-to-source boundary

Every promoted claim must answer:

```text
What exact claim is being made?
Which source evidence supports it?
Was that evidence actually inspected?
What provenance class applies?
What observation/version boundary applies?
What would falsify or weaken the claim?
```

A source can support some claims and not others.

## Promotion gate

A claim derived from an external source is eligible for synthesis only when:

- source identity is sufficiently resolved for the claim;
- relevant content was actually inspected;
- capture is sufficient or retrieval is reproducible;
- provenance is explicit;
- claim boundaries are explicit;
- contradictions and limitations are preserved;
- no blocked or unknown field has been silently promoted into fact.

For high-impact or time-sensitive claims, require stronger evidence and fresh verification.

## Failure behavior

When source intake fails:

```text
cannot resolve          → BLOCKED / POINTER_ONLY
cannot access content   → BLOCKED / POINTER_ONLY
metadata only           → METADATA_ONLY / UNVERIFIED
partial evidence        → PARTIAL / bounded claims only
conflicting evidence    → CONTRADICTED or INCONCLUSIVE
source disappeared      → DEAD; preserve prior snapshot if one exists
```

The correct output may be `UNKNOWN` or `BLOCKED`.

That is not a failed research process. It is a truthful state.

## Relationship to repository layers

```text
source intake
  → mining-site: research map, source registry, access/provenance state
  → quarry: extracted evidence and bounded interpretation
  → brainstorming/design/architecture/...: synthesis
  → prove: claim-evidence verification
  → MK gate: promotion decision
  → main: reviewed canon
```

A quarry is never authorized to bypass source intake.

## Constitutional additions

1. Pointer ≠ source identity.
2. Source identity ≠ inspected evidence.
3. Search snippet ≠ source content.
4. Accessible ≠ verified.
5. Captured ≠ true.
6. Blocked remains blocked.
7. Unknown remains unknown.
8. Source drift must be observable, not silently overwritten.
9. Every promoted claim needs a traceable evidence path.
10. Promotion must fail closed when the source boundary cannot support the claim.
