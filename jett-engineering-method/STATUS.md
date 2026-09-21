# Jett Engineering Method — STATUS

## Current MK

`MK1 — Normalize & Classify`

## State

`IN PROGRESS — SOURCE INTAKE NORMALIZATION`

MK0 remains **CLOSED — INTERNAL CANON FOUNDATION**. MK1 extends that foundation; it does not rewrite the historical MK0 certification boundary.

## MK0 foundation preserved

- Core purpose and scope defined.
- Problem → Recover → Brainstorm → Design → Architecture → Plan → Build → Test → Prove → Release/Promote → Observe → Learn lifecycle documented.
- Product, Implementation, Evidence, Operational and Commercial truth separated.
- Permanent and contextual gates defined.
- Claim discipline and provenance taxonomy documented.
- Constitutional rules consolidated.
- Monorepo branch/promotion rule integrated.

## MK1 — completed in current slice

- [x] source pointer, source identity and inspected evidence are separated;
- [x] access, capture, verification and promotion states are modeled independently;
- [x] short-link failure behavior is fail-closed;
- [x] snippets/previews cannot silently substitute for underlying source content;
- [x] dynamic/mutable sources require an observation boundary;
- [x] reusable source-intake record template exists;
- [x] JEM lifecycle and claim discipline route through the source-intake boundary.

Artifacts:

- [`SOURCE-INTAKE-CONTRACT.md`](./SOURCE-INTAKE-CONTRACT.md)
- [`templates/SOURCE-INTAKE-RECORD.md`](./templates/SOURCE-INTAKE-RECORD.md)
- [`mk/MK1/README.md`](./mk/MK1/README.md)

## Remaining MK1 work for this slice

- [ ] exercise the contract against representative real-source fixtures;
- [ ] compare terminology with domain-specific source registries already present in `personal_knowledge`;
- [ ] verify that no existing domain treats previews/snippets as canonical evidence;
- [ ] resolve any contradictions found during that audit;
- [ ] run an MK1 review before declaring this contract cross-domain certified.

## Blocked / unresolved

No architectural blocker is known.

Individual incoming sources may legitimately remain `BLOCKED`, `UNKNOWN` or `INCONCLUSIVE` when their content cannot be inspected. That state must not block unrelated repository work and must not be converted into inferred source content.

## Next gate

Use real source fixtures to test whether the contract is sufficient across:

```text
stable documentation
versioned repositories
PDFs
dynamic web pages
social posts
short-links / redirectors
screenshots / user-provided captures
mutable analytics dashboards
```

Then review the normalized state vocabulary and either:

```text
PASS
PASS WITH LIMITATIONS
FAIL
UNKNOWN
```

for cross-domain adoption.

## Certification boundary

Current MK1 work is **not yet a completed JEM MK1**.

The new contract is an active normalization candidate until representative fixtures and contradiction review close.

## Last verified

2026-09-21 — branch `knowledge/jett-method-mk1-source-intake`.
