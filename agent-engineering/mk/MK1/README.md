# MK1 — Normalize & Classify

Status: **🟡 OPEN / IN PROGRESS**  
Precondition: **MK0 CLOSED**

## Purpose

MK1 turns mined evidence into a **framework-independent classification system**. It normalizes vocabulary and architecture descriptions before MK2 converts them into operational contracts.

This README is the **entrypoint/index** for MK1. The schema, dimensions, rules, queue, unknowns and gates live in dedicated files.

## Package map

| Artifact | Responsibility |
|---|---|
| [`CLASSIFICATION_SCHEMA.md`](./CLASSIFICATION_SCHEMA.md) | normalized machine/human-readable record shape |
| [`DIMENSIONS.md`](./DIMENSIONS.md) | control, capabilities, side effects, memory, HITL, retry, termination, eval, protocol, multi-agent and evidence axes |
| [`NORMALIZATION_RULES.md`](./NORMALIZATION_RULES.md) | rules preventing framework labels, hidden assumptions and dimension collapse |
| [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md) | prioritized systems/families and classification workflow |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | inherited and MK1-specific uncertainty register |
| [`GATES.md`](./GATES.md) | pressure tests and closure criteria |

## Mission

The classification model must be:

- orthogonal where possible;
- explicit about control authority;
- explicit about reachable capabilities and compositions;
- explicit about side effects independently of autonomy;
- explicit about state/checkpoint/persistence/memory lifecycle;
- explicit about human approval and dispatcher enforcement;
- explicit about retries/errors/unknown outcomes;
- explicit about semantic termination and resource budgets;
- explicit about evaluation evidence;
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
SIDE-EFFECT CLASS
STATE / CHECKPOINT / PERSISTENCE
MEMORY LIFECYCLE
HUMAN CONTROL
ERROR / RETRY OWNERSHIP
TERMINATION
EVALUATION
PROTOCOL REVISION
SECURITY / CONTAINMENT
REPRODUCIBILITY
EVIDENCE STATE
UNKNOWNs
```

Full definitions: [`DIMENSIONS.md`](./DIMENSIONS.md).

## First pressure-test set

MK1 begins with:

- minimal while-loop;
- HITL approval;
- trace-evaluation harness;
- E2E generated-code/browser execution;
- self-healing generated code;
- HR messaging;
- social publishing;
- document intake/data egress;
- DataScribe database authority;
- reflection/self-improvement claim;
- memory system;
- multi-agent system;
- legacy/current MCP comparison.

Full queue: [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md).

## State transition

```text
MK0 evidence/framing
        ↓
MK1 normalize/classify      ← current
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
