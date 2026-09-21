# Source Intake Record

Use this template when a new external source enters a domain or research corpus.

## Identity

```text
source_id:
received_at:
input_pointer:
resolved_identity:
title:
author_or_publisher:
publication_or_version_date:
observed_at:
source_type:
```

## State

```text
access_state: RECEIVED | RESOLVED | ACCESSIBLE | BLOCKED | DEAD
capture_state: NONE | METADATA_ONLY | PARTIAL | SNAPSHOT | REPRODUCIBLE
verification_state: UNVERIFIED | VERIFIED | CONTRADICTED | INCONCLUSIVE
promotion_state: POINTER_ONLY | QUARRY_ONLY | ELIGIBLE_FOR_SYNTHESIS | PROMOTED | RETIRED
provenance: OFFICIAL | OBSERVED | INFERRED | INSPIRED | GENERATED
```

## Evidence boundary

### Inspected

- 

### Not inspected / unavailable

- 

### Claims this source can currently support

- 

### Claims this source cannot currently support

- 

## Contradictions / drift

- 

## Confidence

```text
confidence:
reason:
```

## Next action

```text
RESOLVE | CAPTURE | VERIFY | CROSS-CHECK | EXTRACT | HOLD | RETIRE
```

## Promotion checklist

- [ ] Final source identity is sufficiently resolved for the intended claim.
- [ ] Relevant content was actually inspected.
- [ ] Capture/retrieval is sufficient for review.
- [ ] Provenance is explicit.
- [ ] Claim boundaries are explicit.
- [ ] Contradictions/limitations are preserved.
- [ ] No snippet, redirector or generated summary is being substituted for source evidence.
- [ ] Remaining unknowns are explicit.
