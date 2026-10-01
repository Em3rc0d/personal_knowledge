# EM3RC0D System Map

Status: **MK0 SYNTHESIS / NOT PRODUCT-ARCHITECTURE CERTIFICATION**

Pinned source estate: `../../research-corpora/em3rc0d-repositories-2026-10-01/`.

## Capability graph

```text
                         personal_knowledge
                                │
                      evidence + promoted knowledge
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
      build-room              FRAME                ink-vk
   experience method      project framing       source adaptation
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                         EM3RC0D Foundry
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
              TALOS         automation           RAG
       process semantics   process execution   knowledge context
                │               │                │
                └───────┬───────┴───────┬────────┘
                        │               │
                        ▼               ▼
                      m-pago       infra-monitor
                      payment      health/alerts
                        │               │
                        └───────┬───────┘
                                ▼
                           client outcome
                                │
                   ┌────────────┴────────────┐
                   ▼                         ▼
              content-seller                NINFA
             social distribution       long-form/media
                   │                         │
                   └────────────┬────────────┘
                                ▼
                        market learning
```

## Supporting primitives

- `transcript-voice`: speech → text intake primitive.
- `barbershop-ia-whatsapp`: vertical reference implementation for conversational appointment automation.

## External donor corpora

- `open-seo`: MIT fork; SEO/MCP/agent-skill donor.
- `temporal-ai-agent`: MIT fork; durable agent-loop/Temporal/MCP donor.
- `skills`: Anthropic fork with mixed source terms; pointer-only until file-level licensing is classified.

## High-value product path to investigate

```text
real business process
  → TALOS understanding/review
  → Automation/Savings Workflow mapping
  → provider bindings
  → controlled execution
  → m-pago where payment is in scope
  → infra-monitor / incident evidence
  → savings + process evidence
  → content/case-study learning
```

This path is an **INFERRED/GENERATED integration hypothesis**. The repositories remain independently authoritative for their own current implementation state until integration is actually built and tested.

## Important non-equivalences

- source repository exists != integration exists
- compatible concepts != compatible contracts
- same owner != shared release lifecycle
- field trial != product-market fit
- reference implementation != reusable production primitive
- forked donor != EM3RC0D-owned product IP
