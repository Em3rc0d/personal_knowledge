# SD-001 — Evidence-bound Architecture Decision

Status: `REFERENCE_ONLY / MK1 CLASSIFIED` · Class: `INSPIRED` + `GENERATED`.
Source: [chapter 03](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/03.%20System%20Design%20Framework/Readme.md).
Canonical lifecycle **owner**: [Jett Engineering Method](../../../../jett-engineering-method/architecture/README.md) — do not clone its gates here.

## Non-duplication disposition
The lifecycle, ADR ownership and promotion gates already live in Jett Engineering Method. This is **a compact discovery cue and cross-reference**, not a second architecture-review framework or an independent gate. If JEM and this card diverge, JEM takes precedence; do not adopt this card as a new canon.

## Use when
Selecting a persistent boundary, architecture style, storage, messaging or external dependency that has meaningful cost or reversibility impact.

## Decision rule
1. State user/business outcome, invariants, hard constraints, **what is unknown**.
2. Quantify relevant scale and failure envelope; cite measurements vs assumptions.
3. Compare at least the minimal baseline with candidate(s): complexity, coupling, costs, latency, security, reversibility and failure modes.
4. Explicitly decide `ADOPT`, `REFERENCE_ONLY`, `REJECT` or `NEEDS_EVIDENCE`.
5. Keep trade-offs, owner and disconfirming evidence in a project-specific ADR; JEM remains process authority.

## Anti-pattern
`We may scale eventually → choose microservices/Kafka today` without workload evidence.

## Test / falsification
A reviewer can reproduce why the chosen option beats the minimal option under given constraints, and can identify a threshold at which it should be revisited. Missing assumption or owner → `NEEDS_EVIDENCE`.

## Boundary
Documentation is not independent architectural certification. No project architecture is approved here.
