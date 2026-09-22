# Railly Skills — Cases, Compiled Knowledge and Learning

Provenance: OBSERVED + INFERRED
Primary upstream: record-a-case, foundry/knowledge/, compiled-knowledge candidate, case-template

## Case is evidence, not canon

record-a-case treats a completed/interrupted/disproven work unit as an **evidence ledger**.

It records independently:

- technical validation;
- human review;
- maintainer acceptance;
- delivery.

A merged PR can therefore be merged while technical evidence remains incomplete.

## One mechanism per case

A case should contain one coherent maintenance unit and one transferable lesson. Unrelated outcomes are split even if they occurred in one session.

This increases retrieval precision and avoids “session summary” artifacts.

## Claim classes

Material statements are kept as:

- retrievable evidence;
- unreviewed report;
- inference;
- unknown.

Drift-prone external state is rechecked rather than copied from transcript memory.

## Smallest durable destination

The extracted lesson chooses the smallest useful destination:

- skill method;
- reference rule;
- exemplar;
- deterministic check;
- behavior eval;
- coverage gap;
- no change.

Portable principle:

    reusable knowledge should not automatically become a new procedure

## Compiled knowledge layer

The source inserts a durable layer between evidence and executable skill.

Authored surfaces:

- patterns with stable IDs;
- skill provenance pages;
- typed evidence relationships;
- typed skill relationships;
- explicit gaps;
- append-only proposal impact.

Generated projections:

- compact index;
- coverage matrix;
- machine graph.

Generated projections are navigation/views, not new authority.

## Relationship model

Evidence relationships include:

- origin;
- application;
- evaluation;
- transfer;
- contradiction;
- rejection.

Skill relationships include:

- motivates;
- supports;
- contradicts;
- supersedes.

Relationship states include:

- active;
- contradicted;
- superseded;
- stale.

This allows old knowledge to remain historically visible without continuing to justify current procedure.

## Textual match audit

One subtle but important mechanism is the reviewed skill-file match audit.

A string match is not treated as method application.

Matches are classified as:

- application;
- evaluation;
- decision;
- reference;
- planned;
- incidental.

Fingerprints cover the exact matching lines. New, removed or changed matches fail validation until reviewed.

Portable lesson:

    retrieval hit != evidence relationship

## Proposal-impact memory

A proposal for procedure evolution is bounded to one skill.

The proposal packet contains only relevant:

- provenance;
- patterns;
- prior impacts;
- reviewed outcomes;
- selected evidence.

Outcomes are preserved even when rejected.

Rejected/absorbed/no-change proposals leave active procedure byte-identical.

Accepted change requires:

- changed active digest;
- eval evidence;
- human authority.

This prevents the Foundry from repeatedly rediscovering and reproposing failed ideas.

## Runtime boundary

Executing agents do not receive the full knowledge graph.

They receive promoted procedure and disclosed references only.

Maintainers/proposers query compiled knowledge separately.

Portable principle:

    memory for evolution != context for execution

## Usage receipts

Private usage telemetry is intentionally weaker than case evidence.

Invocation counts answer adoption questions.

They do not establish:

- exact procedure version;
- outcome quality;
- canonical case;
- maturity support.

High-signal receipts can become **review candidates**, never automatic knowledge/procedure mutations.

## EM3RC0D adaptation

INSPIRED:

The knowledge plane should compile more than skills.

Potential reusable asset targets:

- procedure;
- code primitive;
- UI component;
- product shell;
- design rule;
- architecture pattern;
- test harness;
- deployment recipe;
- research method;
- eval;
- coverage gap;
- no change.

The “smallest durable outcome” rule should apply to all of them.
