# InditexTech — engineering knowledge intake

**Observed:** 2026-10-08  
**Scope:** 40 public `InditexTech` GitHub repositories, repository identity fixed to commit SHA.  
**Lifecycle:** `MK0 / QUARRY_ONLY / NO AUTOMATIC PROMOTION`  
**Mode:** knowledge capture only; **zero vendored code, new runtime dependencies, CI workflows, model calls or product changes**.

## Purpose

Capture source-bounded architecture and engineering patterns without confusing an interesting reference with a current requirement. This corpus is **not** an InditexTech SDK, an endorsement, an adoption plan, a maturity ranking or a security assessment.

## Smallest-reading route

| Question | Open |
|---|---|
| Which of the 40 repositories exists, what does it claim and what exact revision was observed? | [SOURCES.md](SOURCES.md) |
| Which engineering patterns could be useful, under which conditions and with what negative tests? | [PATTERNS.md](PATTERNS.md) |
| What is allowed to become current EM3RC0D engineering canon? | [Jett source intake](../../jett-engineering-method/SOURCE-INTAKE-CONTRACT.md) + owning domain MK gate |

Do **not** load both documents for a narrow question. The source inventory is a provenance layer, not the response default. Read relevant pattern first and drill down to its exact pinned primary source only if necessary.

## Scope and results

- `26` InditexTech-authored/auxiliary repositories; `14` third-party-upstream-lineage repositories (working classification, not a verified diff audit).
- `40/40` repository commit identities resolved on their observed default branch.
- `39/40` root README accessible and inspected at bounded depth; `spring-cloud-stream` README returned `NOT_FOUND`, so only repo/ref and known project provenance were recorded.
- `9` **candidate** engineering patterns with source, extracted rule, applicability, negative-case verification and explicit non-adoption conditions.
- Selected manifests/documents checked for Kumoss, CerbIA, Weave.js, Redkey and FOSS. **No runtime tests, fork-diff analysis or production validation** were performed.

## Knowledge boundary

```text
EXTERNAL REPOSITORY / PINNED REF
           ↓
  SOURCE MAP (SOURCES.md)
           ↓
  OBSERVATION + LIMITS
           ↓
  PATTERN CANDIDATE (PATTERNS.md)
           ↓
  DOMAIN RESEARCH + NEGATIVE TESTS
           ↓
  MK REVIEW / PROMOTION GATE
           ↓
  CANON (only if justified)
```

The current status **stops at pattern candidates**. In particular, this corpus does not modify `agent-engineering` MK1 schema, certify security scanners, deploy Terraform/Kubernetes, add Antora/CRDT packages, run GitHub Actions or alter `Logan Garage`, `ECHO`, `Ninfa`, `Prompt Machine` or any product repository.

## Revisit only on demand

When an actual problem matches a pattern: (1) read exact source and current target-state requirements; (2) check source version drift and ownership/license; (3) compare cheapest adequate options including doing nothing; (4) run risk-proportional test; (5) document KEEP / ADAPT / REJECT with evidence in the owning domain. `UNKNOWN` stays `UNKNOWN`. No recurring monitoring is authorized.
