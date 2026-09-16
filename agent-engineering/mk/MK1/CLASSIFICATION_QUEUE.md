# MK1 — Classification Queue

Status: **ACTIVE / RECORD-DRIVEN**  
Schema: **`mk1-draft-2026-09-16.1`**

## Purpose

This queue defines **which representative systems still need classification pressure and why**.

The authoritative record/materialization state now lives in [`records/README.md`](./records/README.md). This file owns **priority and admission logic**, not duplicate record status.

## Current pressure set

The original first set remains useful, but it is now tracked by record IDs:

```text
REC-001 minimal while-loop agent
REC-002 HITL approval agent
REC-003 trace-evaluation harness
REC-004 generated-code/browser E2E agent
REC-005 self-healing generated-code agent
REC-006 HR messaging agent
REC-007 social publishing agent
REC-008 document-intake/file-egress agent
REC-009 DataScribe/database authority
REC-010 reflection/self-improvement example
REC-011 representative memory system
REC-012 representative multi-agent system
REC-013 legacy/current MCP comparison
REC-014 Strands Agents SDK
```

See [`records/README.md`](./records/README.md) for materialized/open/blocked state.

## Current priority

The highest remaining schema pressure is:

```text
P0  REC-004 generated-code/browser capability composition
P0  REC-008 document/file egress
P0  REC-011 memory lifecycle
P0  REC-012 multi-agent baseline/admission evidence
P0  A2A revision/auth/transport receipt
P1  REC-003 trace-evaluation harness
P1  REC-009 database authority if it adds distinct dispatcher pressure
P2  REC-005/006/007/010 only where they add non-redundant dimensions
```

REC-001, REC-002, REC-013 and REC-014 are already materialized/qualified.

## Strands pressure-test disposition

Strands originally surfaced three candidate qualifiers:

1. concurrency semantics;
2. budget enforcement boundary / overshoot semantics;
3. intervention enforcement owner.

Those are **no longer pending candidates**.

Independent contrast against LangGraph and OpenAI Agents SDK satisfied the admission rule, and schema revision `mk1-draft-2026-09-16.1` promoted them as:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Historical receipt: [`STRANDS_AGENTS_PRESSURE_TEST.md`](./STRANDS_AGENTS_PRESSURE_TEST.md).  
Cross-runtime promotion evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

## Classification workflow

```text
select representative record
    ↓
verify existing pinned evidence first
    ↓
re-open source only if material evidence is missing/stale
    ↓
fill normalized record against current schema
    ↓
mark unsupported facts UNKNOWN
    ↓
reconstruct capability/effect path where consequential
    ↓
identify schema pressure / overlap / contradiction
    ↓
compare against existing records
    ↓
change schema only if admission rule is satisfied
    ↓
update record registry + gates/unknowns if state changed
```

## Required family coverage

Before MK1 closes, the materialized record set must cover:

- minimal/deterministic or model-directed control;
- model-tool loop;
- high-capability generated-code/browser path;
- consequential/HITL mutation;
- document/data-egress path;
- database authority where distinct;
- state/memory lifecycle;
- evaluator/critic/evaluation path;
- multi-agent topology + benefit evidence;
- revision-aware protocol/integration;
- modern runtime/framework.

The closure audit may mark redundant queue entries `COVERED_BY` another record rather than creating documents for their own sake.

## Admission rule for schema changes

Do not add a new top-level axis because one framework exposes a new class or field.

A schema change should be introduced only when:

1. existing fields cannot represent a material engineering difference without distortion;
2. the difference affects behavior, risk, reliability, evaluation or reproducibility;
3. at least two independent examples or one strong counterexample justify it;
4. the field does not duplicate another dimension;
5. change type is recorded in [`SCHEMA_HISTORY.md`](./SCHEMA_HISTORY.md).

Framework-specific terms remain evidence vocabulary, not domain taxonomy.

## Separate open gates

Two closure blockers are not ordinary record-writing tasks:

- A2A protocol receipt → [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md)
- multi-agent baseline/admission evidence → [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md)

They feed both representative records and the schema freeze audit.

## Output expectation

MK1 ends with:

```text
frozen framework-independent schema
+ representative normalized records
+ explicit UNKNOWN routing
+ protocol receipts
+ multi-agent admission evidence
+ closure receipt
```

Only then may MK2 operationalize the surviving semantics.
