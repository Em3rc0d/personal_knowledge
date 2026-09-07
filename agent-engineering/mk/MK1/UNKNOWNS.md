# MK1 — UNKNOWN Register

Status: **ACTIVE**

MK1 does not try to eliminate every unknown. It makes uncertainty classifiable and routes it to the MK where evidence can actually resolve it.

## Resolved by first record pressure tests

These were open taxonomy questions and now have a working disposition:

### Observed vs reachable side effects

**RESOLVED FOR MK1:** store both `observed_class` and `reachable_class`.

Reason: R-001/R-004/R-005 prove that benign observed behavior can run on shell/general-Python authority capable of materially stronger effects.

### Model count/topology vs control authority

**RESOLVED FOR MK1:** keep topology/model count independent from `control_class` and support `deterministic_multi_role`.

Reason: R-012 uses multiple named roles but fixed C0 orchestration.

### Multi-agent admission evidence

**RESOLVED STRUCTURALLY:** schema now includes admission hypothesis, parallelism, context partition, permission isolation, verifier role, specialization, baseline, measured benefit and coordination cost.

Evidence can still remain `UNKNOWN` per record.

### Memory labels

**RESOLVED STRUCTURALLY:** memory requires lifecycle fields; source labels such as `long-term` do not override observed scope/persistence.

R-011 normalizes a source-claimed long-term implementation to `session + process`; R-016 independently fits the same lifecycle model.

## Inherited from MK0 — still open where system-specific

### Runtime / reproducibility

- per-notebook execution proof under current dependencies;
- exact behavior under current model/provider versions;
- current SDK migration details for legacy examples;
- complete external API compatibility receipts.

### Security / containment

- project-specific sandbox effectiveness;
- tenant/secrets isolation;
- authenticated browser mutation reachability for browser examples;
- complete consequential dispatcher enforcement outside the tested HITL slice;
- external-service retention behavior.

### Side effects / retries

- exact retry/idempotency semantics for every tutorial;
- unknown-outcome handling after timeout;
- compensating actions where idempotency is unavailable;
- DataScribe's exact lower-level mutation path and permission enforcement;
- universal approval coverage for HR outbound communication.

### Memory / epistemics

- quality metrics by memory family;
- memory-write validation and poisoning resistance;
- retention/deletion policies;
- durable identity/isolation for cross-session memory;
- persistent improvement evidence for `self-improving` claims.

### Multi-agent / operations

- benchmarked multi-agent gains;
- dynamic delegation behavior;
- coordination cost under realistic workloads;
- failure containment;
- deployment/rollback/SLO evidence;
- production observability completeness.

## MK1-specific unknowns still requiring pressure tests

The normalization process still must determine:

- whether `horizon` should remain inside control metadata or become a completely independent top-level axis;
- whether S0-S4 plus `data_egress` is sufficient for confidentiality-sensitive systems;
- whether `sandbox` can be represented by one enum or requires capability-specific isolation fields;
- whether evaluation layers E0-E7 are better represented as independent booleans than an ordinal shorthand;
- whether human-control H0-H4 remains useful once timing, editability and dispatcher binding are independently populated;
- how nested/dynamic agent systems should represent child authorities without flattening dangerous differences;
- how to version/freeze the classification schema once external pressure tests complete;
- whether the schema cleanly handles C1 model routing and C3 open-horizon behavior;
- whether authenticated transactional browser authority needs fields beyond current browser/action + side-effect dimensions;
- how to represent unknown-outcome mutation/reconciliation without mixing retry policy and outcome verification.

## Required evidence before MK1 closure

- C1 model-routed example;
- C3/open-horizon example;
- dynamic multi-agent delegation;
- durable cross-session memory;
- authenticated transactional browser;
- explicit unknown-outcome mutation/reconciliation;
- production-oriented external source;
- independent source/framework outside the NirDiamant corpus.

## Routing rule

```text
unknown about vocabulary/dimensions
  → MK1

unknown about required operational behavior/contract
  → MK2

unknown requiring integration across domains
  → MK3

unknown requiring automated verification
  → MK4

unknown requiring repeated execution / real-system evidence
  → MK5+
```

## Non-negotiable rule

`UNKNOWN` is not technical debt when the evidence genuinely does not exist. Hidden assumptions are technical debt.
