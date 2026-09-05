# Web Design — Source Registry

This registry records research sources before their content is normalized into domain knowledge.

## Provenance rule

A source entry must identify:

- source ID;
- owner/author where known;
- canonical URL;
- source type;
- why it matters;
- what claims it can support;
- limitations or attribution boundaries;
- retrieval/update date where relevant.

## Sources

### SRC-RICOUI

- **Name:** RICOUI DESIGN
- **Owner/author:** Rico / `ricocc`
- **Primary:** https://design.ricoui.com/
- **About:** https://design.ricoui.com/about
- **Repository:** https://github.com/ricocc/ricoui-design-md
- **Type:** website + open-source design-system workspace
- **Seed role:** `PRIMARY_SEED / EXTERNAL_REFERENCE`
- **Relevant topics:** `DESIGN.md`, local-first authoring, canonical source model, structured preview, tokens, CSS, Tailwind theme export, AI-assisted review, brand references, release/delivery workflow.
- **Boundary:** RICOUI is not an official source for the brands represented in its reference library. Brand material is learning/analysis material and RICOUI itself documents upstream derivation.

### SRC-RICOUI-BRANDS

- **Name:** RICOUI Brand references
- **Primary:** https://design.ricoui.com/brands
- **Supporting repository:** https://github.com/ricocc/brands-design-md
- **Type:** derived read-only reference corpus
- **Role:** visual/design grammar research corpus
- **Boundary:** values must not be promoted to official brand guidelines without independent first-party confirmation.

### SRC-RICOUI-SKILLS

- **Name:** rico-skills / rico-design-md
- **Repository:** https://github.com/ricocc/rico-skills
- **Relevant artifact:** `skills/rico-design-md/references/DESIGN-TEMPLATE.md`
- **Type:** implementation/reference material
- **Role:** evidence for the structure Rico uses to describe visual theme, tokens, components, layout, do/don't rules, imagery and agent prompts.

## Upstream attribution discovered through RICOUI

RICOUI states that built-in Brand-reference material is derived from:

- `getdesign.md`;
- `VoltAgent/awesome-design-md`;

and then secondarily parsed by RICOUI for its `DESIGN.md` workflow.

These upstreams must be mined independently before any claim is made about their exact methodology, licensing or authority.
