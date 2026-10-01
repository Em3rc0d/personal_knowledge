# EM3RC0D Foundry — Repository Contract

Status: **MK0 canonical routing contract**

## Purpose

This domain separates four things that must not collapse:

1. external source evidence;
2. processed observations;
3. current EM3RC0D architecture proposals;
4. promoted operational knowledge.

## Authority precedence

For current Foundry-state questions:

    STATUS.md
    > active MK package
    > architecture/ when the active MK explicitly adopts it
    > quarries/
    > mining-site/
    > external raw corpus

For “what does Railly/skills actually contain?” questions:

    pinned raw snapshot
    > S-001 source receipt
    > quarry synthesis
    > architecture adaptation

An EM3RC0D adaptation never overwrites an upstream fact.

## Layer contracts

### research-corpora/.../upstream/

OFFICIAL/OBSERVED external corpus.

Rules:

- immutable within the distillation branch except a deliberate upstream refresh;
- no EM3RC0D edits;
- no generated annotations inside it;
- exact source identity must remain recoverable.

### mining-site/

Owns source identity, scope, legal/provenance boundary, inspected surfaces, freshness triggers and open source-level questions.

It does not own synthesized Foundry rules.

### quarries/

Owns processed source-derived observations and interpretation.

Every material statement must make clear whether it is:

- OBSERVED — directly in source/code/artifact;
- INFERRED — derived from multiple observations;
- INSPIRED — adapted for our environment;
- GENERATED — proposed by us and awaiting evidence.

### architecture/

Owns candidate/current structural models for EM3RC0D Foundry.

In MK0, architecture is GENERATED/INSPIRED by default. It becomes canonical only through an MK gate.

### mk/

Owns maturity, normalization, gates and promotion decisions.

Only this layer may say a Foundry rule/schema has passed the current MK.

## Copy boundary

The Railly source is MIT and its license is preserved in the raw snapshot. Where a later EM3RC0D implementation copies substantial source text/code, keep applicable attribution/license notices.

Distilled ideas should be independently phrased and provenance-linked rather than copied verbatim unless verbatim reuse is materially useful.

## No hidden promotion

Forbidden transformations:

- Railly does X → EM3RC0D must do X.
- Railly marks dogfooded → validated for us.
- one successful case → universal procedure.
- invocation count → quality evidence.
- merged/released → technically verified.
- agent report → observed proof.
- generated architecture → implementation authority.

## Change transaction

New evidence changes understanding in this order:

    source receipt / raw evidence
      → quarry update
      → MK impact assessment
      → architecture update if needed
      → promoted rule/schema update if gate passes
      → status update

Generated indexes may improve navigation but never become an independent competing source of truth.
