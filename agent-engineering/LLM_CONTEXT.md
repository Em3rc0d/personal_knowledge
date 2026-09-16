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
human_map: KNOWLEDGE_MAP.md
```

## Folder semantics

```yaml
folders:
  systems:
    role: current system-specific synthesis
    canonical_for: current interpretation of a concrete framework/runtime
  mk:
    role: maturity pipeline and normalized domain canon
    canonical_for: schemas, dimensions, gates, promoted vocabulary
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

When two documents appear inconsistent because research progressed over time, prefer:

```text
1. STATUS.md
2. systems/<system>/ current synthesis
3. active/frozen MK schema + GATES + UNKNOWNS
4. quarries/
5. mining-site/ source receipts
```

This precedence answers **what is current**. It does not replace evidence tracing.

## Provenance traversal

For “why?”, “source?”, “evidence?”, “how was this decided?” questions:

```text
current synthesis
→ MK decision/gate
→ quarry/cross-source synthesis
→ mining-site source receipt
→ pinned upstream source/spec
```

Never cite a current synthesis as if it were the original external source.

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

Do not silently turn `UNKNOWN` into a likely guess.

## Core domain rules currently safe to use

These are high-confidence working principles carried through MK0/MK1. They are not all operationally certified until later MKs.

```yaml
principles:
  - framework identity is not taxonomy
  - use the simplest sufficient architecture
  - critical policy belongs in enforceable code/policy boundaries
  - model intent and runtime authorization are distinct
  - tools are typed interfaces but permissions/side effects are separate
  - capability composition determines blast radius
  - side effects require explicit risk/verification reasoning
  - edited actions are new actions and require revalidation when approval binding matters
  - context, state, checkpoints, persistence and memory are distinct
  - persistence does not imply concurrency safety
  - budget values require enforcement-boundary semantics
  - cancellation semantics require an effective boundary and do not imply rollback
  - human control requires enforcement owner/boundary and dispatcher coverage
  - runtime termination does not prove external task success
  - outcome and trajectory evaluation are distinct
  - stochastic systems need repeated evaluation for reliability claims
  - multi-agent topology must prove benefit against simpler baselines
  - least privilege and containment are agent-system invariants
  - protocol compatibility must be revision-aware and is not authorization
  - production readiness is a vector of project evidence, not a framework label
```

## Query routing

| Query | Preferred path |
|---|---|
| “What is agent engineering here?” | `README.md` → `KNOWLEDGE_MAP.md` |
| “What are we working on now?” | `STATUS.md` |
| “What is the MK process?” | `mk/README.md` |
| “How do we classify systems?” | `mk/MK1/CLASSIFICATION_SCHEMA.md` + `DIMENSIONS.md` |
| “What rules prevent bad normalization?” | `mk/MK1/NORMALIZATION_RULES.md` |
| “What still blocks MK1?” | `mk/MK1/GATES.md` + `UNKNOWNS.md` + `CLASSIFICATION_QUEUE.md` |
| “What do we know about Strands?” | `systems/strands/LLM_CONTEXT.md` |
| “Why was an MK1 field added?” | relevant cross-source quarry + schema revision note |
| “What is the raw source/snapshot?” | `mining-site/SOURCES.md` + relevant `S-xxx` receipt |
| “What are the original observations?” | relevant `quarries/*` |
| “Is a source claim production-certified?” | default no; inspect evidence/gates |

## Strands package

The first complete canonical system package is:

```text
systems/strands/
├── README.md
├── CLASSIFICATION.md
├── ENGINEERING_RULES.md
├── PROTOCOLS.md
├── EVIDENCE.md
└── LLM_CONTEXT.md
```

Use `systems/strands/LLM_CONTEXT.md` before retrieving historical Strands quarries.

## Important historical-state behavior

Quarries can be **correct historical documents and stale current summaries at the same time**.

Example pattern:

```text
T1: Strands surfaces candidate field
T2: independent runtimes confirm the distinction
T3: MK1 promotes field
```

Do not rewrite T1 as though the field had always been canon. Instead report the transition.

The same applies to an UNKNOWN later closed or qualified by execution evidence.

## Framework comparison rule

When comparing frameworks:

Do not rank by feature count.

Normalize each against dimensions such as:

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

A framework can support multiple architecture classes simultaneously.

## Safety against overclaiming

Before asserting any of the following, require project/system-specific evidence:

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

## MK discipline

```text
MK0 = evidence/framing
MK1 = normalize/classify
MK2 = operational contracts/tests
MK3 = integrate with broader engineering method/domains
MK4 = automate checks/evals
MK5+ = repeated/independent certification
```

Do not promote an MK1 classification distinction into an operationally certified rule merely because its vocabulary is stable.

## Update discipline

When new evidence arrives:

1. pin source/snapshot;
2. add/update source receipt;
3. process evidence in quarry;
4. compare against current normalized schema;
5. pressure-test proposed schema changes independently;
6. update system package when current understanding changes;
7. update STATUS/GATES/UNKNOWNS;
8. preserve historical reasoning and state transitions.

## Retrieval objective

Prefer the **smallest canonical path that answers the question**, then descend only when evidence detail is needed. This reduces token waste while preserving auditability.
