# Jett Engineering Method — MK1

State: **IN PROGRESS**

## Objective

Normalize JEM concepts that were framed in MK0 into reusable contracts, schemas and classifications without changing the MK0 historical foundation.

## First normalized contract — source intake

The first MK1 slice formalizes a gap exposed by real research work: receiving a URL or other pointer does not prove that the underlying source was resolved, inspected or captured.

Artifacts:

- [Source Intake Contract](../../SOURCE-INTAKE-CONTRACT.md)
- [Source Intake Record template](../../templates/SOURCE-INTAKE-RECORD.md)

## Acceptance criteria for this slice

- [x] pointer, source identity and evidence are explicitly separated;
- [x] access, capture, verification and promotion states are independent;
- [x] short-link failure behavior is fail-closed;
- [x] snippets/previews cannot silently substitute for source content;
- [x] dynamic-source drift has an observation boundary;
- [x] a reusable source intake record exists;
- [ ] contract is exercised against representative real-source fixtures;
- [ ] terminology is checked against existing domain-specific source registries;
- [ ] contradictions with existing provenance semantics are resolved;
- [ ] MK1 review certifies the contract for cross-domain use.

Until those remaining checks close, this is an active MK1 normalization slice, not a completed JEM MK1.
