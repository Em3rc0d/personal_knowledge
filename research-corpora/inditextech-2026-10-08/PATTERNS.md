# InditexTech — reusable pattern candidates (MK0)

**Status:** research quarry / **NOT CANON**, not approved for implementation. **Observation:** 2026-10-08. Evidence inventory: [SOURCES.md](SOURCES.md). This synthesis is `INSPIRED` unless a narrower source statement is explicitly marked `OFFICIAL` (project README or docs) or `OBSERVED` (inspected repository manifest). All adoption criteria below are our **GENERATED** engineering rules, *not* Inditex rules.

## P-01 — Separate proposal, policy decision and side-effectful execution

- **Evidence:** [Kumoss README](https://github.com/InditexTech/kumoss/blob/5bd6fceda4e7034a3546acf526a7500b6863ef5e/README.md) (`OFFICIAL`, source-reported): proposed IaC change, Terraform/OpenTofu plan, impact/cost report, compliance gate, human review for high-impact changes and apply on request. [Core dependencies](https://github.com/InditexTech/kumoss/blob/5bd6fceda4e7034a3546acf526a7500b6863ef5e/core/pyproject.toml) (`OBSERVED`): FastAPI, LiteLLM, OTEL.
- **Extracted rule (`INSPIRED`):** a model may propose a change; permission to make that change belongs to independently enforced runtime/policy code. Bind approval to exact action + context; revalidate on mutation; collect outcome receipt.
- **Relevant to:** `agent-engineering`, Ninfa/prodAgentic **as a review prompt**, not a deployment commitment.
- **Test before promotion:** inject an unapproved high-impact action; verify no tool executes. Change parameters after approval; verify old approval does not authorize the new action. Ensure failure and rollback receipts.
- **Do not adopt:** no Kubeflow, Terraform or always-on agent infrastructure unless the actual product uses IaC/cloud changes and a defined operator can own it. A syntactically valid plan does **not** prove safety.
- **Confidence:** HIGH that project documents this intended separation; UNKNOWN runtime enforcement reliability.

## P-02 — Compose security checks but never label them security proof

- **Evidence:** [CerbIA README](https://github.com/InditexTech/cerbia/blob/485aee70c0928d4176996c776d1e5fa91fcde590/README.md) (`OFFICIAL`): loaders, preprocessors, scanners, aggregate verdict; optional local ML, Presidio PII, ProtectAI integrations. README explicitly says scanner results are heuristic/model-based, not certification.
- **Extracted rule (`INSPIRED`):** classify untrusted inputs and outbound content; treat detector results as advisory signals within least privilege, tool authorization, output filtering and audit. Define which enforcement boundary fails closed.
- **Relevant to:** `agent-engineering` (external documents, retrieved text, generated outputs), possible future Ninfa/Prompt Machine gates.
- **Test before promotion:** multilingual adversarial samples, secret leakage examples, false positives, false negatives, bypass cases, latency/cost budget and cross-provider failure paths. No claim of universal prompt-injection detection.
- **Do not adopt:** install CerbIA or ML dependencies merely because agents exist; start with bounded policy, allowlist and deterministic checks when sufficient.
- **Confidence:** HIGH for documented capability surface; UNKNOWN empirical detection quality in our traffic.

## P-03 — Documentation publishing is distinct from knowledge authority

- **Evidence:** [Docouture README](https://github.com/InditexTech/docouture/blob/47143cffc46cff654d0f42ac45a8221d90351628/README.md) (`OFFICIAL`): Antora site + CLI, Nx/pnpm monorepo, reusable docs UX. [FOSS manifesto](https://github.com/InditexTech/foss/blob/bceb58a854845275b856004a717d1cc7bf5e171e/MANIFESTO.md) (`OFFICIAL`): adopt with judgement, publish useful work, preserve secure practices.
- **Extracted rule (`INSPIRED`):** discovery/source/quarry, canonical claims and docs delivery remain separate. Publishing or attractive navigation does not promote a research claim.
- **Relevant to:** `personal_knowledge`, knowledge-foundry and future public learning material.
- **Test before promotion:** a question routes to one authoritative page; every exported claim links to supporting evidence/version; duplicate pages do not diverge. Measure retrieval friction before considering a docs platform.
- **Do not adopt:** Antora/Nx/pnpm solely to host current Markdown. No mirrored canon, new root domain or auto-doc-generation pipeline from this research.
- **Confidence:** HIGH for documented tool architecture; UNKNOWN benefit to this repository until real usage evidence.

## P-04 — Decouple collaborative shared state from visual rendering

- **Evidence:** [Weave.js README](https://github.com/InditexTech/weavejs/blob/2bd36726d06f7b15131c0a921a8d3cc50e7e069b/README.md) (`OFFICIAL`): headless collaboration framework built on Yjs/SyncedStore, Konva and custom React reconciler. [package.json](https://github.com/InditexTech/weavejs/blob/2bd36726d06f7b15131c0a921a8d3cc50e7e069b/code/package.json) (`OBSERVED`): workspace architecture. [Frontend manifest](https://github.com/InditexTech/weavejs-frontend/blob/0a60b10e5f360373872bf9f90c0bf4aa997db990/code/package.json) (`OBSERVED`) shows Vite/TanStack dependencies although README references Next.js; treat README stack descriptions as drift-prone.
- **Extracted rule (`INSPIRED`):** when concurrent editing is a demonstrated requirement, separate document identity, synchronization, rendered scene and UI commands; test merge, undo, persistence and awareness semantics explicitly.
- **Relevant to:** `diagram-design` only if shared live editing is required and validated. Generic diagrams do not need a CRDT framework.
- **Test before promotion:** two editors with concurrent divergent operations, offline/reconnect, undo boundaries, object identity, save/reload, version skew and bandwidth/memory profiling.
- **Do not adopt:** Weave/React/Konva in a static diagramming feature, Flutter app or existing UI solely for architectural curiosity.
- **Confidence:** HIGH that source advertises architecture; UNKNOWN performance and conflict semantics under target workloads.

## P-05 — Verify release tooling with isolated consumers and live gates

- **Evidence:** [Shared actions README](https://github.com/InditexTech/gh-actions/blob/3dac9bbff47d1e983604671191a08e4d345d9064/README.md) and [PyPI testing boundary](https://github.com/InditexTech/gh-actions/blob/3dac9bbff47d1e983604671191a08e4d345d9064/pypi/TESTING.md) (`OFFICIAL`): prebuilt distribution validation, immutable action references, provider-specific canary external to action repository. [npm canary](https://github.com/InditexTech/npmjs-ci-testing/blob/b31d345936c9b02ed083ca2c6259350f8ad57c42/README.md) and [Maven canary](https://github.com/InditexTech/mavencentral-ci-testing/blob/d5a9b949779aeb15485becb76c1666b6ecb93a3d/README.md).
- **Extracted rule (`INSPIRED`):** test delivery contracts separately from application business logic. Distinguish static validation from actual provider publication; record exact revisions, permissions and receipts.
- **Relevant to:** repositories publishing packages or deliverables. For `Logan Garage`, local Flutter/SDK build remains the desired path; no GitHub Actions APK jobs are authorized.
- **Test before promotion:** local validator rejecting malformed inputs; intentional negative test; provider smoke test only if publication is explicitly authorized and cost justified. No fake claim of published artifact from local check.
- **Do not adopt:** organization-wide CI fleet, package registries, canary repos or protected runner resources for projects not publishing libraries.
- **Confidence:** HIGH for documented test architecture; UNKNOWN for actual successful live publication in this audit.

## P-06 — Link a change to its cause, but minimize ceremony

- **Evidence:** [gh-sherpa README](https://github.com/InditexTech/gh-sherpa/blob/c65accd34d1eaa774d73a8f992188680a86c5ecf/README.md) (`OFFICIAL`): gh CLI extension for branch/PR naming from GitHub/Jira issues, with non-interactive flags for coding agents.
- **Extracted rule (`INSPIRED`):** material changes should have a traceable issue/decision/evidence link; CLI is an adapter, not the authority or necessity.
- **Relevant to:** Jett repo workflow when branch volume or traceability friction is observed.
- **Test before promotion:** check issue→branch→PR mapping and collision/duplicate issue handling with existing repo conventions; prove time saved with actual use.
- **Do not adopt:** a new CLI dependency or issue per typo; maintain existing knowledge/<domain>-<mk>-<purpose> flow.
- **Confidence:** HIGH for documented behavior; UNKNOWN productivity impact.

## P-07 — Commit application state and outgoing message atomically when required

- **Evidence:** [SCS-Outbox README](https://github.com/InditexTech/scs-outbox/blob/2199be21710b5eca2b56732ebce16e95176589cd/README.md) (`OFFICIAL`): JDBC/Mongo transaction-backed capture with `StreamBridge`, scheduled publish, at-least-once delivery; no reactive backend support.
- **Extracted rule (`INSPIRED`):** if a business write and an event must survive one another, study transactional outbox plus consumer idempotency instead of naïve dual writes.
- **Relevant to:** Spring services that truly publish domain events; not every REST app.
- **Test before promotion:** crash between DB commit/publish, retry duplicates, ordering scope, poison message, idempotent consumer, recovery and DB compatibility/version check.
- **Do not adopt:** Kafka/Cloud Stream/Outbox for offline-first SQLite apps or low-throughput systems with no such atomicity problem.
- **Confidence:** HIGH for README delivery guarantee as project claim; UNKNOWN empirical behavior without tests.

## P-08 — Reconciliation is a domain-specific control loop, not generic automation

- **Evidence:** [Redkey operator architecture](https://github.com/InditexTech/redkey-operator/blob/0461c179667f8dc74c351cec02051fc2fa5e4ea5/docs/architecture.md) (`OFFICIAL`): separate operator/coordinator and Robin reconciler via Kubernetes custom resources; [overcommit operator](https://github.com/InditexTech/k8s-overcommit-operator/blob/0be5fbf674dafcbfbbb5213ce9d1eeb84baf9c1f/README.md) demonstrates admission-based resource policy.
- **Extracted rule (`INSPIRED`):** for resources that must converge continuously, declare desired/observed state, reconcile idempotently, expose status and tolerate repeated execution.
- **Relevant to:** future platform engineering only, not personal/mobile MVPs.
- **Test before promotion:** divergent state, repeated retries, partial failures, stale CRs, runaway reconciliation, rollback and least-privilege RBAC.
- **Do not adopt:** Kubernetes/Redis operators or resource overcommit where there is no validated Kubernetes workload.
- **Confidence:** HIGH for documented design; UNKNOWN for operations at scale.

## P-09 — API diffs should be inspectable, not assumed safe

- **Evidence:** [Swagger UI diff highlight README](https://github.com/InditexTech/swagger-ui-plugin-diff-highlight/blob/e3e50dee086d31697a2b57a31e845fbc4204b988/README.md) (`OFFICIAL`): renders `x-diff-*` markers in Swagger UI; it expects annotated specifications.
- **Extracted rule (`INSPIRED`):** changes to public APIs should produce versioned evidence of operations/schemas changed. Visual diff and breaking-change detection are distinct mechanisms.
- **Relevant to:** REST contract governance in web services.
- **Test before promotion:** removed required field or incompatible type must be flagged by a semantic checker; ensure visualization faithfully reflects inputs without claiming independent compatibility proof.
- **Do not adopt:** plugin/UI runtime unless we already publish OpenAPI docs and consumers need inline comparison.
- **Confidence:** HIGH for plugin contract; UNKNOWN accuracy for untested annotation producers.

## Admission matrix (not a roadmap)

| Candidate | Current stance | Promotion owner / missing proof |
|---|---|---|
| P-01 Policy-bound execution | STUDY | `agent-engineering` MK1→MK2 gates; negative execution tests |
| P-02 Security gates | STUDY | `agent-engineering` threat model + calibrated tests |
| P-03 Documentation delivery | HOLD | `knowledge-usage` evidence of retrieval/publishing pain |
| P-04 CRDT rendering | HOLD | `diagram-design` validated multi-user requirement |
| P-05 Publication canaries | HOLD | a concrete package-publication pipeline + authorization |
| P-06 GitHub traceability | HOLD | real repeated branch/PR friction |
| P-07 Transactional outbox | HOLD | atomic event-publication requirement |
| P-08 Reconciliation operators | HOLD | Kubernetes control-plane requirement |
| P-09 API diff | HOLD | API compatibility/release governance requirement |

**Non-goal:** a dependency checklist. `STUDY` means the idea is captured, not that we build it. The standing instruction is **knowledge now, dependencies only after a real problem and gate**. No claim here demonstrates time, money, token or incident reduction.
