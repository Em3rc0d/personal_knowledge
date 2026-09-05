# RICOUI Quarry — DESIGN.md Model

Source: `SRC-RICOUI`, primarily RICOUI project documentation and user tutorial.

## Q-RICOUI-001 — Canonical readable source

**Classification:** `OFFICIAL`

RICOUI documents `DESIGN.md` as the canonical source. Structured controls, previews and exports derive from it.

### Why this matters

Multiple editable representations of the same design system create drift. A canonical readable source gives humans and tools one location from which downstream artifacts can be regenerated.

### Candidate domain rule

`INFERRED → INSPIRED`

> A substantial website should define one canonical semantic design contract and treat machine-oriented files as generated or explicitly synchronized artifacts.

## Q-RICOUI-002 — Semantics beyond tokens

**Classification:** `INFERRED`

A token such as:

```text
--radius-lg: 12px
```

preserves a value but not necessarily intent. A semantic document can also express:

- role;
- allowed usage;
- disallowed usage;
- visual hierarchy;
- component behavior;
- imagery treatment;
- layout rhythm;
- do/don't constraints.

### Candidate rule

Do not reduce a design system to token values alone.

## Q-RICOUI-003 — Human + machine readability

**Classification:** `INFERRED`

Markdown provides a useful interchange surface because it can be reviewed in Git, read directly by humans, parsed by tools and supplied as context to AI agents.

This does **not** establish Markdown as the only valid design-system representation. Our domain should preserve the semantic contract, not hard-code a single serialization forever.

## Q-RICOUI-004 — Agent prompt guidance

RICOUI-related templates include an Agent Prompt Guide. This suggests a design system can expose guidance specifically for generative tooling.

Our stronger interpretation is:

```text
agent guidance
  must derive from
semantic design rules
  not replace them
```

Agent prompts are consumers of the design system, not the canonical design system itself.
