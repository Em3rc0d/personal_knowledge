# MK1 → MK2 Handoff Contract

Status: **DESIGN CONTRACT / MK2 STILL BLOCKED**

## Purpose

Define the exact package MK2 is allowed to consume when MK1 closes.

This prevents MK2 from deriving operational policy directly from raw quarries, framework documentation or unresolved candidate semantics.

## Entry rule

MK2 opens only when MK1 has:

```text
CLOSURE.md = present
schema revision = FROZEN
representative record coverage = PASS
material UNKNOWN routing = complete
GATES.md = PASS
```

Until then:

```text
MK2 = BLOCKED / DESIGN SEEDED
```

## Required handoff inputs

### 1. Frozen classification schema

Must include:

- exact revision ID;
- schema shape;
- dimension definitions;
- normalization rules;
- schema history/change type;
- compatibility/migration note.

Expected source:

```text
MK1/CLASSIFICATION_SCHEMA.md
MK1/DIMENSIONS.md
MK1/NORMALIZATION_RULES.md
MK1/SCHEMA_HISTORY.md
```

### 2. Representative normalized records

Must demonstrate schema behavior across the material engineering families.

Expected source:

```text
MK1/records/README.md
+ materialized record files
+ canonical system CLASSIFICATION.md records linked by registry
```

MK2 uses these as examples/counterexamples when deriving contracts, not as universal templates.

### 3. Promoted principles

Only principles whose terminology survived MK1 normalization may become MK2 contract candidates.

Each promoted principle must carry:

```yaml
principle:
scope:
evidence_basis:
qualifications:
anti_claims:
related_dimensions:
```

A principle still marked candidate/UNKNOWN does not silently become policy.

### 4. Protocol receipts

Protocol-related MK2 work consumes **revision-aware receipts**, never protocol booleans.

Each relevant receipt should expose:

- revision;
- role;
- transport/binding;
- discovery/lifecycle semantics;
- authentication and authorization boundary;
- cancellation/unknown-outcome semantics;
- execution-evidence strength;
- explicit UNKNOWNs/version drift.

Current MK1 examples include:

- Strands MCP `2026-07-28` — supported/upstream-executed/qualified;
- Strands A2A `0.3` vs current A2A `1.0` — classification-shape PASS/qualified, with `1.0` compatibility explicitly **NOT ESTABLISHED**.

MK2 must pin whichever protocol revision a concrete operational contract targets. Routed version debt is not a compatibility default.

### 5. UNKNOWN routing table

Every material MK1 UNKNOWN must be categorized:

```text
CLOSED
QUALIFIED
ROUTED_MK2
ROUTED_MK3_PLUS
ROUTED_MK5_PLUS
OUT_OF_SCOPE
```

MK2 must not treat a routed UNKNOWN as an established invariant.

### 6. MK1 closure receipt

`MK1/CLOSURE.md` must state:

- closure date;
- frozen schema revision;
- gates passed;
- record set;
- important qualifications;
- explicit non-claims;
- open debt routed forward.

This becomes the authoritative transition receipt.

## What MK2 may derive

Once opened, MK2 may derive operational artifacts such as:

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

Names remain subject to MK2 design review; each must trace back to stable MK1 semantics.

## What MK2 must not do

MK2 must not:

- reopen framework-name taxonomy without evidence that MK1 failed;
- promote a quarry claim directly into policy;
- treat a framework feature as an application requirement;
- convert `UNKNOWN` into a default;
- infer production readiness from a classification record;
- require multi-agent architecture because one benchmark favored it;
- treat protocol interoperability as authorization;
- equate cancellation with rollback;
- infer A2A `1.0` compatibility from a Strands `0.3.x` receipt;
- encode one framework's API names as domain-level contracts.

## Traceability requirement

Every operational contract family should expose:

```yaml
contract_id:
source_mk1_dimensions:
source_principles:
evidence_examples:
unknowns_inherited:
test_obligations:
promotion_gate:
```

A reader should be able to move from an MK2 rule back to:

```text
MK2 contract
→ MK1 dimension/principle
→ representative record
→ quarry/evidence
→ source receipt
```

## Change after freeze

If later evidence proves a frozen MK1 semantic materially wrong:

1. do not silently patch MK2 only;
2. reopen/version MK1 classification semantics explicitly;
3. issue a new schema revision if needed;
4. identify affected MK2 contracts;
5. migrate with a traceable change receipt.

A frozen schema is stable input, not immutable truth.

## Activation checklist

Before changing this document's status from design/blocked to active handoff:

- [ ] MK1 `CLOSURE.md` exists;
- [ ] schema revision is frozen;
- [ ] `MK1/GATES.md` closure checklist passes;
- [ ] `MK1/records/README.md` shows required family coverage;
- [x] A2A protocol debt is represented and current-version compatibility debt is explicitly routed without becoming a false PASS;
- [ ] multi-agent baseline gate passes;
- [ ] MK1 UNKNOWNs are fully routed;
- [ ] `STATUS.md` changes MK2 from BLOCKED to ACTIVE.

## Current state

```text
MK1 schema                  mk1-draft-2026-09-16.1 / ACTIVE DRAFT
representative records      11 MATERIALIZED/QUALIFIED + 2 COVERED_BY + REC-012 OPEN
A2A classification shape    PASS / QUALIFIED
A2A 1.0 compatibility       NOT ESTABLISHED / ROUTED DEBT
multi-agent baseline        OPEN / BLOCKING
MK1 closure                 NOT YET
MK2 handoff                 NOT ACTIVE
MK2 status                  BLOCKED / DESIGN SEEDED
```
