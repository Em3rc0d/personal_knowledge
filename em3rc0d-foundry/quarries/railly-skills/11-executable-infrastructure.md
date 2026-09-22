# Railly Skills — Executable Infrastructure

Provenance: OBSERVED + INFERRED
Primary upstream: scripts/, .github/workflows/validate.yml

## Why scripts matter

The source repeatedly turns prose rules into code.

This is the central transition from “methodology” to “factory”.

## Work-item CLI

scripts/work-item.mjs provides:

- manifest initialization;
- validation;
- stage-receipt insertion;
- section insertion;
- downstream invalidation;
- usage-receipt annotations;
- close-cycle receipt.

Writes use temp file + rename for atomic replacement.

Portable lesson:

    state transitions deserve a machine transaction surface

## Manifest validator

scripts/lib/work-item-manifest.mjs enforces:

- schema version;
- valid authority;
- profile budget;
- exact stage status;
- pass requires skill revision;
- pass/fail/invalidated requires evidence;
- skip/unavailable/not-triggered requires reason;
- fingerprint fields;
- cross-head reuse constraints;
- non-intersection with relevant paths;
- orchestration degradation;
- bounded schema failures;
- outcome/close-cycle schema.

The important mechanism is not JSON specifically. It is **fail-closed state validity**.

## Catalog validator

scripts/validate-skills.mjs checks:

- unique skill names;
- frontmatter;
- installable path vs channel;
- marketplace grouping;
- maturity registry;
- decision path existence;
- SKILL.md compactness;
- canonical writer markers;
- no live Foundry output inside distributed skill packages;
- eval/trigger schema;
- internal links;
- case schema;
- Issue Contract validity.

This makes architectural boundaries testable.

## Procedure identity doctor

skills-doctor compares:

- canonical package digest;
- digest at current Git revision;
- installed package.

It detects:

- clean;
- dirty source;
- diverged install;
- missing install.

A review result can therefore be tied to the procedure revision that produced it.

Portable principle:

    procedure version is part of evidence identity

## Knowledge compiler

compile-knowledge:

- loads authored patterns/provenance/impact;
- validates relationships;
- verifies reviewed textual-match audit;
- compiles generated index/coverage/graph;
- check mode detects stale projections.

Authored source and generated views remain distinct.

## Proposal packet / impact recorder

build-proposal-packet constrains proposal context to one target skill.

record-impact preserves an append-only normalized history and idempotent retry semantics.

Portable principle:

    bound the mutation surface before asking an agent to evolve the system

## Usage-receipt compiler

Private receipt export is schema-validated.

The compiler:

- excludes unregistered skills;
- aggregates routine usage;
- counts unknown outcomes separately;
- emits only high-signal candidates;
- requires human review;
- explicitly disables automatic case/knowledge/procedure mutation.

Portable principle:

    telemetry pipeline must preserve weaker epistemic status than evidence pipeline

## Eval aggregation

aggregate-skill-eval computes:

- no-skill pass rate;
- current pass rate;
- candidate pass rate;
- candidate delta vs current;
- current delta vs no skill.

It also admits unavailable timing/token metrics rather than inventing them.

## Textual-match audit

knowledge-audit discovers exact skill-token matches, fingerprints lines and requires reviewed semantic classification.

A changed matching line makes the audit stale.

This is a sophisticated example of converting “grep-based provenance” into a fail-closed review queue.

## CI implication

A Foundry becomes reliable when its own boundaries are testable:

- stale generated view;
- broken provenance link;
- unsupported maturity;
- invalid contract;
- diverged runtime skill;
- missing eval;
- malformed case

should be CI-detectable where practical.

## EM3RC0D adaptation

INSPIRED:

MK2 should implement only the deterministic machinery that proved necessary during MK0/MK1 dogfood.

Do not port every Railly script.

Prioritize:

1. Work Contract/manifest validator;
2. receipt writer + invalidation;
3. provenance/knowledge validator;
4. reusable asset registry validator;
5. eval runner/aggregator;
6. runtime package identity check.

Everything else must earn itself from friction or escaped defects.
