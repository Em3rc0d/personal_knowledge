# MK1 — UNKNOWN Register

Status: **ACTIVE / CLOSURE-ROUTED**

MK1 does not try to eliminate every unknown. It makes uncertainty explicit and routes it to the stage where evidence can actually resolve it.

## UNKNOWN states

Every material item should eventually be in one of these states:

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

### U-MK1-001 — Representative family coverage

State: **OPEN_MK1**

The current record registry has materialized:

- REC-001 minimal while-loop;
- REC-002 HITL approval;
- REC-013 MCP revision drift;
- REC-014 Strands Agents.

Still required for closure pressure:

- generated-code/browser high-capability composition;
- document/data-egress path;
- dedicated memory lifecycle record;
- evaluator/critic pressure;
- multi-agent baseline/admission evidence.

Registry: [`records/README.md`](./records/README.md).

### U-MK1-002 — A2A revision/auth/transport evidence

State: **OPEN_MK1**

Current Strands evidence establishes A2A capability surfaces but does not yet pin enough current protocol semantics for reproducible distributed-agent classification.

Required evidence: [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md).

### U-MK1-003 — Multi-agent measured benefit model

State: **OPEN_MK1**

Topology is classifiable, but MK1 still needs one representative baseline comparison demonstrating that topology and measured benefit are independent fields.

Contract: [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md).

### U-MK1-004 — Final schema overlap/freeze audit

State: **OPEN_MK1 / BLOCKED BY RECORD SET**

Questions still to resolve at closure:

- whether `horizon` should stay nested under control or be independent;
- whether S0–S4 plus `data_egress` sufficiently separates integrity/impact from confidentiality;
- whether one `sandbox` enum is sufficient for classification or requires capability-specific containment qualifiers;
- whether current evaluation fields are sufficiently orthogonal without an ordinal layer;
- whether H0–H4 remains useful alongside explicit enforcement-owner/boundary fields;
- whether nested child-agent authority is represented cleanly enough by current topology/capability fields;
- whether the active schema can freeze without a breaking revision.

Procedure: [`SCHEMA_HISTORY.md`](./SCHEMA_HISTORY.md) + [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md).

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

Cross-source basis:

- Strands;
- LangGraph;
- OpenAI Agents SDK.

Residual implementation details remain per-system UNKNOWNs rather than schema blockers.

### U-RUN-002 — Budget enforcement boundary

State: **CLOSED / PROMOTED**

Promoted into `termination`:

```text
*_budget_enforcement
overshoot_semantics
cancellation_effective_boundary
```

Residual exact boundaries remain implementation-specific.

### U-RUN-003 — Intervention enforcement owner

State: **CLOSED / PROMOTED**

Promoted into `human_control`:

```text
enforcement_owner
enforcement_boundary
```

`dispatcher_enforcement` and `approval_binding` remain separate stronger call-path properties.

Evidence for all three: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

## Protocol questions

### U-PROTO-001 — Strands × MCP `2026-07-28`

State: **QUALIFIED / CORE INTEROPERABILITY CLOSED**

Supported by pinned source + upstream execution evidence for:

- modern `server/discover` path;
- explicit rejection of legacy `initialize` fallback in the regression fixture;
- Streamable HTTP;
- tool listing/invocation;
- structured result/error behavior;
- multi-round-trip input;
- prompts/resources;
- list-changed subscription;
- OpenTelemetry trace continuity.

Receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

Residual qualifications:

- independent local rerun blocked by environment network/package constraints;
- external protected-server OAuth E2E remains deployment-specific;
- cancellation does not imply remote-effect rollback;
- universal server interoperability is not certified;
- versions outside pinned dependency range require new evidence.

### U-PROTO-002 — A2A

State: **OPEN_MK1**

See U-MK1-002.

## Routed operational UNKNOWNs

These do not need universal closure for MK1 if the final record set proves the taxonomy can represent them explicitly.

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
- compensating actions when idempotency is unavailable → **ROUTED_MK2**;
- DataScribe exact lower-level mutation dispatcher/filter semantics → **OPEN only if REC-009 is required for distinct schema pressure; otherwise route forward explicitly**;
- universal HR sender approval coverage → **ROUTED_MK2/MK5+** after representative classification.

### Memory / epistemics

- memory quality metrics by family → **ROUTED_MK2/MK5+**;
- poisoning/write validation → **ROUTED_MK2/MK5+**;
- retention/deletion enforcement → **ROUTED_MK2**;
- persistent improvement proof for self-improvement claims → **ROUTED_MK5+**, while MK1 only classifies claim/evidence type.

### Production / operations

- deployment/rollback/SLO evidence → **ROUTED_MK2/MK5+**;
- production observability completeness → **ROUTED_MK2/MK5+**;
- incident operability → **ROUTED_MK2/MK5+**;
- capacity/cost limits → **ROUTED_MK2**.

### Framework-specific residuals

- Python/TypeScript provider feature parity over time → **system-package freshness debt / OUT_OF_SCOPE for schema freeze** unless it changes classification;
- concrete backend locking semantics → **per-system record UNKNOWN / MK2+**;
- exact hard/cooperative/best-effort cancellation per tool/provider path → **per-record UNKNOWN / MK2+**;
- adversarial reliability of LLM steering → **ROUTED_MK5+**.

## Reproducibility UNKNOWNs inherited from MK0

Universal per-notebook execution proof is not required to freeze a framework-independent classification schema.

Route:

- representative record execution evidence → **MK1 where it changes classification**;
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
