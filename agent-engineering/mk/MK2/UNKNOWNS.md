# MK2 — Operational UNKNOWNs

Status: **DESIGN SEED / OPEN**

MK2 must not turn missing implementation evidence into default policy. These questions are expected to remain open until MK1 stabilizes or project-specific evidence exists.

## Contract design unknowns

- exact schema-versioning strategy and migration policy;
- which contract fields are globally mandatory versus capability-dependent;
- whether side-effect severity and confidentiality/data-egress severity require separate policy objects;
- whether sandbox semantics need capability-specific profiles instead of one enum;
- how nested/child-agent contracts inherit or restrict parent authority;
- how to bind authorization receipts across distributed runtimes.

## Retry / side-effect unknowns

- standard representation for timeout with unknown external outcome;
- minimum idempotency evidence required for each mutation family;
- compensating-action semantics when external APIs offer no idempotency;
- duplicate prevention across crash/replay boundaries.

## Memory unknowns

- portable memory quality metrics across semantic/episodic/procedural stores;
- validation/provenance requirements before memory writes;
- deletion/tombstone propagation across derived memories;
- cross-agent shared-memory permission and poisoning controls.

## Evaluation unknowns

- minimum repeated-trial counts by risk/stochasticity class;
- when trajectory constraints should be exact versus outcome-driven;
- how to compare model/provider changes without overfitting to one harness;
- minimum production-observability evidence for a `production-ready` claim.

## Security unknowns

- portable isolation guarantees across process/container/VM/managed sandboxes;
- safe browser-session credential delegation models;
- capability escalation/revocation across long-running agents;
- trust semantics for third-party MCP/tool servers and dynamic discovery.

## Resolution policy

An operational unknown can be closed only by one of:

- stabilized MK1 classification evidence;
- explicit design decision with rationale and bounded applicability;
- current official contract/specification;
- executable fixture/test;
- real integration/production evidence in later MKs.

`reasonable default` is not a sufficient closure reason for high-impact unknowns.
