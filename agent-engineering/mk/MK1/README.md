# MK1 — Normalize & Classify

Status: **🟡 OPEN / IN PROGRESS**  
Precondition: **MK0 CLOSED**  
Current schema: **`mk1-draft-2026-09-16.1`**

## Mission

MK1 turns mined evidence into a **framework-independent classification system** that can describe materially different agent systems without relying on framework names, marketing labels or hidden assumptions.

MK1 answers:

```text
What kind of system is this?
Who/what controls execution?
What can it reach and mutate?
How does state/memory/concurrency work?
Where are policy, approval and termination enforced?
What evidence supports the classification?
What remains UNKNOWN?
```

MK1 does **not** define the full operational policy a production system must satisfy. That is MK2.

## Package map

### Core semantics

| Artifact | Responsibility |
|---|---|
| [`CLASSIFICATION_SCHEMA.md`](./CLASSIFICATION_SCHEMA.md) | current normalized record shape |
| [`DIMENSIONS.md`](./DIMENSIONS.md) | semantic definitions for each dimension |
| [`NORMALIZATION_RULES.md`](./NORMALIZATION_RULES.md) | anti-collapse / anti-framework normalization rules |
| [`SCHEMA_HISTORY.md`](./SCHEMA_HISTORY.md) | revision/change ledger and freeze procedure |

### Evidence application

| Artifact | Responsibility |
|---|---|
| [`records/README.md`](./records/README.md) | canonical normalized-record registry and family coverage |
| [`records/TEMPLATE.md`](./records/TEMPLATE.md) | record materialization contract |
| [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md) | priority/admission logic for remaining evidence |
| [`STRANDS_AGENTS_PRESSURE_TEST.md`](./STRANDS_AGENTS_PRESSURE_TEST.md) | historical first-pass Strands receipt |

### Closure control

| Artifact | Responsibility |
|---|---|
| [`GATES.md`](./GATES.md) | formal closure gates |
| [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md) | executable dependency plan |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | uncertainty register/routing |
| [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md) | reusable A2A evidence contract; current gate PASS/QUALIFIED |
| [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md) | remaining primary evidence gate |

## Current system synthesis

For current framework/runtime answers, prefer canonical system packages over historical pressure tests.

Current complete package: [`../../systems/strands/`](../../systems/strands/).

- human mental model → [`../../systems/strands/README.md`](../../systems/strands/README.md)
- current normalized profile → [`../../systems/strands/CLASSIFICATION.md`](../../systems/strands/CLASSIFICATION.md)
- protocols → [`../../systems/strands/PROTOCOLS.md`](../../systems/strands/PROTOCOLS.md)
- provenance → [`../../systems/strands/EVIDENCE.md`](../../systems/strands/EVIDENCE.md)
- machine context → [`../../systems/strands/LLM_CONTEXT.md`](../../systems/strands/LLM_CONTEXT.md)

## Core classification principle

> Classify what the system can actually decide and do, not what the repository/framework calls it.

A single SDK may expose deterministic workflows, model-routed branches, model-directed loops, peer handoffs and remote-agent protocols. Framework identity cannot substitute for architecture classification.

## Primary dimensions

```text
CONTROL AUTHORITY
HORIZON / TOPOLOGY
CAPABILITIES + COMPOSITION
SIDE-EFFECT CLASS
STATE / CHECKPOINT / PERSISTENCE / CONCURRENCY
MEMORY LIFECYCLE
HUMAN CONTROL + ENFORCEMENT OWNER/BOUNDARY
ERROR / RETRY OWNERSHIP
TERMINATION + BUDGET ENFORCEMENT
EVALUATION
PROTOCOL REVISION
SECURITY / CONTAINMENT
REPRODUCIBILITY
EVIDENCE STATE
UNKNOWNs
```

Full definitions: [`DIMENSIONS.md`](./DIMENSIONS.md).

## Current representative records

```text
MATERIALIZED / QUALIFIED
REC-001  minimal while-loop / model-tool loop / shell
REC-002  HITL approval / protected dispatcher
REC-003  trace evaluation / outcome-vs-trajectory
REC-004  generated code + browser + host blast radius
REC-007  social publication / dry-run / idempotency
REC-008  document/data egress
REC-009  database authority / least privilege
REC-010  reflection/adaptation claim discipline
REC-011  state/persistence/memory lifecycle contrast
REC-013  MCP revision drift
REC-014  Strands Agents canonical classification

COVERED_BY
REC-005  REC-004 + REC-003
REC-006  REC-002 + REC-007

OPEN / BLOCKING
REC-012  multi-agent baseline/admission evidence
```

Registry: [`records/README.md`](./records/README.md).

The set exists to pressure-test the schema, not to maximize document count.

## Closed runtime-semantics promotion

Independent contrast across Strands, LangGraph and OpenAI Agents SDK promoted:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

## Protocol state

### MCP

Strands ↔ MCP `2026-07-28` is **SUPPORTED / QUALIFIED** with upstream execution evidence for the modern path and explicit authorization/cancellation limits.

Evidence: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

### A2A

The A2A classification-shape gate is now **PASS / QUALIFIED**.

Pinned Strands evidence shows:

```text
Python SDK        a2a-sdk >=0.3.0,<0.4.0
TypeScript SDK    @a2a-js/sdk ^0.3.10
implemented line  A2A 0.3
current line      A2A 1.0
fixtures          source present / integration scope present
specific CI PASS  not verified
independent run   not run
A2A 1.0 compat    NOT ESTABLISHED
```

Receipt: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md).

The taxonomy can represent this version drift without `A2A=true`; therefore current-version migration debt remains explicit but is not a hidden MK1 taxonomy blocker.

## Remaining closure blockers

```text
REC-012 multi-agent baseline/admission evidence    OPEN / BLOCKING
final UNKNOWN reconciliation                       PENDING REC-012
cross-dimension + overlap audit                     PENDING
schema freeze decision                              NOT YET
MK1 CLOSURE.md                                     NOT YET
MK2 activation                                     BLOCKED
```

Execution order: [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md).

## Historical-document rule

Historical receipts are intentionally preserved. If `STRANDS_AGENTS_PRESSURE_TEST.md` says a field is candidate/open, interpret it as first-pass state, not current truth.

Current-state precedence:

```text
STATUS.md
> systems/<system>/
> current MK schema/gates/records
> quarries/
> mining-site/
```

## MK1 output contract

MK1 closes with:

```text
frozen schema revision
+ normalized dimensions/rules
+ complete representative record coverage
+ revision-aware protocol evidence
+ multi-agent admission/baseline evidence
+ routed UNKNOWNs
+ closure receipt
```

Then, and only then, MK2 receives the package defined by [`../MK2/HANDOFF_CONTRACT.md`](../MK2/HANDOFF_CONTRACT.md).

## Current promotion state

```text
MK0                           CLOSED
MK1                           IN PROGRESS
SCHEMA                        mk1-draft-2026-09-16.1
RUNTIME SEMANTICS CROSSCHECK  PASS
STRANDS MCP 2026-07-28        SUPPORTED / QUALIFIED
A2A CLASSIFICATION SHAPE      PASS / QUALIFIED
A2A 1.0 COMPATIBILITY         NOT ESTABLISHED
STRANDS SYSTEM PACKAGE        SOLIDIFIED
REPRESENTATIVE RECORD SET     NEAR-COMPLETE
MULTI-AGENT BASELINE          OPEN / BLOCKING
SCHEMA FREEZE                 NOT YET
MK2                           BLOCKED / DESIGN SEEDED
```
