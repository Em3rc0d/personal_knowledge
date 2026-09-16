# Agent Engineering — Status

Updated: 2026-09-16

## Current gate

```text
DOMAIN                    agent-engineering
CURRENT MK                MK1
STATE                     IN PROGRESS
MK0                       CLOSED / STRUCTURED EVIDENCE PACKAGE
MK1                       ACTIVE / STRUCTURED NORMALIZATION PACKAGE
MK2                       BLOCKED / DESIGN PACKAGE SEEDED
SCHEMA REVISION           mk1-draft-2026-09-16.1
KNOWLEDGE MAP             AVAILABLE / KNOWLEDGE_MAP.md
LLM ROUTER                AVAILABLE / LLM_CONTEXT.md
SYSTEM PACKAGE LAYER      AVAILABLE / systems/
PRIMARY MINING SITE       NirDiamant/GenAI_Agents
UPSTREAM SNAPSHOT         4c95ae14cc2462c442b5c064cccd74430d02bc46
MEMORY CROSS-SOURCE       Agent_Memory_Techniques@b7f7240e...
PRODUCTION CROSS-SOURCE   agents-towards-production@141b0679...
MCP CONTRACT              2026-07-28
STRANDS SYSTEM PACKAGE    systems/strands / CURRENT CANONICAL SYNTHESIS
STRANDS PRESSURE TEST     harness-sdk@a9361c54... / COMPLETE
RUNTIME CROSS-SOURCE      STRANDS + LANGGRAPH + OPENAI AGENTS SDK / COMPLETE
STRANDS MCP 2026-07-28    SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED
LICENSE BOUNDARY          RECORDED / S-001 NON-COMMERCIAL CUSTOM LICENSE
REPOSITORY INVENTORY      COMPLETE FOR MK0
NORMALIZED INVENTORY      SEED COMPLETE
P0/P1 CALL PATHS          CLOSED FOR CLASSIFICATION
LOOP/HARNESS MODEL        MK0 FRAME COMPLETE
TOOLS / ACI               MK0 FRAME COMPLETE
HITL / SIDE EFFECTS       MK0 FRAME COMPLETE
TRACE EVALUATION          MK0 FRAME COMPLETE
MEMORY / PERSISTENCE      CROSS-SOURCE FRAME COMPLETE
MULTI-AGENT               QUALIFIED / MK1 NORMALIZATION OPEN
CONCURRENCY SEMANTICS     PROMOTED UNDER STATE / CROSS-RUNTIME SUPPORTED
BUDGET ENFORCEMENT        PROMOTED UNDER TERMINATION / CROSS-RUNTIME SUPPORTED
INTERVENTION OWNER        PROMOTED UNDER HUMAN_CONTROL / CROSS-RUNTIME SUPPORTED
CAPABILITY / RISK SCAN    COMPLETE FOR MK0
THREAT MODEL              MK0 SEED COMPLETE
SCIENTIFIC CONTRAST       COMPLETE FOR MK0
REUSABLE RULES            CANDIDATE / NORMALIZATION IN PROGRESS
CANON RULE CERTIFICATION  BLOCKED BY MK1/MK2+
```

## Reading contract

For current answers:

```text
STATUS.md
→ systems/<system>/
→ current MK schema/gates
```

For provenance/audit:

```text
current synthesis
→ MK decision
→ quarry
→ source receipt
→ pinned upstream source
```

Navigation:

- human knowledge map: [`KNOWLEDGE_MAP.md`](./KNOWLEDGE_MAP.md)
- machine/LLM router: [`LLM_CONTEXT.md`](./LLM_CONTEXT.md)
- concrete-system packages: [`systems/`](./systems/)

## MK progression

| MK | Objective | State | Package |
|---|---|---|---|
| MK0 | Mine source, establish vocabulary, provenance, claims, evidence, contradictions and candidate rules | **✅ CLOSED** | [`mk/MK0/`](./mk/MK0/) |
| MK1 | Normalize taxonomy and classify architectures, state, tools, control and failure modes | **🟡 IN PROGRESS** | [`mk/MK1/`](./mk/MK1/) |
| MK2 | Convert findings into operational contracts, checklists, schemas and tests | **🔒 BLOCKED / DESIGN SEEDED** | [`mk/MK2/`](./mk/MK2/) |
| MK3 | Integrate agent engineering with Jett Engineering Method, security and project workflows | BLOCKED | — |
| MK4 | Automate static checks, eval harness templates and evidence gates | BLOCKED | — |
| MK5+ | Certify rules against independent agent systems and production-like fixtures | BLOCKED | — |

## Documentation architecture

The domain now has both a maturity/evidence pipeline and a current system-view layer.

```text
agent-engineering/
├── README.md
├── STATUS.md
├── KNOWLEDGE_MAP.md
├── LLM_CONTEXT.md
├── systems/
│   ├── README.md
│   └── strands/
│       ├── README.md
│       ├── CLASSIFICATION.md
│       ├── ENGINEERING_RULES.md
│       ├── PROTOCOLS.md
│       ├── EVIDENCE.md
│       └── LLM_CONTEXT.md
├── architecture/
├── mining-site/
├── quarries/
└── mk/
    ├── README.md
    ├── MK0/
    │   ├── README.md
    │   ├── SCOPE.md
    │   ├── ONTOLOGY.md
    │   ├── INVARIANTS.md
    │   ├── EVIDENCE.md
    │   ├── UNKNOWNS.md
    │   ├── GATES.md
    │   └── CLOSURE.md
    ├── MK1/
    │   ├── README.md
    │   ├── CLASSIFICATION_SCHEMA.md
    │   ├── DIMENSIONS.md
    │   ├── NORMALIZATION_RULES.md
    │   ├── CLASSIFICATION_QUEUE.md
    │   ├── STRANDS_AGENTS_PRESSURE_TEST.md
    │   ├── UNKNOWNS.md
    │   └── GATES.md
    └── MK2/
        ├── README.md
        ├── CONTRACT_CATALOG.md
        ├── SCHEMAS.md
        ├── CHECKLISTS.md
        ├── TEST_MODEL.md
        ├── PROMOTION_GATE.md
        ├── BACKLOG.md
        └── UNKNOWNS.md
```

README files are entrypoints/indexes. `systems/` answers “what do we know today about this concrete system?”; `quarries/` and `mining-site/` retain the evidence/history needed to audit the answer.

## Canonical system views

### Strands Agents

Current package: [`systems/strands/`](./systems/strands/)

Preferred human path:

```text
README
→ ENGINEERING_RULES
→ CLASSIFICATION
→ PROTOCOLS
→ EVIDENCE as needed
```

Preferred LLM path:

```text
systems/strands/LLM_CONTEXT.md
→ smallest canonical document that answers the query
→ descend to evidence only when needed
```

The package reconciles the original Strands quarry, the MK1 pressure test, the Strands/LangGraph/OpenAI runtime crosscheck and the Strands↔MCP `2026-07-28` execution receipt.

## MK0 closure evidence

Closure receipt: [`mk/MK0/CLOSURE.md`](./mk/MK0/CLOSURE.md)

MK0 closed after establishing:

- exact primary upstream snapshot and legal boundary;
- normalized inventory covering all 55 GenAI_Agents tutorial entries;
- P0/P1 priority model and call-path verification at classification depth;
- direct evidence for generated code, shell, browser, external messaging/publication, file egress and database-risk families;
- explicit UNKNOWNs where implementation detail could not be proven;
- specialized memory comparison against `Agent_Memory_Techniques`;
- production-claim comparison against `agents-towards-production`;
- MCP tutorial contradiction against current `2026-07-28` protocol lifecycle;
- current official and scientific contradiction pass;
- capability-centered threat model and adversarial fixtures;
- framework-independent MK1 schema foundation.

Detailed package:

- framing: [`mk/MK0/SCOPE.md`](./mk/MK0/SCOPE.md)
- ontology/distinctions: [`mk/MK0/ONTOLOGY.md`](./mk/MK0/ONTOLOGY.md)
- candidate rules/anti-patterns: [`mk/MK0/INVARIANTS.md`](./mk/MK0/INVARIANTS.md)
- evidence ledger: [`mk/MK0/EVIDENCE.md`](./mk/MK0/EVIDENCE.md)
- transferred unknowns: [`mk/MK0/UNKNOWNS.md`](./mk/MK0/UNKNOWNS.md)
- gates: [`mk/MK0/GATES.md`](./mk/MK0/GATES.md)

## High-confidence findings carried into MK1

- workflow and agent are different control structures; model-directed control must be explicit;
- framework identity is not taxonomy;
- critical invariants belong in code/policy/tool boundaries rather than prompt-only instructions;
- generated code, general shell and broad browser authority are high-blast-radius capabilities requiring containment;
- externally visible mutations should support deterministic safe modes, idempotency and receipts where feasible;
- data egress is consequential even when the logical operation is `read/transform`;
- HITL must gate the actual consequential dispatcher when policy requires approval;
- edited actions are new actions and must be revalidated/re-authorized;
- state, context, checkpointing, persistence, memory and knowledge are distinct contracts;
- persistence does not imply concurrency safety;
- budget values require enforcement-boundary semantics;
- intervention mechanisms require enforcement owner and consequential-dispatch coverage;
- tool design is a first-class interface/authorization/error problem;
- outcome verification is stronger evidence than agent narration;
- trace evaluation is useful but does not replace outcome evaluation or repeated trials;
- intrinsic reflection is not evidence of persistent improvement without external verification;
- multi-agent topology must prove benefit against a simpler baseline;
- production security requires least privilege and containment around reachable capabilities;
- protocol interoperability does not imply execution authorization;
- protocol revision belongs in integration evidence;
- production readiness is a vector of evidence, not a label.

## MK1 Strands pressure-test findings

Source/evidence package:

- current synthesis: [`systems/strands/README.md`](./systems/strands/README.md)
- source receipt: [`mining-site/S-109-strands-agents.md`](./mining-site/S-109-strands-agents.md)
- processed quarry: [`quarries/strands-agents.md`](./quarries/strands-agents.md)
- historical normalized pressure test: [`mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](./mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)

The initial Strands pass exposed three candidate qualifiers:

1. concurrency semantics;
2. budget enforcement boundary;
3. intervention enforcement owner.

They were initially held as UNKNOWN/promotion debt pending independent evidence.

## MK1 cross-runtime promotion — 2026-09-16

Independent contrast against LangGraph and OpenAI Agents SDK closed that debt.

Evidence package:

- `S-110`: [`mining-site/S-110-langgraph-runtime-semantics.md`](./mining-site/S-110-langgraph-runtime-semantics.md)
- `S-111`: [`mining-site/S-111-openai-agents-sdk-runtime-semantics.md`](./mining-site/S-111-openai-agents-sdk-runtime-semantics.md)
- synthesis: [`quarries/runtime-semantics-strands-langgraph-openai.md`](./quarries/runtime-semantics-strands-langgraph-openai.md)

Promotion result:

- **concurrency semantics** → promoted as `state` qualifiers;
- **budget enforcement boundary / overshoot / cancellation boundary** → promoted under `termination`;
- **intervention enforcement owner + boundary** → promoted under `human_control`;
- no framework-specific top-level dimension was required.

Schema revision: [`mk/MK1/CLASSIFICATION_SCHEMA.md`](./mk/MK1/CLASSIFICATION_SCHEMA.md) → `mk1-draft-2026-09-16.1`.

This strengthens, rather than replaces, existing fields such as `replay_semantics`, `dispatcher_enforcement`, `approval_binding`, semantic success predicates and error/idempotency contracts.

## Strands × MCP `2026-07-28` compatibility gate — 2026-09-16

Current canonical protocol view: [`systems/strands/PROTOCOLS.md`](./systems/strands/PROTOCOLS.md)  
Detailed receipt: [`quarries/strands-mcp-2026-07-28-compatibility.md`](./quarries/strands-mcp-2026-07-28-compatibility.md).

The previous `exact Strands/MCP execution compatibility` unknown is now closed at the current source-evidence level.

Evidence includes:

- declared MCP 2.x support in the pinned Strands dependency range;
- a protocol-aware `server/discover` negotiation path;
- an integration fixture whose server rejects any legacy `initialize` handshake;
- real MCP 2.x `MCPServer` execution over Streamable HTTP;
- tools/list + tools/call, structured result/error behavior and modern multi-round-trip input;
- prompts/resources and modern list-change subscription behavior in the current pinned fixture;
- successful upstream CI for the MCP 2.x integration suite;
- a separate merged end-to-end MCP 2.x OpenTelemetry trace-continuity test.

Normalized evidence state:

```text
CORE INTEROPERABILITY        SUPPORTED / UPSTREAM-EXECUTED
MODERN LIFECYCLE             REGRESSION-TESTED
TRACE CONTINUITY             UPSTREAM E2E TESTED
AUTH ADAPTER                 SUPPORTED
EXTERNAL OAUTH E2E           DEPLOYMENT-SPECIFIC / OPEN
REMOTE EFFECT ROLLBACK       NOT IMPLIED BY CANCELLATION
INDEPENDENT LOCAL RE-RUN     BLOCKED BY CURRENT ENVIRONMENT NETWORK
```

This strengthens the rule that protocol compatibility is a **vector of evidence**, not a boolean. Interoperability remains separate from authorization and transactional safety.

## Known UNKNOWNs transferred beyond MK0

These remain open because they require normalization, operationalization or execution evidence:

1. exact current executability of every upstream notebook;
2. per-notebook dependency/provider compatibility under current runtimes;
3. sandbox effectiveness for generated-code examples;
4. universal sender approval coverage in HR examples;
5. exact DataScribe lower-level mutation dispatcher/filter semantics;
6. authenticated mutating-browser reachability;
7. complete idempotency/retry contracts for every external write;
8. project-specific memory quality/isolation/retention behavior;
9. benchmarked multi-agent benefit for individual topologies;
10. project-specific deployment/rollback/SLO/incident evidence;
11. per-language protocol/SDK feature parity as versions evolve;
12. backend-specific concurrency implementation details after the normalized state qualifiers are populated;
13. exact hard/cooperative/best-effort cancellation behavior for individual model/tool/remote paths;
14. application-specific approval binding and revalidation coverage;
15. external protected-server MCP OAuth authorization E2E and deployment-specific policy behavior;
16. A2A revision/auth/transport receipt for reproducible distributed-agent classification.

Canonical registers:

- [`mk/MK0/UNKNOWNS.md`](./mk/MK0/UNKNOWNS.md)
- [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md)
- [`mk/MK2/UNKNOWNS.md`](./mk/MK2/UNKNOWNS.md)

## MK0 closure gate

All MK0 gates are closed. See [`mk/MK0/GATES.md`](./mk/MK0/GATES.md) and the historical [`mk/MK0/CLOSURE.md`](./mk/MK0/CLOSURE.md).

## MK1 current work

Active package: [`mk/MK1/`](./mk/MK1/)

Immediate queue: [`mk/MK1/CLASSIFICATION_QUEUE.md`](./mk/MK1/CLASSIFICATION_QUEUE.md)

Current work remains to finish representative normalized records, resolve remaining overlaps, preserve unknowns and freeze a schema revision suitable for MK2 input.

Next evidence after the Strands MCP gate:

- continue representative classifications needed by the MK1 closure checklist;
- pin A2A revision/auth/transport semantics before using it as distributed-agent reproducibility evidence;
- benchmark at least one multi-agent topology against a simpler baseline before deriving a performance rule;
- decide whether remaining classification records are sufficient to freeze `mk1-draft-2026-09-16.1` or require another additive draft.

## MK2 state

MK2 has a visible design package at [`mk/MK2/`](./mk/MK2/) so the handoff is explicit. It is **not active** and its schemas/contracts are not canon until MK1 closes.

## Promotion state

```text
MK0 FRAME / EVIDENCE BASE    ✅ CLOSED
MK1 NORMALIZATION            🟡 IN PROGRESS
STRANDS SYSTEM PACKAGE       ✅ CURRENT SYNTHESIS AVAILABLE
STRANDS PRESSURE TEST        ✅ COMPLETE
RUNTIME SEMANTICS CROSSCHECK ✅ COMPLETE
STRANDS MCP 2026-07-28       ✅ SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED
SCHEMA REVISION              mk1-draft-2026-09-16.1
MK2 OPERATIONALIZATION       🔒 BLOCKED / DESIGN SEEDED
CANON RULE CERTIFICATION     🔒 BLOCKED
```

Closing MK0 did not certify candidate rules. MK1 classifies them; MK2 will operationalize survivors; later MKs must integrate, automate and certify them against real systems.
