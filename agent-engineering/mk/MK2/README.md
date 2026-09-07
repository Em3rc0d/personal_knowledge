# MK2 — Operationalize

Status: **BLOCKED BY MK1**  
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

## Precondition

MK2 implementation work does not begin until MK1 closes and freezes a classification-schema version suitable as input.

The files in this directory are therefore **design scaffolding**, not certified rules.

## Package map

- [`CONTRACT_CATALOG.md`](./CONTRACT_CATALOG.md) — operational contract families to derive from MK1.
- [`SCHEMAS.md`](./SCHEMAS.md) — proposed machine-readable shapes for contracts and receipts.
- [`CHECKLISTS.md`](./CHECKLISTS.md) — human-operable pre-build/pre-release checks.
- [`TEST_MODEL.md`](./TEST_MODEL.md) — required test/eval layers and adversarial fixtures.
- [`PROMOTION_GATE.md`](./PROMOTION_GATE.md) — MK2 entry/exit criteria and promotion semantics.
- [`BACKLOG.md`](./BACKLOG.md) — work to execute once MK1 unblocks MK2.
- [`UNKNOWNS.md`](./UNKNOWNS.md) — unresolved operational questions that must not be hidden.

## Planned contract families

```text
AgentSystemContract
ToolContract
CapabilityPolicy
SideEffectPolicy
HumanApprovalContract
RetryPolicy
TerminationPolicy
MemoryPolicy
EvidenceReceipt
ProtocolReceipt
EvaluationPlan
ReproducibilityReceipt
```

These names are provisional until MK1 pressure-testing proves the underlying dimensions are stable.

## Non-goals

MK2 does not:

- choose one framework;
- generate application code by default;
- certify a system merely because it satisfies a document template;
- replace runtime testing with checklists;
- allow a source/tutorial claim to become policy without normalized evidence.

## Current state

```text
MK0  Mine & Frame          ✅ CLOSED
MK1  Normalize & Classify  🟡 IN PROGRESS
MK2  Operationalize        🔒 BLOCKED / DESIGN SEED ONLY
MK3  Integrate             🔒 BLOCKED
MK4  Automate              🔒 BLOCKED
MK5+ Certify / Refine      🔒 BLOCKED
```
