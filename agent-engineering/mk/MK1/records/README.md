# MK1 — Normalized Record Registry

Status: **ACTIVE / REPRESENTATIVE COVERAGE NEAR-COMPLETE**  
Schema: `mk1-draft-2026-09-16.1`

## Purpose

This registry tracks whether MK1's classification schema has been **materially instantiated against representative systems**, rather than merely discussed in prose.

Evidence in a quarry is not enough for closure. A required family must have either:

- a normalized record against the current schema; or
- an explicit `COVERED_BY` decision showing why another record already provides the same schema pressure.

## Record states

```text
EVIDENCE_READY   enough source/quarry evidence exists to classify
IN_PROGRESS      normalization is being written/reconciled
MATERIALIZED     normalized record exists against current schema
QUALIFIED        materialized with explicit important UNKNOWNs/limits
BLOCKED          missing evidence prevents useful classification
COVERED_BY       another normalized record/set already supplies the material schema pressure
SUPERSEDED       historical record replaced by a newer schema/revision
```

`QUALIFIED` is a valid completed record state when uncertainty is real and explicit.

## Record registry

| ID | Representative system/family | Primary pressure | State | Normalized record / coverage |
|---|---|---|---|---|
| REC-001 | minimal while-loop agent | control authority, loop, termination, shell capability | **MATERIALIZED / QUALIFIED** | [`REC-001-minimal-while-loop.md`](./REC-001-minimal-while-loop.md) |
| REC-002 | HITL approval agent | human control, dispatcher enforcement, edited action | **MATERIALIZED / QUALIFIED** | [`REC-002-hitl-approval.md`](./REC-002-hitl-approval.md) |
| REC-003 | trace-evaluation harness | outcome vs trajectory, evaluation evidence | **MATERIALIZED / QUALIFIED** | [`REC-003-trace-evaluation-harness.md`](./REC-003-trace-evaluation-harness.md) |
| REC-004 | generated-code/browser E2E agent | capability composition, sandbox/blast radius | **MATERIALIZED / QUALIFIED** | [`REC-004-generated-code-browser-e2e.md`](./REC-004-generated-code-browser-e2e.md) |
| REC-005 | self-healing generated-code agent | generated-code execution + verifier/promotion boundary | **COVERED_BY** | REC-004 covers generated-code execution; REC-003 covers verification/gating separation. Upstream evidence remains in P0/P1 quarry. |
| REC-006 | HR outbound messaging agent | external send + incomplete approval coverage | **COVERED_BY** | REC-002 covers dispatcher-enforced HITL positive case; REC-007 covers external-send/publication mutation. HR-specific approval gap remains preserved in quarry/UNKNOWN evidence. |
| REC-007 | social publishing agent | live publication, dry-run enforcement, idempotency | **MATERIALIZED / QUALIFIED** | [`REC-007-social-publication.md`](./REC-007-social-publication.md) |
| REC-008 | document-intake/file-egress agent | data egress, confidentiality, read-vs-side-effect distinction | **MATERIALIZED / QUALIFIED** | [`REC-008-document-data-egress.md`](./REC-008-document-data-egress.md) |
| REC-009 | DataScribe/database authority | effective DB credential authority, lower-level dispatcher UNKNOWNs | **MATERIALIZED / QUALIFIED** | [`REC-009-database-authority.md`](./REC-009-database-authority.md) |
| REC-010 | reflection/self-improvement example | reflection/adaptation vs persistent improvement evidence | **MATERIALIZED / QUALIFIED** | [`REC-010-reflection-adaptation.md`](./REC-010-reflection-adaptation.md) |
| REC-011 | memory lifecycle | state/checkpoint/persistence vs memory vs knowledge | **MATERIALIZED / QUALIFIED CONTRAST** | [`REC-011-memory-lifecycle-contrast.md`](./REC-011-memory-lifecycle-contrast.md) |
| REC-012 | representative multi-agent system | topology, admission hypothesis, baseline/benefit | **BLOCKED / OPEN_MK1** | waits on [`../MULTI_AGENT_BASELINE_SPEC.md`](../MULTI_AGENT_BASELINE_SPEC.md) execution evidence |
| REC-013 | legacy/current MCP integration | protocol revision, lifecycle drift, auth boundary | **MATERIALIZED / QUALIFIED** | [`REC-013-mcp-revision-drift.md`](./REC-013-mcp-revision-drift.md) |
| REC-014 | Strands Agents SDK | modern runtime, mixed topology, concurrency/budgets/intervention/protocols | **MATERIALIZED / QUALIFIED** | [`../../../systems/strands/CLASSIFICATION.md`](../../../systems/strands/CLASSIFICATION.md) |

## Coverage decisions

### REC-005 → `COVERED_BY REC-004 + REC-003`

The self-healing example adds a useful implementation example but no new MK1 dimension beyond:

```text
generated model code crosses execution boundary   → REC-004
verification/test success != safe promotion        → REC-003 + REC-004 qualifications
```

Its source evidence remains preserved; a dedicated normalized record would duplicate pressure rather than improve schema coverage.

### REC-006 → `COVERED_BY REC-002 + REC-007`

The HR sender is important negative evidence because human interrupts elsewhere do not prove the outbound-message dispatcher is protected.

MK1 already represents both halves:

```text
dispatcher-enforced approval semantics   → REC-002
external-send/publication mutation       → REC-007
```

The HR-specific universal-approval gap remains `UNKNOWN` in quarry evidence and is not silently treated as safe.

## Materialized pressure set

```text
REC-001  model-tool loop / shell / bounded termination
REC-002  HITL / protected consequential dispatcher
REC-003  trace vs outcome evaluation / regression gate
REC-004  generated code + browser + host blast radius
REC-007  external publication / dry-run / idempotency
REC-008  file data-egress / confidentiality boundary
REC-009  database authority / least-privilege credential boundary
REC-010  reflection/adaptation vs learning claim
REC-011  persistence/state vs memory lifecycle contrast
REC-013  protocol revision/lifecycle drift
REC-014  modern mixed-control runtime / Strands
```

The only required record family still **structurally blocked by missing new evidence** is REC-012 multi-agent benefit/admission.

## Family coverage view

| Engineering family | Coverage | State |
|---|---|---|
| minimal/model-directed control | REC-001 / REC-014 | **COVERED** |
| HITL / consequential mutation | REC-002 / REC-007 | **COVERED** |
| generated code / browser / high capability | REC-004 | **COVERED** |
| external communication/publication | REC-007 + REC-006 quarry negative case | **COVERED** |
| document / data egress | REC-008 | **COVERED** |
| database authority | REC-009 | **COVERED / QUALIFIED** |
| state / memory lifecycle | REC-011 / REC-014 | **COVERED / QUALIFIED** |
| evaluation / critic / epistemic claims | REC-003 / REC-010 | **COVERED** |
| multi-agent | REC-012 / REC-014 topology surfaces | **OPEN — baseline/benefit evidence missing** |
| protocol / interoperability | REC-013 / REC-014 MCP | **COVERED FOR MCP; A2A OPEN** |
| modern runtime/framework | REC-014 | **COVERED** |

## Schema pressure discovered by records

No new field has yet earned immediate promotion from the new representative records.

Two questions are explicitly deferred to the **schema freeze audit**:

1. `REC-008` — whether `data_egress` needs stronger confidentiality/data-classification severity structure beyond current side-effect fields;
2. `REC-011` — whether memory update-conflict/forgetting/evaluation belong in MK1 classification or should remain MK2 operational contracts.

They are not silently ignored and do not trigger schema mutation from one record alone.

## Closure requirement

Representative-record coverage passes only when:

1. REC-012 multi-agent gate has measured baseline/admission evidence;
2. A2A protocol evidence is either represented through an appropriate record/system package or explicitly routed by the closure audit;
3. freeze audit confirms `COVERED_BY` decisions do not hide a material distinction;
4. every material record remains interpretable under the frozen schema;
5. architecture classification stays separate from production certification.

## Record location

### Domain representative record

```text
mk/MK1/records/REC-xxx-<slug>.md
```

### Canonical current-system record

```text
systems/<system>/CLASSIFICATION.md
```

Do not duplicate a complete system classification under `records/`; link it here.

## Record contract

Full template: [`TEMPLATE.md`](./TEMPLATE.md).

Every materialized record must identify:

```yaml
record_id:
schema_revision:
identity:
source_receipts:
evidence_scope:
classification:
material_unknowns:
production_certification:
```

## Evidence discipline

Primary current evidence bases include:

- `../../../quarries/genai-agents.md`;
- `../../../quarries/genai-agents-risk-scan.md`;
- `../../../quarries/genai-agents-p0-p1-callpaths.md`;
- `../../../quarries/cross-source-memory-production-mcp.md`;
- `../../../quarries/runtime-semantics-strands-langgraph-openai.md`;
- `../../../systems/strands/`.

Do not re-mine upstream when pinned evidence is sufficient. Re-open source when a material field is unsupported, contradicted or freshness-sensitive.

## Next record action

```text
REC-012 multi-agent
```

must wait for actual baseline/admission evidence rather than being filled from topology documentation alone.

Spec: [`../MULTI_AGENT_BASELINE_SPEC.md`](../MULTI_AGENT_BASELINE_SPEC.md).
