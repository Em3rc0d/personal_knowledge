# Agent Engineering

Dominio de conocimiento para diseñar, construir y validar sistemas agentic/LLM con criterios de ingeniería, no por afinidad con un framework.

## Estado actual

```text
MK0  Mine & Frame          ✅ CLOSED
MK1  Normalize & Classify  🟡 IN PROGRESS
MK2  Operationalize        🔒 BLOCKED / DESIGN SEEDED
```

## Empieza aquí

| Necesidad | Archivo |
|---|---|
| entender el dominio | [`README.md`](./README.md) |
| ver estado vivo | [`STATUS.md`](./STATUS.md) |
| saber qué ejecutar después | [`ROADMAP.md`](./ROADMAP.md) |
| entender qué archivo manda sobre qué | [`REPOSITORY_CONTRACT.md`](./REPOSITORY_CONTRACT.md) |
| navegar el knowledge graph | [`KNOWLEDGE_MAP.md`](./KNOWLEDGE_MAP.md) |
| dar contexto mínimo a un LLM/agente | [`LLM_CONTEXT.md`](./LLM_CONTEXT.md) |
| ver sistemas concretos actuales | [`systems/`](./systems/) |
| estudiar Strands actualmente | [`systems/strands/README.md`](./systems/strands/README.md) |
| continuar/cerrar MK1 | [`mk/MK1/README.md`](./mk/MK1/README.md) |

## Cómo está diseñado el dominio

```text
¿QUÉ SABEMOS HOY?                    ¿CÓMO LLEGAMOS A SABERLO?

STATUS.md                            mining-site/
systems/<system>/                    quarries/
mk/ canon vigente                    MK pressure tests / receipts
```

La estructura se organiza por **rol epistemológico**, no por popularidad de frameworks.

```text
agent-engineering/
│
├── README.md                 orientación humana
├── STATUS.md                 estado canónico actual
├── ROADMAP.md                secuencia de ejecución vigente
├── REPOSITORY_CONTRACT.md    autoridad / lifecycle / conflict rules
├── KNOWLEDGE_MAP.md          mapa humano
├── LLM_CONTEXT.md            router para máquinas
│
├── systems/                  síntesis actual por sistema
├── mk/                       madurez / canon normalizado
├── architecture/             artefactos cross-system
├── quarries/                 evidencia procesada / historia
└── mining-site/              receipts / snapshots / provenance
```

Contrato: [`REPOSITORY_CONTRACT.md`](./REPOSITORY_CONTRACT.md).

## Propósito

Este dominio estudia cómo convertir un modelo probabilístico en un sistema capaz de ejecutar trabajo de manera controlada mediante **runtime, estado, contexto, herramientas, políticas, persistencia, observabilidad y evaluación**.

La unidad de análisis no es un framework concreto. Es el **sistema agentic completo** y sus invariantes.

## Alcance

Incluye:

- control authority y workflow/agent;
- agent loop / harness / runtime;
- routing/orchestration;
- tools / ACI;
- protocolos revision-aware como MCP/A2A;
- state/checkpoint/context/memory/persistence;
- concurrency/writer/conflict semantics;
- retries, termination, budgets y enforcement boundaries;
- HITL, enforcement owner y approval binding;
- side effects, data egress, idempotencia y receipts;
- outcome/trajectory evaluation;
- seguridad, permissions, sandboxing y blast radius;
- multi-agent admission hypotheses, coordination/failure modes y baseline evidence;
- reproducibilidad y version drift.

Fuera de alcance por defecto:

- coleccionar prompts/notebooks sin extraer principios verificables;
- convertir marketing o nombres de frameworks en taxonomía;
- asumir que `multi-agent`, `reflection`, `memory` o `self-improving` implican mejora demostrada;
- promover código de terceros como plantilla canónica sin validar licencia, reproducibilidad y evidencia.

## Modelo conceptual

```text
                    ┌───────────────┐
request / objective │    POLICY     │
        ───────────►│ risk / scope  │
                    └──────┬────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ AGENT HARNESS /  │
                 │ RUNTIME          │
                 │ loop + budgets   │
                 └───┬─────────┬────┘
                     │         │
            context  │         │ actions
                     ▼         ▼
              ┌──────────┐  ┌───────────┐
              │ MODEL    │  │ TOOLS /   │
              │          │  │ ENV       │
              └────┬─────┘  └─────┬─────┘
                   │              │
                   └──────┬───────┘
                          ▼
                  ┌──────────────┐
                  │ STATE /      │
                  │ CHECKPOINTS  │
                  └──────┬───────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       observability          evaluator / gate
       traces / receipts      outcome + trajectory
```

El modelo puede proponer; el runtime/policy boundary decide qué está permitido ejecutar.

## Working principles actuales

1. **Use the simplest sufficient architecture.** Más autonomía/topología exige una necesidad demostrable.
2. **Policy belongs in enforceable code.** Una regla crítica no puede depender solo del prompt.
3. **Every loop is bounded.** Budget value y enforcement boundary son contratos distintos.
4. **Tools are typed interfaces, not permission proofs.**
5. **Capability composition determines blast radius.**
6. **Side effects and data egress cross policy boundaries.**
7. **Modified actions are new actions** cuando approval binding importa.
8. **Context is curated state**, no sinónimo de chat history.
9. **Persistence is not memory.**
10. **Durability is not concurrency safety.**
11. **Runtime DONE != task DONE.**
12. **Outcome and trajectory are separate evaluation surfaces.**
13. **Stochastic reliability requires repeated evidence.**
14. **Reflection != demonstrated persistent improvement.**
15. **Multi-agent must earn its complexity.** Topology y benefit son campos distintos.
16. **Least privilege is an agent invariant.**
17. **Frameworks are adapters, not truth.**
18. **Protocol compatibility is a vector**, no un booleano.
19. **Protocol interoperability != authorization.**
20. **Production readiness is an evidence vector.**

Los contratos operacionales completos de estas ideas pertenecen a MK2+.

## Fuentes y provenance

El primer mining site fue `NirDiamant/GenAI_Agents` fijado en:

```text
snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
observed: 2026-09-07
```

Es cantera pedagógica/pattern source, no especificación normativa.

El dominio incorporó además fuentes especializadas para memory/production, MCP `2026-07-28`, A2A `1.0.x`, Strands, LangGraph, OpenAI Agents SDK y literatura científica relevante.

Registry: [`mining-site/SOURCES.md`](./mining-site/SOURCES.md).

## MK1 — estado real

Schema activo:

```text
mk1-draft-2026-09-16.1
```

Clasificamos dimensiones ortogonales:

```text
control authority
capabilities + composition
side effects
state / checkpoints / persistence / concurrency
memory lifecycle
human control + enforcement owner/boundary
errors / retries
termination + budget enforcement/cancellation
evaluation
protocol revision
security boundary
reproducibility evidence
UNKNOWNs
```

### Representative records

```text
11 MATERIALIZED / QUALIFIED
REC-001 REC-002 REC-003 REC-004 REC-007 REC-008
REC-009 REC-010 REC-011 REC-013 REC-014

2 COVERED_BY
REC-005 → REC-004 + REC-003
REC-006 → REC-002 + REC-007

1 OPEN / BLOCKING
REC-012 multi-agent baseline/admission evidence
```

Registry: [`mk/MK1/records/README.md`](./mk/MK1/records/README.md).

### Cross-runtime promotions already closed

Strands surfaced, y LangGraph + OpenAI Agents SDK confirmaron:

```text
concurrency semantics        → state
budget enforcement boundary  → termination
intervention owner/boundary  → human_control
```

### Protocol state

```text
MCP 2026-07-28              SUPPORTED / QUALIFIED
A2A classification shape    PASS / QUALIFIED
Strands A2A 0.3 path        SUPPORTED / QUALIFIED
Strands A2A 1.0 compat      NOT ESTABLISHED
```

A2A `0.3 → 1.0` se conserva como version-drift explícito; no se transforma en un falso PASS de compatibilidad actual.

Vista Strands: [`systems/strands/`](./systems/strands/).  
A2A receipt: [`quarries/strands-a2a-version-drift.md`](./quarries/strands-a2a-version-drift.md).

## Qué falta para cerrar MK1

El trabajo de orden documental y la mayor parte de la clasificación representativa ya están cerrados. La ruta real restante es:

```text
REC-012 multi-agent baseline        🟡 OPEN / BLOCKING
        ↓
final UNKNOWN reconciliation
        ↓
cross-dimension + overlap audit
        ↓
schema freeze decision
        ↓
MK1 CLOSURE.md
        ↓
MK2 handoff activation
```

Plan exacto: [`mk/MK1/CLOSURE_PLAN.md`](./mk/MK1/CLOSURE_PLAN.md).  
Roadmap: [`ROADMAP.md`](./ROADMAP.md).

## MK2 handoff

MK2 tiene diseño sembrado, pero sigue bloqueado.

No consume raw quarries como policy. Recibirá únicamente un paquete MK1 cerrado/frozen según [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md).

## Flujo de madurez

```text
MK0  Mine & Frame                    ✅ CLOSED
 ↓
MK1  Normalize & Classify            🟡 CURRENT
 ↓
MK2  Operationalize contracts/tests  🔒 BLOCKED / DESIGN SEEDED
 ↓
MK3  Integrate
 ↓
MK4  Automate
 ↓
MK5+ Certify / Refine
```

`STATUS.md` es el tablero canónico; `ROADMAP.md` la secuencia de ejecución; `REPOSITORY_CONTRACT.md` define autoridad y lifecycle de cada capa.
