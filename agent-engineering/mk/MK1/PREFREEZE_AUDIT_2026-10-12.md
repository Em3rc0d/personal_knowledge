# MK1 — Preliminary freeze/overlap audit (2026-10-12)

Status: **STATIC PRE-AUDIT / NOT C5–C6 GATE PASS**  
Schema reviewed: `mk1-draft-2026-09-16.1`  
Blocked dependency: REC-012 representative real-model comparison remains missing.  
Sources reviewed: `CLASSIFICATION_SCHEMA.md`, `DIMENSIONS.md`, `NORMALIZATION_RULES.md`, `CLASSIFICATION_QUEUE.md`, `records/TEMPLATE.md`, REC-002/004/007/008/011/012, Strands classification, `GATES.md` and `SCHEMA_HISTORY.md`.

## Scope and reading rule

Static review can detect *documented field mismatch*, obvious orthogonality loss or unsupported promotion. It cannot replace the final all-record representability audit, nor produce evidence of multi-agent model benefit. **No schema fields have been modified or frozen.**

## Preliminary findings (traceable, action-oriented)

| ID | Finding | Existing evidence | Preliminary disposition |
|---|---|---|---|
| PA-01 | The documentation describes a model for comparing multi-agent topologies, but the current normalized YAML schema does **not** explicitly name `admission_hypothesis`, `baseline`, `measured_benefit` or `coordination_cost`. | `DIMENSIONS.md` §10 contains `reason`, `baseline`, `measured_benefit`, `coordination_cost`; `CLASSIFICATION_SCHEMA.md` has `control.topology/model_count` and evaluation outputs, but no direct equivalent named comparison contract. REC-012 draft stores these under a separate comparison block. | **OPEN — schema-vs-evidence-contract decision.** Do not add fields automatically: determine whether a separate per-experiment evidence receipt is authoritative or whether a minimal schema reference is needed after real-agent evidence. |
| PA-02 | `single_model` topology label is not semantically accurate for a baseline with **zero** models (offline policy actor). | `CLASSIFICATION_SCHEMA.md` allowed topology enum; [REC-012 deterministic draft](./records/REC-012-deterministic-topology-draft.md) has `model_count: 0`. | **QUALIFIED / MODEL-SCOPE BOUNDARY.** Do not distort the agentic taxonomy to accommodate a non-LLM control fixture; keep control metadata separate until real-model run. |
| PA-03 | Side-effect severity and data confidentiality are distinct. Data-egress may occur without S3/S4 mutating business state. | `DIMENSIONS.md` S0–S4, `side_effects.data_egress`, `security.data_classification`, REC-008 external upload. | **REPRESENTABLE / QUALIFIED.** Existing separate fields support the distinction; MK2 policy severity, retention/deletion, sensitivity grading and egress authorization remain separate operational questions. No new field admitted yet. |
| PA-04 | Durable runtime checkpoint, concurrency safety and semantic memory are independent; memory conflict-resolution and retention enforcement should not be silently inferred. | `state.*concurrency*`, `memory.*`, REC-011 memory contrast, Strands system classification. | **REPRESENTABLE / QUALIFIED.** Runtime writer model stays under `state`, semantic memory lifecycle under `memory`; route detailed forgetting/conflict controls to MK2 unless new evidence forces classification distinction. |
| PA-05 | `H0–H4` shorthand can coexist with effective authorization only when dispatcher/owner/boundary/approval-binding details are preserved. | `DIMENSIONS.md` §5; REC-002 approval gate vs REC-007 publication without universal HITL guarantee. | **REPRESENTABLE / QUALIFIED.** H4 is not an automatic proof from a UI or workflow label; do not reduce policy strength to an ordinal number. |
| PA-06 | One `security.sandbox` enum may hide partial/tool-specific containment and nested worker authority. | `security.trust_boundaries`, `capabilities.capability_compositions`, `control.topology`; Strands package and REC-004 generated code. | **OPEN / AUDIT QUESTION.** Keep precise scope in trust boundaries and UNKNOWNs; require a real-model nested-actor case before deciding whether a structured containment/authority subrecord is necessary. |
| PA-07 | Outcome/trajectory evidence, repeated stochastic trials and production observability remain distinct from architecture or quality maturity. | `evaluation.*`, `DIMENSIONS.md` §8, REC-003. | **REPRESENTABLE / QUALIFIED.** No ordinal maturity variable needed. |
| PA-08 | Protocol support is revision-scoped, not deployment authorization. | `protocols[].revision/role/transport/auth_model`, Strands A2A 0.3 vs 1.0 qualification, MCP receipt. | **REPRESENTABLE / QUALIFIED.** Do not promote missing cross-version interoperability to PASS. |
| PA-09 | Cancellation and resource limits depend on actual enforcement boundary, not nominal numbers; real local threads demonstrate overshoot. | `termination.*budget_enforcement`, `cancellation_effective_boundary`, [REC-012 deterministic receipt](../../quarries/rec-012-offline-topology-baseline.md). | **REPRESENTABLE / QUALIFIED.** Existing fields suffice; correct value must remain per runtime and task. |

## Independent mechanical check

A static string/field presence audit of the source documents confirmed:

```text
DIMENSIONS.md:
  baseline                 PRESENT
  measured_benefit         PRESENT
  coordination_cost        PRESENT

CLASSIFICATION_SCHEMA.md:
  baseline                 ABSENT (as explicit field)
  measured_benefit         ABSENT
  coordination_cost        ABSENT
  control.topology         PRESENT
  evaluation.outcome       PRESENT

records/TEMPLATE.md:
  baseline                 ABSENT (as explicit field)
  measured_benefit         ABSENT
  coordination_cost        ABSENT
```

This **does not by itself prove** an actual missing schema dimension; MK1 could preserve the comparison as a separate evidence contract. It identifies one decision requiring closure before a freeze to prevent benchmark data from being irretrievably buried in notes.

## Gate-aware execution plan

1. **Now / completed:** run environment feasibility; classify the real-model experiment as `BLOCKED_ENVIRONMENT` with [evidence](../../experiments/rec-012/LLM_FEASIBILITY_2026-10-12.md).
2. **Now / completed:** static pre-audit of key schema/record contrasts PA-01–PA-09. This is pressure mapping, **not G9 PASS**.
3. **HOLD:** do not create a new MK1 revision from PA-01–PA-09 alone. Preserve the strongest question PA-01 for the final evidence+schema decision.
4. **When runner/model available:** execute same-task LLM single-vs-multi under [REC-012 contract](./MULTI_AGENT_BASELINE_SPEC.md), multiple trials, cost/latency/outcome/handoff/termination proof.
5. **After REC-012 evidence:** perform full representative-set + `COVERED_BY` audit, route remaining UNKNOWNs, decide PA-01/PA-06, then C5/C6 freeze or issue a new versioned draft.

## Gate decisions

```yaml
static_preaudit: EXECUTED
pa01_comparison_schema_contract: OPEN
pa06_nested_authority_containment: OPEN
multiagent_real_model_evidence: BLOCKED_ENVIRONMENT
mk1_g7: OPEN
mk1_g8: PARTIAL
mk1_g9: PARTIAL_STATIC_AUDIT_ONLY
mk1_schema_frozen: false
mk2_activated: false
```

No speculative schema revision. No false `PASS` on G7/G9/C5/C6. Existing Source → Quarry → normalized evidence chain remains intact.
