# MK1 — Normalize & Classify

Status: **🟡 OPEN / IN PROGRESS**  
Precondition: **MK0 CLOSED**

## Purpose

MK1 turns mined evidence into a **framework-independent classification system**. It normalizes vocabulary and architecture descriptions before MK2 converts survivors into operational contracts.

This README is the **entrypoint/index** for MK1. The schema, dimensions, records, pressure tests, unknowns and gates live in dedicated artifacts.

## Package map

| Artifact | Responsibility |
|---|---|
| [`CLASSIFICATION_SCHEMA.md`](./CLASSIFICATION_SCHEMA.md) | normalized machine/human-readable record shape |
| [`DIMENSIONS.md`](./DIMENSIONS.md) | control, capabilities, side effects, memory, HITL, retry, termination, eval, protocol, multi-agent and evidence axes |
| [`NORMALIZATION_RULES.md`](./NORMALIZATION_RULES.md) | rules preventing framework labels, hidden assumptions and dimension collapse |
| [`records/`](./records/) | evidence-backed normalized system records |
| [`PRESSURE_TESTS.md`](./PRESSURE_TESTS.md) | schema challenges, refinements and surviving cases |
| [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md) | completed first set + next pressure-test queue |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | inherited and MK1-specific uncertainty register |
| [`GATES.md`](./GATES.md) | pressure tests and closure criteria |

## Current milestone

```text
original first set R-001..R-013     ✅ COMPLETE
all MK0 P0 call paths R-001..R-015 ✅ COVERED
external cross-source R-016        ✅ FIRST PASS
schema pressure refinements        ✅ MATERIAL CHANGES RECORDED
MK1 closure                        🟡 NOT YET
```

The current record set is indexed in [`records/README.md`](./records/README.md).

## Mission

The classification model must be:

- orthogonal where possible;
- explicit about control authority;
- explicit about reachable capabilities and compositions;
- explicit about observed vs reachable side effects;
- explicit about state/checkpoint/persistence/memory lifecycle;
- explicit about human approval and dispatcher enforcement;
- explicit about retries/errors/unknown outcomes;
- explicit about semantic termination and resource budgets;
- explicit about evaluation evidence;
- explicit about multi-agent admission hypothesis/baseline;
- revision-aware for protocols/integrations;
- capable of preserving `UNKNOWN` instead of forcing a label.

## Core principle

> Classify what the system can actually decide and do, not what the repository/framework calls it.

A single system may be deterministic in one stage, model-routed in another, model-directed for tools, human-gated for writes and durably checkpointed by the runtime. Therefore a single `agent_type` is insufficient.

## Primary dimensions

```text
CONTROL AUTHORITY
HORIZON / TOPOLOGY
CAPABILITIES + COMPOSITION
OBSERVED / REACHABLE SIDE EFFECTS
STATE / CHECKPOINT / PERSISTENCE
MEMORY LIFECYCLE
HUMAN CONTROL
ERROR / RETRY OWNERSHIP
TERMINATION
EVALUATION
MULTI-AGENT ADMISSION / BASELINE
PROTOCOL REVISION
SECURITY / CONTAINMENT
REPRODUCIBILITY
EVIDENCE STATE
UNKNOWNs
```

Full definitions: [`DIMENSIONS.md`](./DIMENSIONS.md).

## What the first records already disproved

- a framework constructor is not an agent taxonomy;
- a harmless observed shell/code run does not imply low reachable authority;
- an HITL node elsewhere does not prove sender authorization;
- `long-term memory` in prose does not imply durable cross-session persistence;
- multiple named agents do not imply model-directed orchestration;
- `MCP` without revision/capabilities/auth semantics is underspecified;
- production-like labels do not replace operational evidence.

## Remaining pressure-test frontier

MK1 stays open for materially different cases:

- C1 model-routed workflow;
- C3/open-horizon agent;
- dynamic multi-agent delegation;
- durable cross-session memory;
- authenticated transactional browser;
- unknown-outcome mutating timeout/reconciliation;
- production-oriented external system;
- independent source/framework outside the NirDiamant corpus.

See [`PRESSURE_TESTS.md`](./PRESSURE_TESTS.md) and [`GATES.md`](./GATES.md).

## State transition

```text
MK0 evidence/framing
        ↓
MK1 normalize/classify      ← current
        ↓
pressure against independent/extreme cases
        ↓
freeze classification schema revision
        ↓
MK2 operationalize contracts/tests
```

MK2 already contains **design scaffolding only** so the handoff shape is visible, but MK2 implementation remains blocked until MK1 closes.

## Current promotion state

```text
MK0 = CLOSED
MK1 = IN PROGRESS
MK2 = BLOCKED / DESIGN SEEDED
CANON OPERATIONAL RULES = NOT YET
```
