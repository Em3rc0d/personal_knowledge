# DOGFOOD-001 — F1 Receipt: Vercel Web Deployment Reconciliation

Date: 2026-10-07  
Target: `Em3rc0d/Future-Wardrobe`  
Stage: `TEST / PROVE`  
Slice: `VERCEL_WEB_DEPLOYMENT_RECONCILIATION`  
Verdict: **PASS — BOUNDED**

## Exact input

```text
base branch: astra/release-rc1
base SHA: a80f1aacc4936ce6329f0e71b499d371086be6fa
F1 branch: foundry/dogfood001-f1-vercel-web
final F1 SHA: f443743eb41226fb799624a146eddf7ceb9aa1f6
```

No merge or production promotion occurred.

## Final diff against RC1

Exactly three files changed:

- `vercel.json` — web-only Vercel boundary;
- `package.json` — root `next@16.3.4` declaration for Vercel framework detection;
- `pnpm-lock.yaml` — matching root importer entry so frozen-lockfile remains authoritative.

No product, domain, UX, database, worker or mobile source changed.

## Executed iterations

### Attempt F1-A

SHA: `ecc6323302e89e14ca12e56fc0f4e255df42e471`

Change:

- add `vercel.json`;
- build only `pnpm --filter @wardrobe/web build`;
- keep `pnpm install --frozen-lockfile`.

Result: **ERROR**

Evidence:

- Expo/mobile failure from the original RC1 was eliminated;
- Vercel failed framework detection because the root package did not declare `next`;
- error: `No Next.js version detected`.

Interpretation:

The web-only build boundary was directionally correct but incomplete.

### Attempt F1-B

SHA: `6116b8480b550f95326b6b3c8948ee0a3f6351b3`

Change:

- add root `next@16.3.4`.

Result: **ERROR — EXPECTED FAIL-CLOSED**

Evidence:

```text
ERR_PNPM_OUTDATED_LOCKFILE
Cannot install with frozen-lockfile because pnpm-lock.yaml is not up to date
1 dependency added: next@16.3.4
```

Interpretation:

This is positive evidence for the deployment contract: the frozen lockfile correctly rejected an inconsistent package graph instead of silently rewriting it.

The historical preview branch used `--no-frozen-lockfile`; F1 intentionally did not copy that bypass.

### Attempt F1-C

SHA: `f443743eb41226fb799624a146eddf7ceb9aa1f6`

Change:

- update root lockfile importer for `next@16.3.4`.

Vercel deployment:

`dpl_HQ4CNiL9d9kg5guGesUg2Pta7DJY`

Result: **READY**

Executed evidence:

- `pnpm install --frozen-lockfile` succeeded;
- log: `Lockfile is up to date, resolution step is skipped`;
- Vercel detected `Next.js 16.3.4`;
- executed build command: `pnpm --filter @wardrobe/web build`;
- Next compilation succeeded;
- TypeScript build phase succeeded;
- static/dynamic route generation completed;
- Vercel produced deployment outputs;
- preview root returned HTTP 200;
- `/api/health` returned HTTP 200:
  `{"service":"future-wardrobe-web","version":"1.0.0-rc.1","configured":true}`.

Preview deployment URL:

`https://future-wardrobe-ap8hr7uke-faridmerinos-projects.vercel.app`

## Acceptance evaluation

| Acceptance | Result |
|---|---|
| Exact source SHA recorded | PASS |
| Preview reaches READY | PASS |
| Logs show web-only build | PASS |
| Expo/mobile not used as web deployment authority | PASS |
| No product/domain invariant change | PASS |
| Evidence boundaries explicit | PASS |

## What this proves

This receipt supports:

> The exact RC1 codebase can produce a READY Vercel web preview when the monorepo deployment boundary is explicit, the root Next framework identity is declared, and the package graph remains frozen-lockfile consistent.

It also supports:

> The historical preview branch contained a useful mechanism, but copying its `--no-frozen-lockfile` behavior was unnecessary and weaker than the final F1 solution.

## What this does not prove

This receipt does **not** prove:

- full RC1 engineering readiness;
- GitHub Actions health;
- Railway worker readiness;
- current Supabase staging readiness;
- hosted RLS/storage/TUS/pgmq continuation;
- live media-provider behavior;
- EAS/native mobile builds;
- physical-device behavior;
- production release safety;
- PR #8 merge readiness.

`ENGINEERING_READY=NO` and `RELEASE_READY=NO` remain unchanged.

## Foundry mechanism evidence

Observed useful mechanisms:

1. **earliest-invalid-node re-entry** avoided product/design/architecture replay;
2. **dependency-aware reuse** mined only the useful deployment mechanism from a divergent historical branch;
3. **fail-closed evidence** preserved frozen-lockfile discipline and turned an intermediate failure into meaningful evidence;
4. **bounded mutation** changed only three deployment/package metadata files;
5. **claim <= evidence** prevents a READY web preview from becoming a full-release claim.

## Reusable-capital candidates

Candidate, not yet promoted:

- monorepo web deployment boundary pattern:
  - explicit web build target;
  - root framework identity only when platform detection requires it;
  - lockfile importer updated with package metadata;
  - preview evidence pinned to exact source SHA.

Do not promote globally from one case.

## Next exact boundary

The Vercel web deployment slice is closed.

The next unresolved external execution boundary is:

> **Railway media-worker exact-RC1 reconciliation**

Current known B0 state:

- service exists;
- no current successful live deployment;
- configured source SHA is behind RC1;
- prior failures/removals exist.

No Railway mutation is authorized by this receipt.
