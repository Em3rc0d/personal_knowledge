# Web Design — Design Layer

This layer turns mined evidence into explicit design principles and semantic contracts.

## Target model

```text
visual primitives
      +
visual grammar
      +
interaction semantics
      +
responsive / a11y / motion constraints
      =
portable design system
```

## Required distinction

```text
DESIGN TOKENS ≠ DESIGN RULES
```

Tokens encode values. Rules encode intent, applicability and constraints.

Example:

```text
Token:
  radius-lg = 12px

Rule:
  Use large radius on elevated product surfaces.
  Do not apply it automatically to navigation or dense table cells.
```

The semantic layer exists so a designer, developer and AI agent can converge on the same intended behavior.
