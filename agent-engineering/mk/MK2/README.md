# MK2 — Operationalize

Status: **🔒 BLOCKED BY MK1**  
Mode: **DESIGN SEED / NOT ACTIVE CANON**

## Mission

Convert the stable classifications and normalized rules produced by MK1 into **operational engineering artifacts**:

- machine-readable contracts;
- schemas;
- checklists;
- test obligations;
- acceptance criteria;
- evidence receipts;
- promotion gates.

MK2 answers a different question from MK1:

```text
MK1: What kind of system is this, what authority does it have, and what is known?
MK2: What must be true, recorded and tested before we may build/operate/promote it?
```

## Activation boundary

MK2 implementation work does not begin until MK1 closes and freezes a classification-schema revision.

Transition contract: [`HANDOFF_CONTRACT.md`](./HANDOFF_CONTRACT.md).

Required incoming package:

```text
frozen MK1 schema
+ normalized dimensions/rules
+ complete representative record coverage
+ promoted principles with scope
+ revision-aware protocol receipts
+ routed UNKNOWNs
+ MK1 CLOSURE.md
```

Until that package exists, files here remain **design scaffolding**, not certified operational rules.

## Package map

| Artifact | Responsibility |
|---|---|
| [`HANDOFF_CONTRACT.md`](./HANDOFF_CONTRACT.md) | exact MK1→MK2 entry contract and traceability rules |
| [`CONTRACT_CATALOG.md`](./CONTRACT_CATALOG.md) | candidate operational contract families |
| [`SCHEMAS.md`](./SCHEMAS.md) | proposed machine-readable shapes for contracts/receipts |
| [`CHECKLISTS.md`](./CHECKLISTS.md) | human-operable pre-build/pre-release checks |
| [`TEST_MODEL.md`](./TEST_MODEL.md) | test/eval layers and adversarial fixture model |
| [`PROMOTION_GATE.md`](./PROMOTION_GATE.md) | MK2 entry/exit and promotion semantics |
| [`BACKLOG.md`](./BACKLOG.md) | work to execute after activation |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | operational questions that must remain visible |

## Planned contract families

```text
AgentSystemContract
ToolContract
CapabilityPolicy
SideEffectPolicy
HumanApprovalContract
RetryPolicy
TerminationPolicy
ConcurrencyPolicy
MemoryPolicy
ProtocolReceipt
EvidenceReceipt
EvaluationPlan
ReproducibilityReceipt
```

These remain design candidates until MK1 freezes the semantics they depend on.

## Traceability invariant

An MK2 contract must trace backward:

```text
MK2 operational rule
→ frozen MK1 dimension/principle
→ representative record
→ processed evidence
→ source receipt / pinned upstream source
```

Raw quarries do not become policy directly.

## Non-goals

MK2 does not:

- choose one framework;
- generate application code by default;
- certify a system because it satisfies a document template;
- replace runtime testing with checklists;
- promote source/tutorial claims directly into policy;
- reinterpret MK1 UNKNOWNs as favorable defaults;
- encode framework API names as universal contracts.

## Current incoming-package state

```text
representative records       NEAR-COMPLETE
  materialized/qualified     11
  COVERED_BY                 2
  open                       REC-012 multi-agent
MCP protocol evidence        PASS / QUALIFIED
A2A classification shape     PASS / QUALIFIED
A2A 1.0 compatibility        NOT ESTABLISHED / routed version debt
multi-agent baseline         OPEN / BLOCKING
UNKNOWN final routing        PENDING
MK1 schema freeze            NOT YET
MK1 closure receipt          NOT YET
MK2 handoff activation       BLOCKED
```

The A2A `1.0` compatibility debt does not become an MK2 assumption. Any operational A2A contract must pin the protocol revision it actually targets.

## Current blocker chain

```text
REC-012 multi-agent baseline
        ↓
final UNKNOWN reconciliation
        ↓
cross-dimension/schema freeze audit
        ↓
MK1 CLOSURE.md
        ↓
HANDOFF_CONTRACT activation
        ↓
MK2 OPEN
```

See [`../MK1/CLOSURE_PLAN.md`](../MK1/CLOSURE_PLAN.md).

## Current state

```text
MK0  Mine & Frame          ✅ CLOSED
MK1  Normalize & Classify  🟡 IN PROGRESS
MK2  Operationalize        🔒 BLOCKED / DESIGN SEEDED
MK3  Integrate             🔒 BLOCKED
MK4  Automate              🔒 BLOCKED
MK5+ Certify / Refine      🔒 BLOCKED
```
