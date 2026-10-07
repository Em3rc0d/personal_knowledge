# S-005 — Rights, Licensing and Provenance

Observed: 2026-10-07  
Status: **INSPECTED**

## GitHub licensing guidance

Identity:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

Observed rule: without a license, default copyright rules apply to the author's own material; a public GitHub repository is not automatically open source.

Repository observation: `personal_knowledge` currently has no root LICENSE file.

## Creative Commons

Sources:
- https://creativecommons.org/chooser/
- https://creativecommons.org/faq/
- https://creativecommons.org/share-your-work/cclicenses/

Observed boundaries:

- CC offers multiple licenses with BY/NC/ND/SA conditions;
- licensors should have authority to license the work;
- the chooser explicitly warns CC licensing is not revocable;
- CC does not recommend its licenses for software/hardware.

## SPDX

Source:
https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/

SPDX 3.0.1 defines machine-readable license expressions, including compound terms using identifiers and operators such as AND/OR/WITH.

Boundary: strongest fit is software/dependency licensing; it does not replace a richer rights model for educational media/content.

## W3C PROV-O

Source:
https://www.w3.org/TR/prov-o/

PROV-O provides a stable vocabulary for provenance entities, activities, agents and derivation relationships.

Boundary: Knowledge Foundry may reuse the conceptual model without adopting RDF/OWL in MK0.
