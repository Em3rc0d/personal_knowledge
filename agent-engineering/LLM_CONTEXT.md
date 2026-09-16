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

Before retrieving detail, classify the user's intent:

```yaml
intent:
  current_state: STATUS.md
  next_work: ROADMAP.md
  repository_semantics: REPOSITORY_CONTRACT.md
  system_specific_current: systems/<system>/LLM_CONTEXT.md
  classification_semantics: mk/MK1/README.md + schema/dimensions
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

When documents conflict because research progressed over time:

```text
1. STATUS.md
2. systems/<system>/ current synthesis
3. active/frozen MK schema + records + GATES + UNKNOWNS
4. quarries/
5. mining-site/ source receipts
```

For **work priority**:

```text
1. ROADMAP.md
2. active MK CLOSURE_PLAN.md
3. active MK CLASSIFICATION_QUEUE.md / specialized gate spec
```

These precedence rules answer **what is current / what is next**. They do not replace evidence tracing.

## Provenance traversal

For “why?”, “source?”, “evidence?”, “how was this decided?” questions:

```text
current synthesis/record
→ MK decision/gate
→ quarry/cross-source synthesis
→ mining-site source receipt
→ pinned upstream source/spec/test
```

Never present a current synthesis as though it were the original external source.

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

Do not silently turn `UNKNOWN` into a probable/favorable default.

## Current live snapshot

```yaml
mk1:
  state: IN_PROGRESS
  schema: mk1-draft-2026-09-16.1
  materialized_records:
    - REC-001 minimal while-loop
    - REC-002 HITL approval
    - REC-013 MCP revision drift
    - REC-014 Strands Agents
  blockers:
    - generated-code/browser high-capability record
    - data-egress record
    - dedicated memory record
    - evaluation/critic pressure
    - A2A reproducibility receipt
    - multi-agent baseline/admission evidence
    - final schema freeze audit
mk2:
  state: BLOCKED_DESIGN_SEEDED
  handoff: mk/MK2/HANDOFF_CONTRACT.md
```

For newer state, defer to `STATUS.md`.

## Core domain rules safe as working knowledge

These are high-confidence working principles carried through MK0/MK1. They are not automatically operational certification until MK2+.

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
| What rules prevent bad normalization? | `mk/MK1/NORMALIZATION_RULES.md` |
| What still blocks MK1? | `GATES.md` + `CLOSURE_PLAN.md` + `UNKNOWNS.md` |
| What evidence is required for A2A? | `mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md` |
| What evidence is required for multi-agent? | `mk/MK1/MULTI_AGENT_BASELINE_SPEC.md` |
| What does MK2 receive? | `mk/MK2/HANDOFF_CONTRACT.md` |
| How do I add a current system package? | `systems/PACKAGE_SPEC.md` |
| What do we know about Strands? | `systems/strands/LLM_CONTEXT.md` |
| What is the source/snapshot? | `mining-site/SOURCES.md` + relevant `S-xxx` |
| What were original observations? | relevant `quarries/*` |

## Normalized-record rule

A quarry containing evidence is **not equivalent** to a materialized MK1 record.

For closure claims, inspect:

```text
mk/MK1/records/README.md
```

A record must instantiate the current schema or link to a canonical system `CLASSIFICATION.md`.

Do not claim family coverage from evidence-only rows.

## Strands package

Current complete system package:

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

A historical document may be correct for its time while stale for current status.

Example:

```text
T1 Strands surfaces candidate concurrency/budget/intervention fields
T2 LangGraph + OpenAI Agents SDK confirm distinctions
T3 MK1 promotes fields into schema
```

Report the transition. Do not rewrite T1 as if the field had always been canon, and do not treat T1's candidate label as current.

## Framework comparison rule

Do not rank frameworks by feature count.

Normalize each against:

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

A framework may support multiple architecture classes simultaneously.

## High-bar claims

Require system/project-specific evidence before asserting:

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

Do not infer:

```text
framework has feature
→ application enables feature

protocol supported
→ invocation authorized

cancellation sent
→ remote effect rolled back

state persisted
→ concurrent writers safe

structured output valid
→ semantic output correct

human review exists
→ every consequential dispatcher is protected

multi-agent topology exists
→ task performance improves

source says production-ready
→ project is production-ready
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

Do not promote an MK1 classification distinction into a certified operational rule merely because its vocabulary is stable.

## Update discipline

When new material evidence arrives:

1. pin source/revision;
2. update/add source receipt;
3. process evidence in quarry;
4. compare against current schema;
5. materialize/update normalized record if classification changes or coverage is needed;
6. pressure-test schema changes independently;
7. update system package if current system understanding changes;
8. update GATES/UNKNOWNS/record registry;
9. update STATUS/ROADMAP only when state or priority changes;
10. preserve historical reasoning.

Repository-wide structure rules: `REPOSITORY_CONTRACT.md`.

## Retrieval objective

Prefer the **smallest current canonical path that answers the question**, then descend only when evidence detail is required.

This minimizes token waste while preserving provenance and prevents historical quarries from becoming accidental current truth.
