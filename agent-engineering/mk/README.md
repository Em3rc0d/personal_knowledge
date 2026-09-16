# Agent Engineering — MK Progression

MKs represent **knowledge maturity**, not release marketing. Each MK is a package with explicit entry/exit semantics; documentation volume is never a closure criterion.

## Progression

| MK | Name | State | Exit condition |
|---|---|---|---|
| [`MK0`](./MK0/) | Mine & Frame | **✅ CLOSED** | source space, vocabulary, claims, contradictions, risks and candidate rules are evidence-backed |
| [`MK1`](./MK1/) | Normalize & Classify | **🟡 IN PROGRESS** | framework-independent taxonomy survives representative records/protocol/multi-agent pressure and freezes a schema revision |
| [`MK2`](./MK2/) | Operationalize | **🔒 BLOCKED / DESIGN SEEDED** | frozen MK1 semantics become contracts, schemas, checklists, tests and measurable acceptance criteria |
| MK3 | Integrate | **🔒 BLOCKED** | contracts connect cleanly with Jett Engineering Method, project architecture, security and delivery workflows |
| MK4 | Automate | **🔒 BLOCKED** | validators/eval harnesses test key invariants automatically and fail closed |
| MK5+ | Certify / Refine | **🔒 BLOCKED** | rules survive independent systems, adverse fixtures, version changes and real-project evidence |

## MK0 package

`MK0/` is the historical evidence/framing package:

```text
README.md
SCOPE.md
ONTOLOGY.md
INVARIANTS.md
EVIDENCE.md
UNKNOWNS.md
GATES.md
CLOSURE.md
```

MK0 is closed. Do not reopen it to solve MK1 normalization or MK2 operational questions unless new evidence proves the MK0 framing itself materially wrong.

## MK1 package

`MK1/` is the active normalization/classification package.

```text
README.md
CLASSIFICATION_SCHEMA.md
DIMENSIONS.md
NORMALIZATION_RULES.md
SCHEMA_HISTORY.md
CLASSIFICATION_QUEUE.md
records/
CLOSURE_PLAN.md
A2A_EVIDENCE_REQUIREMENTS.md
MULTI_AGENT_BASELINE_SPEC.md
UNKNOWNS.md
GATES.md
STRANDS_AGENTS_PRESSURE_TEST.md   # historical receipt
```

Core separation:

```text
schema/dimensions     define vocabulary
records/              instantiate vocabulary against real systems
GATES                  define pass/fail
CLOSURE_PLAN           defines execution order
UNKNOWNS               preserves/routs uncertainty
SCHEMA_HISTORY         versions/freeze semantics
```

MK1 does not close until a `CLOSURE.md` exists and names the frozen schema/record set.

## MK2 package

`MK2/` exists so the operational transition is designed before activation, but remains blocked.

```text
README.md
HANDOFF_CONTRACT.md
CONTRACT_CATALOG.md
SCHEMAS.md
CHECKLISTS.md
TEST_MODEL.md
PROMOTION_GATE.md
BACKLOG.md
UNKNOWNS.md
```

`HANDOFF_CONTRACT.md` is the entry boundary. MK2 must not derive policy directly from raw quarries.

## Transition model

```text
MK0 evidence/framing
        ↓
MK1 normalized schema + representative records
        ↓
MK1 schema freeze + CLOSURE.md
        ↓
MK2 HANDOFF_CONTRACT
        ↓
MK2 operationalization
```

If a later MK discovers a frozen assumption is materially wrong, change it through an explicit version/migration path rather than silently patching downstream artifacts.

## Canonical state and work order

- live state: [`../STATUS.md`](../STATUS.md)
- execution order: [`../ROADMAP.md`](../ROADMAP.md)
- repository authority rules: [`../REPOSITORY_CONTRACT.md`](../REPOSITORY_CONTRACT.md)

MK-local files explain evidence/gates; `STATUS.md` says what is currently open, closed or blocked.

## Promotion principle

```text
interesting example
      !=
reusable pattern
      !=
validated classification distinction
      !=
operational contract
      !=
certified engineering contract
```

No MK advances because a framework is popular, a README claims production readiness or a demo succeeds once.
