# MK1 — Closure Plan

Status: **ACTIVE EXECUTION PLAN**  
Schema under evaluation: **`mk1-draft-2026-09-16.1`**

## Goal

Close MK1 only when the classification system is stable enough that MK2 can derive operational contracts **without reopening basic vocabulary, framework-specific exceptions or hidden assumptions**.

## Current gate graph

```text
REPRESENTATIVE RECORD SET
11 materialized + 2 COVERED_BY
        │
        ├── A2A classification shape ✅ PASS / QUALIFIED
        │      └── A2A 1.0 compatibility → routed version debt
        │
        └── REC-012 multi-agent 🟡 OPEN / BLOCKING
                         ↓
                UNKNOWN reconciliation
                         ↓
               cross-dimension audit
                         ↓
                schema freeze audit
                   ┌─────┴─────┐
                   │           │
                 PASS         FAIL
                   │           │
             freeze mk1-v1     new explicit draft
                   │           └→ rerun affected records
                   ↓
               MK1 CLOSURE.md
                   ↓
            MK2 HANDOFF activation
```

## Gate C1 — Representative records

State: **PASS EXCEPT REC-012**  
Owner: [`records/README.md`](./records/README.md)

Current coverage already includes:

- model-tool loop / shell / bounded termination;
- HITL / dispatcher enforcement;
- generated code + browser + host blast radius;
- publication / safe mode / idempotency;
- file/data egress;
- database effective authority;
- trace/outcome evaluation;
- reflection/adaptation claim discipline;
- state/persistence/memory lifecycle;
- protocol revision drift;
- modern mixed-control runtime.

Two redundant candidates are explicitly `COVERED_BY`; they are not silently omitted.

C1 fully passes when REC-012 materializes from actual multi-agent baseline evidence and final review confirms the `COVERED_BY` decisions hide no unique schema pressure.

## Gate C2 — A2A classification evidence

State: **PASS / QUALIFIED FOR MK1 CLASSIFICATION SHAPE**  
Contract: [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md)  
Receipt: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md)

Established:

```text
pinned Strands A2A family        0.3
current official A2A family      1.0
client/server/discovery shape    represented
invoke/stream/task semantics     represented
state/concurrency boundary       represented
security/auth boundary           represented / qualified
integration fixture source       present
specific successful CI receipt   not verified
independent rerun                not run
A2A 1.0 compatibility            NOT ESTABLISHED
```

The gate passes because MK1 can represent the implementation and its version drift without `A2A=true` or invented compatibility.

A2A `1.0` migration/interoperability remains **system freshness/version debt**, not an implicit PASS and not a taxonomy blocker.

## Gate C3 — Multi-agent baseline/admission evidence

State: **OPEN / PRIMARY EVIDENCE BLOCKER**  
Owner: [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md)

Pass when one representative topology has:

- explicit admission hypothesis;
- simpler baseline;
- equivalent task/eval contract;
- quality/outcome comparison;
- latency comparison;
- token/cost comparison when measurable;
- coordination/failure observations;
- termination behavior;
- neutral, positive, negative or inconclusive result recorded without changing the gate semantics.

The gate validates the classification/evidence model, not a general claim that multi-agent is superior.

## Gate C4 — UNKNOWN reconciliation

State: **BLOCKED UNTIL C3**  
Owner: [`UNKNOWNS.md`](./UNKNOWNS.md)

Not every UNKNOWN must be closed. Every material one must be exactly one of:

```text
CLOSED
QUALIFIED
ROUTED_MK2
ROUTED_MK3_PLUS
ROUTED_MK5_PLUS
OUT_OF_SCOPE
```

No `OPEN_MK1` item may survive closure.

## Gate C5 — Cross-dimension audit

State: **BLOCKED UNTIL COMPLETE REPRESENTATIVE SET**

The final set must preserve these distinctions independently:

```text
control authority != side-effect severity
capability != authorization
persistence != memory
persistence != concurrency safety
budget value != enforcement boundary
cancellation != rollback
HITL presence != dispatcher enforcement
structured output != semantic correctness
runtime termination != outcome verification
protocol interoperability != authorization
protocol family support != future/current revision compatibility
multi-agent topology != measured benefit
framework capability != deployment property
```

Explicit freeze questions include:

- whether `data_egress` needs stronger confidentiality/data-classification severity structure in MK1 or belongs to MK2 policy;
- whether memory update-conflict/forgetting/evaluation belongs in MK1 classification or MK2 operational contracts;
- whether `horizon`, H0–H4, sandbox and evaluation fields remain orthogonal and useful;
- whether nested child-agent authority is represented without framework-specific fields.

## Gate C6 — Schema freeze audit

Inputs:

- `CLASSIFICATION_SCHEMA.md`;
- `DIMENSIONS.md`;
- `NORMALIZATION_RULES.md`;
- full representative record set;
- `UNKNOWNS.md`;
- cross-runtime/protocol receipts;
- multi-agent baseline;
- `SCHEMA_HISTORY.md`.

Pass criteria:

1. ordinary representative systems require no framework-name taxonomy;
2. no material distinction is hidden in notes because the schema cannot represent it;
3. no two dimensions encode the same concept under different names;
4. optional fields do not force unsupported assumptions;
5. protocol records are revision-aware;
6. concurrency/budget/intervention qualifiers survive the full set;
7. all records remain interpretable under the proposed frozen revision;
8. unresolved facts are explicit UNKNOWNs rather than schema holes;
9. MK2 contract families map to stable MK1 dimensions;
10. final change type is recorded in `SCHEMA_HISTORY.md`.

Outcome:

```text
PASS → freeze mk1-draft-2026-09-16.1 as mk1-v1
or
FAIL → issue explicit additive/clarifying/breaking draft and rerun affected records
```

## Gate C7 — Closure receipt

After C1–C6 pass, create `CLOSURE.md` containing:

- closure date;
- frozen schema revision;
- exact record set;
- gates passed;
- important qualifications;
- UNKNOWN routing table;
- schema change history;
- explicit non-claims;
- MK2 handoff pointer.

Until then:

```text
MK1 = IN PROGRESS
```

## Gate C8 — MK2 handoff

Use [`../MK2/HANDOFF_CONTRACT.md`](../MK2/HANDOFF_CONTRACT.md).

MK2 opens only after the closure receipt names the exact frozen inputs.

## Work ordering

```text
1. execute multi-agent baseline / materialize REC-012
2. final representative-set review
3. reconcile UNKNOWNs
4. run cross-dimension + schema freeze audit
5. issue new draft only if audit requires it
6. write MK1 CLOSURE.md
7. activate MK2
```

## Anti-shortcut rules

Do not close MK1 because:

- the schema looks comprehensive;
- documentation is extensive;
- Strands fits it;
- A2A 0.3 has fixtures;
- A2A 1.0 debt seems likely to resolve later;
- multi-agent topology exists;
- MK2 scaffolding already exists.

Close MK1 only when representative evidence demonstrates the taxonomy is stable for its declared scope.
