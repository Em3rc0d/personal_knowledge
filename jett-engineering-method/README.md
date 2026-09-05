# Jett Engineering Method

Jett Engineering Method (JEM) es el operating model interno para llevar un problema desde incertidumbre hasta conocimiento, software o decisiones que podamos defender con evidencia.

> **Jett reviews; agents execute.**

JEM no es un estándar externo ni una certificación de terceros. Es conocimiento interno consolidado a partir de práctica colaborativa, revisión de proyectos y decisiones repetidas. Su autoridad dentro de `personal_knowledge` proviene de haber sido explícitamente adoptado como método de trabajo.

## Purpose

JEM intenta evitar dos fallos recurrentes:

1. construir antes de comprender;
2. declarar terminado algo que todavía no puede demostrarse.

El método conecta:

```text
problem
  ↓
recovery / research
  ↓
brainstorming
  ↓
design
  ↓
architecture
  ↓
plan
  ↓
build
  ↓
test
  ↓
prove
  ↓
release / promote
  ↓
observe
  ↓
learn
  ↓
iterate / scale / hold / kill
```

En un dominio de conocimiento, `release / promote` normalmente significa que el conocimiento superó su gate y puede integrarse en `main`.

## Core distinction

JEM mantiene separadas cinco clases de verdad:

### Product Truth
Qué debería hacer o permitir el producto/sistema.

### Implementation Truth
Qué existe realmente en código, artefactos o procesos.

### Evidence Truth
Qué podemos demostrar con evidencia reproducible y trazable.

### Operational Truth
Qué continúa funcionando repetidamente bajo condiciones realistas.

### Commercial Truth
Qué crea suficiente valor como para justificar el coste y complejidad de construirlo u operarlo.

Una clase de verdad no implica automáticamente las demás.

## Knowledge lifecycle

Dentro de `personal_knowledge`, JEM convive con el pipeline epistemológico del monorepo:

```text
SOURCE
  ↓
MINING SITE
  ↓
QUARRY
  ↓
BRAINSTORM
  ↓
DESIGN
  ↓
ARCHITECTURE
  ↓
PLAN
  ↓
BUILD
  ↓
TEST
  ↓
PROVE
  ↓
MK GATE
  ↓
MAIN / CANON
```

Este pipeline expresa madurez del conocimiento; no obliga a crear burocracia o documentos vacíos en cada fase.

## Phase contracts

### 1. PROBLEM

Preguntas mínimas:

```text
What is actually wrong?
Why does it matter?
What do we know?
What do we not know?
Who or what is affected?
What evidence indicates the problem exists?
What capability or decision should this work enable?
```

Regla: **problem before solution**.

### 2. RECOVER

Se usa cuando ya existe historia, implementación o conocimiento previo.

```text
inspect current state
  ↓
recover decisions and history
  ↓
separate AS-IS / TO-BE / DEPRECATED / UNKNOWN
  ↓
identify contradictions
  ↓
establish baseline
```

Regla: **recovery before construction**. No reescribir silenciosamente la historia.

### 3. BRAINSTORM

Espacio para hipótesis, ideas, alternativas y direcciones abiertas.

Regla: **brainstorming is not canon**.

### 4. DESIGN

Define cómo debería funcionar, comportarse, entenderse o sentirse el sistema/conocimiento. Puede incluir journeys, semántica, estados, UX, reglas de interacción y modelos conceptuales.

### 5. ARCHITECTURE

Define estructura y relaciones: boundaries, responsabilidades, ownership, contratos, modelos, dependencias, seguridad, persistence, provenance y failure model.

Regla: **architecture should reduce complexity, not merely organize it**.

### 6. PLAN

Convierte decisiones suficientemente cerradas en slices ejecutables con scope, non-scope, dependencias, riesgos, entregables, acceptance criteria y evidencia requerida.

### 7. BUILD

Produce artefactos operacionales: código, schemas, templates, datasets, rulesets, scripts, decision matrices o componentes reutilizables.

Regla: **BUILD is not the beginning**.

### 8. TEST

Comprueba afirmaciones mediante evidencia apropiada: inspección, static validation, unit, integration, E2E, provider real, physical/field evidence, negative cases, regression y fail-closed testing.

Regla: **evidence strength must be proportional to risk and claim strength**.

### 9. PROVE

Responde: **¿qué podemos afirmar legítimamente ahora?**

```text
CLAIM
  ↓
EVIDENCE
  ↓
SOURCE
  ↓
PROVENANCE
  ↓
VERIFICATION
```

Estados recomendados:

```text
PASS
PASS WITH LIMITATIONS
FAIL
UNKNOWN
BLOCKED
INCONCLUSIVE
```

`looks good`, `should work` o un agente diciendo `DONE` no constituyen certificación.

### 10. RELEASE / PROMOTE

Un release no equivale automáticamente a merge o deploy. El boundary depende del claim. Puede requerir commit exacto, CI, artifact, deployment, migration, security proof, real provider, browser evidence, physical evidence o rollback capability.

En este monorepo, promoción a canon implica revisión y merge a `main`.

### 11. OBSERVE

Después de release/promoción se observa realidad: fallos, uso, performance, contradicciones nuevas, feedback, cambios de fuentes y supuestos obsoletos.

Canon no significa eternamente verdadero; significa mejor conocimiento consolidado disponible en ese momento.

### 12. LEARN

```text
observation
  ↓
finding
  ↓
analysis
  ↓
decision
  ↓
case / regression / updated knowledge
```

El objetivo es compound engineering: un problema bien resuelto mejora proyectos futuros.

### 13. ITERATE / SCALE / HOLD / KILL

Decisiones válidas después de aprender:

- `ITERATE`: mejorar.
- `SCALE`: ampliar cobertura/inversión.
- `HOLD`: preservar sin consumir trabajo activo.
- `KILL`: retirar hipótesis, enfoque o producto deliberadamente.

Regla: **kill decisions are also engineering decisions**.

## Permanent gates

JEM utiliza gates alrededor de las fases, no fases burocráticas adicionales.

### Issue Contract

Un issue serio debería incluir:

```text
Problem
Desired outcome
Scope
Non-scope
Acceptance criteria
Evidence required
Dependencies
Risks
```

### Handoff

Debe responder:

```text
What was requested?
What changed?
What evidence exists?
What assumptions were made?
What remains unresolved?
What should the reviewer inspect?
```

### Review Gate

Salida esperada:

```text
PASS
PASS WITH LIMITATIONS
FAIL
UNKNOWN
```

### Record a Case

```text
failure
  ↓
reproduction
  ↓
diagnosis
  ↓
fix / decision
  ↓
verification
  ↓
regression protection
  ↓
reusable case
```

### Quality Baseline

Debe ser proporcional al riesgo y consecuencias del dominio.

### Test Strength

No todos los tests tienen el mismo peso probatorio. La prueba elegida debe poder soportar el claim concreto.

## Contextual gates

Cuando aplique:

- `Trail Decisions`: preservar contexto, alternativas, decisión y consecuencias.
- `Solution Gate`: no construir mientras queden decisiones fundamentales abiertas.
- `Resilience Audit`: demostrar comportamiento ante fallos relevantes.
- `Performance Proof`: exigir benchmarks solo cuando performance sea parte del claim.
- `Signature Repro`: preservar una reproducción estable para fallos críticos.

## Claim discipline

Nunca promover silenciosamente:

```text
implemented          → production-ready
test passed          → physically certified
repository exists    → product finished
UI exists            → workflow operational
public repository    → permission to publish
inference            → fact
prototype            → production system
agent says DONE      → verified completion
```

Cuando algo no se sabe, `UNKNOWN` permanece `UNKNOWN`.

## Provenance

Taxonomía base del monorepo:

- `OFFICIAL`: autoridad primaria relevante.
- `OBSERVED`: comportamiento observado directamente.
- `INFERRED`: conclusión razonada desde evidencia incompleta.
- `INSPIRED`: patrón derivado de una referencia, sin afirmar equivalencia.
- `GENERATED`: contenido producido por nosotros o por agentes/IA.

Nunca promover `INFERRED → OFFICIAL` o `GENERATED → VERIFIED` sin nueva evidencia.

## Constitutional rules

1. Evidence over narrative.
2. No claim without evidence; no evidence without provenance.
3. Facts, observations, inference, assumptions and plans are different things.
4. Recovery before construction.
5. Brainstorming is not canon.
6. Serious knowledge belongs in repositories.
7. Jett reviews; agents execute.
8. Problem → Brainstorm → Design → Architecture → Plan → Build → Test → Prove.
9. Gates surround the process; they do not replace it.
10. Engineering must be proportional to necessity and risk.
11. Choose the problem before the technology.
12. Preserve reversibility and history.
13. Security is architecture.
14. Provenance is architecture.
15. Never inflate ownership, maturity or evidence.
16. Donor/reference ≠ copy.
17. Premium quality ≠ unnecessary complexity.
18. Physical claims require physical evidence.
19. Evidence strength is proportional to risk.
20. BUILD is not the beginning.
21. BUILD is not the end.
22. Working once ≠ working reliably.
23. A project without feedback remains an experiment.
24. Limit work in progress.
25. Not every good idea deserves a roadmap.
26. Architecture should reduce complexity.
27. Process exists to improve shipped and usable outcomes.
28. UNKNOWN remains UNKNOWN.
29. Claims require explicit boundaries.
30. Kill decisions are valid engineering decisions.

## Relationship with other domains

JEM answers:

> **How do we responsibly take a problem from uncertainty to proven knowledge/software?**

HESTIA, when documented in this monorepo, answers a different question:

> **What level of solution makes commercial sense?**

The Knowledge Environment answers:

> **How do we preserve and evolve what we learned?**

Product/domain knowledge answers:

> **What do we currently know about this specific problem space?**

These layers are related but must not be collapsed into one concept.

## Branch rule

New knowledge is developed on ephemeral branches:

```text
knowledge/<domain>-<mk>-<purpose>
```

`main` is not where we think. `main` is where knowledge remains after surviving research, reasoning, evidence, review and validation.

## Current maturity

See [`STATUS.md`](./STATUS.md) and [`mk/README.md`](./mk/README.md).
