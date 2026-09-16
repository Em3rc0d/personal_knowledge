# Agent Engineering — Roadmap

Status: **CURRENT EXECUTION ROADMAP**  
Current stage: **MK1 — Normalize & Classify**

`STATUS.md` answers **what state are we in now?**  
This document answers **what sequence closes the current stage without skipping evidence?**

## Current snapshot

```text
MK0                              ✅ CLOSED

MK1                              🟡 ACTIVE
 ├─ Strands canonical package    ✅ SOLIDIFIED
 ├─ concurrency semantics        ✅ PROMOTED
 ├─ budget enforcement semantics ✅ PROMOTED
 ├─ intervention ownership       ✅ PROMOTED
 ├─ MCP 2026-07-28 / Strands     ✅ SUPPORTED / QUALIFIED
 ├─ record infrastructure        ✅ READY
 ├─ representative records       🟡 PARTIAL (4 materialized)
 ├─ A2A reproducibility receipt  🟡 OPEN
 ├─ multi-agent baseline         🟡 OPEN
 └─ schema freeze audit          🔒 WAITS ON ABOVE

MK2                              🔒 BLOCKED / DESIGN SEEDED
```

## Execution principle

Do not work by topic popularity. Work by **closure dependency and remaining schema pressure**.

```text
representative records
        ├──────────────┐
        │              │
A2A evidence           │
        │              ▼
        └──────► schema pressure / UNKNOWN reconciliation
                       │
multi-agent baseline ──┘
                       │
                       ▼
                 schema freeze audit
                       │
                       ▼
                    MK1 PASS
                       │
                       ▼
               MK1 → MK2 handoff
                       │
                       ▼
                    MK2 OPEN
```

## Workstream A — Representative MK1 records

State: **PARTIAL**

Registry: [`mk/MK1/records/README.md`](./mk/MK1/records/README.md).

Materialized now:

```text
REC-001 minimal while-loop
REC-002 HITL approval
REC-013 MCP revision drift
REC-014 Strands Agents
```

Highest remaining pressure:

```text
REC-004 generated-code/browser E2E
REC-008 document/file egress
REC-011 dedicated memory lifecycle
REC-003 trace-evaluation/critic
REC-012 multi-agent after baseline evidence
```

Minimum closure expectations:

- control/model-tool loop;
- consequential/HITL system;
- generated-code/browser or high-capability system;
- data-egress system;
- memory/state system;
- evaluator/critic system;
- multi-agent system;
- revision-aware protocol system;
- modern runtime/framework.

Acceptance:

```text
for each required family:
  normalized record exists or explicit COVERED_BY decision
  source/snapshot pinned
  material UNKNOWNs explicit
  architecture != production certification
  no framework-name taxonomy
```

## Workstream B — A2A reproducibility receipt

State: **OPEN**

Purpose: convert `A2A supported` from a feature statement into a revision-aware interoperability record.

Evidence contract: [`mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md`](./mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md).

Must establish for a pinned implementation path:

- protocol revision/spec identity;
- role(s);
- discovery/identity semantics;
- transport;
- authentication/authorization boundary;
- invocation/task lifecycle;
- cancellation/unknown-outcome semantics;
- observability/trace continuity if available;
- implementation snapshot/dependency receipt;
- execution evidence or explicit `NOT_RUN` reason.

Not required:

- universal A2A interoperability;
- universal security certification;
- production SLO evidence.

## Workstream C — Multi-agent baseline

State: **OPEN**

Contract: [`mk/MK1/MULTI_AGENT_BASELINE_SPEC.md`](./mk/MK1/MULTI_AGENT_BASELINE_SPEC.md).

At least one representative topology must be compared against a simpler baseline under the same task/evaluation contract.

The repository must be able to represent independently:

- admission hypothesis;
- topology;
- authority/task partitioning;
- coordination cost;
- quality/outcome;
- latency;
- tokens/cost where measurable;
- failure/termination behavior.

A neutral/no-gain result is valid evidence.

## Workstream D — Schema freeze audit

State: **BLOCKED until A/B/C are sufficiently complete**

Inputs:

- current schema;
- representative records;
- A2A receipt;
- multi-agent baseline;
- GATES;
- UNKNOWN register;
- schema history.

Questions:

1. Does every material family fit without a new top-level category?
2. Are dimensions orthogonal enough to avoid misleading collapse?
3. Are concurrency/budget/intervention qualifiers stable?
4. Are protocols revision-aware?
5. Can multi-agent benefit remain independent from topology?
6. Can `UNKNOWN` survive without form-filling pressure?
7. Can MK2 derive contracts without reopening terminology?
8. Are any fields framework-specific accidents?
9. Are any fields duplicated under different names?
10. Is the final change additive/clarifying/breaking?

Possible outcomes:

```text
FREEZE mk1-draft-2026-09-16.1 as mk1-v1
or
ISSUE another explicit draft revision and rerun affected records
```

Do not rename a draft to `v1` until the gate passes.

## Workstream E — MK1 → MK2 handoff

State: **BLOCKED by MK1 closure**

Contract: [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md).

MK2 may open only when it receives:

- frozen schema revision;
- normalized dimension definitions;
- representative records;
- promoted principles with scope;
- explicit UNKNOWN routing;
- evidence/protocol receipts;
- MK1 closure receipt.

## Priority order

```text
P0  REC-004 generated-code/browser record
P0  REC-008 data-egress record
P0  REC-011 memory-lifecycle record
P0  A2A revision/auth/transport receipt
P0  multi-agent baseline / REC-012
P1  REC-003 evaluation record
P1  remaining non-redundant pressure records
P1  UNKNOWN reconciliation
P1  schema freeze audit
P1  MK1 closure receipt
P1  activate MK2 handoff
P2  add more system packages only when evidence warrants them
```

## Stop conditions

Do not open MK2 while any of these remain true:

- ordinary representative systems still force schema invention;
- major families exist only as quarry evidence, not normalized records;
- protocol records collapse to booleans;
- multi-agent remains an untested architecture preference;
- material `OPEN_MK1` UNKNOWNs remain;
- MK2 contract families depend on undefined MK1 vocabulary.

## Definition of “well armed”

A new human or LLM should be able to answer without reconstructing history manually:

```text
where am I?
what is current?
what is evidence?
what is historical?
what remains unknown?
what exact gate is next?
what artifact do I create?
what evidence must it contain?
what would falsify the claim?
what does the next MK receive?
```

When MK1 closes, preserve this roadmap's completed state in the closure receipt and replace its active execution section with the MK2 roadmap.
