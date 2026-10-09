# Design Contract → Foundry (architecture candidate)

Status: INSPIRED / GENERATED · PROPOSED (not promoted to runtime canon)
Date: 2026-10-09
Source study: [M3E Canvas](../../web-design/mining-site/m3e-canvas.md)
Authority: human promotion required; no implementation authorized.

## Decision boundary

The **canonical, schema-versioned design JSON** is the source of truth for UI design intent. Prompts, previews, CSS/tokens and generated code are derivatives or implementations, not competing authorities.

This does **not** replace authoritative business requirements, API specifications, security controls, architecture records or product evidence. Design JSON must reference these other contracts rather than claim ownership of their domains.

## Proposed artifact graph

```text
Evidence + UX requirements + existing product contracts
                       |
                       v
        Canonical Design JSON (versioned)
                       |
             schema + invariants
                       |
             +---------+----------+
             |                    |
             v                    v
    Human preview             Agent prompt
             |                    |
             +---------+----------+
                       |
             Foundry implementation
                       |
       conformance tests + independent review
                       |
              delivery / evidence
```

## Minimum proposed design JSON facets

- schemaVersion, documentId, revision, parent revision, provenance, and decision/evidence references;
- platform targets and supported viewport/device classes;
- semantic screens, routes, hierarchy, and reusable component references;
- design tokens for color, typography, spacing, shape, elevation and motion;
- component states, events, transitions, focus and error/empty/loading states;
- accessibility rules including contrast, semantic labeling, keyboard and reduced motion;
- responsive transformation rules, constraints, overflow and safe-area behavior;
- asset references with licenses and origin;
- acceptance criteria and explicit unknowns.

Exact schemas and versioning strategy remain OPEN pending a scoped MK design exercise. Do not mistake this list for an accepted JSON Schema.

## Contract gates (proposal)

G0. SOURCE: each rule points to OFFICIAL, OBSERVED, INFERRED, INSPIRED or GENERATED evidence; missing evidence is UNKNOWN.
G1. VALIDATE: parse, schema validation, reference integrity, uniqueness, allowed state transitions, token resolution, migration and compatibility checks.
G2. DERIVE: prompts and previews are produced from an identified design revision; capture generator version and any nondeterministic inputs.
G3. IMPLEMENT: code generation consumes a pinned revision; generated artifacts record lineage; target runtime is explicit (e.g., Flutter versus web).
G4. PROVE: independent assertions check layout at chosen breakpoints, component states, interactions, accessibility, semantics and visual regression. Static success alone is insufficient.
G5. RECONCILE: a manual code change that alters UI intent creates a discrepancy; reconcile through proposed JSON contract change + validation + human promotion. Never silently reverse-sync code into accepted source.
G6. PROMOTE: explicit human approval governs contract promotion and delivery. No generator can self-certify.

## Failure semantics

- Unsupported or ambiguous source fields: FAIL CLOSED, request a contract revision.
- External domain conflicts (business, API, security): block implementation rather than let UI data override external authority.
- Preview / prompt / code drift: record discrepancy and revise canonical contract; do not overwrite evidence.
- Nondeterministic agent interpretation: classify as implementation variability and verify outputs against the contract.
- Missing device coverage: UNKNOWN, not "responsive passed".

## Adoption decision

ADOPT as research framing only. Do not import M3E code, add packages, fork repositories, introduce hosted services or trigger product implementation. The next eligible work is a scoped schema comparison and a testable proof plan, both behind existing Foundry MK gates.
