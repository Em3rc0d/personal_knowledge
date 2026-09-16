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
| continuar MK1 | [`mk/MK1/README.md`](./mk/MK1/README.md) |

## Cómo está diseñado el dominio

El repositorio conserva dos vistas simultáneas:

```text
¿QUÉ SABEMOS HOY?                    ¿CÓMO LLEGAMOS A SABERLO?

STATUS.md                            mining-site/
systems/<system>/                    quarries/
mk/ canon vigente                    MK pressure tests / gates
```

La estructura no está organizada por popularidad de frameworks sino por **rol epistemológico**.

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

Contrato completo: [`REPOSITORY_CONTRACT.md`](./REPOSITORY_CONTRACT.md).

## Propósito

Este dominio estudia cómo convertir un modelo probabilístico en un sistema capaz de ejecutar trabajo de manera controlada mediante **runtime, estado, contexto, herramientas, políticas, persistencia, observabilidad y evaluación**.

La unidad de análisis no es `LangGraph`, `LangChain`, `CrewAI`, `AutoGen`, Strands, MCP ni un proveedor concreto. Es el **sistema agentic completo** y sus invariantes.

## Alcance

Incluye:

- control authority y diferencias workflow/agent;
- agent loop / harness / runtime;
- planificación, routing y orchestration;
- herramientas y Agent-Computer Interface (ACI);
- protocolos como MCP/A2A tratados por revisión/rol/transport/auth, no como arquitectura completa;
- state, checkpoint, context, memory y persistence;
- concurrency/writer/conflict semantics;
- retries, termination, budgets y enforcement boundaries;
- Human-in-the-Loop (HITL), enforcement owner y approval boundaries;
- side effects, idempotencia y auditabilidad;
- evaluación de outcome, trajectory/trace y regresiones;
- seguridad, permissions, sandboxing y blast radius;
- multi-agent coordination, admission hypotheses y failure modes;
- reproducibilidad, version drift y lifecycle de agent systems.

Fuera de alcance por defecto:

- coleccionar prompts o notebooks sin extraer principios verificables;
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

## Principios de ingeniería actualmente seguros como working knowledge

Estos principios sobrevivieron MK0/MK1 como reglas de trabajo de alta confianza, aunque sus contratos operacionales completos pertenecen a MK2+.

1. **Use the simplest sufficient architecture.** Más autonomía/topología requiere una necesidad demostrable.
2. **Policy belongs in enforceable code.** Una regla crítica no puede depender exclusivamente del prompt.
3. **Every loop is bounded.** Budget value y enforcement boundary son contratos distintos.
4. **Tools are typed contracts.** Schema no equivale a permission ni a safety.
5. **Capability composition determines blast radius.** El riesgo emerge de combinaciones alcanzables.
6. **Side effects cross a policy boundary.** Mutación y data egress requieren clasificación explícita.
7. **Modified actions are new actions.** Cambiar argumentos invalida autorización/validación cuando el binding importa.
8. **Context is curated state.** No es sinónimo de chat history.
9. **Persistence is not memory.** Durabilidad y semántica de recuerdo son contratos distintos.
10. **Durability is not concurrency safety.** Writer/merge/locking semantics deben registrarse aparte.
11. **Runtime DONE != task DONE.** Stop reason no demuestra outcome externo.
12. **Outcome and trajectory are separate evaluation surfaces.** Ambas pueden fallar independientemente.
13. **Stochastic reliability requires repeated evidence.** Un único run no certifica estabilidad.
14. **Reflection requires verifier/feedback for improvement claims.** Autocrítica no equivale a aprendizaje.
15. **Multi-agent must earn its complexity.** Topología y beneficio medido son campos distintos.
16. **Least privilege is an agent invariant.** Shell/red/filesystem/secrets mutantes necesitan containment proporcional.
17. **Frameworks are adapters, not truth.** La taxonomía debe sobrevivir cambios de SDK/proveedor.
18. **Protocol compatibility is a vector.** Revision/lifecycle/transport/auth/extensions/cancellation/evidence importan.
19. **Protocol interoperability != authorization.** Capability discovery no concede permiso de ejecución.
20. **Production readiness is an evidence vector.** Un framework production-capable no certifica la aplicación.

## Fuentes y provenance

El primer mining site fue `NirDiamant/GenAI_Agents`, fijado en:

```text
repository: NirDiamant/GenAI_Agents
snapshot:   4c95ae14cc2462c442b5c064cccd74430d02bc46
observed:   2026-09-07
```

Se utiliza como **catálogo pedagógico/cantera de patrones**, no como especificación normativa.

Fuentes complementarias ya incorporadas incluyen:

- `Agent_Memory_Techniques@b7f7240e...` para memory;
- `agents-towards-production@141b0679...` para production concerns;
- MCP `2026-07-28` como contrato protocolar vigente del pass actual;
- Strands Agents, LangGraph y OpenAI Agents SDK como presión cross-runtime sobre MK1.

Registry: [`mining-site/SOURCES.md`](./mining-site/SOURCES.md).

### Boundary legal

`GenAI_Agents` usa licencia custom de uso no comercial con atribución/reserva comercial. Por eso este dominio:

- no copia notebooks/implementaciones como canon;
- registra metadata y observaciones;
- redacta principios independientemente;
- mantiene provenance/snapshot;
- contrasta con fuentes oficiales y literatura independiente.

## MK1 — estado real

Schema actual:

```text
mk1-draft-2026-09-16.1
```

No usamos un único `agent_type`. Clasificamos:

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

Materializado actualmente:

```text
REC-001  minimal while-loop
REC-002  HITL approval
REC-013  MCP revision drift
REC-014  Strands Agents
```

Registry: [`mk/MK1/records/README.md`](./mk/MK1/records/README.md).

### Hallazgos de Strands ya promovidos

Strands tensionó el schema y reveló:

```text
concurrency semantics
budget enforcement boundary
intervention enforcement owner/boundary
```

No se promovieron por Strands solo. LangGraph + OpenAI Agents SDK confirmaron esas diferencias y quedaron incorporadas en `mk1-draft-2026-09-16.1`.

Strands ↔ MCP `2026-07-28` también pasó a **SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED**, sin convertir interoperabilidad en autorización ni cancelación en rollback.

Vista consolidada: [`systems/strands/`](./systems/strands/).

## Qué falta para cerrar MK1

```text
generated-code/browser record      OPEN
data-egress record                  OPEN
dedicated memory record             OPEN
eval/critic pressure                OPEN
A2A reproducibility receipt         OPEN
multi-agent baseline                OPEN
schema freeze audit                 BLOCKED BY ABOVE
MK1 CLOSURE.md                      NOT YET
```

Plan exacto: [`mk/MK1/CLOSURE_PLAN.md`](./mk/MK1/CLOSURE_PLAN.md).  
Roadmap del dominio: [`ROADMAP.md`](./ROADMAP.md).

## MK2 handoff

MK2 tiene diseño sembrado, pero sigue bloqueado.

No consume raw quarries como policy. Recibirá únicamente un paquete MK1 cerrado/frozen según:

[`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md).

## Flujo de madurez

```text
MK0  Mine & Frame                    ✅ CLOSED
 ↓
MK1  Normalize & Classify            🟡 CURRENT
 ↓
MK2  Operationalize contracts/tests  🔒 BLOCKED / DESIGN SEEDED
 ↓
MK3  Integrate with Jett Engineering Method + domains
 ↓
MK4  Automate validators / eval harnesses
 ↓
MK5+ Certify against independent systems/counterexamples
```

`STATUS.md` es el tablero canónico; `ROADMAP.md` es la secuencia de ejecución; `REPOSITORY_CONTRACT.md` define la autoridad de cada capa.
