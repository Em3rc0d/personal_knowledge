# Agent Engineering — Status

Updated: 2026-09-07

## Current gate

```text
DOMAIN                    agent-engineering
CURRENT MK                MK0
STATE                     IN PROGRESS
PRIMARY MINING SITE       NirDiamant/GenAI_Agents
UPSTREAM SNAPSHOT         4c95ae14cc2462c442b5c064cccd74430d02bc46
LICENSE BOUNDARY          RECORDED / NON-COMMERCIAL CUSTOM LICENSE
REPOSITORY INVENTORY      INITIAL PASS COMPLETE
AGENT TAXONOMY            INITIAL PASS COMPLETE
LOOP/HARNESS MODEL        INITIAL PASS COMPLETE
TOOLS / ACI               INITIAL PASS COMPLETE
HITL / SIDE EFFECTS       INITIAL PASS COMPLETE
TRACE EVALUATION          INITIAL PASS COMPLETE
MEMORY / PERSISTENCE      INITIAL PASS COMPLETE
MULTI-AGENT               INITIAL PASS COMPLETE
SECURITY                   INITIAL PASS COMPLETE
SCIENTIFIC CONTRAST       INITIAL PASS COMPLETE
REUSABLE RULES            CANDIDATE ONLY
CANON PROMOTION           BLOCKED
```

## MK progression

| MK | Objective | State |
|---|---|---|
| MK0 | Mine source, establish vocabulary, provenance, claims, evidence, contradictions and candidate rules | IN PROGRESS |
| MK1 | Normalize taxonomy and classify architectures, state, tools, control and failure modes | BLOCKED BY MK0 |
| MK2 | Convert findings into operational contracts, checklists, schemas and tests | BLOCKED |
| MK3 | Integrate agent engineering with Jett Engineering Method, security and project workflows | BLOCKED |
| MK4 | Automate static checks, eval harness templates and evidence gates | BLOCKED |
| MK5+ | Certify rules against multiple independent agent systems and production-like fixtures | BLOCKED |

## What was established in this pass

- upstream repository and exact snapshot pinned;
- root structure, tutorial inventory, dependency baseline, contribution validator and tests inspected;
- recent HITL and trace-evaluation slices inspected at implementation/test level;
- minimal while-loop agent inspected as a runtime/harness case study;
- repository claims separated from source-level observations;
- open issues sampled for reproducibility, taxonomy and error-model failure signals;
- license restriction captured before knowledge extraction;
- official Anthropic, LangGraph and MCP material used as independent technical contrast;
- scientific literature used to qualify ReAct, reflection/self-correction, agent benchmarking and multi-agent claims;
- initial portable rules written without copying upstream implementation code.

## Current high-confidence findings

### Promote toward MK1

- workflow and agent are different control structures; model-directed control should be explicit;
- critical invariants must be enforced by code/policy/tool boundaries rather than prompt-only instructions;
- agent loops need hard budgets and explicit termination behavior;
- HITL must pause before consequential side effects and resume from persisted state;
- changed action arguments must be validated again;
- agent state, context, memory and persistence are distinct concepts;
- tool design is a first-class interface/contract problem;
- outcome verification is stronger evidence than agent narration;
- trace/trajectory evaluation is useful but cannot replace outcome evaluation or repeated trials;
- intrinsic reflection is not evidence of improvement without external feedback/verifiers;
- multi-agent introduces additional coordination, alignment, verification and termination failure modes;
- production security requires least privilege and containment around tool/environment access;
- framework-specific examples must be normalized into framework-independent patterns.

### Keep as quarry evidence, not canon

- exact SDK APIs and version-specific LangGraph syntax;
- vendor/model names used by notebooks;
- tutorial-specific scoring weights;
- arbitrary thresholds such as a fixed understanding percentage;
- claims like `self-improving` based only on reflection loops;
- broad claims that every agent is literally the same loop implementation;
- claims that a notebook is `ready-to-use` without execution evidence under a pinned environment.

## Material concerns found

1. **Dependency drift.** Root `requirements.txt` still pins LangGraph/LangChain-era versions from 2024 while newer tutorials target later APIs and at least one test explicitly requires a notebook-pinned LangGraph version.
2. **Partial test coverage.** Only a small subset of recent tutorial slices has dedicated automated tests.
3. **No visible repository-wide GitHub Actions workflow.** Tests exist, but the inspected `.github/` contains funding and Dependabot configuration, not a CI workflow proving the catalog continuously.
4. **Notebook validator != runtime validation.** It checks structure/documentation/output hygiene/local image references; it does not prove notebooks execute or integrations still work.
5. **Taxonomy ambiguity.** Community issues correctly motivate distinguishing scripted LLM workflows from model-directed agents; nomenclature alone is not evidence of autonomy.
6. **Reproducibility signals.** Open issues report dependency/runtime breakage and at least one data-retrieval behavior mismatch. These are signals to investigate, not universal claims about the repo.
7. **Safety boundary.** A pedagogical minimal agent includes model-accessible shell execution; this is useful for explaining the loop but must not be generalized into a safe production default.
8. **License.** Upstream custom license is materially more restrictive than common permissive OSS licenses; extraction must remain independently synthesized.

## MK0 closure gate

- [x] domain contract exists;
- [x] primary upstream snapshot pinned;
- [x] license/provenance boundary recorded;
- [x] repository root and tutorial taxonomy mapped;
- [x] current dependency baseline inspected;
- [x] contribution validation model inspected;
- [x] representative recent tests inspected;
- [x] minimal loop/harness pattern inspected;
- [x] HITL approval pattern inspected;
- [x] trace evaluation pattern inspected;
- [x] memory/persistence usage sampled;
- [x] open issue failure signals sampled;
- [x] initial official-source contradiction pass completed;
- [x] initial scientific contradiction pass completed;
- [x] candidate portable rules identified;
- [ ] build a normalized inventory of all tutorials by `control model / state / tools / side effects / persistence / eval / risk` rather than README category;
- [ ] inspect every high-risk tutorial that can mutate external state or execute generated code;
- [ ] map termination and retry semantics across representative architecture families;
- [ ] map tool schema/error contracts across representative architecture families;
- [ ] verify MCP tutorial against the current protocol revision at message/capability level;
- [ ] compare memory examples against the dedicated upstream Agent_Memory_Techniques source and current persistence guidance;
- [ ] compare production claims with the separate `agents-towards-production` upstream rather than inferring production maturity from this catalog;
- [ ] derive an explicit threat model for agent tools, prompt injection, untrusted data and side effects;
- [ ] construct MK1 taxonomy with mutually exclusive/orthogonal dimensions;
- [ ] final MK0 review finds no unlabelled source-claim vs observation vs inference mixing.

Until those items close, **MK0 stays IN PROGRESS and no rule is certified into `main`.**
