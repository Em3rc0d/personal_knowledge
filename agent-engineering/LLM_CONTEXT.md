# Agent Engineering — LLM Context Contract

Status: **MACHINE-ORIENTED DOMAIN ROUTER**

Use this file when an LLM/agent needs to retrieve, summarize, compare or continue work inside `agent-engineering/`.

## Domain identity

```yaml
domain: agent-engineering
purpose: framework-independent engineering knowledge for agentic/LLM systems
current_mk: MK1
mk0: CLOSED
mk1: IN_PROGRESS
mk2: BLOCKED_DESIGN_SEEDED
current_schema: mk1-draft-2026-09-16.1
canonical_status: STATUS.md
execution_roadmap: ROADMAP.md
repository_contract: REPOSITORY_CONTRACT.md
human_map: KNOWLEDGE_MAP.md
```

## First routing decision

```yaml
intent:
  current_state: STATUS.md
  next_work: ROADMAP.md
  repository_semantics: REPOSITORY_CONTRACT.md
  system_specific_current: systems/<system>/LLM_CONTEXT.md
  classification_semantics: mk/MK1/README.md + CLASSIFICATION_SCHEMA.md + DIMENSIONS.md
  record_status: mk/MK1/records/README.md
  closure_blockers: mk/MK1/CLOSURE_PLAN.md + GATES.md + UNKNOWNS.md
  provenance: systems/*/EVIDENCE.md -> quarries -> mining-site
  next_mk_input: mk/MK2/HANDOFF_CONTRACT.md
```

Do not load raw quarries first for a current-state question when a canonical system/MK entrypoint exists.

## Folder semantics

```yaml
folders:
  systems:
    role: current system-specific synthesis
    canonical_for: current interpretation of a concrete framework/runtime
    package_contract: systems/PACKAGE_SPEC.md
  mk:
    role: maturity pipeline and normalized domain canon
    canonical_for: schemas, dimensions, records, gates, promoted vocabulary
  architecture:
    role: cross-system architecture/threat artifacts
  quarries:
    role: processed evidence and historical reasoning
    canonical_for_current_state: false
  mining-site:
    role: source identity, snapshot, provenance, license
    canonical_for_current_state: false
```

## Current-state precedence

```text
1. STATUS.md
2. systems/<system>/ current synthesis
3. active/frozen MK schema + records + GATES + UNKNOWNS
4. quarries/
5. mining-site/ source receipts
```

For work priority:

```text
1. ROADMAP.md
2. active MK CLOSURE_PLAN.md
3. active MK CLASSIFICATION_QUEUE.md / specialized gate spec
```

For provenance:

```text
current synthesis/record
→ MK decision/gate
→ quarry/cross-source synthesis
→ mining-site source receipt
→ pinned upstream source/spec/test
```

## Reasoning-state vocabulary

```yaml
reasoning_states:
  SOURCE_CLAIM: upstream states it
  OBSERVED: directly visible in source/code/test/artifact
  INFERRED: derived from explicit observations
  SUPPORTED: enough evidence for scoped claim
  QUALIFIED: supported with important boundaries
  CONTRADICTED: evidence rejects claim as stated
  UNKNOWN: material evidence missing
```

Provenance vocabulary:

```text
OFFICIAL | OBSERVED | INFERRED | INSPIRED | GENERATED
```

Never convert `UNKNOWN` into a favorable default.

## Current live snapshot

```yaml
mk1:
  state: IN_PROGRESS
  schema: mk1-draft-2026-09-16.1
  record_coverage:
    materialized_or_qualified: 11
    covered_by: 2
    open_blocking:
      - REC-012 multi-agent baseline/admission evidence
  protocols:
    mcp_2026_07_28: SUPPORTED_QUALIFIED
    a2a_classification_shape: PASS_QUALIFIED
    strands_a2a_0_3: SUPPORTED_QUALIFIED
    strands_a2a_1_0_compatibility: NOT_ESTABLISHED
  blockers:
    - REC-012 multi-agent baseline/admission evidence
    - final UNKNOWN reconciliation
    - cross-dimension/overlap audit
    - schema freeze decision
    - MK1 CLOSURE.md
mk2:
  state: BLOCKED_DESIGN_SEEDED
  handoff: mk/MK2/HANDOFF_CONTRACT.md
```

For newer state, defer to `STATUS.md`.

## Current record set

Materialized/qualified:

```text
REC-001 minimal while-loop
REC-002 HITL approval
REC-003 trace evaluation
REC-004 generated-code/browser E2E
REC-007 social publication
REC-008 document/data egress
REC-009 database authority
REC-010 reflection/adaptation
REC-011 memory lifecycle contrast
REC-013 MCP revision drift
REC-014 Strands Agents
```

Coverage decisions:

```text
REC-005 COVERED_BY REC-004 + REC-003
REC-006 COVERED_BY REC-002 + REC-007
```

Open:

```text
REC-012 multi-agent baseline/admission evidence
```

Authoritative registry: `mk/MK1/records/README.md`.

## Core domain rules safe as working knowledge

```yaml
principles:
  - framework identity is not taxonomy
  - use the simplest sufficient architecture
  - critical policy belongs in enforceable code/policy boundaries
  - model intent and runtime authorization are distinct
  - tools are typed interfaces but permissions/side effects are separate
  - capability composition determines blast radius
  - side effects and data egress require explicit risk/verification reasoning
  - edited actions are new actions when approval binding matters
  - context, state, checkpoints, persistence and memory are distinct
  - persistence does not imply concurrency safety
  - budget values require enforcement-boundary semantics
  - cancellation requires an effective boundary and does not imply rollback
  - human control requires enforcement owner/boundary and dispatcher coverage
  - runtime termination does not prove external task success
  - outcome and trajectory evaluation are distinct
  - stochastic reliability claims require repeated evidence
  - multi-agent topology and measured benefit are separate
  - least privilege and containment are agent-system invariants
  - protocol compatibility is revision-aware and not authorization
  - framework capability is not deployment configuration
  - production readiness is a project evidence vector, not a framework label
```

These are working principles, not automatic MK2 operational certification.

## Query routing

| Query | Preferred path |
|---|---|
| What is agent engineering here? | `README.md` → `KNOWLEDGE_MAP.md` |
| What are we working on now? | `STATUS.md` → `ROADMAP.md` |
| What exact work closes MK1? | `mk/MK1/CLOSURE_PLAN.md` |
| Which representative records exist? | `mk/MK1/records/README.md` |
| How do I create a new record? | `mk/MK1/records/TEMPLATE.md` |
| How do we classify systems? | `mk/MK1/CLASSIFICATION_SCHEMA.md` + `DIMENSIONS.md` |
| Why did the schema change? | `mk/MK1/SCHEMA_HISTORY.md` + relevant quarry |
| What still blocks MK1? | `mk/MK1/GATES.md` + `CLOSURE_PLAN.md` + `UNKNOWNS.md` |
| What is the A2A status? | `systems/strands/PROTOCOLS.md` + `quarries/strands-a2a-version-drift.md` |
| What evidence contract applies to A2A? | `mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md` |
| What evidence is required for multi-agent? | `mk/MK1/MULTI_AGENT_BASELINE_SPEC.md` |
| What does MK2 receive? | `mk/MK2/HANDOFF_CONTRACT.md` |
| How do I add a current system package? | `systems/PACKAGE_SPEC.md` |
| What do we know about Strands? | `systems/strands/LLM_CONTEXT.md` |
| What is the source/snapshot? | `mining-site/SOURCES.md` + relevant `S-xxx` |
| What were original observations? | relevant `quarries/*` |

## A2A anti-overclaim rule

Current safe statement:

```text
Pinned Strands supports A2A 0.3 surfaces with source + integration-fixture evidence.
Current A2A protocol line is 1.0.
Strands A2A 1.0 compatibility is NOT ESTABLISHED.
```

Do not turn `A2A classification-shape PASS / QUALIFIED` into `A2A 1.0 interoperability PASS`.

## Normalized-record rule

A quarry containing evidence is not equivalent to a materialized MK1 record. For family-coverage/closure claims inspect `mk/MK1/records/README.md`.

A record must instantiate the current schema or link to a canonical system `CLASSIFICATION.md`. `COVERED_BY` is allowed only when the registry explicitly records why a separate record would add no material schema pressure.

## Strands package

```text
systems/strands/
├── README.md
├── CLASSIFICATION.md
├── ENGINEERING_RULES.md
├── PROTOCOLS.md
├── EVIDENCE.md
└── LLM_CONTEXT.md
```

Use `systems/strands/LLM_CONTEXT.md` before historical Strands quarries for current questions.

## Historical-state behavior

Historical documents may be correct for their observation time and stale for current status.

Example:

```text
T1 Strands surfaces candidate concurrency/budget/intervention fields
T2 LangGraph + OpenAI Agents SDK confirm distinctions
T3 MK1 promotes fields into schema
```

Report state transitions; never rewrite historical evidence as if later conclusions were already known.

## Framework comparison rule

Do not rank frameworks by feature count. Normalize each against:

```text
control authority
horizon/topology
capabilities/composition
side effects
enforcement
state/persistence/concurrency
memory lifecycle
retry/error ownership
termination/budgets/cancellation
evaluation
protocol revision
security boundary
reproducibility evidence
UNKNOWNs
```

## High-bar claims

Require project/system-specific evidence before asserting:

```yaml
high_bar_claims:
  - production ready
  - secure
  - exactly once
  - safe retry
  - sandboxed
  - concurrency safe
  - authorized
  - rollback guaranteed
  - self improving
  - multi-agent performs better
  - memory is trustworthy
  - protocol compatible across all revisions/servers
```

## Prohibited inference patterns

```text
framework has feature             != application enables feature
protocol supported                != invocation authorized
cancellation sent                 != remote effect rolled back
state persisted                   != concurrent writers safe
structured output valid           != semantic output correct
human review exists               != every consequential dispatcher protected
multi-agent topology exists       != task performance improves
source says production-ready      != project production-ready
A2A 0.3 implementation exists     != A2A 1.0 compatibility
fixture exists/in CI scope        != specific CI run passed
```

## MK discipline

```text
MK0 = evidence/framing
MK1 = normalize/classify
MK2 = operational contracts/tests
MK3 = integrate across domains/systems
MK4 = automate checks/evals
MK5+ = repeated/independent certification
```

## Update discipline

When new material evidence arrives:

1. pin source/revision;
2. update/add source receipt;
3. process evidence in quarry;
4. compare against current schema;
5. materialize/update normalized record when classification or coverage changes;
6. pressure-test schema changes independently;
7. update system package when current understanding changes;
8. update GATES/UNKNOWNS/record registry;
9. update STATUS/ROADMAP only when state or priority changes;
10. preserve historical reasoning.

## Retrieval objective

Prefer the **smallest current canonical path that answers the question**, then descend only when provenance or ambiguity requires it. This minimizes token waste without sacrificing auditability.
