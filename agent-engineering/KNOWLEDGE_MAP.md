# Agent Engineering — Knowledge Map

Status: **CANONICAL NAVIGATION MAP**

This document explains how `agent-engineering/` is organized so a human or LLM can locate the **current answer**, the **normalization contract**, and the **evidence trail** without confusing them.

## Repository model

The domain is organized by **epistemic role** rather than by framework popularity.

```text
agent-engineering/
│
├── README.md              # domain orientation / human entrypoint
├── STATUS.md              # current MK state and active blockers
├── KNOWLEDGE_MAP.md       # this navigation contract
├── LLM_CONTEXT.md         # machine routing / precedence rules
│
├── systems/               # current canonical view of concrete systems
│   └── strands/           # first complete system package
│
├── mk/                    # maturity pipeline / normalized domain canon
│   ├── MK0/               # evidence framing — closed
│   ├── MK1/               # taxonomy/classification — active
│   └── MK2/               # operationalization design — blocked
│
├── architecture/          # cross-system architectural artifacts
│
├── mining-site/           # source registry + immutable-ish source receipts
│
└── quarries/              # processed evidence, contradictions, candidates, history
```

## The four knowledge layers

### 1. Current state

Files:

- `STATUS.md`
- `systems/<system>/`

Answers:

- What do we currently believe?
- What has passed a gate?
- What remains open?
- What is the current interpretation of a concrete framework/runtime?

Use this layer first for current answers.

### 2. Normalized domain canon

Files:

- `mk/MK*/`
- `architecture/`

Answers:

- What vocabulary and dimensions are framework-independent?
- Which rules are merely candidates vs promoted?
- Which gates define maturity?
- What schema should another system be classified against?

Use this layer for reusable engineering semantics.

### 3. Processed evidence

Files:

- `quarries/`

Answers:

- What did we observe?
- What contradictions appeared?
- Which candidate distinctions were surfaced?
- How did reasoning evolve before promotion?

A quarry is **not current canon**. It can intentionally contain historical candidate states later resolved elsewhere.

### 4. Source provenance

Files:

- `mining-site/`

Answers:

- Which source/repository/spec was inspected?
- Which snapshot/version/date?
- What authority/license does the source have?
- Where is its processed evidence?

Use this layer to anchor claims and reproduce research scope.

## Canonical information flow

```text
SOURCE
mining-site/S-xxx
      │
      ▼
PROCESSED EVIDENCE
quarries/*
      │
      ├─────────────► systems/<system>/ current synthesis
      │
      ▼
NORMALIZATION / GATES
mk/MK*
      │
      ▼
DOMAIN STATE
STATUS.md
```

The pipeline is not strictly linear: new framework pressure tests may reveal a schema weakness, causing another cross-source pass before promotion.

## Why `systems/` exists

The evidence/MK pipeline is excellent for auditability but expensive for direct retrieval. A reader asking “what do we know about Strands today?” should not need to manually reconcile five historical documents.

`systems/<system>/` provides a **lossless synthesis layer**:

- current mental model;
- current normalized classification;
- reusable engineering rules;
- protocol state;
- evidence/provenance map;
- LLM-specific routing/anti-inference contract.

It never replaces raw evidence.

## Human navigation by intent

| Intent | Start here |
|---|---|
| Understand the domain | `README.md` |
| See what is active/blocked | `STATUS.md` |
| Understand repository structure | `KNOWLEDGE_MAP.md` |
| Understand Strands today | `systems/strands/README.md` |
| Inspect framework-independent classification | `mk/MK1/CLASSIFICATION_SCHEMA.md` |
| Inspect normalized dimensions | `mk/MK1/DIMENSIONS.md` |
| Audit an evidence claim | relevant `systems/*/EVIDENCE.md` → `quarries/` → `mining-site/` |
| See unresolved questions | active MK `UNKNOWNS.md` |
| See closure criteria | active MK `GATES.md` |
| Understand threat/capability model | `architecture/` |

## Recommended human reading paths

### Fast domain orientation

```text
README.md
→ STATUS.md
→ systems/strands/README.md
```

### Deep Strands audit

```text
systems/strands/README.md
→ CLASSIFICATION.md
→ ENGINEERING_RULES.md
→ PROTOCOLS.md
→ EVIDENCE.md
→ underlying quarries/source receipts as needed
```

### Continue MK1 work

```text
STATUS.md
→ mk/MK1/README.md
→ mk/MK1/GATES.md
→ mk/MK1/CLASSIFICATION_QUEUE.md
→ mk/MK1/UNKNOWNS.md
→ schema/dimensions/rules
```

### Build future operational contracts

Do not begin from quarries directly.

```text
frozen/promoted MK1 semantics
→ MK2 contract catalog
→ schemas/checklists/test obligations
```

MK2 remains blocked until MK1 closes.

## LLM navigation

Machine readers should start at [`LLM_CONTEXT.md`](./LLM_CONTEXT.md).

The general precedence for **current state** is:

```text
STATUS
> current system package
> current MK schema/gates
> quarry
> source receipt
```

The precedence for **provenance** is not the same: trace downward until the source receipt and exact upstream snapshot are identified.

## Knowledge preservation rule

Never “clean up” the repository by deleting a historical quarry merely because its candidate state is no longer current.

Instead:

1. preserve the original evidence;
2. add a current canonical synthesis;
3. mark state transitions explicitly;
4. update indexes/LLM routing;
5. keep UNKNOWNs visible until evidence closes them.

This lets the repository answer both:

```text
What do we know now?
```

and:

```text
Why did we come to believe it?
```

## Naming semantics

- `S-xxx-*` — source receipt / evidence identity.
- `quarries/*` — processed but non-canonical evidence.
- `systems/<name>/*` — current system-specific synthesis.
- `mk/MKx/*` — maturity-stage domain artifacts.
- `STATUS.md` — current domain transition state.
- `GATES.md` — explicit admission/closure requirements.
- `UNKNOWNS.md` — uncertainty that must remain visible.

## Current maturity snapshot

```text
MK0  evidence/framing       CLOSED
MK1  normalize/classify     IN PROGRESS
MK2  operationalize         BLOCKED / DESIGN SEEDED

Strands framework pass      COMPLETE
runtime semantic crosscheck COMPLETE
MCP 2026-07-28 core pass    SUPPORTED / QUALIFIED
A2A reproducibility receipt OPEN
```

For the precise live state, always defer to `STATUS.md`.
