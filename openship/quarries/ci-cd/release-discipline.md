# Quarry — CI/CD and Release Discipline

## Tooling

`OBSERVED`

The monorepo uses Bun + Turborepo. CI includes TypeScript checks and test suites across multiple packages. Database tests can run against PGlite without requiring an external PostgreSQL service for every case.

## Release-gate evolution

`OBSERVED / confidence: high`

The repository documents an important historical weakness: releases previously could publish while tests were still running because workflows were independent.

The newer `release-gate.yml` is callable by publishing workflows and contains blocking jobs for:

- API/package type checking;
- unit/integration tests;
- real Docker daemon E2E;
- rollback/restore-oriented scenarios.

The comments explicitly state that a daemon-unavailable E2E must fail rather than silently skip when the release gate expects real Docker.

## Test reachability lesson

CI comments also document a case where security-relevant webmail tests existed but were not reachable from the actual root pipeline. A separate job was added so "green locally" could no longer be mistaken for "executed in release CI".

## Reusable candidate rules

`INSPIRED`

1. **A test that cannot block the artifact it claims to certify is not a release gate.**
2. **Verify that critical tests execute, not merely that test files exist.**
3. **Real-runtime behavior needs at least one non-mocked certification path.**
4. **Release workflows must depend on gate results structurally, not temporally.**
5. **Historical CI weaknesses should become regression tests/contracts, not tribal knowledge.**

## Caveat

Strong release machinery does not imply absence of application bugs. Recent critical-path issues can coexist with a disciplined gate because coverage is always incomplete and behavior evolves.
