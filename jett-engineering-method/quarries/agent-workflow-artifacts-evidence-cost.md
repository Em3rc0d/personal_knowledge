# Agent Workflow Artifacts and Evidence-Cost Discipline

Primary source receipt: [agent-engineering S-114](../../agent-engineering/mining-site/S-114-midudev-higgsfield-landing.md)

Status: **QUARRY / NON-CANONICAL**

## Why this matters to Jett Engineering Method

S-114 is useful because it exposes a compact engineering pattern:

    intent
    → explicit invariants
    → agent/tool execution
    → materialized artifact
    → deterministic integration
    → focused validation

JEM can use this pattern to sharpen artifact lineage/promotion and validation-cost proportionality.

## Candidate artifact rule

An AI-produced output should not become trusted merely because the agent completed successfully.

    artifact
    + lineage
    + acceptance evidence
    + known limitations

not:

    successful tool call

## Candidate execution receipt

For expensive or externally generated artifacts, record logical artifact ID, source/input revisions, provider/capability, model/tool revision when exposed, parameters, prompt/config hash, cost estimate/actual cost when available, output checksum, deterministic post-processing chain, validation result and invalidation conditions.

Unknown provider metadata remains `UNKNOWN`.

## Evidence-cost rule

Validation should use the **cheapest sufficient evidence** for the claim being made.

| Change surface | Minimum evidence | Avoid by default |
|---|---|---|
| documentation/provenance only | diff review, link/path consistency, claim/provenance review | full paid CI/runtime suite |
| generated media only | checksum/metadata, targeted visual/media validation, performance budget | rebuilding unrelated application layers |
| deterministic transform | targeted transform test / reproducible command receipt | provider regeneration |
| runtime code path | targeted unit/integration/browser evidence | repository-wide expensive suites when unaffected |
| release-critical cross-cutting change | broader regression/release gate | skipping evidence because prior layers passed |

This is a **GENERATED candidate rule** from source evidence plus repository operating constraints; later JEM promotion is still required.

## Remote CI billing discipline

Remote CI is an evidence mechanism, not a ritual.

Candidate invariant:

    Do not trigger a paid/limited remote workflow
    unless its result can materially change the decision.

Before dispatching CI:

1. identify the claim the workflow is supposed to verify;
2. verify cheaper/local/static evidence cannot establish that claim;
3. scope the workflow to affected surfaces where possible;
4. avoid duplicate runs for identical revisions;
5. do not rerun accepted expensive generation unless invalidated;
6. preserve prior evidence when inputs and relevant contracts are unchanged.

A documentation-only knowledge ingestion should normally not consume build/test minutes merely to demonstrate activity.

## Workflow execution vs certification

    recipe reproducible
    != bit-identical generation reproducible
    != artifact accepted
    != workflow certified

JEM promotion gates should state which of these is being claimed.

## Deterministic islands

    pinned inputs
    → stochastic step
    → materialize output
    → checksum
    → deterministic normalization
    → targeted validation
    → immutable/pinned accepted artifact

This reduces the surface that must be regenerated or re-evaluated.

## Invalidation before regeneration

Regenerate expensive artifacts only after an explicit invalidation event: source change, acceptance-criteria change, failed validation, intentional model/provider experiment, product-contract change, or performance/legal constraint change.

No invalidation → reuse accepted artifact.

## Promotion boundary

This quarry may influence JEM rules for artifact lineage, AI-generation receipts, evidence-cost proportionality, CI billing discipline, regeneration/invalidation and deterministic boundaries around stochastic steps.

It does not by itself certify a universal workflow format or authorize changes to current JEM canon.
