# MK1 — Full representative-set and freeze-readiness audit

**Date:** 2026-10-12  
**Decision:** **FREEZE HOLD / NOT GO for `mk1-v1`**  
**Scope:** 12 materialized/qualified records including the canonical Strands package, REC-005/006 `COVERED_BY` review, PA-01–PA-09 prefreeze questions, and MK2 derivability.  
**Evidence strength:** direct inspection of the repository's current records and upstream-pinned quarries, plus a local static enumeration-value scan. **No runtime systems/models were re-executed.**  
**Owning control documents:** [GATES](../GATES.md), [CLOSURE_PLAN](../CLOSURE_PLAN.md), [SCHEMA_HISTORY](../SCHEMA_HISTORY.md), [UNKNOWNS](../UNKNOWNS.md).

## Executive decision

- **C1 / G1:** **PASS / QUALIFIED for family coverage.** The 12 records cover the declared engineering pressures; two additional records have narrowly valid `COVERED_BY` reasons. This is a *coverage* PASS, **not** strict record-schema conformance.
- **C3 / G7:** **PASS / QUALIFIED_UPSTREAM**, unchanged. S-118/119 include real-model study evidence, but original provider runs and trace-level latency are not independently reproduced.
- **C4 / G8:** **OPEN.** U-MK1-002 (freeze/cross-dimension), U-MK1-003 (final routing), and new U-MK1-004 (record scalar conformance) still matter.
- **C5 / G9:** **PARTIAL / PA-01 resolved by a linked evidence appendix; PA-06 remains OPEN.** Existing cross-dimension separations are generally representable, but nested child-agent effective authority is not proved by a flat union of permissions.
- **C6 / G10:** **FAIL / HOLD.** Ten of twelve classification blocks contain 87 occurrences of scalar values that do not match their declared enumerated vocabulary in the current MK1 schema/template; contrast-family alternatives have not yet been normalized into per-variant values or explicit `unknown`. A reader can understand the prose, but MK2 must not mistake it for a conformant machine-consumable contract.
- **C7:** MK1 `CLOSURE.md` MUST NOT be created while C6 fails.
- **C8 / G12:** MK2 mapping is available **at design level**, but handoff remains BLOCKED pending C6 and C7. No MK2 activation.

## Representative family verification

| Record | Material pressure | Coverage result | Important qualification |
|---|---|---|---|
| REC-001 | Model-directed loop, shell, termination | COVERED | No blanket sandbox/production claim |
| REC-002 | HITL and dispatcher enforcement | COVERED | Approval validity tied to actual dispatcher path, not all deployments |
| REC-003 | Outcome versus trajectory evaluation | COVERED | Regression/evaluator evidence does not certify reliability |
| REC-004 | Generated code promoted to execution + browser | COVERED | Host process blast radius; sandbox NOT proven |
| REC-005 | Generated self-healing code + verifier | COVERED_BY 004 + 003 | Test/verifier success does not make promotion safe |
| REC-006 | HR outbound sender without universal approval proof | COVERED_BY 002 + 007 | **Negative case**: never infer every send is HITL-gated |
| REC-007 | External publication, dry run, idempotency | COVERED | Post-send timeout/rollback unresolved |
| REC-008 | Remote file upload and confidentiality | COVERED | Unknown retention/sensitivity/authorization per deployment |
| REC-009 | Effective DB credential authority | COVERED / QUALIFIED | Read vs write/S0 vs S3/S4 depends on actual principal |
| REC-010 | Reflection versus measured improvement | COVERED / QUALIFIED | Reflection is not persistent learning |
| REC-011 | Checkpoint, persistence, memory, knowledge | COVERED / QUALIFIED CONTRAST | Not one universally configured implementation |
| REC-012 | Same-task single vs multi real-model comparisons | COVERED / QUALIFIED_UPSTREAM | Published outcome data re-aggregated; no independent LLM rerun |
| REC-013 | MCP revision/lifecycle/auth boundaries | COVERED / QUALIFIED | Protocol interoperability is not authorization |
| REC-014 | Strands mixed-control runtime, budgets, sessions, protocols | COVERED / QUALIFIED | A2A 1.0 compatibility not established |

### Independent `COVERED_BY` review

**REC-005:** The self-healing notebook executes model-generated `new_code` via `exec`, already represented by REC-004's generated-code/host-authority path. Its verify/revise/promote boundary is independently represented by REC-003 trajectory/outcome distinctions. No additional top-level classification dimension is established. The exact repair algorithm still varies by implementation. **Decision: retain `COVERED_BY`, qualified.**

**REC-006:** The HR sender's consequential outbound-message dispatch is a distinct *negative evidence case*: presence of interrupts elsewhere does not establish approval at this dispatcher. REC-002 supplies the strong protected-approval comparator; REC-007 supplies external communication/publication mutation and idempotency/effect semantics. It would be false to call the sender itself H4. **Decision: retain `COVERED_BY`, preserve absence of proven authorization as `unknown`.**

Primary evidence: [risk scan](../../../quarries/genai-agents-risk-scan.md), [P0/P1 call-paths](../../../quarries/genai-agents-p0-p1-callpaths.md), [registry](../records/README.md).

## PA-01–PA-09 cross-dimension disposition

| ID | Final audit disposition | Reason / exact condition |
|---|---|---|
| PA-01 | **RESOLVED FOR MK1 / KEEP APPENDIX** | A comparison is an **evidence receipt** (task/model/baseline/outcome/cost/failures), not a top-level system-property classification axis. The [record template](../records/TEMPLATE.md) already provides `comparison_receipt` outside the schema. Link a versioned receipt in REC-012. Do not silently add fields to `CLASSIFICATION_SCHEMA.md`. |
| PA-02 | **QUALIFIED / NO SCHEMA CHANGE** | Zero-model deterministic actors are an experiment/control fixture, not a `single_model` instantiated LLM topology; compare separately, never force a false model label. |
| PA-03 | **REPRESENTABLE / MK2 ROUTING** | Side-effect S0–S4, `data_egress`, and `security.data_classification` are independent; confidentiality impact severity, storage retention and approval enforcement require MK2 policy tests. |
| PA-04 | **REPRESENTABLE / MK2 ROUTING** | Runtime state/checkpoint, writer-conflict semantics and intentional memory scope are independent; deletion/poisoning/conflict controls are MK2/MK5 concerns. |
| PA-05 | **REPRESENTABLE / QUALIFIED** | H0–H4 shorthand alone does not prove enforcement; keep `dispatcher_enforcement`, owner/boundary and approval binding separate. |
| PA-06 | **OPEN_MK1 — NO FREEZE** | Mixed/nested agents may receive materially different effective tools, credentials or sandbox guarantees. Flat `control.topology` + aggregate `capabilities` + `security.sandbox` may obscure *which child can do what*. Resolve with a pinned real nested-agent example and either a linked per-actor subprofile contract or a minimally versioned schema adjustment; do not infer per-agent isolation from mere topology. |
| PA-07 | **REPRESENTABLE / QUALIFIED** | Outcome, trajectory, stochastic repeats and observability stay orthogonal; no maturity score. |
| PA-08 | **REPRESENTABLE / QUALIFIED** | Protocol `revision/role/auth_model` are independent of compatibility and authorization; preserve MCP/A2A drift. |
| PA-09 | **REPRESENTABLE / QUALIFIED** | Budget value, enforcement point and cancellation effective boundary already separate; historical Python thread stall illustrates overrun, not hard cancellation. |

## Enum conformance — new independent issue

The 12 primary classification YAML blocks were inspected against **the existing enumerated vocabulary** in `CLASSIFICATION_SCHEMA.md` and `records/TEMPLATE.md` (not an invented replacement schema). For enum-typed fields, detect values not equal to **one** allowed literal (including explicit `unknown` where allowed). These can be pipe-delimited alternatives, free prose or framework-specific values. See the [complete scalar-conformance receipt](./ENUM_CONFORMANCE_2026-10-12.md).

**Finding:** **87 candidate enum mismatches across 10/12 records**. These are *field occurrences*, not unique schema dimensions or necessarily 87 independent engineering defects. Static candidate detection can have false positives for documented prose-style contrast fixtures; nevertheless it is **not honest to declare a machine-friendly freeze without resolving them individually**.

Required remediation:
1. Decide whether a record describes **one concrete variant** or **a family/contrast**.
2. For concrete variants choose exactly one supported enum literal, or `unknown` where evidence does not support a stronger value; preserve the original detail in a qualified evidence note.
3. For family/contrast cases preserve variant-specific alternatives as separate structured subprofiles or a linked variant matrix, not a fake compound scalar.
4. Re-scan all 12 records, audit false positives and detect new enum drift; promote only evidence-supported changes.
5. Re-check PA-06 per-child capability ownership, and rerun C5/C6 before any revision name change.

**No automatic mass-rewrite to `unknown`:** that would erase real authority differences, especially REC-009 DB principal and REC-011 memory variants.

## MK2 derivability (design-only)

| Stable MK1 owner | Candidate MK2 contract family |
|---|---|
| control, topology, capabilities, security | `AgentSystemContract`, `ToolContract`, `CapabilityPolicy` |
| side_effects, security, human_control | `SideEffectPolicy`, `HumanApprovalContract` |
| state, memory, locking, writer semantics | `ConcurrencyPolicy`, `MemoryPolicy` |
| errors_and_retries, termination | `RetryPolicy`, `TerminationPolicy` |
| protocols, reproducibility | `ProtocolReceipt`, `ReproducibilityReceipt` |
| evaluation, identity/evidence scope | `EvaluationPlan`, `EvidenceReceipt` |

Mapping follows [MK2 handoff contract](../../MK2/HANDOFF_CONTRACT.md); these are *design labels*, not active, certified or machine-validated MK2 schemas. PA-06 may require tool-specific agent authority subprofiles before the first contract is stable.

## Non-claims and next gate

```yaml
mk1_frozen: false
mk1_closure_receipt_created: false
mk2_active: false
g7_multiagent: PASS_QUALIFIED_UPSTREAM
c1_family_coverage: PASS_QUALIFIED
c5_cross_dimension: PARTIAL_PA06_OPEN
c6_strict_enum_conformance: FAIL_PENDING_MIGRATION
next_step: normalize_enum_values_preserving_variant_provenance_then_recheck_PA06
```

This is a **completed audit with a negative freeze decision**, not a claim that the entire repository or applications were runtime-audited. Do not equate a completed knowledge audit with application certification.
