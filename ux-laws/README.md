# UX Laws

Knowledge domain for psychology-informed UX and product design.

Primary seed source: **Laws of UX** by Jon Yablonski (`lawsofux.com`), complemented over time by original papers, books, standards, empirical studies and product evidence.

## Mission

Convert UX psychology from inspirational heuristics into a **portable, auditable and testable design knowledge system**.

A law is not considered operational merely because it is documented. It must eventually connect:

```text
source evidence
  → normalized concept
  → applicability boundary
  → design rule
  → pattern / antipattern
  → implementation guidance
  → verification method
```

## Evolution model

```text
MK0  Mine & frame
 ↓
MK1  Normalize & classify
 ↓
MK2  Operationalize rules
 ↓
MK3  Design-system integration
 ↓
MK4  Product architecture integration
 ↓
MK5  Automated UX linting / tests
 ↓
MK6+ Empirical refinement & certification
```

MK numbers represent **knowledge maturity**, not arbitrary releases. A new MK only closes when its acceptance criteria are satisfied.

## Workspace structure

```text
ux-laws/
├── README.md
├── STATUS.md
├── brainstorming/
├── design/
├── architecture/
├── plan/
├── build/
├── test/
├── mining-site/
├── quarries/
└── mk/
    ├── MK0/
    ├── MK1/
    └── ...
```

Folders can be materialized only when they contain evidence; Git does not track empty directories.

## Provenance vocabulary

Every meaningful statement should be classifiable as one of:

- `OFFICIAL`: explicitly stated by the authoritative source being studied.
- `OBSERVED`: directly observed in an artifact, interface, experiment or dataset.
- `INFERRED`: reasoned conclusion from available evidence.
- `INSPIRED`: design direction influenced by evidence but not claimed by the source.
- `GENERATED`: synthesized artifact produced by us.

When useful, attach `confidence: high | medium | low` and a source reference.

## Core families

The initial Laws of UX catalog is grouped operationally into:

1. **Cognitive capacity** — cognitive load, working memory, Miller, chunking.
2. **Perception & Gestalt** — proximity, similarity, common region, uniform connectedness, Prägnanz.
3. **Attention & salience** — selective attention, Von Restorff, serial position.
4. **Decision & interaction** — Hick, Fitts, choice overload, Doherty, Parkinson.
5. **Mental models & complexity** — Jakob, mental models, active-user paradox, Tesler, Occam, Postel.
6. **Motivation & remembered experience** — goal gradient, Zeigarnik, flow, peak-end.
7. **Cross-cutting judgment** — cognitive bias, Pareto, aesthetic-usability effect.

This taxonomy is ours (`INFERRED`), not a claim that Laws of UX publishes these exact categories.

## North-star principle

> The user should not need to understand the system's internal complexity in order to benefit from it.

This is a synthesized product principle (`GENERATED / INSPIRED`), not a quotation from Laws of UX.
