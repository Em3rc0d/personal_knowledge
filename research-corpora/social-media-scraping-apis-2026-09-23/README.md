# Social Media Scraping APIs — 2026-09-23

MK0 research corpus for the external repository `cporter202/social-media-scraping-apis`.

## Purpose

Preserve a dated, traceable assessment of a large social-media data-acquisition catalog without treating the catalog, its marketing language, or its listed providers as verified production infrastructure.

This corpus is a **discovery source**, not a recommendation list.

## Source identity

```text
source_repo        https://github.com/cporter202/social-media-scraping-apis
owner              cporter202
captured_at        2026-09-23 America/Lima
default_branch     main
head_commit        18b787f1f24ad2863b6b75467a981b74c993bbda
last_push_seen     2026-01-20T17:57:07Z
license            NONE DECLARED
visibility         public
```

Repository metadata observed at capture time:

```text
stars              2,413
forks              480
open_issues        2
language           JavaScript
```

Counts and popularity are volatile observations, not durable truth.

## Repository shape observed

The repository is unusually data-heavy rather than code-heavy:

```text
README.md                              ~1.33 MB
settings/APIFY_ACTORS.md               ~8.27 MB
settings/fetch_apify_actors.js         acquisition script
settings/generate_readme_clean.js      normalization / documentation generator
social-media-apis-3268/README.md       ~0.93 MB
FOLLOW_CREATOR.md                      promotional artifact
```

The repo description frames the collection around social-media scraping APIs and tools for platforms such as Instagram, LinkedIn, Twitter/X, TikTok, YouTube and Facebook.

## What the code actually does

### Acquisition

`settings/fetch_apify_actors.js`:

- requests the Apify Store endpoint `/v2/store`;
- paginates with `limit` and `offset`;
- retries after errors;
- inserts a short delay between pages;
- extracts actor identity, title, description, URL, stats, categories and timestamps;
- creates affiliate URLs by appending `fpr=p2hrc6`;
- writes JSON and Markdown representations.

### Normalization / publication

`settings/generate_readme_clean.js`:

- filters obvious test/placeholder actors through name-pattern heuristics;
- groups records by category;
- performs category-local deduplication using `name + username`;
- formats category names;
- truncates descriptions for table readability;
- generates a large README and per-category documentation;
- emits promotional claims such as "production-ready" and "updated daily".

## Evidence-quality assessment

### Strong observations

- The collection is generated from Apify Store data rather than being manually authored actor-by-actor.
- The generator applies filtering, categorization and basic deduplication.
- Affiliate tracking is systematically injected into provider links.
- The repository currently has no declared license.
- The latest repository push observed is from 2026-01-20, even though generated copy contains an "Updated Daily" claim.

### Weak / unverified claims

Do **not** promote these without direct validation:

- that every listed actor is production-ready;
- that every actor still exists;
- that pricing, schemas, rate limits or capabilities are current;
- that the catalog is updated daily;
- that popularity or placement implies quality;
- that a listed actor is compliant for a particular use case.

## Commercial-incentive boundary

The source adds affiliate tracking to actor URLs. Therefore:

```text
catalog inclusion      != independent recommendation
description text       != verified capability
marketing claim        != engineering evidence
affiliate link         => commercial incentive must remain visible in provenance
```

This does not make the source unusable. It changes how evidence is weighted.

## Copyright / license boundary

No license was declared in repository metadata at capture time.

Therefore this corpus stores:

- source identity;
- observed repository structure;
- our own abstractions;
- verification rules;
- small factual metadata.

It does **not** mirror the large README, actor list, or descriptions.

## Reusable extraction

### Pattern 1 — Dynamic catalog as candidate generator

Large external catalogs are valuable for **discovery breadth**, but they should feed a candidate queue rather than become canonical truth.

```text
catalog
→ candidate records
→ vendor / upstream verification
→ sandbox test
→ compliance review
→ promote / reject
```

### Pattern 2 — Freshness must be evidenced

A generated "last updated" string is not sufficient evidence of repository freshness.

Minimum freshness evidence should include at least:

- source commit / snapshot identifier;
- capture timestamp;
- upstream documentation timestamp when available;
- successful live test timestamp for any promoted integration.

### Pattern 3 — Separate listing from capability

A tool being listed only proves catalog presence.

Capability promotion requires independent evidence for the exact surface needed:

```text
platform
data object
query semantics
pagination
freshness
authentication
pricing
rate limits
output schema
failure behavior
```

### Pattern 4 — Commercial provenance

Affiliate, sponsored or vendor-owned sources remain useful, but their incentive must be explicit and their claims need stronger verification.

### Pattern 5 — Normalize before ranking

Provider comparison should normalize records before any evaluation. Raw catalog categories and descriptions are not a stable taxonomy.

## Candidate verification gate

Before any scraper/API becomes an approved dependency:

1. **Identity** — exact provider/actor and authoritative docs are known.
2. **Live existence** — endpoint/tool still exists.
3. **Task fit** — it returns the exact surface required.
4. **Schema** — fields and pagination are inspected from a real sample.
5. **Cost** — current pricing is captured.
6. **Reliability** — at least one positive and one failure-path fixture exist.
7. **Freshness** — data latency is measured or bounded.
8. **Compliance** — platform terms, privacy and intended-use constraints are reviewed for the concrete workflow.
9. **Observability** — failures, rate limits and partial results can be detected.
10. **Provenance** — every acquired dataset can identify source, tool, run time and query.

If any high-risk item is unknown, status remains `CANDIDATE`.

## Relevance to personal_knowledge

Most useful downstream connections:

- `content-strategy/` — research tooling for public posts, creators, comments and engagement signals;
- future market-research/data-acquisition domains — provider discovery and collection pipelines;
- `agent-engineering/` — external-tool selection, runtime failure boundaries and provenance.

The source does not justify changing current content-strategy hypotheses by itself.
