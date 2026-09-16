# MK1 — UNKNOWN Register

Status: **ACTIVE / CLOSURE-ROUTED**

MK1 does not try to eliminate every unknown. It makes uncertainty explicit and routes it to the stage where evidence can actually resolve it.

## UNKNOWN states

```text
OPEN_MK1        missing evidence may change MK1 classification/schema
CLOSED          evidence resolved the question
QUALIFIED       scoped claim is supported; important boundary remains
ROUTED_MK2      classification is stable; operational contract remains open
ROUTED_MK3_PLUS integration/system concern beyond MK1
ROUTED_MK5_PLUS requires repeated/production-like/independent evidence
OUT_OF_SCOPE     not required for declared MK1 closure scope
```

No material item may disappear merely because it is inconvenient to close.

## Closure-blocking OPEN_MK1 items

### U-MK1-001 — Multi-agent measured benefit model

State: **OPEN_MK1 / PRIMARY EVIDENCE BLOCKER**

The representative registry is near-complete:

```text
11 MATERIALIZED / QUALIFIED
2  COVERED_BY
1  OPEN → REC-012 multi-agent
```

Topology is already classifiable, but MK1 still needs one representative baseline comparison demonstrating that topology and measured benefit are independent fields.

Contract: [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md).  
Registry: [`records/README.md`](./records/README.md).

### U-MK1-002 — Final schema overlap/freeze audit

State: **OPEN_MK1 / BLOCKED BY REC-012**

Questions still to resolve at closure:

- whether `horizon` should stay nested under control or be independent;
- whether S0–S4 plus `data_egress` sufficiently separates integrity/impact from confidentiality;
- whether one `sandbox` enum is sufficient for classification or needs capability-specific containment qualifiers;
- whether evaluation fields are sufficiently orthogonal without an ordinal maturity layer;
- whether H0–H4 remains useful alongside enforcement owner/boundary/dispatcher fields;
- whether nested child-agent authority is represented cleanly enough by current topology/capability fields;
- whether memory update-conflict/forgetting/evaluation belongs in MK1 or MK2;
- whether the active schema can freeze without a breaking revision.

Procedure: [`SCHEMA_HISTORY.md`](./SCHEMA_HISTORY.md) + [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md).

### U-MK1-003 — Final UNKNOWN routing

State: **OPEN_MK1 / BLOCKED BY FINAL REPRESENTATIVE SET**

Once REC-012 exists, every material remaining UNKNOWN must be assigned one final closure state and recorded in MK1 `CLOSURE.md`.

## Representative family coverage

State: **QUALIFIED / NON-MULTI-AGENT COVERAGE CLOSED**

Materialized/qualified:

- REC-001 minimal while-loop;
- REC-002 HITL approval;
- REC-003 trace evaluation;
- REC-004 generated-code/browser E2E;
- REC-007 social publication;
- REC-008 document/data egress;
- REC-009 database authority;
- REC-010 reflection/adaptation;
- REC-011 memory lifecycle contrast;
- REC-013 MCP revision drift;
- REC-014 Strands Agents.

Explicit coverage decisions:

- REC-005 → `COVERED_BY REC-004 + REC-003`;
- REC-006 → `COVERED_BY REC-002 + REC-007`.

Only REC-012 requires new representative evidence.

## Resolved / promoted runtime-semantics questions

### U-RUN-001 — Concurrency semantics

State: **CLOSED / PROMOTED**

Promoted into `state` in `mk1-draft-2026-09-16.1`:

```text
invocation_concurrency
writer_model
concurrency_conflict_semantics
locking
```

Cross-source basis: Strands + LangGraph + OpenAI Agents SDK.

### U-RUN-002 — Budget enforcement boundary

State: **CLOSED / PROMOTED**

Promoted into `termination`:

```text
*_budget_enforcement
overshoot_semantics
cancellation_effective_boundary
```

### U-RUN-003 — Intervention enforcement owner

State: **CLOSED / PROMOTED**

Promoted into `human_control`:

```text
enforcement_owner
enforcement_boundary
```

`dispatcher_enforcement` and `approval_binding` remain separate stronger call-path properties.

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

## Protocol questions

### U-PROTO-001 — Strands × MCP `2026-07-28`

State: **QUALIFIED / CORE INTEROPERABILITY CLOSED**

Supported by pinned source + upstream execution evidence for modern lifecycle, Streamable HTTP, tools, structured results/errors, multi-round-trip input, prompts/resources, list-change behavior and trace continuity.

Receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

Residual qualifications:

- independent local rerun blocked by environment network/package constraints;
- external protected-server OAuth E2E remains deployment-specific;
- cancellation does not imply remote-effect rollback;
- universal server interoperability is not certified;
- versions outside pinned dependency range require new evidence.

### U-PROTO-002 — A2A classification shape

State: **QUALIFIED / CLOSED FOR MK1 CLASSIFICATION SHAPE**

Pinned Strands evidence now establishes:

```text
Python A2A SDK                    >=0.3.0,<0.4.0
TypeScript A2A SDK                ^0.3.10
implementation protocol family    0.3
current official A2A family       1.0
client/server/discovery semantics represented
invoke/stream/task semantics      represented
state/concurrency boundary        represented
security/auth boundary            represented / qualified
integration fixture source        present
specific successful CI run        NOT VERIFIED
independent rerun                 NOT RUN
A2A 1.0 compatibility             NOT ESTABLISHED
```

Receipt: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md).

Why it no longer blocks MK1 taxonomy:

- protocol revision is explicit;
- evidence strength is explicit;
- current-version drift is explicit;
- existing protocol fields represent the semantics without a framework-specific category;
- no unsupported A2A `1.0` claim is required to classify the pinned implementation.

### U-PROTO-003 — Strands A2A `1.0` migration/interoperability

State: **ROUTED_MK2 / ROUTED_MK5_PLUS / SYSTEM FRESHNESS DEBT**

The pinned Strands snapshot is not proven A2A `1.0` compatible. Future compatibility evidence should update the Strands system package and may feed later operational/certification work.

It reopens MK1 only if a future A2A revision exposes a material semantic distinction the frozen schema cannot represent.

## Routed operational UNKNOWNs

### Security / containment

- project-specific sandbox effectiveness → **ROUTED_MK2/MK5+**;
- tenant/secrets isolation → **ROUTED_MK2/MK5+**;
- authenticated browser mutation reachability per deployment → **ROUTED_MK2/MK5+**;
- complete consequential dispatcher coverage per application → **ROUTED_MK2/MK5+**;
- external-service retention behavior → **ROUTED_MK2/MK5+**.

### Side effects / retries

- exact retry/idempotency contract for every tutorial → **OUT_OF_SCOPE for universal MK1 closure**;
- project-specific mutating retry safety → **ROUTED_MK2/MK5+**;
- timeout unknown-outcome recovery → **ROUTED_MK2**;
- compensating actions without idempotency → **ROUTED_MK2**;
- DataScribe exact lower-level mutation dispatcher/filter semantics → **ROUTED_MK2/MK5+** after REC-009 preserved the classification uncertainty;
- universal HR sender approval coverage → **ROUTED_MK2/MK5+**; REC-006 negative evidence remains preserved.

### Memory / epistemics

- memory quality metrics by family → **ROUTED_MK2/MK5+**;
- poisoning/write validation → **ROUTED_MK2/MK5+**;
- retention/deletion enforcement → **ROUTED_MK2**;
- persistent improvement proof for self-improvement claims → **ROUTED_MK5+**; MK1 classifies claim/evidence type.

### Production / operations

- deployment/rollback/SLO evidence → **ROUTED_MK2/MK5+**;
- production observability completeness → **ROUTED_MK2/MK5+**;
- incident operability → **ROUTED_MK2/MK5+**;
- capacity/cost limits → **ROUTED_MK2**.

### Framework-specific residuals

- Python/TypeScript feature parity over time → **system-package freshness debt / OUT_OF_SCOPE for schema freeze unless classification changes**;
- concrete backend locking semantics → **per-system UNKNOWN / MK2+**;
- exact hard/cooperative/best-effort cancellation per path → **per-record UNKNOWN / MK2+**;
- adversarial reliability of LLM steering → **ROUTED_MK5+**.

## Reproducibility UNKNOWNs inherited from MK0

Universal per-notebook execution proof is not required to freeze a framework-independent classification schema.

- representative execution evidence → **MK1 only when it changes classification**;
- all-tutorial current executability → **OUT_OF_SCOPE for MK1 closure**;
- project/runtime reproducibility contract → **MK2**;
- repeated independent certification → **MK5+**.

## Closure routing rule

Before MK1 closes, each remaining material UNKNOWN must appear in the closure receipt as:

```yaml
id:
state: CLOSED | QUALIFIED | ROUTED_MK2 | ROUTED_MK3_PLUS | ROUTED_MK5_PLUS | OUT_OF_SCOPE
why_it_does_not_block_mk1:
evidence_or_destination:
```

Any item still `OPEN_MK1` blocks closure.

## Non-negotiable rule

`UNKNOWN` is not technical debt when evidence genuinely does not exist.

**Hidden assumptions are technical debt.**
