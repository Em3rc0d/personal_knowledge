# Agent Engineering

Dominio de conocimiento para diseñar, construir y validar sistemas agentic/LLM con criterios de ingeniería, no por afinidad con un framework.

## Estado actual

```text
MK0  Mine & Frame          ✅ CLOSED
MK1  Normalize & Classify  🟡 IN PROGRESS
MK2  Operationalize        🔒 BLOCKED / DESIGN SEEDED
```

### Empieza aquí

- **mapa humano del conocimiento:** [`KNOWLEDGE_MAP.md`](./KNOWLEDGE_MAP.md)
- **router para LLMs/agentes:** [`LLM_CONTEXT.md`](./LLM_CONTEXT.md)
- **tablero canónico de estado:** [`STATUS.md`](./STATUS.md)
- **vista actual de sistemas concretos:** [`systems/`](./systems/)
- **Strands Agents — síntesis canónica:** [`systems/strands/README.md`](./systems/strands/README.md)

### Navegación por capa

- progresión y estructura MK: [`mk/README.md`](./mk/README.md)
- MK0 evidence/framing package: [`mk/MK0/`](./mk/MK0/)
- MK1 normalization package: [`mk/MK1/`](./mk/MK1/)
- MK2 operationalization design package: [`mk/MK2/`](./mk/MK2/)
- threat model: [`architecture/THREAT_MODEL.md`](./architecture/THREAT_MODEL.md)
- source registry: [`mining-site/SOURCES.md`](./mining-site/SOURCES.md)
- processed evidence/quarries: [`quarries/`](./quarries/)

## Cómo leer este dominio

El repositorio conserva dos vistas simultáneas:

```text
¿QUÉ SABEMOS HOY?                    ¿CÓMO LLEGAMOS A SABERLO?

STATUS.md                            mining-site/
systems/<system>/                    quarries/
mk/ canon vigente                    MK pressure tests / gates
```

`systems/` es una capa de síntesis actual por framework/runtime. No reemplaza la evidencia. Un humano puede comenzar por `systems/strands/README.md`; un LLM debe comenzar por `systems/strands/LLM_CONTEXT.md`.

Los `quarries/` conservan observaciones y estados históricos, incluso cuando una deuda luego fue promovida, cerrada o calificada. Para estado actual, no deben leerse aisladamente.

## Propósito

Este dominio estudia cómo convertir un modelo probabilístico en un sistema capaz de ejecutar trabajo de manera controlada mediante **runtime, estado, contexto, herramientas, políticas, persistencia, observabilidad y evaluación**.

La unidad de análisis no es `LangGraph`, `LangChain`, `CrewAI`, `AutoGen`, Strands, MCP ni un proveedor concreto. Es el **sistema agentic completo** y sus invariantes.

## Alcance

Incluye:

- control authority y diferencias workflow/agent;
- agent loop / harness / runtime;
- planificación, routing y orchestration;
- herramientas y Agent-Computer Interface (ACI);
- MCP como contrato de interoperabilidad versionado, no como arquitectura completa;
- state, checkpoint, context, memory y persistence;
- concurrency/writer/conflict semantics;
- retries, termination, budgets y enforcement boundaries;
- Human-in-the-Loop (HITL), enforcement owner y approval boundaries;
- side effects, idempotencia y auditabilidad;
- evaluación de outcome, trajectory/trace y regresiones;
- seguridad, permissions, sandboxing y blast radius;
- multi-agent coordination y failure modes;
- reproducibilidad, version drift y lifecycle de agent systems.

Fuera de alcance por defecto:

- coleccionar prompts o notebooks sin extraer principios verificables;
- convertir marketing o nombres de frameworks en taxonomía;
- asumir que `multi-agent`, `reflection`, `memory` o `self-improving` implican mejora demostrada;
- promover código de terceros como plantilla canónica sin validar licencia, reproducibilidad y evidencia.

## Modelo conceptual

```text
                    ┌───────────────┐
request / objective │   POLICY      │
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

## Reglas candidatas heredadas de MK0

Estas reglas siguen siendo **candidatas**, no canon operacional certificado. La versión estructurada vive en [`mk/MK0/INVARIANTS.md`](./mk/MK0/INVARIANTS.md); MK1 las normaliza y MK2 deberá convertir las que sobrevivan en contratos/tests.

1. **Use the simplest sufficient architecture.** Un workflow determinista es preferible si el problema no necesita control dinámico del modelo.
2. **Policy belongs in enforceable code.** Una regla crítica no puede depender exclusivamente del prompt.
3. **Every loop is bounded.** Turns, tool calls, retries, tiempo, tokens/costo y condiciones terminales deben tener límites explícitos; MK1 además registra dónde se hacen cumplir.
4. **Tools are typed contracts.** Schema, permisos, errores, semántica, idempotencia y outputs forman parte de la arquitectura.
5. **Side effects cross a policy boundary.** Acciones mutantes/consecuenciales requieren risk classification y, cuando aplique, aprobación previa al efecto.
6. **Modified actions are new actions.** Si una persona o el modelo modifica argumentos, deben revalidarse antes de ejecutar.
7. **Context is curated state, not merely chat history.** System instructions, tool definitions, retrieved evidence, structured state, memory y transcript son componentes distintos.
8. **Persistence is not memory.** Checkpointing/durability, conversational memory y long-term knowledge tienen contratos diferentes.
9. **Durability is not concurrency safety.** Persistir estado no demuestra writer/locking/conflict semantics seguros.
10. **Agent says DONE != task is DONE.** El cierre debe probarse mediante estado externo, fixtures, tests o evidencia observable.
11. **Evaluate outcomes and trajectories.** El resultado final y la secuencia de acciones pueden fallar independientemente.
12. **Stochastic systems need repeated evaluation.** Un único run no certifica comportamiento estable.
13. **Reflection needs a verifier or feedback signal.** La autocorrección intrínseca no se presume confiable.
14. **Multi-agent must earn its complexity.** Solo se justifica si partición, paralelismo o especialización mejoran métricas frente a una baseline más simple.
15. **Least privilege is an agent invariant.** Shell, red, filesystem, secrets y herramientas mutantes deben limitar blast radius.
16. **Frameworks are adapters, not truth.** Los principios deben sobrevivir a cambios de SDK, modelo y proveedor.
17. **Version compatibility is evidence.** Un notebook que no se ejecuta contra su entorno declarado es material educativo degradado, no una referencia operacional.
18. **Protocol compatibility is a vector.** Revisión, lifecycle, transport, extensiones, auth, cancelación y execution receipt deben permanecer explícitos.

## Fuente inicial: GenAI_Agents

El primer mining site del dominio es `NirDiamant/GenAI_Agents`, fijado en:

```text
repository: NirDiamant/GenAI_Agents
branch:     main
snapshot:   4c95ae14cc2462c442b5c064cccd74430d02bc46
observed:   2026-09-07
```

Se utiliza como **catálogo pedagógico y cantera de patrones**, no como especificación normativa.

MK0 añadió además fuentes especializadas:

- `NirDiamant/Agent_Memory_Techniques@b7f7240e...` para presión taxonómica de memory;
- `NirDiamant/agents-towards-production@141b0679...` para patrones/claims de production;
- MCP `2026-07-28` como contrato protocolar vigente para esta iteración.

MK1 incorporó además runtimes/frameworks modernos como instrumentos de presión de la taxonomía. El primer system package completo es **Strands Agents** y sus hallazgos fueron contrastados con LangGraph y OpenAI Agents SDK antes de modificar el schema.

### Boundary legal

`GenAI_Agents` usa una licencia custom de uso no comercial con atribución y reserva de derechos comerciales. Por ello este dominio:

- no copia notebooks ni implementaciones;
- no incorpora código upstream como plantilla;
- registra factual metadata, observaciones y principios independientemente redactados;
- mantiene provenance y snapshot;
- contrasta los patrones con documentación oficial y literatura científica independiente.

## Regla de clasificación MK1

No usamos un único `agent_type`. Clasificamos dimensiones ortogonales:

```text
control authority
capabilities + composition
side effects
state / checkpoints / persistence / concurrency
memory lifecycle
human control + enforcement owner/boundary
errors / retries
termination + budget enforcement/cancellation
outcome / trajectory evaluation
protocol revision
security boundary
reproducibility evidence
UNKNOWNs
```

- schema: [`mk/MK1/CLASSIFICATION_SCHEMA.md`](./mk/MK1/CLASSIFICATION_SCHEMA.md)
- dimensions: [`mk/MK1/DIMENSIONS.md`](./mk/MK1/DIMENSIONS.md)
- rules: [`mk/MK1/NORMALIZATION_RULES.md`](./mk/MK1/NORMALIZATION_RULES.md)

## Strands como pressure test

Strands no fue incorporado como “la forma correcta” de construir agentes. Se utilizó para tensionar la taxonomía porque una misma SDK expone varias formas de control y una separación rica de state/session/memory/interventions/protocols.

El pass inicial encontró tres distinciones faltantes:

```text
concurrency semantics
budget enforcement boundary
intervention enforcement owner/boundary
```

No se promovieron desde Strands solo. LangGraph y OpenAI Agents SDK aportaron confirmación independiente y las tres terminaron normalizadas en `mk1-draft-2026-09-16.1`.

El pass posterior Strands ↔ MCP cerró la deuda principal de interoperabilidad `2026-07-28` a nivel **SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED**, preservando como abiertas las garantías de OAuth externo, rollback remoto y compatibilidad universal.

Vista consolidada: [`systems/strands/`](./systems/strands/).

## MK2 handoff

MK2 ya tiene scaffolding explícito en [`mk/MK2/`](./mk/MK2/) para contratos, schemas, checklists, test model, gates y backlog. **Eso no significa que MK2 esté abierto**: permanece bloqueado hasta que MK1 cierre y congele su schema de entrada.

## Flujo de madurez

```text
MK0  Mine & Frame                    ✅
 ↓
MK1  Normalize & Classify            ← current
 ↓
MK2  Operationalize contracts/tests  🔒 design seeded
 ↓
MK3  Integrate with Jett Engineering Method + domains
 ↓
MK4  Automate validators / eval harnesses
 ↓
MK5+ Certify against independent systems/counterexamples
```

`STATUS.md` es el tablero canónico. **Cerrar MK0 no certificó las reglas candidatas**; solo cerró el framing. MK1 normaliza; MK2 operacionaliza; los MK posteriores integran y certifican.
