# Architecture

Architecture define la estructura del método y las relaciones entre problema, conocimiento, ejecución, evidencia y promoción.

## Core model

```text
Problem
  ↓
Recover / Research
  ↓
Brainstorm
  ↓
Design
  ↓
Architecture
  ↓
Plan
  ↓
Build
  ↓
Test
  ↓
Prove
  ↓
Release / Promote
  ↓
Observe
  ↓
Learn
```

Los gates rodean este flujo; no lo reemplazan.

## Boundaries

JEM no debe colapsar:

- Product Truth con Evidence Truth;
- Implementation Truth con Operational Truth;
- HESTIA con JEM;
- Quarry con Canon;
- generated output con verified evidence;
- agent execution con reviewer approval.

## Decision records

Las decisiones arquitectónicas importantes deberían preservar:

```text
context
alternatives
decision
reasoning
consequences
superseded-by
```

Regla: **architecture should reduce complexity, not merely organize it**.
