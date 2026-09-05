# RICOUI Quarry — Extracted Candidate Rules

These are **our candidate rules** derived while studying RICOUI. They are not RICOUI quotations and are not yet certified.

## WD-CAND-001 — Semantic source before implementation

`INSPIRED from SRC-RICOUI`

Define the semantic design system before allowing frontend implementation to become the de facto specification.

## WD-CAND-002 — Tokens need usage semantics

`INFERRED / GENERATED`

Every important token family should carry role or usage semantics. Raw values without intent are insufficient for reliable human or agent implementation.

## WD-CAND-003 — Derived artifacts must be reproducible

`INSPIRED`

When `tokens.json`, CSS variables, theme files or agent guidance are generated from a canonical design contract, the derivation path must be explicit enough to detect drift.

## WD-CAND-004 — Brand references require provenance

`INSPIRED / GENERATED`

A third-party visual reference must be labelled as official, observed, inferred or inspired. Never silently promote a mined value to an official brand guideline.

## WD-CAND-005 — Prefer visual grammar over visual copying

`GENERATED`

Extract reusable properties such as density, rhythm, hierarchy, surface strategy, chromatic behavior and component language; synthesize an original system rather than cloning another brand.

## WD-CAND-006 — Design must include behavior

`GENERATED`

A production design contract should eventually cover component states, responsive transformations, accessibility, motion semantics and content constraints, not only static desktop appearance.

## WD-CAND-007 — AI is a design-system consumer

`INSPIRED / GENERATED`

Agent instructions must derive from the same semantic rules used by humans and frontend code. Agent-specific prompts must not become an undocumented parallel design system.

## WD-CAND-008 — Visual implementation requires evidence

`GENERATED`

Compilation and unit tests do not prove visual fidelity. Important design releases need viewport-aware rendering evidence and regression checks where practical.

## WD-CAND-009 — Design changes should be diffable

`INSPIRED / GENERATED`

A meaningful design-system change should answer what changed, why, which tokens/components are affected and what visual evidence confirms the new state.

## WD-CAND-010 — External references expire epistemically

`GENERATED`

Observed external websites must be treated as dated snapshots. Revalidate a reference before relying on it for current claims.
