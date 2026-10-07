# Knowledge Dependency Manifest

Status: **MK0 candidate / GENERATED**, informed by JEM and S-005 provenance sources.

## Problem

A course can become stale even when its own files never change.

A source-domain rule may be revised, contradicted, deprecated or superseded.

Therefore product releases must pin the knowledge they were compiled from.

## Product-level manifest

```yaml
product_id:
product_version:
compiled_at:
compiler_revision:
dependencies:
  - domain:
    artifact_path:
    repository_commit:
    knowledge_state:
    claim_scope:
    provenance:
    source_revision:
    rights_status:
    observed_at:
    freshness_class:
    refresh_triggers:
generated_artifacts:
review_activity:
pilot_evidence:
release_state:
```

## Minimal provenance mapping

W3C PROV concepts are useful as a conceptual model:

- **Entity** → source artifact / compiled lesson / released product;
- **Activity** → compile / review / pilot / release;
- **Agent** → author / reviewer / compiler;
- `wasDerivedFrom` → product artifact depends on canonical knowledge;
- `wasGeneratedBy` → artifact created by a compiler/review activity;
- `wasAssociatedWith` → responsible human/agent.

MK0 does not require RDF or a PROV implementation. The vocabulary is used to avoid inventing an incompatible provenance model unnecessarily.

## Staleness triggers

A dependency becomes review-required when:

- pinned source path changes materially;
- source domain retires or contradicts the claim;
- source revision is superseded for a time-sensitive topic;
- rights status changes;
- a new standard/version changes the taught behavior;
- an assessment depends on tooling/API behavior that drifted.

## Versioning candidate

Product version changes should be driven by learner-visible/claim-visible impact, not every source commit.

Candidate policy:

- patch — wording/examples/fixes without changed outcome contract;
- minor — new or revised learning content compatible with existing outcome contract;
- major — changed prerequisites, outcomes, assessment interpretation or core taught capability.

This remains a MK1 candidate until dogfood validates it.
