# Agent Engineering — Status

Updated: 2026-09-07

## Current gate

```text
DOMAIN                    agent-engineering
CURRENT MK                MK1
STATE                     IN PROGRESS
MK0                       CLOSED / STRUCTURED EVIDENCE PACKAGE
MK1                       ACTIVE / STRUCTURED NORMALIZATION PACKAGE
MK2                       BLOCKED / DESIGN PACKAGE SEEDED
PRIMARY MINING SITE       NirDiamant/GenAI_Agents
UPSTREAM SNAPSHOT         4c95ae14cc2462c442b5c064cccd74430d02bc46
MEMORY CROSS-SOURCE       Agent_Memory_Techniques@b7f7240e...
PRODUCTION CROSS-SOURCE   agents-towards-production@141b0679...
MCP CONTRACT              2026-07-28
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
CAPABILITY / RISK SCAN    COMPLETE FOR MK0
THREAT MODEL              MK0 SEED COMPLETE
SCIENTIFIC CONTRAST       COMPLETE FOR MK0
REUSABLE RULES            CANDIDATE / NORMALIZATION IN PROGRESS
CANON RULE CERTIFICATION  BLOCKED BY MK1/MK2+
```

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

Each MK is a **knowledge package**, not a giant README.

```text
mk/
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

README files are entrypoints/indexes. Substantive knowledge is split by responsibility so provenance, gates and uncertainty remain auditable.

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
- tool design is a first-class interface/authorization/error problem;
- outcome verification is stronger evidence than agent narration;
- trace evaluation is useful but does not replace outcome evaluation or repeated trials;
- intrinsic reflection is not evidence of persistent improvement without external verification;
- multi-agent topology must prove benefit against a simpler baseline;
- production security requires least privilege and containment around reachable capabilities;
- protocol interoperability does not imply execution authorization;
- protocol revision belongs in integration evidence;
- production readiness is a vector of evidence, not a label.

## Known UNKNOWNs transferred beyond MK0

These do not invalidate MK0 closure because they require normalization, operationalization or execution evidence:

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
11. per-language MCP SDK migration details beyond protocol-level contradiction.

Canonical registers:

- [`mk/MK0/UNKNOWNS.md`](./mk/MK0/UNKNOWNS.md)
- [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md)
- [`mk/MK2/UNKNOWNS.md`](./mk/MK2/UNKNOWNS.md)

## MK0 closure gate

All MK0 gates are closed. See [`mk/MK0/GATES.md`](./mk/MK0/GATES.md) and the historical [`mk/MK0/CLOSURE.md`](./mk/MK0/CLOSURE.md).

## MK1 current work

Active package: [`mk/MK1/`](./mk/MK1/)

Immediate queue: [`mk/MK1/CLASSIFICATION_QUEUE.md`](./mk/MK1/CLASSIFICATION_QUEUE.md)

The current work is to pressure-test the classification schema against representative systems, resolve overlapping dimensions, preserve unknowns and freeze a schema revision suitable for MK2 input.

## MK2 state

MK2 has a visible design package at [`mk/MK2/`](./mk/MK2/) so the handoff is explicit. It is **not active** and its schemas/contracts are not canon until MK1 closes.

## Promotion state

```text
MK0 FRAME / EVIDENCE BASE   ✅ CLOSED
MK1 NORMALIZATION           🟡 IN PROGRESS
MK2 OPERATIONALIZATION      🔒 BLOCKED / DESIGN SEEDED
CANON RULE CERTIFICATION    🔒 BLOCKED
CURRENT BRANCH MERGE        🔒 PENDING REVIEW
```

Closing MK0 did not certify candidate rules. MK1 classifies them; MK2 will operationalize survivors; later MKs must integrate, automate and certify them against real systems.
