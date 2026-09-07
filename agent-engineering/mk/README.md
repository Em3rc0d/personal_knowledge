# Agent Engineering — MK progression

MKs represent **knowledge maturity**, not release marketing. Each MK is a package of artifacts with one README as entrypoint; substantive knowledge is split by responsibility instead of accumulated in a monolithic README.

## Progression

| MK | Name | State | Exit condition |
|---|---|---|---|
| [`MK0`](./MK0/) | Mine & Frame | **✅ CLOSED** | source space, vocabulary, claims, contradictions, risks and candidate rules are evidence-backed |
| [`MK1`](./MK1/) | Normalize & Classify | **🟡 IN PROGRESS** | framework-independent taxonomy is coherent, dimensions survive pressure tests and major families classify consistently |
| [`MK2`](./MK2/) | Operationalize | **🔒 BLOCKED / DESIGN SEEDED** | stable rules become schemas, contracts, checklists, tests and measurable acceptance criteria |
| MK3 | Integrate | **🔒 BLOCKED** | contracts connect cleanly with Jett Engineering Method, project architecture, security and delivery workflows |
| MK4 | Automate | **🔒 BLOCKED** | validators/eval harnesses test key invariants automatically and fail closed |
| MK5+ | Certify / Refine | **🔒 BLOCKED** | rules survive independent systems, adverse fixtures, version changes and real-project evidence |

## MK0 package

`MK0/` is the historical evidence/framing package:

- `README.md` — index;
- `SCOPE.md` — mission/boundaries;
- `ONTOLOGY.md` — initial ontology/distinctions;
- `INVARIANTS.md` — candidate invariants/anti-patterns;
- `EVIDENCE.md` — evidence ledger;
- `UNKNOWNS.md` — transferred uncertainty;
- `GATES.md` — exit/promotion semantics;
- `CLOSURE.md` — closure receipt.

## MK1 package

`MK1/` is the active normalization package:

- `README.md` — index;
- `CLASSIFICATION_SCHEMA.md` — record shape;
- `DIMENSIONS.md` — normalized axes;
- `NORMALIZATION_RULES.md` — classification discipline;
- `CLASSIFICATION_QUEUE.md` — pressure-test queue/workflow;
- `UNKNOWNS.md` — uncertainty register;
- `GATES.md` — closure criteria.

## MK2 package

`MK2/` exists so the operational handoff is explicit, but remains blocked until MK1 closes:

- `README.md` — index/state;
- `CONTRACT_CATALOG.md` — planned operational contract families;
- `SCHEMAS.md` — provisional machine-readable shapes;
- `CHECKLISTS.md` — human-operable evidence-linked checks;
- `TEST_MODEL.md` — deterministic/stochastic/adversarial verification model;
- `PROMOTION_GATE.md` — entry/exit/promotion semantics;
- `BACKLOG.md` — queued implementation slices;
- `UNKNOWNS.md` — unresolved operational design questions.

## Canonical state

The domain status board remains [`../STATUS.md`](../STATUS.md). MK-local files explain the evidence and gates; `STATUS.md` says what is currently open, closed or blocked.

## Promotion principle

```text
interesting example
      !=
reusable pattern
      !=
validated rule
      !=
operational contract
      !=
certified engineering contract
```

No MK advances because a framework is popular, a README claims production readiness or a demo succeeds once.

Closing one MK never silently promotes later claims. MK0 closure does not imply operationalization; MK1 closure will not by itself imply production certification; MK2 closure will still require later integration and real-system evidence.
