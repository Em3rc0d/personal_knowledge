# Railly Skills — Evolution Lessons

Provenance: OBSERVED + INFERRED
Primary upstream: foundry/rounds/, foundry/deprecated/, foundry/maturity.json

## The system is valuable partly because it records when ideas lose

A Foundry that only preserves promoted ideas creates survivorship bias.

Railly’s rounds preserve:

- rejection;
- deprecation;
- absorption;
- human override;
- evidence debt;
- zero-delta evaluations;
- overlap questions.

## Key lifecycle corrections

### Prose improvement that did not improve behavior

Round 001:

- candidate proof record/exemplars tied released behavior;
- no measurable improvement;
- candidate skill change rejected;
- evaluation infrastructure retained.

Distilled rule:

    better-looking instructions are not an upgrade without behavior delta

### Reviewer generated true finding then “proved” it away

Round 002:

- correct candidates were generated;
- verification used wrong-layer evidence;
- true positives were dropped;
- procedure changed to require same-layer refutation.

Distilled rule:

    verification is itself a failure surface

### Broad umbrella lost to phase-specific operations

Round 004:

- Unfold had broad conceptual coverage;
- observed workflow used narrower operations;
- umbrella was deprecated and archived;
- contracts and phase methods remained.

Distilled rule:

    orchestration abstractions must earn operational use, not merely architectural elegance

### Invocation count did not equal maturity

Round 006:

- skill-name/call counts were checked against actual case/run evidence;
- only verified applications supported maturity changes;
- coincidental/planned mentions were rejected as evidence.

Distilled rule:

    telemetry drives investigation, not promotion

### Human policy override remained visibly weaker evidence

Round 007:

- human raised maturity/channel for selected skills;
- evidence gap was explicitly preserved.

Distilled rule:

    authority can choose policy without rewriting epistemic history

### Compatibility alias intentionally died

Round 010:

- deprecated alias contradicted current registry and had drifted;
- removed from active surface;
- history preserved under deprecated/.

Distilled rule:

    compatibility has a cost and should have an exit condition

### New factory protocol entered with an explicit deprecation condition

Round 011 software-factory:

- overlap with existing skills acknowledged;
- no real run existed;
- registration allowed experimentally;
- first run required to show coordination value or justify deprecation.

Distilled rule:

    speculative infrastructure should define what evidence would kill it

### Full router added only after phase methods existed

Round 013:

- factory-loop did not precede component methods;
- it was added to solve ordering/freshness/authority problems observed across them.

Distilled rule:

    compose proven/named operations before inventing the orchestrator

### Security review stayed “evaluated” after a positive benchmark

Round 014:

- one controlled five-case comparison improved assertions;
- transfer/repeated trials missing;
- maturity stopped at evaluated.

Distilled rule:

    positive pilot != validation

## Deprecated corpus

The pinned tree preserves:

- Unfold;
- pick-an-issue;

under foundry/deprecated/.

This is important because deprecation does not erase the historical artifact/evals that explain later architecture.

## EM3RC0D anti-pattern to avoid

Do not make EM3RC0D Foundry a one-way “promotion machine”.

It needs:

    candidate
      → pass / fail / absorb / supersede / no-change / deprecate

and each outcome should reduce future rediscovery.
