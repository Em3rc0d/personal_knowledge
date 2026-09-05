# Web Design — Test

The design system must eventually be testable at multiple layers.

## Planned test families

### Provenance tests

- no `INFERRED` claim masquerades as `OFFICIAL`;
- source IDs resolve;
- dated observations retain timestamps where required.

### Semantic tests

- required design-contract sections exist;
- token roles are defined;
- contradictory rules are detected or explicitly scoped.

### Component tests

- required states exist;
- variant/state combinations are valid;
- disabled/loading/focus semantics are represented.

### Responsive tests

- target viewport classes render;
- no accidental overflow;
- documented transformations occur.

### Accessibility tests

- contrast/focus/semantic requirements can be linked to implementation evidence;
- reduced-motion expectations are honored where applicable.

### Visual regression

- canonical viewport baselines;
- component fixtures;
- controlled screenshot diffs;
- explicit review for intentional change.

## MK0 test gate

For MK0 the immediate test is epistemic: source claims, observations and our inferences must remain visibly separated.
