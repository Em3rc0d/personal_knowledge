# ACTA DE CONFORMIDAD — CA-001
## WhatsApp Links Knowledge Corpus 2025–2026

**Issued:** 2026-09-06  
**Corpus:** 89 unique URLs + 1 attached image  
**Decision:** **APPROVED FOR KNOWLEDGE-REPOSITORY INTEGRATION**

## Certification scope

This act certifies the **promoted knowledge subset**, not the truth of every source in the ZIP.

It certifies that:

- all 89 unique URLs have an explicit disposition;
- inaccessible content remains explicitly inaccessible;
- gaps are not reconstructed as if directly observed;
- social posts/popularity are not treated as authority;
- claims promoted to reusable knowledge have scope, provenance, confidence and evidence class;
- scientific empirical claims use peer-reviewed evidence where available;
- normative claims are identified as standards/specifications rather than mislabeled as scientific evidence;
- implementation behavior is identified as official/implementation evidence rather than universal science;
- contradiction passes were performed and material overgeneralizations were repaired;
- active hypotheses remain outside canon;
- sensitive-provenance material is not promoted for literal reuse without rights review;
- time-sensitive facts remain version/date scoped.

## Corpus accounting

### Sources
- Unique URLs: **89/89 accounted**
- Attached image: **1/1 accounted**
- Fabricated direct-access claims: **0**

### Access state
- Direct verified: 27
- Indexed original content: 10
- Indexed repost: 4
- Primary alternative source: 4
- Partial: 10
- Inaccessible: 32
- Unresolved redirect: 1
- Canonical duplicate: 1

Total: **89**

### Knowledge outcomes
- Promoted reusable claims/patterns: **27**
- GAP dispositions: **37**
- Discovery-only dispositions: **21**
- Active unpromoted hypotheses: **4**
- Superseded proprietary-AI-BOM hypothesis: **1**
- Explicitly rejected/degraded misleading claims: retained in evidence, not canon.

## Required invariants

1. **UNKNOWN remains UNKNOWN.**
2. **No claim without evidence; no evidence without provenance.**
3. `confidence != evidence_class`.
4. `official != scientific`.
5. `popular != authoritative`.
6. `public != licensed for general reuse`.
7. `standard-compliant != content-accurate`.
8. `local != private != secure != offline`.
9. `compatible API != equivalent behavior`.
10. `reproducible benchmark != valid deployment evidence`.
11. `retrieval relevance != universal context utility`.
12. `historical snapshot != current state`.

## Scientific contradiction audit result

The final promoted catalog incorporates counterevidence from peer-reviewed work on:

- benchmark instability / underspecification;
- simple vs complex agent architectures;
- contradictory context/RAG/long-context behavior;
- SBOM incompleteness and dependency-graph accuracy;
- mixed individual/aggregate evidence synthesis;
- WebAssembly performance and isolation limitations.

No unresolved material contradiction remains **inside the promoted set** after v5 cross-consistency repair.

This does not claim the scientific literature is closed or immutable. Every time-scoped or research-sensitive rule remains subject to revalidation.

## Promotion decision

```text
B0–B10  research / source analysis                  PASS
B11     discernment                                 PASS
B11-A   contradiction audit                         PASS
B11-B   scientific adversarial audit                PASS
B11-C   cross-consistency / evidence-class repair   PASS
CA-001  conformity                                  PASS

B12     repository integration                      AUTHORIZED
```

## Repository architecture decision

The corpus should **not** be organized as one project per external URL.

Use a hybrid model:

- a canonical provenance corpus under `research-corpora/whatsapp-links-2025-2026/`;
- source/project names remain provenance identifiers inside the corpus;
- reusable knowledge is organized semantically by claim/domain rather than by publisher;
- later domain projects may import/promote a claim by reference, preserving the original corpus source ID.

This prevents external project naming from becoming the ontology of the user's knowledge base.

## Final declaration

**CA-001: CONFORMITY GRANTED.**

The promoted subset is sufficiently traceable, scoped, contradiction-tested and evidence-classified to enter the knowledge repository.

Gaps and inaccessible sources remain preserved as gaps, not converted to knowledge.
