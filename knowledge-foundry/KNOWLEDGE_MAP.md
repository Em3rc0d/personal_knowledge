# Knowledge Foundry — Knowledge Map

## Human routing

```text
README.md
├── STATUS.md
├── ROADMAP.md
├── REPOSITORY_CONTRACT.md
├── LLM_CONTEXT.md
├── architecture/
│   ├── KNOWLEDGE_COMPILER.md
│   ├── DOMAIN_INPUT_CONTRACT.md
│   ├── ASSESSMENT_EVIDENCE_MODEL.md
│   ├── ACCESSIBILITY_AND_INCLUSION.md
│   ├── RIGHTS_AND_LICENSING.md
│   ├── KNOWLEDGE_DEPENDENCY_MANIFEST.md
│   └── PILOT_DATA_BOUNDARY.md
├── mining-site/
│   ├── SOURCES.md
│   ├── S-001-agent-skills.md
│   ├── S-002-learning-science.md
│   ├── S-003-assessment-quality.md
│   ├── S-004-accessibility-inclusive-design.md
│   ├── S-005-rights-provenance.md
│   └── S-006-pilot-data-peru.md
├── quarries/
│   ├── agent-skills-education-mechanisms.md
│   ├── learning-science-primitives.md
│   ├── assessment-validity-and-fairness.md
│   ├── accessibility-inclusive-learning.md
│   ├── rights-provenance-commercialization.md
│   └── personal-knowledge-readiness-audit-2026-10-07.md
├── mk/
│   └── MK0/
│       ├── README.md
│       ├── GATES.md
│       ├── UNKNOWNS.md
│       └── DISTILLATION_LEDGER.md
└── products/
    └── README.md
```

## Question routing

| Question | Start here |
|---|---|
| What is Knowledge Foundry? | `README.md` |
| Where are we now? | `STATUS.md` |
| What happens next? | `ROADMAP.md` |
| What is authoritative? | `REPOSITORY_CONTRACT.md` |
| Can this source-domain slice be compiled? | `architecture/DOMAIN_INPUT_CONTRACT.md` |
| How does compilation work? | `architecture/KNOWLEDGE_COMPILER.md` |
| How strong is an assessment claim? | `architecture/ASSESSMENT_EVIDENCE_MODEL.md` |
| What accessibility/inclusion target applies? | `architecture/ACCESSIBILITY_AND_INCLUSION.md` |
| Can material be reused commercially? | `architecture/RIGHTS_AND_LICENSING.md` |
| What makes a product stale? | `architecture/KNOWLEDGE_DEPENDENCY_MANIFEST.md` |
| Can pilot data be stored here? | `architecture/PILOT_DATA_BOUNDARY.md` |
| What source was studied? | `mining-site/` |
| What did we extract from it? | `quarries/` |
| Is personal_knowledge ready as an input? | `quarries/personal-knowledge-readiness-audit-2026-10-07.md` |
| What must pass to close MK0? | `mk/MK0/GATES.md` |
| What remains uncertain? | `mk/MK0/UNKNOWNS.md` |
| Where will educational outputs live? | `products/` |

## Evidence traversal

For a released lesson claim:

```text
product lesson
  ↓
product dependency manifest
  ↓
compiled educational spec
  ↓
eligible source-domain artifact + pinned revision
  ↓
domain evidence / quarry
  ↓
source receipt
```

The educational layer remains auditable without copying the entire evidence chain into each product.
