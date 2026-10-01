# Railly Skills — Lifecycle and Routing

Provenance: OBSERVED + INFERRED
Primary upstream: README.md, factory-loop, issue-intake, work-intake, workstream-reconcile

## Canonical lifecycle

The public workflow and factory-loop converge on:

    select if needed
      → admit
      → contract
      → shape
      → execute
      → independent Spec
      → Review Gate
      → human-readable evidence
      → human promotion
      → delivery
      → case capture

The router owns transitions. Delegated skills own phase methods.

This avoids a common orchestration failure: using the correct operations in the wrong order.

## Selection is not admission

issue-intake:

- surveys cheaply;
- narrows to three to five candidates;
- keeps uncertainty visible;
- may use xref rankings/clusters as evidence;
- recommends, but the user makes the final selection;
- stops before reproduction/implementation.

work-intake starts **after one source is selected** and is read-only.

It classifies one source into:

- question-support;
- investigation-research;
- unverified-bug;
- feature-request;
- mechanical-maintenance;
- nonmechanical-change;
- pull-request-review.

It then recommends the minimum versioned Formula and waits for explicit human confirmation.

Portable rule:

    classification does not grant mutation authority

## Minimum workflow, not maximum ceremony

The admitted Formula controls how far the item travels.

Support, investigation, reproduction and review can stop at their own human decision. They do not automatically become code-change pipelines.

This is one of the strongest anti-bureaucracy mechanisms in the source.

## Work profiles

factory-loop defines profiles with default wall-time budgets:

- mechanical: 20 minutes;
- standard: 60;
- high-risk: 180;
- external-pr: 90.

OBSERVED: budgets are implementation choices in the source.
INSPIRED: proportional process is portable.
Do not copy the exact minute values into EM3RC0D canon before dogfood.

## Earliest incomplete state

factory-loop does not trust transcript memory.

It:

1. reads the manifest;
2. verifies drift-prone identity/evidence;
3. finds the earliest incomplete current phase;
4. reuses still-valid upstream evidence;
5. reruns only invalidated dependency cones;
6. always preserves final exact-state checks.

This is the key continuation mechanism.

## Open-cycle continuity

handoff is used when a cycle remains open.

handoff:

- verifies Git/disk before prose;
- reports current state, exact next command and owner decisions;
- separates delivery, verification and human judgment;
- is historical lead on resume.

workstream-reconcile then revalidates volatile claims against authoritative current surfaces before routing resumes.

Thus:

    handoff != truth
    handoff = retrieval index + historical checkpoint

## Closed-cycle continuity

When the item closes and leaves a transferable lesson, record-a-case takes over.

A handoff is not a case and a case is not a handoff.

## EM3RC0D implication

INSPIRED lifecycle:

    opportunity/problem
      → qualify
      → admit
      → product/work contract
      → design/shape
      → plan
      → build
      → prove
      → review
      → package
      → exact-action human promotion
      → deliver
      → observe
      → record

Not every product profile needs every phase. The router should choose the smallest evidence-complete path.
