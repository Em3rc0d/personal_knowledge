# Agent Engineering — System Package Specification

Status: **CANONICAL PACKAGE CONTRACT**  
Applies to: `agent-engineering/systems/<system>/`

## Purpose

A system package provides the **current, reconciled view of one concrete agent framework/runtime/system** without forcing readers to reconstruct conclusions from historical evidence.

It is a synthesis layer, not a replacement for provenance.

## Admission criteria

Create a package only when all are true:

1. the system has a pinned source/spec/repository identity;
2. there is enough processed evidence to describe more than marketing/features;
3. at least one MK classification or pressure-test relationship exists;
4. material limitations/UNKNOWNs can be stated explicitly;
5. the package can point back to evidence rather than inventing new claims.

A package is not required for every source receipt.

## Required files

```text
systems/<system>/
├── README.md              required
├── CLASSIFICATION.md      required when MK1 classification applies
├── ENGINEERING_RULES.md   required
├── EVIDENCE.md            required
├── LLM_CONTEXT.md         required
└── PROTOCOLS.md           required when protocol integrations are material
```

Additional files may exist only when they own a distinct question.

## `README.md` contract

Owns: **human mental model**.

Must answer:

- what the system is;
- what it is not;
- core control model;
- major architecture surfaces;
- state/context/memory model;
- tool/capability boundary;
- intervention/policy model;
- termination/budget/cancellation model;
- evaluation/observability posture;
- security boundary;
- protocol posture;
- current important UNKNOWNs;
- reading map to deeper files.

Avoid turning the README into raw source notes.

## `CLASSIFICATION.md` contract

Owns: **current normalized mapping into the active/frozen MK schema**.

Requirements:

- include `schema_revision`;
- classify system capabilities, not brand reputation;
- distinguish framework capability from application/deployment fact;
- use `unknown` rather than inferred defaults;
- preserve protocol revision detail;
- separate availability of evaluation features from evidence that a project uses them;
- link to the canonical schema and supporting pressure tests.

A field should be omitted/unknown if evidence cannot justify one of the allowed values.

## `ENGINEERING_RULES.md` contract

Owns: **reusable lessons extracted from the system**.

Each rule should state:

- rule;
- evidence scope;
- engineering consequence;
- non-claim / boundary;
- promotion state when relevant.

Example structure:

```text
Rule: persistence != concurrency safety
Evidence: system-specific + cross-runtime
Consequence: classify writer/conflict semantics separately
Does not prove: a specific backend is unsafe
State: promoted into MK1
```

Do not use this file to duplicate API documentation.

## `EVIDENCE.md` contract

Owns: **claim → evidence → provenance mapping**.

For each material current claim, record:

- claim;
- reasoning state;
- supporting quarry/MK/source receipt;
- source snapshot/revision where material;
- limitations;
- freshness trigger.

The evidence map should make it possible to answer:

> “What would I inspect to verify this?”

without searching the repository blindly.

## `LLM_CONTEXT.md` contract

Owns: **machine retrieval and anti-inference behavior**.

Must contain:

```yaml
system_identity:
current_snapshot:
canonical_files:
safe_facts:
prohibited_inferences:
unknowns:
freshness_triggers:
query_routing:
```

The exact serialization may remain Markdown/YAML hybrid, but those semantics must be present.

Important: include negative rules such as:

```text
feature available != feature enabled
protocol supported != authorized
cancellation != rollback
persistence != concurrency-safe
structured output != correct output
```

## `PROTOCOLS.md` contract

Owns: **revision-aware interoperability state**.

Do not write:

```text
MCP: yes
A2A: yes
```

Instead record, where known:

```yaml
name:
revision:
role:
transport:
discovery_or_negotiation:
capabilities:
authentication:
authorization_boundary:
cancellation:
observability:
extensions:
execution_evidence:
unknowns:
```

Protocol support must remain separate from application policy/security.

## Package-level status vocabulary

Use these states when useful:

```text
SEED             insufficient for current canonical package
ACTIVE           current package maintained
QUALIFIED        current package has material limitations/UNKNOWNs
STALE            known to require refresh before current claims are trusted
SUPERSEDED       replaced by another canonical package/revision
```

Do not use `CERTIFIED` unless a later MK actually defines and passes a certification gate.

## Freshness model

A package must identify conditions that force revalidation.

Typical triggers:

- major SDK release;
- repository migration;
- protocol revision change;
- changed dependency range;
- changed session/concurrency semantics;
- changed guardrail/intervention execution path;
- changed tool permission model;
- new execution evidence contradicting current synthesis.

A date alone is not a freshness policy.

## Package update transaction

When new evidence changes current understanding:

```text
source receipt/quarry updated first or in same change set
        ↓
MK impact evaluated
        ↓
system package updated
        ↓
EVIDENCE.md updated
        ↓
LLM_CONTEXT safe facts / anti-inference rules updated
        ↓
STATUS/GATES updated only if domain state changed
```

## Duplication boundary

A system package may restate a conclusion for accessibility, but must not become a disconnected second evidence store.

Prefer:

```text
concise current claim
+ link to evidence
```

over copying full quarry detail.

## Current reference implementation

The first complete package is [`strands/`](./strands/).

Use it as a structural reference, **not as a semantic template**. Another framework may have different relevant surfaces and may legitimately leave fields unknown or omit `PROTOCOLS.md` when protocols are not material.
