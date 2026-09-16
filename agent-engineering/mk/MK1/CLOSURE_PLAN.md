# MK1 — Closure Plan

Status: **ACTIVE EXECUTION PLAN**  
Schema under evaluation: **`mk1-draft-2026-09-16.1`**

## Goal

Close MK1 only when the classification system is stable enough that MK2 can derive operational contracts **without reopening basic vocabulary, framework-specific exceptions or hidden assumptions**.

This document converts the broad checklist in `GATES.md` into an executable dependency plan.

## Current gate graph

```text
                    ┌─────────────────────────────┐
                    │ REPRESENTATIVE RECORD SET   │
                    │ records/README.md           │
                    └──────────────┬──────────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
   ┌─────────────────┐   ┌─────────────────┐   ┌────────────────────┐
   │ A2A RECEIPT     │   │ MULTI-AGENT     │   │ HIGH-RISK RECORDS  │
   │ revision/auth/  │   │ BASELINE        │   │ capability/effects │
   │ transport/eval  │   │ admission test  │   │ HITL/egress/etc.   │
   └────────┬────────┘   └────────┬────────┘   └─────────┬──────────┘
            │                     │                      │
            └─────────────────────┴──────────────────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │ SCHEMA FREEZE AUDIT    │
                     │ dimensions + records  │
                     │ unknown reconciliation│
                     └────────────┬───────────┘
                                  │
                     ┌────────────▼───────────┐
                     │ MK1 CLOSURE RECEIPT    │
                     │ freeze schema revision│
                     └────────────┬───────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │ MK2 HANDOFF CONTRACT   │
                     └────────────────────────┘
```

## Gate C1 — Representative records materialized

Owner artifact: [`records/README.md`](./records/README.md)

Pass when:

- every required engineering family has at least one normalized record;
- P0/high-capability cases include capability composition;
- consequential systems reconstruct dispatcher/effect/verification boundaries;
- memory is lifecycle-classified;
- protocol records are revision-aware;
- material UNKNOWNs are visible;
- records explicitly deny production certification unless separate evidence exists.

Do not require redundant records that add no schema pressure. Mark them `COVERED_BY` during closure review if justified.

## Gate C2 — A2A reproducibility evidence

Owner artifact: [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md)

Pass when at least one current A2A path relevant to the studied runtime ecosystem has a pinned, reproducible receipt covering the minimum contract:

```text
spec/revision
implementation snapshot
authoritative role
transport
discovery/identity
invocation/task lifecycle
auth boundary
cancellation / unknown-outcome semantics
execution evidence or explicit environment block
```

It is acceptable for security or universal interoperability to remain qualified/unknown. It is not acceptable to represent `A2A=true` as the whole protocol classification.

## Gate C3 — Multi-agent baseline/admission evidence

Owner artifact: [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md)

Pass when one representative topology has:

- explicit admission hypothesis;
- simpler baseline;
- equivalent task/eval contract;
- quality/outcome comparison;
- latency comparison;
- token/cost comparison when available;
- coordination/failure observations;
- termination behavior;
- result that can be neutral, positive or negative without changing the gate semantics.

This gate validates the **classification/evidence model**, not a claim that multi-agent is generally superior.

## Gate C4 — Cross-dimension audit

Pass when normalized records demonstrate these distinctions remain independently expressible:

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
multi-agent topology != measured benefit
framework capability != deployment property
```

If a representative record cannot express one distinction cleanly, MK1 remains open.

## Gate C5 — Schema freeze audit

Inputs:

- `CLASSIFICATION_SCHEMA.md`;
- `DIMENSIONS.md`;
- `NORMALIZATION_RULES.md`;
- representative records;
- `UNKNOWNS.md`;
- cross-runtime receipts;
- protocol receipts;
- multi-agent baseline.

Pass criteria:

1. no ordinary representative system requires a framework-name field;
2. no material distinction is hidden in free-form notes because the schema cannot express it;
3. no two dimensions encode the same concept under different names;
4. optional fields do not force unsupported assumptions;
5. protocol representation is revision-aware;
6. concurrency/budget/intervention qualifiers survive the representative set;
7. current records remain interpretable under the proposed frozen revision;
8. unresolved facts are explicit UNKNOWNs, not schema holes;
9. downstream MK2 contract families map to stable MK1 dimensions;
10. schema change type is declared in `SCHEMA_HISTORY.md`.

Possible result:

```text
PASS → freeze as mk1-v1
or
FAIL → issue additive/clarifying/breaking draft and rerun affected records
```

## Gate C6 — UNKNOWN reconciliation

Not every UNKNOWN must be closed.

Every material UNKNOWN must be in exactly one state:

```text
CLOSED
ROUTED_TO_MK2
ROUTED_TO_MK3+
ROUTED_TO_MK5+
OUT_OF_SCOPE
BLOCKS_MK1
```

MK1 cannot close while a material item is simultaneously marked `UNKNOWN` and implicitly assumed by a promoted rule.

## Gate C7 — Closure receipt

When C1–C6 pass, create `CLOSURE.md` under MK1 containing:

- closure date;
- frozen schema revision;
- exact record set used;
- gates passed;
- known qualifications;
- UNKNOWN routing table;
- schema change history;
- explicit non-claims;
- MK2 handoff pointer.

Until that file exists and gates pass:

```text
MK1 = IN PROGRESS
```

## Gate C8 — MK2 handoff

Use [`../MK2/HANDOFF_CONTRACT.md`](../MK2/HANDOFF_CONTRACT.md).

MK2 opens only after the closure receipt names the exact frozen inputs.

## Work ordering

```text
1. materialize minimal high-pressure records
2. close A2A evidence contract
3. execute multi-agent baseline contract
4. complete record family coverage
5. reconcile UNKNOWNs
6. run schema freeze audit
7. write MK1 CLOSURE.md
8. activate MK2
```

Steps 1–4 may run in parallel where evidence is independent. Steps 5–8 are ordered gates.

## Anti-shortcut rules

Do not close MK1 because:

- the schema “looks comprehensive”;
- Strands fits it;
- three frameworks share one runtime semantic;
- documentation is extensive;
- MK2 scaffolding already exists;
- the remaining unknowns seem likely to resolve favorably.

Close MK1 only because representative evidence demonstrates the taxonomy is stable for its declared scope.
