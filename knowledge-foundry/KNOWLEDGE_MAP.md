# Knowledge Foundry — Knowledge Map

## Human routing

```text
README.md
├── STATUS.md
├── ROADMAP.md
├── REPOSITORY_CONTRACT.md
├── LLM_CONTEXT.md
├── architecture/
│   └── KNOWLEDGE_COMPILER.md
├── mining-site/
│   ├── SOURCES.md
│   └── S-001-agent-skills.md
├── quarries/
│   └── agent-skills-education-mechanisms.md
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
| How does compilation work? | `architecture/KNOWLEDGE_COMPILER.md` |
| What source was studied? | `mining-site/` |
| What did we extract from it? | `quarries/` |
| What must pass to close MK0? | `mk/MK0/GATES.md` |
| What remains uncertain? | `mk/MK0/UNKNOWNS.md` |
| Where will educational outputs live? | `products/` |

## Evidence traversal

For a released lesson claim:

```text
product lesson
  ↓ pointer
compiled educational spec
  ↓ pointer
domain canon
  ↓
domain evidence / quarry
  ↓
source receipt
```

The educational layer must remain auditable back to the underlying knowledge without copying the entire evidence chain into each product.
