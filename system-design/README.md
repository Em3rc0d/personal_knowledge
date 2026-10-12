# System Design — bounded knowledge extraction

**Purpose:** reusable, falsifiable decisions about system architecture; not another framework, production dependency or copy of interview notes.

**Status:** `MK0: PASS WITH LIMITATIONS`; `MK1: CLOSED WITH LIMITATIONS — INTERNAL NORMALIZATION ONLY`. Operational/production certification: **NOT GRANTED**. See [STATUS](./STATUS.md).

## Fast navigation

- [Source receipt](./mining-site/S-001-system-design-notes.md) → upstream identity, version and limitations.
- [28-chapter screening](./mk/MK0/INVENTORY.md) → what's extracted/deferred.
- [MK0 gate](./mk/MK0/REVIEW-GATE.md) → claim boundary.
- [Quarry](./quarries/Q-001-reusable-architecture-patterns.md) → extraction map and cross-source evidence.
- [MK1 classification](./mk/MK1/README.md) → five assessed records (one reference only, three unvalidated candidates, one synthetic-lab-supported candidate).
- [PILOT-001](./mk/MK1/PILOT-001-payment-idempotency.md) → synthetic lab executed with limitations; [read-only Plate comparison](./mk/MK1/experiments/PILOT-001/PLATE-READONLY-CROSSWALK-2026-10-12.md) (no product changes).
- [MK1 adversarial review](./mk/MK1/ADVERSARIAL-REVIEW-2026-10-12.md) and [gate](./mk/MK1/REVIEW-GATE.md) → why internal classification can close without production/operational certification.

## Authority and duplication boundary

- Process/MK/source intake are owned by [Jett Engineering Method](../jett-engineering-method/README.md) and its [Source Intake Contract](../jett-engineering-method/SOURCE-INTAKE-CONTRACT.md); this domain **links** rather than duplicates that method.
- These notes are **secondary learning material**, not a vendor spec, security certification, real-system audit, or production implementation proof.
- `mining-site` is source identity; `quarries` are observations and synthesis; `mk/MK1/patterns` are **classified knowledge** (REFERENCE_ONLY / CANDIDATE / LAB_SUPPORTED_CANDIDATE), not product architecture or formally certified implementation guidance.
- Preserve `UNKNOWN` for product-specific providers, throughput, costs and reliability targets.
- Do not preload this whole domain. Read one pattern if a decision needs it.
