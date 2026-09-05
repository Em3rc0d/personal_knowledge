# OpenShip Knowledge Domain

Dominio de conocimiento dedicado al estudio técnico de **OpenShip** (`oblien/openship`) como plataforma open-source/self-hostable de deployment y control plane.

Este dominio **no es un fork ni una copia de implementación**. Su objetivo es extraer arquitectura, invariantes, decisiones, trade-offs, patrones y anti-patrones reutilizables para sistemas de infraestructura, plataformas developer-first y productos operables por humanos, CLI y agentes de IA.

## Snapshot estudiado

```text
UPSTREAM                 oblien/openship
UPSTREAM VERSION         v0.7.0
REFERENCE COMMIT         6510d3fd942473e54b6a41c2b1f99e0f2a483fd6
REFERENCE DATE           2026-09-03
LICENSE                  Apache-2.0
PRIMARY LANGUAGE         TypeScript
```

El upstream evoluciona rápidamente. Toda conclusión debe distinguir entre el **snapshot observado** y el estado futuro de `main`.

## Mission

Convertir el estudio de OpenShip en un sistema de conocimiento portable:

```text
source artifact
  → observed mechanism
  → trust / failure boundary
  → architectural rationale
  → reusable pattern
  → applicability constraints
  → verification rule
```

## Core model observado

OpenShip se comporta como un **control plane unificado** que puede ser operado desde distintas superficies y que compone infraestructura mediante adapters:

```text
Desktop / Dashboard / CLI / REST / MCP
                  │
                  ▼
               API / Control Plane
                  │
        ┌─────────┼─────────┐
        │         │         │
     Runtime    Routing     SSL
        │         │         │
        └─────────┼─────────┘
                  │
             System / Executor
                  │
       local host / SSH / cloud API
```

El valor arquitectónico principal no es "hacer Docker fácil". Es **normalizar múltiples targets y múltiples interfaces detrás de un mismo control plane y de contratos comunes**.

## Evolution model

```text
MK0  Mine & frame
 ↓
MK1  Normalize patterns & boundaries
 ↓
MK2  Operationalize reusable rules
 ↓
MK3  Integrate into platform architecture templates
 ↓
MK4  Agent/control-plane safety model
 ↓
MK5  Automated architecture/security/deployment checks
 ↓
MK6+ Empirical validation & certification
```

## Workspace structure

```text
openship/
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
│   ├── architecture/
│   ├── deployment-engine/
│   ├── runtimes/
│   ├── operations/
│   ├── edge/
│   ├── security/
│   ├── mcp/
│   └── ci-cd/
└── mk/
    └── MK0/
```

## Provenance vocabulary

- `OFFICIAL`: claim explícito del upstream/documentación.
- `OBSERVED`: comportamiento o estructura observado directamente en código, workflows, issues o artefactos.
- `INFERRED`: conclusión razonada a partir de evidencia.
- `INSPIRED`: dirección de diseño influida por OpenShip, sin atribuirla al proyecto.
- `GENERATED`: síntesis o artefacto propio.

Cuando importe, añadir `confidence: high | medium | low`.

## Boundaries

1. No asumir que documentación vieja representa el runtime actual.
2. No convertir decisiones específicas de OpenShip en reglas universales sin describir contexto.
3. No certificar madurez operacional únicamente por claims del README.
4. Issues y fixes recientes son evidencia de comportamiento observado, no necesariamente estado permanente.
5. Respetar Apache-2.0 y evitar copiar grandes bloques de código; priorizar síntesis y referencias.

## North-star insight

`GENERATED / INSPIRED`

> Una plataforma de infraestructura gana valor cuando humanos, automatización y agentes pueden operar el mismo modelo de sistema sin obtener acceso directo e indiscriminado a la infraestructura subyacente.
