# Agent Engineering — Roadmap

Status: **CURRENT EXECUTION ROADMAP**  
Current stage: **MK1 — Normalize & Classify**

`STATUS.md` answers **where are we?**  
This document answers **what sequence closes MK1 without skipping evidence?**

## Current snapshot

```text
MK0                              ✅ CLOSED

MK1                              🟡 ACTIVE
 ├─ Strands canonical package    ✅ SOLIDIFIED
 ├─ concurrency semantics        ✅ PROMOTED
 ├─ budget enforcement semantics ✅ PROMOTED
 ├─ intervention ownership       ✅ PROMOTED
 ├─ MCP 2026-07-28 / Strands     ✅ SUPPORTED / QUALIFIED
 ├─ representative records       ✅ 11 MATERIALIZED + 2 COVERED_BY
 ├─ A2A classification shape     ✅ PASS / QUALIFIED
 │   └─ A2A 1.0 compatibility    ⚠️ NOT ESTABLISHED / ROUTED DEBT
 ├─ multi-agent baseline         🟡 OPEN / BLOCKING
 ├─ final UNKNOWN reconciliation 🟡 PENDING
 └─ schema freeze audit          🔒 WAITS ON ABOVE

MK2                              🔒 BLOCKED / DESIGN SEEDED
```

## Closure dependency graph

```text
multi-agent baseline / REC-012
          ↓
final representative-set review
          ↓
UNKNOWN reconciliation
          ↓
cross-dimension + overlap audit
          ↓
schema freeze decision
    ┌─────┴─────┐
    │           │
  PASS         FAIL
    │           │
freeze mk1-v1   issue explicit new draft
    │           └→ rerun affected records
    ↓
MK1 CLOSURE.md
    ↓
MK2 handoff activation
```

## Workstream A — Representative records

State: **NEAR-COMPLETE**

Registry: [`mk/MK1/records/README.md`](./mk/MK1/records/README.md).

```text
11 MATERIALIZED / QUALIFIED
2  COVERED_BY
1  OPEN / BLOCKING → REC-012 multi-agent
```

Required families already represented:

- model-tool loop / bounded termination;
- consequential/HITL dispatcher enforcement;
- generated-code/browser high capability;
- external publication/safe mode/idempotency;
- document/data egress;
- database authority;
- evaluation/outcome-vs-trajectory;
- reflection/adaptation claim discipline;
- state/persistence/memory lifecycle;
- revision-aware MCP;
- modern mixed-control runtime.

The only remaining required family needing **new evidence**, rather than more normalization, is multi-agent benefit/admission.

## Workstream B — A2A protocol classification

State: **PASS / QUALIFIED FOR MK1 SHAPE**

Evidence contract: [`mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md`](./mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md).  
Receipt: [`quarries/strands-a2a-version-drift.md`](./quarries/strands-a2a-version-drift.md).

Established for the pinned Strands path:

```text
protocol family              A2A 0.3
Python dependency            >=0.3.0,<0.4.0
TypeScript dependency        ^0.3.10
client/server roles          represented
Agent Card/discovery         represented
invoke/stream/task shape     represented
context/concurrency boundary represented
security/auth boundary       represented / qualified
integration fixture source   present
specific CI PASS             not verified
independent run              not run
current A2A line             1.0
0.3 → 1.0 compatibility      NOT ESTABLISHED
```

The taxonomy gate is satisfied because the schema can represent all of those facts without collapsing to `A2A=true`.

A2A `1.0` migration/interoperability remains explicit system freshness debt and must not be reported as PASS.

## Workstream C — Multi-agent baseline

State: **OPEN / PRIMARY BLOCKER**

Contract: [`mk/MK1/MULTI_AGENT_BASELINE_SPEC.md`](./mk/MK1/MULTI_AGENT_BASELINE_SPEC.md).

One representative topology must be compared against a simpler baseline under the same task/evaluation contract.

The result may be positive, neutral, negative or inconclusive. The gate tests whether MK1 can represent independently:

- admission hypothesis;
- topology/authority split;
- outcome quality;
- latency;
- model/tool cost where measurable;
- coordination failures;
- termination behavior;
- benefit vs complexity.

A showcase run without a baseline does not pass.

## Workstream D — Final UNKNOWN reconciliation

State: **BLOCKED UNTIL REC-012 EXISTS**

Every remaining material UNKNOWN must become exactly one of:

```text
CLOSED
QUALIFIED
ROUTED_MK2
ROUTED_MK3_PLUS
ROUTED_MK5_PLUS
OUT_OF_SCOPE
```

No material `OPEN_MK1` item may survive closure.

Owner: [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md).

## Workstream E — Schema freeze audit

State: **BLOCKED UNTIL C + D**

Inputs:

- current schema/dimensions/rules;
- full representative record set;
- A2A receipt;
- multi-agent baseline/REC-012;
- GATES;
- UNKNOWN register;
- schema history.

Required decisions include:

1. Does every material family fit without framework-name taxonomy?
2. Does `data_egress` need a stronger confidentiality/data-classification dimension in MK1, or is that MK2 policy?
3. Do memory update-conflict/forgetting/evaluation fields belong in MK1 classification or MK2 operational contracts?
4. Are `horizon`, side-effect severity, human-control levels and evaluation fields orthogonal enough?
5. Are any dimensions duplicates under different names?
6. Can MK2 derive contracts without reopening basic vocabulary?
7. Is the resulting revision additive/clarifying/breaking?

Possible outcome:

```text
PASS → freeze mk1-draft-2026-09-16.1 as mk1-v1
FAIL → issue a new explicit draft and rerun only affected records
```

Do not create `mk1-v1` early.

## Workstream F — MK1 → MK2 handoff

State: **BLOCKED BY MK1 CLOSURE**

Contract: [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md).

MK2 receives only:

- frozen schema revision;
- normalized dimensions/rules;
- representative records;
- promoted principles with scope;
- revision-aware protocol receipts;
- routed UNKNOWNs;
- MK1 closure receipt.

Raw quarries do not become operational policy directly.

## Priority order

```text
P0  execute multi-agent baseline / materialize REC-012
P0  final UNKNOWN reconciliation
P0  cross-dimension + schema freeze audit
P1  issue new draft only if freeze audit requires it
P1  write MK1 CLOSURE.md
P1  activate MK2 handoff after PASS
P2  refresh A2A to 1.0 when Strands/current implementation evidence warrants it
P2  add additional system packages only when they add distinct evidence value
```

## Stop conditions

Do not open MK2 while any of these remain true:

- REC-012 lacks actual baseline evidence;
- material `OPEN_MK1` UNKNOWNs remain;
- schema overlap questions are unresolved;
- the schema still needs ordinary framework-specific exceptions;
- no frozen schema revision exists;
- `MK1/CLOSURE.md` does not exist.

## Definition of “well armed”

A new human or LLM should be able to answer without reconstructing history manually:

```text
where am I?
what is current?
what is historical evidence?
what remains unknown?
what exact gate is next?
what artifact must be created?
what evidence must it contain?
what would falsify the claim?
what does the next MK receive?
```

When MK1 closes, preserve this roadmap's completed state in the closure receipt and promote the active execution plan to MK2.
