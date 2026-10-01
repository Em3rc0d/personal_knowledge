# Railly Skills — Shaping and Solution Selection

Provenance: OBSERVED + INFERRED
Primary upstream: skills/solution-gate/, especially SKILL.md and references/

## Why Solution Gate exists

Review Gate asks whether a completed diff is good enough. Solution Gate asks an earlier question:

    is this the right thing to build?

It fires when materially different solution shapes exist, especially when they differ in ownership, lifecycle, persistent state, compatibility, authority or contract.

Mechanical changes deliberately skip it.

## Evidence-only Frame

Before proposals exist, Solution Gate freezes:

- violated property and desired outcome;
- observable success;
- external product constraints;
- must-not-change behavior;
- unknowns;
- evidence handles;
- temporal transition contract when state persists.

The packet excludes the candidate mechanism.

Portable mechanism:

    freeze the problem before exposing a favored solution

This reduces anchoring and sunk-cost bias.

## Independent shaping

The source asks for two isolated Shaping passes, preferably different model families and not the implementer.

Both receive the same frozen packet.

Each produces its native Shaping artifacts:

- requirements table;
- solution shapes and parts;
- flags/unknowns;
- R × Shape fit check;
- required spikes;
- recommendation.

Solution Gate does not create a second competing requirements/proposal format.

Portable rule:

    orchestrator owns evidence/order;
    specialist method owns its native artifact

## Reconcile without averaging

Model agreement is not evidence.

The gate:

- reconciles requirements before solution preference;
- preserves product-policy disagreement for human judgment;
- probes factual disagreements;
- normalizes equivalent shapes without erasing provenance;
- refuses majority vote as proof.

## Attack weakest load-bearing links

For each surviving shape:

- trace forward effects;
- mark links observed/inferred/guessed;
- extract falsifiable predictions;
- run the cheapest probe that could refute the mechanism;
- feed the evidence back into Shaping;
- rerun fit checks after material changes.

A prose verdict cannot override a failed fit-check cell.

## Temporal contracts

The source’s temporal-contract reference is especially portable.

For any stateful input, model:

- owner and lifetime;
- initial default;
- unset → set;
- set → omitted;
- set → same;
- set → changed;
- set → explicit clear;
- reuse/restart/migrate behavior;
- continuity observables.

Critical rule:

    omission != explicit clear unless the product contract proves equivalence

A same-session multi-command probe is required when continuity matters. Exit code alone is not enough.

## Existing candidate audit

When an implementation already exists, the source uses blind reconstruction:

1. seal candidate implementation/details;
2. reconstruct the contract independently;
3. generate blind solution shapes;
4. probe those shapes;
5. reveal candidate;
6. treat candidate as another shape under the same discriminator matrix;
7. adopt, amend, absorb/recreate, reject, or return to contract.

Portable rule:

    existing work does not lower the evidence bar

## Failure-shape catalog

Solution Gate also compares the selected shape against a catalog of known failure shapes harvested from real review/history. This turns prior misses into adversarial design checks before implementation.

## EM3RC0D adaptation

INSPIRED:

For product work, Solution Gate should become a general **Shape Gate** spanning:

- product behavior;
- UX interaction model;
- state ownership;
- architecture;
- external dependency choice;
- trust/authority boundaries;
- data lifecycle;
- delivery and rollback shape.

But the gate must remain conditional. A product Foundry that forces multi-agent shaping onto trivial work will destroy its throughput advantage.
