# EM3RC0D Foundry — Candidate Artifact Model

Provenance: GENERATED + INSPIRED
Status: MK0 candidate.

## Why artifacts matter

Conversation is not state.

The Foundry needs durable artifacts that survive:

- session changes;
- model changes;
- context compaction;
- branch changes;
- reviewer handoff;
- later contradiction.

## Candidate artifacts

### 1. Source Receipt

Purpose: pin provenance.

Fields:

- source ID;
- owner/origin;
- exact version/commit/date;
- access status;
- license/usage boundary;
- inspected surfaces;
- limitations;
- refresh trigger.

### 2. Work Contract

Human-readable mission.

Candidate sections:

- outcome;
- observed;
- expected;
- acceptance IDs;
- non-goals;
- invariants;
- source/evidence;
- design/architecture decisions;
- change surface;
- risk;
- verification map;
- authority;
- open decisions;
- change history.

### 3. Work Manifest

Machine transaction state.

Candidate fields:

- work identity;
- source digest;
- repo/artifact identity;
- profile;
- authority;
- stage states;
- procedure/asset revisions;
- evidence receipts;
- invalidation history;
- orchestration mode;
- outcome;
- close-cycle state.

### 4. Stage Receipt

One stage’s exact proof.

Minimum identity:

- stage;
- status;
- exact state;
- method/skill revision;
- command or observation;
- environment;
- relevant paths/dependency cone;
- evidence handles;
- duration if available;
- reason/gap;
- reuse eligibility.

### 5. Decision Trail

Append-only record of non-mechanical choices made during implementation/design.

Use only for decisions a reviewer would plausibly ask “why this instead of that?”

Avoid logging mechanical noise.

### 6. Evidence Pack

Human-review surface.

May include:

- screenshots;
- before/after;
- demo URL;
- CLI transcript;
- benchmark;
- test-strength result;
- resilience matrix;
- security receipt;
- release candidate identity.

Every artifact states what it does **not** prove.

### 7. Review Receipt

Exact-state verdict with:

- deterministic checks;
- triggered lenses;
- specialist receipts consumed;
- findings;
- gaps;
- exemptions;
- claim/property/oracle links.

### 8. Promotion Receipt

Records:

- exact state;
- exact external action;
- human authority;
- timestamp;
- destination/result.

One approval does not silently authorize adjacent actions.

### 9. Case

Evidence ledger after meaningful work.

Separates:

- technical validation;
- human review;
- product/maintainer acceptance;
- delivery/production state.

### 10. Reusable Asset Record

Candidate/promoted asset with:

- type;
- version;
- contract;
- source cases;
- applicable contexts;
- exclusions;
- tests/evals;
- maturity;
- owner;
- deprecation path.

### 11. Impact Record

Append-only record of a proposed change to reusable capital.

Stores accepted, rejected, absorbed, superseded and no-change outcomes.

## Artifact design rules

- one source of truth per mutable fact;
- generated views are regenerated, not hand-edited;
- machine state and human narrative may coexist but not disagree silently;
- exact identity is required for evidence reuse;
- open gaps are first-class;
- deprecated artifacts remain retrievable for provenance.
