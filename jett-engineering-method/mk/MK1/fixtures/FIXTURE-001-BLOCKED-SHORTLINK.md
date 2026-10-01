# FIXTURE-001 — Unresolved LinkedIn short-link

Purpose: exercise Source Intake failure behavior against a real incoming pointer without inventing the destination or source content.

## Identity

```text
source_id: JEM-MK1-FIXTURE-001
received_at: 2026-09-21
input_pointer_type: LinkedIn safety redirect wrapper
embedded_short_link: https://lnkd.in/eZf28tC5
resolved_identity: UNKNOWN
title: UNKNOWN
author_or_publisher: UNKNOWN
publication_or_version_date: UNKNOWN
observed_at: 2026-09-21
source_type: short-link / redirector
```

The original wrapper carried the embedded destination pointer `https://lnkd.in/eZf28tC5`. Tracking/security-wrapper parameters are not treated as source identity.

## State

```text
access_state: BLOCKED
capture_state: METADATA_ONLY
verification_state: UNVERIFIED
promotion_state: POINTER_ONLY
provenance: OBSERVED
```

## Resolution evidence

Observed in the current research environment:

1. The LinkedIn safety-wrapper URL did not yield the target content.
2. Direct access to `https://lnkd.in/eZf28tC5` was unavailable.
3. Web search for the exact short code / URL returned no indexed destination.
4. No final canonical URL was established.

These observations describe the current access boundary. They do **not** prove that the external link is dead or invalid for other clients.

## Claims currently supported

- A pointer containing the short-link `https://lnkd.in/eZf28tC5` was received for research.
- The current environment did not resolve enough source identity/content to inspect it.
- The correct repository state is therefore `BLOCKED / METADATA_ONLY / UNVERIFIED / POINTER_ONLY`.

## Claims not supported

The fixture does not support claims about:

- the final destination URL;
- the source title;
- the author/publisher;
- the topic or thesis;
- the correctness, usefulness or novelty of the source;
- any domain knowledge allegedly contained behind the short-link.

## Failure behavior demonstrated

```text
pointer received
  ↓
resolution fails
  ↓
BLOCKED
  ↓
no semantic extraction
  ↓
no quarry promotion
  ↓
no canonical claim
```

This is the intended fail-closed behavior.

## Next action

`RESOLVE`

When a client can expose the final destination or the source content is provided directly, create/update a domain-appropriate source record and continue through capture → verification → quarry.

Do not mutate this historical fixture to pretend the earlier access succeeded; record the later successful observation separately or append a dated resolution event.
