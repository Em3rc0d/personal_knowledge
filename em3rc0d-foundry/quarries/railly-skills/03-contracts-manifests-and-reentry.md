# Railly Skills — Contracts, Manifests and Re-entry

Provenance: OBSERVED + INFERRED
Primary upstream: foundry/missions/, scripts/work-item.mjs, scripts/lib/work-item-manifest.mjs, factory-loop

## Two representations of one mission

The source deliberately separates:

### Human-readable Issue Contract

Carries:

- observable outcome;
- observed and expected behavior;
- acceptance IDs;
- non-goals;
- invariants;
- change surface;
- verification commands;
- risk;
- promotion status;
- handoff;
- contract changes.

### Machine-readable manifest

Carries transactional state:

- exact source/repository/cwd;
- base/head/dirty digest;
- authorization;
- profile/budget;
- skill revisions/digests;
- orchestration mode and degradation;
- per-stage receipts;
- outcome;
- close-cycle state.

Portable mechanism:

    narrative contract + transactional manifest

The first is understandable. The second is enforceable.

## Exact-state evidence

A stage receipt can bind evidence to:

- head_sha;
- changed_paths_digest;
- contract_digest;
- command;
- environment_digest;
- skill_revision;
- relevant_paths;
- reuse flag and reuse evidence.

This makes “tests passed earlier” insufficient when the code, environment, contract or procedure changed.

## Dependency-aware reuse

Evidence can survive a later head only when the manifest proves:

- source and target heads;
- unchanged contract digest;
- unchanged environment digest;
- unchanged skill revision;
- the later changed paths do not intersect the receipt’s relevant paths.

This is a high-value speed mechanism: preserve evidence that is still valid instead of restarting everything.

## Explicit invalidation

work-item.mjs supports invalidating from a named stage.

The model is downstream invalidation, not global amnesia.

Example:

    shape changes
      → implementation and downstream proof stale

    docs-only change outside parser receipt cone
      → parser Test Strength may remain reusable
      → final exact-head review still required

## Authorization is data

The manifest models distinct authorization levels:

- read-only;
- local-write;
- commit;
- push;
- pull-request;
- merge;
- release;
- deploy;
- external-communication.

This prevents authority creep such as “you may implement” becoming “you may publish”.

## Orchestration degradation is evidence

Execution mode is explicit:

- native_subagent;
- fx_worker;
- herdr_worker;
- sequential_isolated;
- single_context;
- unavailable.

Degraded modes must carry an independence gap.

The manifest also encodes a circuit breaker for invalid orchestration calls: no identical retries; bounded schema failures.

Portable rule:

    capability degradation must narrow claims, not be hidden

## State transitions

Issue mission states are evidence-gated, not prose-gated:

    selected
    → reproducing
    → reproduced
    → implementing
    → proof-ready
    → spec-reviewed
    → standards-reviewed
    → closed

A state returns backward if new evidence changes scope or invalidates a contract claim.

## EM3RC0D implication

INSPIRED:

Generalize Issue Contract to Work/Product Contract.

Preserve:

- human-readable requirements and decisions;
- machine exact-state sidecar;
- action-specific authority;
- stage receipts;
- dependency-aware invalidation;
- resumability from earliest invalid state.

Do not preserve issue/PR-specific fields when the work source is a market opportunity, design experiment or product launch.
