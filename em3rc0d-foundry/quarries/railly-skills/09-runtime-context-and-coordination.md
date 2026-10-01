# Railly Skills — Runtime, Context and Coordination

Provenance: OBSERVED + INFERRED
Primary upstream: subagents/, herdr-workstreams, compiled knowledge, work-item manifest

## Roles are boundaries, not personalities

The source defines three subagent roles:

- brahe — read-only reconnaissance/evidence packets;
- kepler — bounded implementation;
- occam — independent review.

The valuable abstraction is not the names.

It is:

    reconnaissance authority
      != implementation authority
      != review authority

## Recon

brahe:

- frames one question;
- locates before reading broadly;
- anchors claims to file/line;
- classifies observed/inferred/reported/unknown;
- remains read-only;
- produces an evidence packet, not a repo tour.

Portable lesson:

    research should serve the next decision, not maximize context gathered

## Implementation

kepler:

- bounds one outcome + proof before edit;
- reuses existing infrastructure before reinventing;
- reads current source/docs before external API code;
- keeps evidence chain;
- stops blind iteration after repeated failure;
- proves before saying done;
- never silently widens external authority.

## Review

occam:

- compiles house conventions into runnable checks;
- deterministic layer first;
- only triggered judgment lenses;
- adversarial verification;
- mandatory exemptions/issue-candidate reporting;
- read-only.

## Context != authority

herdr-workstreams states this explicitly.

A context root may expose notes/handoffs, while commands run inside the selected checkout.

Access to context does not grant mutation authority over it.

This is highly portable for personal knowledge + project repo integration.

## Minimal persistent topology

The source prefers:

- one workspace per checkout/worktree;
- one persistent lead;
- optional runtime process;
- specialist agents only when a method requires them.

It rejects a permanently running panel of reviewers.

Portable lesson:

    keep durable coordination minimal;
    create specialist context just-in-time

## Runtime adapters should not own method

Herdr only materializes topology and agent lifecycle.

Solution Gate, Software Factory and Review Gate remain method owners.

This protects procedure portability across execution harnesses.

## Degradation

When preferred independent runtime fails, the system records:

- actual execution mode;
- degraded-from mode;
- independence gap.

Sequential isolated self-review is not described as independent.

## Compiled context

The Foundry knowledge layer is deliberately unavailable to ordinary installed execution.

This supports two contexts:

### Execution context

Small:

- current contract;
- current procedure;
- needed references;
- current evidence handles.

### Evolution context

Larger:

- cases;
- patterns;
- provenance;
- rejected proposals;
- maturity/evals;
- usage candidates.

Mixing them would spend tokens and leak evolutionary/private context into ordinary work.

## EM3RC0D adaptation

INSPIRED:

Create a provider-neutral runtime adapter contract later.

Do not encode:

- Herdr;
- FX;
- one model vendor;
- macOS Keychain;
- one specific agent directory

as Foundry architecture requirements.

The Foundry should specify required properties such as isolation, authority, artifact return and model-family independence where needed. Runtime adapters satisfy those properties.
