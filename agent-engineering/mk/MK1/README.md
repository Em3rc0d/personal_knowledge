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

MK1 does **not** yet define the full operational policy a production system must satisfy. That is MK2.

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
| [`CLASSIFICATION_QUEUE.md`](./CLASSIFICATION_QUEUE.md) | priority/admission logic for remaining records |
| [`STRANDS_AGENTS_PRESSURE_TEST.md`](./STRANDS_AGENTS_PRESSURE_TEST.md) | historical first-pass Strands pressure-test receipt |

### Closure control

| Artifact | Responsibility |
|---|---|
| [`GATES.md`](./GATES.md) | formal closure checklist |
| [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md) | executable dependency plan for closing MK1 |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | uncertainty register and routing |
| [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md) | protocol evidence contract for the open A2A gate |
| [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md) | admission/baseline contract for multi-agent evidence |

## Current system synthesis

Do not reconstruct current framework knowledge from historical pressure tests when a canonical system package exists.

Current complete package:

```text
../../systems/strands/
├── README.md
├── CLASSIFICATION.md
├── ENGINEERING_RULES.md
├── PROTOCOLS.md
├── EVIDENCE.md
└── LLM_CONTEXT.md
```

For Strands:

- human mental model → [`../../systems/strands/README.md`](../../systems/strands/README.md)
- current normalized profile → [`../../systems/strands/CLASSIFICATION.md`](../../systems/strands/CLASSIFICATION.md)
- protocols → [`../../systems/strands/PROTOCOLS.md`](../../systems/strands/PROTOCOLS.md)
- provenance → [`../../systems/strands/EVIDENCE.md`](../../systems/strands/EVIDENCE.md)
- machine context → [`../../systems/strands/LLM_CONTEXT.md`](../../systems/strands/LLM_CONTEXT.md)

## Core classification principle

> Classify what the system can actually decide and do, not what the repository/framework calls it.

A single SDK may expose deterministic workflows, model-routed branches, model-directed loops, peer handoffs and remote-agent protocols. Framework identity therefore cannot substitute for architecture classification.

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

## Current normalized records

Materialized/qualified records currently include:

```text
REC-001  minimal while-loop agent
REC-002  HITL approval agent
REC-013  MCP legacy/current revision-drift comparison
REC-014  Strands Agents SDK (canonical system classification)
```

See [`records/README.md`](./records/README.md) for live coverage and remaining gaps.

The representative set exists to **pressure-test the schema**, not to build a catalog for its own sake.

## Cross-runtime promotion already closed

The first Strands pass surfaced three distinctions:

1. concurrency semantics;
2. budget enforcement boundary / overshoot;
3. intervention enforcement owner/boundary.

They were not promoted from Strands alone. Independent contrast against LangGraph and OpenAI Agents SDK confirmed them as reusable engineering semantics.

Current mapping:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

Schema revision: `mk1-draft-2026-09-16.1`.

## MCP revision-aware gate already closed for Strands

The Strands MCP path is no longer represented as `MCP=true`.

Current scoped evidence:

```text
revision                     2026-07-28
core interoperability        SUPPORTED / UPSTREAM-EXECUTED
modern lifecycle             REGRESSION-TESTED
Streamable HTTP              UPSTREAM-EXECUTED
MRTR/prompts/resources       SUPPORTED BY PINNED FIXTURE
list-changed subscription    UPSTREAM-EXECUTED
trace continuity             UPSTREAM E2E TESTED
auth adapter                 SUPPORTED / deployment authorization separate
remote rollback on cancel    NOT IMPLIED
independent local rerun      ENVIRONMENT-BLOCKED
```

Evidence: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

This closes one implementation path. The broader A2A protocol gate remains open under [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md).

## Remaining closure blockers

```text
representative high-pressure records      OPEN
A2A revision/auth/transport receipt        OPEN
multi-agent baseline/admission evidence    OPEN
schema freeze audit                        BLOCKED BY ABOVE
MK1 CLOSURE.md                             NOT YET
MK2 activation                             BLOCKED
```

Execution order: [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md).

## Historical-document rule

Historical receipts are intentionally preserved.

If `STRANDS_AGENTS_PRESSURE_TEST.md` says a field is a candidate or MCP execution is open, interpret that as the state of the **first pass**, not current domain truth.

Current-state precedence remains:

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
+ representative materialized records
+ protocol evidence
+ multi-agent admission evidence
+ routed UNKNOWNs
+ closure receipt
```

Then, and only then, MK2 receives the package defined by [`../MK2/HANDOFF_CONTRACT.md`](../MK2/HANDOFF_CONTRACT.md).

## State transition

```text
MK0 evidence/framing                 ✅ CLOSED
        ↓
MK1 normalize/classify               🟡 CURRENT
        ↓
representative records + gates
        ↓
schema freeze audit
        ↓
MK1 closure receipt
        ↓
MK2 handoff                          🔒 BLOCKED UNTIL PASS
```

## Current promotion state

```text
MK0                           CLOSED
MK1                           IN PROGRESS
SCHEMA                        mk1-draft-2026-09-16.1
RUNTIME SEMANTICS CROSSCHECK  PASS
STRANDS MCP 2026-07-28        SUPPORTED / QUALIFIED
STRANDS SYSTEM PACKAGE        SOLIDIFIED
REPRESENTATIVE RECORD SET     PARTIAL
A2A RECEIPT                   OPEN
MULTI-AGENT BASELINE          OPEN
SCHEMA FREEZE                 NOT YET
MK2                           BLOCKED / DESIGN SEEDED
```
