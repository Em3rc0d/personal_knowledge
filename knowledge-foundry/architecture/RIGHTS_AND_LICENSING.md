# Rights and Licensing Model

Status: **MK0 candidate / GENERATED**, informed by S-005.

This is an engineering/provenance model, not legal advice.

## Current repository fact

At the 2026-10-07 audit, the root of `Em3rc0d/personal_knowledge` contains **no repository-wide LICENSE file**.

Per GitHub's licensing guidance, absent a license the default copyright regime applies to the repository author's own material, while GitHub Terms still permit platform viewing/forking behavior.

Third-party corpora and copied upstream material keep their own license boundaries.

Knowledge Foundry must **not** add a root license automatically. Licensing the repo or future course products is a deliberate business/legal decision.

## Rights basis

Every externally influenced product artifact should be able to record:

```yaml
asset_or_source:
owner:
rights_basis: OWNED | LICENSED | PERMISSION | PUBLIC_DOMAIN | EXCEPTION_LIMITATION | REFERENCE_ONLY | UNKNOWN
license_identifier:
license_uri:
commercial_use: YES | NO | CONDITIONAL | UNKNOWN
adaptation: YES | NO | CONDITIONAL | UNKNOWN
attribution_required:
attribution_text:
third_party_exclusions:
evidence:
legal_review_required:
```

## Creative Commons boundary

Creative Commons licenses can apply to copyrightable educational works.

Important operational distinctions:

- `BY` requires attribution;
- `NC` limits licensed reuse to noncommercial purposes;
- `ND` restricts sharing adaptations;
- `SA` applies share-alike conditions to adaptations;
- applying a CC license is intended to be non-revocable for recipients who comply.

Creative Commons itself does not recommend CC licenses for software; use software licenses for software.

## SPDX boundary

SPDX license expressions are useful for machine-readable software/dependency licensing and can represent compound license terms with identifiers and operators.

Do not force every educational-content rights situation into SPDX. Course media, permissions, reference-only sources and jurisdictional exceptions may need explicit rights metadata beyond a software license expression.

## Source vs product license

The product's license never erases dependency obligations.

```text
product license
≠
license of every embedded dependency
```

A product manifest must identify third-party material excluded from the product-level license.

## Commercial gate

Commercial release is blocked when a material dependency has:

- `rights_basis=UNKNOWN`;
- unknown commercial-use permission for reproduced/adapted material;
- unresolved attribution requirements;
- unresolved share-alike/derivative restrictions that affect the planned distribution.

Using a source as evidence/reference is not the same as copying its protected expression; when the boundary is uncertain, mark it for review rather than guessing.
