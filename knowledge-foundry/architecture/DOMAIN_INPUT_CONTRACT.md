# Domain Input Contract

Status: **MK0 candidate / GENERATED**

## Purpose

Define when a bounded slice of `personal_knowledge` may be compiled into an educational product.

The compiler consumes **knowledge slices**, not whole folders and not repository reputation.

## Eligibility states

- `ELIGIBLE` — sufficiently canonical, traceable, fresh and rights-safe for the declared product claim.
- `ELIGIBLE_WITH_LIMITATIONS` — usable only within explicit scope/limitations.
- `RESEARCH_ONLY` — useful for exploration, not for instructional truth claims.
- `BLOCKED` — missing evidence, authority, freshness, rights or contradiction resolution.

## Minimum input record

```yaml
domain:
artifact_path:
artifact_revision:
knowledge_state:
authority:
provenance:
evidence_path:
known_unknowns:
contradictions:
freshness:
rights_status:
allowed_claim_scope:
eligibility:
limitations:
refresh_triggers:
```

Unknown fields remain `UNKNOWN`.

## Admission rules

A slice is eligible only when:

1. its authority inside the source domain is explicit;
2. its maturity/promotion state is explicit;
3. claims can be traced to inspected evidence;
4. material contradictions are resolved or bounded;
5. freshness is adequate for the claim;
6. rights/reuse boundaries are known for any reproduced material;
7. an exact revision or observation boundary can be pinned;
8. the compiler can detect when the dependency becomes stale.

A whole domain does **not** need to be fully mature if a bounded package has its own explicit promotion state and evidence boundary.

Example: a solidified system package inside an active MK can be `ELIGIBLE_WITH_LIMITATIONS` while the rest of the domain remains in progress.

## Legacy source-registry rule

Older domains predate the normalized JEM Source Intake Contract.

Missing `access_state`, `capture_state`, `verification_state`, `promotion_state` or claim boundary fields must be treated as **UNKNOWN**, not inferred from the existence of a URL.

Knowledge Foundry does not rewrite those domains automatically. It records the debt and blocks claims that depend on the missing dimension.

## Commercial-release rule

For a paid/released product, eligibility is stricter than for an internal pilot:

- source revision pinned;
- rights basis explicit;
- dependency manifest complete;
- time-sensitive claims refreshed;
- no unresolved contradiction that changes the taught capability.

## Anti-pattern

```text
domain exists
→ README looks good
→ compile course
```

Correct:

```text
bounded knowledge slice
→ authority
→ maturity
→ evidence
→ freshness
→ rights
→ dependency pin
→ eligibility decision
```
