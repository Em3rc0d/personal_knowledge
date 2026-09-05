# Web Design

Knowledge domain for building websites from an explicit, traceable and verifiable design system instead of styling screens ad hoc.

## Mission

Convert visual references, UX evidence and implementation knowledge into a **portable design intelligence layer** usable by humans, frontend systems and AI agents.

The target lifecycle is:

```text
product context
  → UX constraints
  → reference mining
  → visual evidence
  → normalized design knowledge
  → semantic design contract
  → tokens + component contracts
  → responsive / a11y / motion rules
  → implementation
  → visual verification
  → versioned design release
```

## Core principle

> Do not code the look. Model the design, then implement it.

A website is not considered well-designed merely because individual screens look polished. The system must preserve intent, rules, boundaries and verification criteria across pages, breakpoints, states and future changes.

## Scope

This domain covers:

- reference and brand research;
- visual evidence capture and classification;
- visual grammar and design personality;
- semantic design specifications such as `DESIGN.md`;
- design tokens and generated frontend artifacts;
- component contracts and state behavior;
- responsive transformation rules;
- accessibility constraints;
- motion semantics and reduced-motion behavior;
- imagery and content-system rules;
- visual regression and design consistency checks;
- design-system releases, diffs and lineage;
- AI-agent consumption of design knowledge.

## Source boundary

External systems are **mines**, not our architecture.

RICOUI is an important seed source because it demonstrates a local-first `DESIGN.md` workflow, a readable canonical source, derived token/CSS exports, brand references and explicit human review of AI changes. However:

```text
RICOUI ≠ web-design
RICOUI = external source inside web-design research
```

Its material is captured in:

```text
mining-site/ricoui.md
        ↓
quarries/ricoui/*
        ↓
normalization / review
        ↓
design/* + architecture/* + build/*
```

Every adopted rule must preserve enough lineage to answer **where it came from** and whether it is `OFFICIAL`, `OBSERVED`, `INFERRED`, `INSPIRED` or `GENERATED`.

## Provenance vocabulary

- `OFFICIAL` — explicitly stated by the authoritative source being studied.
- `OBSERVED` — directly visible in an artifact, behavior or implementation.
- `INFERRED` — reasoned conclusion derived from evidence.
- `INSPIRED` — our design direction influenced by external evidence but not claimed by that source.
- `GENERATED` — artifact or rule synthesized by us.

When uncertainty matters, add `confidence: high | medium | low` and exact source references.

## Relationship with `ux-laws`

`ux-laws/` and `web-design/` are complementary:

```text
UX laws                         Web design
--------                        ----------
human cognition                 visual language
attention                       visual hierarchy
choice / interaction            components
mental models                   design grammar
memory / load                   information density
                                tokens / implementation
             \                  /
              \                /
               product UI system
```

A visually consistent design can still be unusable; an interaction that follows cognitive principles can still lack coherent visual implementation. Product work should use both domains where applicable.

## Evolution model

```text
MK0  Mine & frame sources, concepts, provenance and boundaries
MK1  Normalize visual/design knowledge and taxonomy
MK2  Operationalize into enforceable design rules and schemas
MK3  Integrate tokens, components, states, responsive, a11y and motion
MK4  Automate generation, retrieval and validation workflows
MK5+ Certify, compare, regress and empirically refine
```

MK numbers represent maturity, not arbitrary releases.
