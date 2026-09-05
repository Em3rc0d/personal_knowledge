# RICOUI — Mining Site Record

```text
SOURCE ID       SRC-RICOUI
DOMAIN          web-design
CLASS           external design-system research source
ROLE            primary MK0 seed
STATUS          mined / not authoritative for third-party brands
RETRIEVED       2026-09-05
```

## Origin

Primary surfaces:

- https://design.ricoui.com/
- https://design.ricoui.com/brands
- https://design.ricoui.com/about
- https://github.com/ricocc/ricoui-design-md
- https://github.com/ricocc/brands-design-md
- https://github.com/ricocc/rico-skills

## Why it matters

RICOUI exposes a useful bridge between human-readable design documentation and machine-consumable implementation artifacts. Its central pattern is that a readable `DESIGN.md` remains canonical while structured views, previews and exports are derived from that source.

Relevant areas:

1. semantic design specification;
2. canonical-source discipline;
3. local-first editing;
4. structured token extraction;
5. preview/inspection workflow;
6. design artifact generation;
7. brand-reference retrieval;
8. human-reviewed AI assistance;
9. delivery/release concepts;
10. design knowledge that can be consumed by AI agents.

## What RICOUI officially states

The following are recorded as `OFFICIAL` claims from RICOUI's own project documentation, not universal truths:

- RICOUI DESIGN is a local-first design-system workspace built around `DESIGN.md`.
- `DESIGN.md` is the canonical source in its document model.
- structured controls and preview derive from that source.
- `tokens.json`, CSS and ZIP exports are generated outputs rather than independent sources.
- AI changes that may modify source are presented as a reviewable diff and require explicit application.
- Brand references are read-only learning/analysis material.
- RICOUI does not claim that every derived brand value was confirmed by the original brand.
- built-in Brand-reference material is derived from getdesign.md and VoltAgent/awesome-design-md and then parsed for RICOUI's workflow.

## What we infer

The following are `INFERRED` and must not be attributed to RICOUI as direct claims:

- a semantic specification can reduce the design search space for AI agents;
- tokens alone are insufficient to preserve full design intent;
- design lineage should be carried into generated code and validation artifacts;
- a design system can be governed similarly to a software release;
- a brand/design corpus can become a retrieval layer for generating original design directions.

## Boundaries

RICOUI must not be used to justify:

- claiming a third-party brand's unofficial values as official;
- copying a brand identity without transformation;
- treating a preview fallback as a canonical brand token;
- assuming visual observations remain current indefinitely;
- omitting independent accessibility, responsive or interaction validation;
- conflating RICOUI's product architecture with this repository's architecture.

## Research posture

```text
RICOUI
  → evidence
  → quarry
  → compare with additional sources
  → normalize
  → adopt / reject / refine
  → web-design rule with lineage
```
