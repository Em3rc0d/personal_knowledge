# Semantic Design-System Contract — Draft

Status: `MK0 DRAFT / NOT CERTIFIED`

This is our initial normalized contract, inspired in part by RICOUI's `DESIGN.md` approach but expanded for production website work.

## 1. Identity and direction

Define:

- product/brand purpose;
- target audience;
- visual personality;
- desired emotional qualities;
- explicitly excluded aesthetics;
- source/reference lineage.

## 2. Theme and color semantics

For each meaningful color define:

- semantic name;
- value;
- role;
- allowed contexts;
- contrast/accessibility constraint;
- light/dark behavior if applicable.

## 3. Typography

Define:

- families and fallbacks;
- display/body/mono roles;
- scale;
- line height;
- tracking;
- responsive transformations;
- content-density constraints.

## 4. Spacing and layout

Define:

- spacing scale;
- container behavior;
- grids;
- section rhythm;
- alignment rules;
- density modes where applicable.

## 5. Surfaces and depth

Define:

- surface hierarchy;
- borders;
- shadows/elevation;
- radius strategy;
- overlays;
- depth anti-patterns.

## 6. Component contracts

Each important component should eventually specify:

```text
purpose
variants
states
content constraints
interaction
responsive behavior
a11y requirements
motion
allowed tokens
do / don't
```

## 7. Responsive behavior

Responsive rules are first-class, not cleanup after desktop design.

Document:

- breakpoints or fluid thresholds;
- priority changes;
- stacking/reordering;
- navigation transformations;
- typography scaling;
- component substitutions;
- overflow behavior;
- touch target requirements.

## 8. Accessibility

Design-level constraints may include:

- contrast targets;
- focus visibility;
- keyboard reachability expectations;
- semantic hierarchy;
- touch target sizing;
- error-state communication;
- reduced-motion treatment;
- non-color-only status communication.

Implementation remains responsible for technical conformance; a design document cannot prove accessibility alone.

## 9. Motion

For meaningful motion define:

```text
purpose
trigger
duration/easing class
state transition
interruptibility
reduced-motion fallback
```

## 10. Imagery and iconography

Define:

- photography/illustration role;
- framing;
- crop behavior;
- density;
- icon style;
- decorative vs informative distinction;
- alt-text/content responsibilities where relevant.

## 11. Do / Don't / anti-patterns

Rules must be actionable enough that an implementation can be reviewed against them.

## 12. Agent consumption

AI-agent guidance may contain examples and implementation prompts, but must derive from this semantic contract.

## 13. Provenance

Any rule materially influenced by external evidence should preserve source lineage at the appropriate granularity.

## 14. Verification hooks

The contract should identify what can later be tested by:

- schema validation;
- static linting;
- component tests;
- accessibility tests;
- viewport screenshots;
- visual regression;
- human design review.

## 15. Implementation and runtime boundary

Status: `MK0 DRAFT / GENERATED`, pressure-tested by `SRC-TORQUE-STATIC-V2`.

The semantic design contract must not silently require a specific frontend runtime unless a product requirement makes that runtime part of the contract.

Distinguish:

    component contract
    ≠ authoring framework
    ≠ delivery runtime

Document when relevant:

- whether a component requires client-side state;
- whether the requirement can use a native browser primitive;
- whether JavaScript is progressive enhancement or core functionality;
- authoring-only dependencies versus shipped dependencies;
- expected behavior when JavaScript is unavailable or reduced;
- runtime/performance budget attributable to the component;
- the product requirement that justifies framework/runtime complexity.

Candidate layering:

    tokens
      → primitives
      → variants
      → domain components
      → compositions

Framework/library components may inform the contract, but the product must own its semantic roles, visual identity and acceptance criteria.
