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
 ├─ representative records       🟡 OPEN
 ├─ A2A reproducibility receipt  🟡 OPEN
 ├─ multi-agent baseline         🟡 OPEN
 └─ schema freeze audit          🔒 WAITS ON ABOVE

MK2                              🔒 BLOCKED / DESIGN SEEDED
```

## Execution principle

Do not work by topic popularity. Work by **closure dependency**.

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

State: **OPEN**

Purpose: prove the schema can classify materially different systems without creating framework-specific fields or hiding UNKNOWNs.

Required coverage is tracked in [`mk/MK1/RECORDS.md`](./mk/MK1/RECORDS.md).

Minimum closure expectations:

- deterministic/single-call or workflow-like system;
- model-tool loop;
- consequential/HITL system;
- generated-code/browser or high-capability system;
- memory/state system;
- evaluator/critic or trace-evaluation system;
- multi-agent system;
- revision-aware protocol/integration system;
- modern runtime/framework pressure test.

Acceptance:

```text
for each required family:
  normalized record exists
  source/snapshot pinned
  material UNKNOWNs explicit
  architecture != production certification
  no framework-name taxonomy
```

## Workstream B — A2A reproducibility receipt

State: **OPEN**

Purpose: convert `A2A supported` from a feature statement into a revision-aware interoperability record.

Evidence contract: [`mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md`](./mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md).

Must establish, for the selected pinned implementation path:

- protocol revision/spec identity;
- role(s): client/server/remote agent;
- discovery/card/identity semantics where applicable;
- transport;
- authentication/authorization boundary;
- invocation/task lifecycle;
- cancellation/unknown-outcome semantics;
- observability/trace continuity if available;
- implementation snapshot/dependency receipt;
- actual execution evidence or an explicit `NOT_RUN` reason.

Not required for MK1 closure:

- proving every A2A implementation interoperates;
- universal security certification;
- production SLO evidence.

## Workstream C — Multi-agent baseline

State: **OPEN**

Purpose: prevent `multi-agent` from becoming a maturity label or unmeasured architecture preference.

Benchmark/admission contract: [`mk/MK1/MULTI_AGENT_BASELINE_SPEC.md`](./mk/MK1/MULTI_AGENT_BASELINE_SPEC.md).

At minimum one representative multi-agent topology must be compared against a simpler baseline under the same task/evaluation contract.

The objective is not to prove multi-agent is better. It is to establish that the repository can represent:

- admission hypothesis;
- topology;
- task partitioning;
- coordination cost;
- quality/outcome;
- latency;
- token/cost footprint;
- failure/termination behavior;
- conditions where complexity is or is not justified.

A neutral/no-gain result is valid evidence.

## Workstream D — Schema freeze audit

State: **BLOCKED until A/B/C are sufficiently complete**

Inputs:

- current schema;
- representative records;
- protocol receipt;
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
10. Is the revision additive/clarifying/breaking relative to prior records?

Possible outcomes:

```text
FREEZE mk1-draft-2026-09-16.1 as mk1-v1
or
ISSUE additive draft mk1-draft-...
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
- explicit UNKNOWNs routed forward;
- evidence/protocol receipts;
- closure receipt.

MK2 must not consume raw quarries as if they were operational policy.

## Priority order

```text
P0  finish representative record registry + highest-value records
P0  A2A revision/auth/transport receipt
P0  multi-agent baseline/admission evidence
P1  schema freeze audit
P1  MK1 closure receipt
P1  activate MK2 handoff
P2  expand system packages beyond Strands when evidence warrants it
```

## Stop conditions

Do not open MK2 if any of these remain true:

- schema still changes to accommodate ordinary representative systems;
- representative records are mostly implied rather than materialized;
- protocol records collapse to booleans;
- multi-agent remains an untested architectural preference;
- material UNKNOWNs are hidden or implicitly assumed;
- MK2 contract families require undefined MK1 vocabulary.

## Definition of “well armed” for this domain

The repository is operationally well-armed when a new human or LLM can answer, without reconstructing history manually:

```text
where am I?
what is current?
what is evidence?
what is historical?
what remains unknown?
what exact gate is next?
what artifact do I create?
what evidence must it contain?
what would make the claim invalid?
what does the next MK receive?
```

This roadmap is intentionally finite. When MK1 closes, archive its active sequence into the closure receipt and update this document to the MK2 execution plan.
