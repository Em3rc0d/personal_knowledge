# Q-004 — Social-media data acquisition catalog

Date: 2026-09-23  
Domain: content-strategy  
Stage: MK0 / quarry  
Primary source: `cporter202/social-media-scraping-apis`  
Source commit: `18b787f1f24ad2863b6b75467a981b74c993bbda`  
Provenance: `OBSERVED + INFERRED`

## Research question

How can a large third-party scraping/API catalog improve content research without turning vendor listings or scraped metrics into unverified strategy evidence?

## Finding

The repository is useful primarily as a **provider-discovery surface**.

It should not be used as:

- a quality ranking;
- proof that a scraper is currently operational;
- proof that a platform allows a concrete collection workflow;
- a substitute for first-party account analytics;
- a source of causal content-performance claims.

## Distilled workflow

```text
research question
→ required data surface
→ candidate discovery
→ normalize candidates
→ verify authoritative docs
→ sandbox sample
→ inspect schema / cost / freshness / failures
→ compliance gate
→ approved collector
→ dated dataset with provenance
→ analysis
```

## Data-surface-first selection

Never begin with "Which scraper should we use?"

Begin with the observation required.

Examples:

```text
creator discovery
public profile snapshot
recent public posts
comments / replies
search results
hashtags / keywords
transcripts
engagement counters
competitor publishing cadence
```

Then evaluate tools against that surface.

## Candidate record schema

A future collector registry should minimally capture:

```text
candidate_id
platform
data_surface
provider
tool_or_actor
discovery_source
catalog_snapshot
authoritative_docs
auth_model
pricing_model
rate_limit
pagination_model
freshness
output_schema
failure_modes
export_formats
observability
terms_privacy_review
fixture_positive
fixture_negative
last_live_test
status
provenance
```

Suggested statuses:

```text
DISCOVERED
DOCS_VERIFIED
SANDBOXED
APPROVED
REJECTED
STALE
UNKNOWN
```

## Promotion gates

### G0 — Discovery

Candidate exists in a catalog.

Evidence strength: low.

### G1 — Identity

Exact provider, product/tool identity and authoritative documentation are resolved.

### G2 — Capability

The exact required data surface and query semantics are documented.

### G3 — Runtime

A real sample proves schema, pagination and failure behavior.

### G4 — Economics / compliance

Current cost and relevant terms/privacy constraints are understood for the intended workflow.

### G5 — Promotion

Only now may the collector be referenced as an approved implementation option.

## Content-strategy boundary

Scraped/public-market data and first-party account analytics answer different questions.

```text
first-party analytics
    → what happened on our account

public external collection
    → what is visible in the market / competitor / creator environment
```

Do not silently merge the two evidence classes.

A competitor's public engagement counter does not provide the same measurement surface as our own retention, audience-source or conversion analytics.

## Provenance rule for collected datasets

Every external dataset should retain:

```text
platform
query
collector/provider
collector version or actor identity
run timestamp
source URLs / public IDs when lawful and appropriate
pagination / truncation state
errors / missing pages
raw-vs-derived field distinction
```

Without this, downstream analysis cannot distinguish absence from collection failure.

## Source-specific cautions

Observed in the source repository:

- actor data is pulled from Apify Store;
- output documentation is generated programmatically;
- placeholder filtering is heuristic;
- deduplication is basic;
- affiliate parameters are appended to links;
- no license is declared;
- latest observed push is 2026-01-20 while generated copy claims daily updating.

Therefore the catalog is retained as `DISCOVERY_ONLY`.

## What is promoted now

Promoted to MK0 working knowledge:

1. social-data tooling must be selected by required data surface, not by catalog popularity;
2. discovery catalogs need independent capability and freshness verification;
3. affiliate/vendor claims require explicit provenance;
4. scraper outputs need run-level provenance and failure visibility;
5. external public data must remain separated from first-party analytics;
6. no provider becomes canonical without sandbox evidence.

## What remains open

- Which platforms/data surfaces are actually needed for Content Seller, Logan and LinkedIn research.
- Whether official APIs can satisfy some surfaces more safely or reliably.
- Which provider candidates pass live tests today.
- Current prices and rate limits.
- Platform-specific terms/privacy constraints for each intended collection workflow.
- Whether a unified collector or per-platform collectors are operationally superior.

No vendor recommendation is made by this quarry.
