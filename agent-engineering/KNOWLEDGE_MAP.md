# Agent Engineering — Knowledge Map

Status: **CANONICAL NAVIGATION MAP**

This document explains how `agent-engineering/` is organized so a human or LLM can locate the **current answer**, the **execution plan**, the **normalization contract**, and the **evidence trail** without confusing them.

## Repository model

The domain is organized by **epistemic role** and **maturity role**, not by framework popularity.

```text
agent-engineering/
│
├── README.md                # domain orientation / human entrypoint
├── STATUS.md                # live state: active, closed, blocked
├── ROADMAP.md               # execution order / next gates
├── REPOSITORY_CONTRACT.md   # authority, lifecycle, conflict rules
├── KNOWLEDGE_MAP.md         # this navigation map
├── LLM_CONTEXT.md           # machine routing / anti-inference rules
│
├── systems/                 # current canonical view of concrete systems
│   ├── PACKAGE_SPEC.md      # contract for future system packages
│   └── strands/             # first complete system package
│
├── mk/                      # maturity pipeline / normalized domain canon
│   ├── MK0/                 # evidence framing — closed
│   ├── MK1/                 # taxonomy/classification — active
│   │   ├── records/         # normalized representative classifications
│   │   ├── CLOSURE_PLAN.md  # exact closure dependency graph
│   │   └── ...
│   └── MK2/                 # operationalization design — blocked
│       └── HANDOFF_CONTRACT.md
│
├── architecture/            # cross-system architectural artifacts
├── mining-site/             # source registry + source receipts
└── quarries/                # processed evidence, contradictions, history
```

Structure contract: [`REPOSITORY_CONTRACT.md`](./REPOSITORY_CONTRACT.md).

## The five operational questions

```text
1. Where are we?              → STATUS.md
2. What happens next?         → ROADMAP.md
3. What do we know today?     → systems/ + active/frozen MK
4. Why do we believe it?      → quarries/ + mining-site/
5. What must be true to move? → active MK GATES / CLOSURE_PLAN / handoff
```

## Knowledge layers

### 1. Live control layer

Files:

- `STATUS.md`
- `ROADMAP.md`
- `REPOSITORY_CONTRACT.md`

Answers:

- What is active/blocked/closed?
- Which blocker should be attacked next?
- Which file owns which kind of truth?
- What transition rules prevent silent promotion?

### 2. Current system layer

Files:

- `systems/<system>/`

Answers:

- What do we currently know about this concrete framework/runtime?
- What is its current normalized classification?
- What reusable engineering lessons did it expose?
- What protocol evidence/UNKNOWNs remain?

System-package contract: [`systems/PACKAGE_SPEC.md`](./systems/PACKAGE_SPEC.md).

### 3. Normalized domain layer

Files:

- `mk/MK*/`
- `architecture/`

Answers:

- What vocabulary/dimensions are framework-independent?
- Which schema revision is active/frozen?
- Which records instantiate it?
- What closes the current MK?
- What will the next MK receive?

In MK1:

```text
CLASSIFICATION_SCHEMA.md
DIMENSIONS.md
NORMALIZATION_RULES.md
SCHEMA_HISTORY.md
records/
GATES.md
CLOSURE_PLAN.md
UNKNOWNS.md
```

### 4. Processed evidence layer

Files:

- `quarries/`

Answers:

- What did we observe?
- What contradiction/failure surfaced?
- Which candidate distinction emerged?
- What did the state look like before promotion?

A quarry is **not current canon**. It can preserve a candidate/UNKNOWN that was later promoted, qualified or closed.

### 5. Source provenance layer

Files:

- `mining-site/`

Answers:

- Which source/spec/repository was inspected?
- Which snapshot/revision/date?
- What authority/license applies?
- Where is its processed evidence?

## Canonical information flow

```text
SOURCE / SPEC
mining-site/S-xxx
      │
      ▼
PROCESSED EVIDENCE
quarries/*
      │
      ├─────────────► systems/<system>/ current synthesis
      │
      ▼
NORMALIZATION / RECORDS / GATES
mk/MK*
      │
      ▼
DOMAIN STATE + EXECUTION
STATUS.md + ROADMAP.md
```

New evidence may loop backward and pressure the schema again. The flow is auditable, not strictly one-way.

## Current-state precedence

```text
1. STATUS.md
2. systems/<system>/ current package
3. active/frozen MK schema + records + gates + unknowns
4. quarries/
5. mining-site/
```

For execution priority:

```text
ROADMAP.md
> active MK CLOSURE_PLAN.md
> active MK CLASSIFICATION_QUEUE.md
```

For provenance, traverse downward to the pinned source.

## Human navigation by intent

| Intent | Start here |
|---|---|
| Understand the domain | `README.md` |
| See active/blocked state | `STATUS.md` |
| Know exactly what to do next | `ROADMAP.md` |
| Understand repository authority/lifecycle | `REPOSITORY_CONTRACT.md` |
| Understand repository structure | `KNOWLEDGE_MAP.md` |
| Understand Strands today | `systems/strands/README.md` |
| Inspect system-package requirements | `systems/PACKAGE_SPEC.md` |
| Inspect current classification schema | `mk/MK1/CLASSIFICATION_SCHEMA.md` |
| See representative record coverage | `mk/MK1/records/README.md` |
| See MK1 closure dependencies | `mk/MK1/CLOSURE_PLAN.md` |
| See formal MK1 gates | `mk/MK1/GATES.md` |
| See unresolved/routed uncertainty | `mk/MK1/UNKNOWNS.md` |
| See schema revision history | `mk/MK1/SCHEMA_HISTORY.md` |
| Inspect A2A evidence contract | `mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md` |
| Inspect current A2A receipt | `quarries/strands-a2a-version-drift.md` |
| Understand multi-agent baseline contract | `mk/MK1/MULTI_AGENT_BASELINE_SPEC.md` |
| Understand MK1→MK2 input | `mk/MK2/HANDOFF_CONTRACT.md` |
| Audit a system claim | `systems/*/EVIDENCE.md` → `quarries/` → `mining-site/` |
| Understand threat/capability model | `architecture/` |

## Recommended reading paths

### Fast orientation

```text
README.md
→ STATUS.md
→ ROADMAP.md
```

### Continue active MK1 engineering

```text
STATUS.md
→ ROADMAP.md
→ mk/MK1/README.md
→ mk/MK1/CLOSURE_PLAN.md
→ mk/MK1/MULTI_AGENT_BASELINE_SPEC.md
```

### Deep Strands audit

```text
systems/strands/README.md
→ CLASSIFICATION.md
→ ENGINEERING_RULES.md
→ PROTOCOLS.md
→ EVIDENCE.md
→ quarries/source receipts as needed
```

### Add another system package

```text
REPOSITORY_CONTRACT.md
→ systems/PACKAGE_SPEC.md
→ verify source/quarry/MK evidence
→ create systems/<system>/
→ link normalized record registry
```

### Materialize a new MK1 record

```text
mk/MK1/records/README.md
→ records/TEMPLATE.md
→ existing quarry/source evidence
→ normalized record
→ registry update
→ GATES/UNKNOWNS only if state changed
```

### Freeze MK1 / open MK2

```text
mk/MK1/CLOSURE_PLAN.md
→ GATES.md
→ SCHEMA_HISTORY.md
→ CLOSURE.md
→ mk/MK2/HANDOFF_CONTRACT.md
```

MK2 remains blocked until that transition actually passes.

## LLM navigation

Machine readers start at [`LLM_CONTEXT.md`](./LLM_CONTEXT.md).

> Load the smallest current canonical context sufficient for the question, then descend into evidence only when provenance or ambiguity requires it.

## Knowledge preservation rule

Never delete historical evidence merely because a later pass resolved it.

Instead:

1. preserve evidence/history;
2. mark state transition;
3. update current synthesis;
4. update record/gate/UNKNOWN status;
5. update machine/human routing if retrieval behavior changed.

The repository must answer both:

```text
What do we know now?
Why did we come to believe it?
```

## Naming semantics

- `S-xxx-*` — source receipt / evidence identity.
- `quarries/*` — processed non-canonical evidence/history.
- `systems/<name>/*` — current system-specific synthesis.
- `mk/MKx/records/REC-xxx-*` — representative normalized classification.
- `SCHEMA_HISTORY.md` — schema version/change ledger.
- `GATES.md` — formal pass/fail criteria.
- `CLOSURE_PLAN.md` — executable route to satisfying gates.
- `UNKNOWNS.md` — uncertainty/routing register.
- `HANDOFF_CONTRACT.md` — exact MK transition input contract.
- `STATUS.md` — live domain transition state.
- `ROADMAP.md` — current execution ordering.

## Current maturity snapshot

```text
MK0                              CLOSED
MK1                              IN PROGRESS
MK2                              BLOCKED / DESIGN SEEDED

Strands package                  SOLIDIFIED
runtime semantic crosscheck      COMPLETE
MCP 2026-07-28 core pass         SUPPORTED / QUALIFIED
representative record set        NEAR-COMPLETE (11 + 2 COVERED_BY)
A2A classification shape         PASS / QUALIFIED
A2A 1.0 compatibility            NOT ESTABLISHED
multi-agent baseline / REC-012   OPEN / BLOCKING
UNKNOWN reconciliation           FINAL PASS PENDING
schema freeze                    NOT YET
```

For precise live state, always defer to `STATUS.md`.
