# Railly Skills — Review and Failure Catalog

Provenance: OBSERVED
Primary upstream:
- skills/review-gate/references/gates.md
- skills/solution-gate/references/failure-shapes.md

This file preserves the **catalog structure** without duplicating the full 58 KB gate prose. Exact trigger/check/provenance must be retrieved from upstream when applying a specific gate.

## Deterministic Review Gate checks

The pinned catalog contains 17 named deterministic checks:

1. Stale-value zero-hits
2. Force-red
3. Surface sweep
4. Silent-revert signature
5. PR staleness
6. Comment punctuation
7. Doc-sibling sweep
8. Caller sweep
9. Wait-ceiling sweep
10. Artifact cleanup registration
11. Head coverage
12. Shell-metacharacter coverage
13. Raw-input re-derivation sweep
14. New-flag doc sweep
15. External executable installer parity
16. Executable configuration example compatibility
17. Classifier-narrowing producer sweep

These are not all universal. They are triggered by change shape and repository conventions.

### What the deterministic family encodes

Recurring escaped-defect patterns:

- renamed behavior copied across surfaces;
- regression tests never proven red-capable;
- one updated surface while a sibling/caller/producer stays stale;
- old PR assumptions against newer subsystem invariants;
- timing ceilings that ignore slower producers;
- new persistent files without cleanup registration;
- review evidence not tied to current HEAD;
- parser/resolver changes whose old raw derivations remain elsewhere;
- new public flags absent from sibling documentation;
- runtime executable use without installer parity;
- documented examples impossible under production validation;
- narrowed classifiers that forget old producer shapes.

Portable abstraction:

    when the failure class is enumerable, generate the set and check all members

## Judgment lenses

The pinned catalog contains 23 focused lenses:

### Promoted

- Inverse regression surface
- New-domain matrix
- Resolution-rule consistency across consumers
- Substrate differential corpus
- Error-path forcing
- Substrate verification

### Candidate

- Shell re-parse append domain
- Emission channel and one-shot latch reachability
- Shim hermeticity
- Deliberate-default check
- Fresh-seam scan
- Reference-implementation oracle
- New-failure-outcome propagation
- Flag-propagation dispatch sweep
- Non-destructive recovery
- Cancellation and timeout hygiene
- Boundary pipeline trace
- Dogfood the built artifact
- Newly-asserted invariant ownership
- Docs-behavior parity
- Demonstrative example
- Choice audit
- Complexity budget

A lens is a focused reviewer pass, not a mega-prompt containing every concern.

## Lens admission discipline

Observed rule:

- a gate/lens enters from a recorded case or confirmed external review miss;
- promotion requires recurrence or maintainer-confirmed evidence;
- findings must be verified at the layer of the claim;
- unverified findings remain gaps rather than being silently discarded.

This is one of the strongest Foundry-compounding mechanisms:

    escaped defect
      → case
      → enumerated failure class
      → deterministic gate or focused lens
      → future review

## Solution Gate failure shapes

The pinned failure-shape catalog contains 13 named failure families:

1. S1 Over-reach — fix generalizes past the finding.
2. S2 Under-reach — fixes instance, not class.
3. S3 Direction inheritance — only one direction of two-way cause.
4. S4 Proxy property — guard proves adjacent property.
5. S5 Unregistered peer — new state unknown to other consumers.
6. S6 Peer-version blindness — cross-process contract assumes peer version.
7. S7 Wrong layer — mechanism is sound, delivery layer is broken.
8. S8 Guard-derived cells — verification inherits guard blind spot.
9. S9 Test pins the wrong thing — green for wrong reason.
10. S10 Claim from prose — load-bearing fact comes from docs, not execution.
11. S11 Asymmetric validation across consumers.
12. S12 Primitive-contract mismatch — mechanism violates primitive promise.
13. S13 Invocation-state collapse — omission becomes removal.

These are applied before final shape selection, not only after code exists.

## EM3RC0D implication

INSPIRED:

Do not copy this as a global checklist.

Start a Foundry review catalog empty/small and harvest from:

- our escaped defects;
- external audits;
- production incidents;
- repeated design regressions;
- commercial/user failures where they map to build process.

The Railly catalog is a **research corpus of failure shapes**, not automatic EM3RC0D canon.
