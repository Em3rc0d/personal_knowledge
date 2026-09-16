# MK1 — Normalized Record Registry

Status: **ACTIVE**  
Schema: `mk1-draft-2026-09-16.1`

## Purpose

This registry tracks whether MK1's classification schema has been **materially instantiated against representative systems**, rather than merely discussed in prose.

A record is not considered complete because evidence exists somewhere in a quarry. It must have a normalized classification artifact or a canonical system classification linked here.

## Record states

```text
EVIDENCE_READY   enough source/quarry evidence exists to classify
IN_PROGRESS      normalization is being written/reconciled
MATERIALIZED     normalized record exists against current schema
QUALIFIED        materialized with explicit important UNKNOWNs/limits
BLOCKED          missing evidence prevents useful classification
SUPERSEDED       historical record replaced by a newer schema/revision
```

`QUALIFIED` is a valid completed record state when uncertainty is real and explicit.

## Required representative coverage

MK1 does not need one record for every tutorial or framework. It needs enough **materially different systems** to pressure-test every important dimension.

| ID | Representative system/family | Primary pressure | Evidence state | Normalized record |
|---|---|---|---|---|
| REC-001 | minimal while-loop agent | control authority, loop, termination | EVIDENCE_READY | OPEN |
| REC-002 | HITL approval agent | human control, dispatcher enforcement, edited action | EVIDENCE_READY | OPEN |
| REC-003 | trace-evaluation harness | outcome vs trajectory, evaluation evidence | EVIDENCE_READY | OPEN |
| REC-004 | generated-code / browser E2E agent | capability composition, sandbox/blast radius | EVIDENCE_READY | OPEN |
| REC-005 | self-healing generated-code agent | retry ownership, verifier boundary, code execution | EVIDENCE_READY | OPEN |
| REC-006 | HR outbound messaging agent | consequential external send, HITL/idempotency | EVIDENCE_READY | OPEN |
| REC-007 | social publishing agent | live publication, irreversible/visible effects | EVIDENCE_READY | OPEN |
| REC-008 | document-intake / file-egress agent | data egress, confidentiality, read-vs-side-effect distinction | EVIDENCE_READY | OPEN |
| REC-009 | DataScribe / database authority | DB read/write authority, lower-level dispatcher UNKNOWNs | EVIDENCE_READY | OPEN |
| REC-010 | reflection / self-improvement example | intrinsic correction vs external verification | EVIDENCE_READY | OPEN |
| REC-011 | representative memory system | context/session/persistence/memory lifecycle | EVIDENCE_READY | OPEN |
| REC-012 | representative multi-agent system | topology, admission hypothesis, baseline/benefit | BLOCKED/PARTIAL | waits on baseline evidence |
| REC-013 | legacy/current MCP integration example | protocol revision, lifecycle drift, auth boundary | EVIDENCE_READY | OPEN |
| REC-014 | Strands Agents SDK | modern runtime, mixed topology, concurrency/budgets/intervention/protocols | MATERIALIZED / QUALIFIED | [`../../../systems/strands/CLASSIFICATION.md`](../../../systems/strands/CLASSIFICATION.md) |

## Family coverage view

| Engineering family | Record coverage |
|---|---|
| deterministic / minimal control | REC-001 |
| model-tool loop | REC-001 / REC-014 |
| HITL / consequential mutation | REC-002 / REC-006 / REC-007 |
| generated code / browser / high capability | REC-004 / REC-005 |
| document / data egress | REC-008 |
| database authority | REC-009 |
| state / memory | REC-011 / REC-014 |
| evaluation / critic | REC-003 / REC-010 / REC-014 |
| multi-agent | REC-012 / REC-014 topology surfaces |
| protocol / interoperability | REC-013 / REC-014 MCP |
| modern agent runtime | REC-014 |

## Closure requirement

MK1 does **not** require all 14 rows to become separate long documents if some are redundant.

It does require:

1. every material engineering family above to have at least one normalized record;
2. P0/high-blast-radius examples to have explicit capability-composition and side-effect classification;
3. memory to be represented by lifecycle fields, not a boolean;
4. protocol examples to be revision-aware;
5. multi-agent to include admission/baseline fields rather than topology alone;
6. records to preserve UNKNOWN rather than infer missing implementation details;
7. architecture description to remain separate from production certification.

A closure audit may mark some queue entries `COVERED_BY` another record when there is no additional schema pressure. That decision must be explicit.

## Record location

Prefer one of two forms:

### Domain representative record

```text
mk/MK1/records/REC-xxx-<slug>.md
```

Use for tutorial/example/system records that exist primarily to pressure-test MK1.

### Canonical system record

```text
systems/<system>/CLASSIFICATION.md
```

Use when a complete current system package already exists. Do not duplicate the classification under `records/`; link it from this registry.

## Record contract

Every materialized record must identify:

```yaml
record_id:
schema_revision:
identity:
source_receipts:
evidence_scope:
classification:
material_unknowns:
production_certification: false | qualified-by-separate-evidence
```

Full template: [`TEMPLATE.md`](./TEMPLATE.md).

## Evidence sources already available

The initial queue is primarily backed by:

- `../../quarries/genai-agents.md`;
- `../../quarries/genai-agents-inventory.md`;
- `../../quarries/genai-agents-risk-scan.md`;
- `../../quarries/genai-agents-p0-p1-callpaths.md`;
- `../../quarries/cross-source-memory-production-mcp.md`;
- `../../quarries/runtime-semantics-strands-langgraph-openai.md`;
- `../../systems/strands/`.

Do not re-mine upstream by default when existing pinned evidence is sufficient. Re-open source only when a material classification field remains unsupported or freshness is required.

## Next materialization order

To maximize schema pressure while minimizing redundant work:

```text
1. REC-001 minimal while-loop
2. REC-002 HITL approval
3. REC-004 generated-code/browser E2E
4. REC-008 document/file egress
5. REC-011 memory
6. REC-013 protocol legacy/current MCP
7. REC-012 multi-agent after baseline evidence
8. fill additional records only where they add distinct pressure
```

This sequence is a work plan, not a ranking of system quality.
