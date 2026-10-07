# DOGFOOD-001 — Current Work Contract

Status: **B0 COMPLETE / F1 MUTATION BOUNDARY IDENTIFIED**  
Target repository: `Em3rc0d/Future-Wardrobe`

## Outcome

Resume Future Wardrobe RC1 at the earliest invalid evidence node and close release evidence without reopening already-valid product/design/architecture decisions.

## Exact input state

```text
repo: Em3rc0d/Future-Wardrobe
base branch: astra/release-rc1
base SHA: a80f1aacc4936ce6329f0e71b499d371086be6fa
PR: #8 OPEN / DRAFT
ENGINEERING_READY: NO
RELEASE_READY: NO
```

## Observed

- product scope/invariants remain stable;
- current RC1 GitHub Actions fail before any step executes;
- exact RC1 Vercel deployment executes but fails because root build includes Expo web without `react-native-web`;
- Vercel preview branch is READY when configured to build only `@wardrobe/web`;
- Supabase staging project is currently INACTIVE;
- Railway media worker has no current successful/live deployment and is pinned behind RC1.

## Earliest invalid node

`TEST / PROVE — deployment/environment reproduction`

## F1 first slice

**Release deployment reconciliation — Vercel web boundary only.**

Candidate change surface:

- add/adapt a root `vercel.json` on an F1 branch from exact RC1;
- configure Vercel to build only `@wardrobe/web`;
- keep lockfile verification fail-closed;
- do not merge unrelated preview-branch changes;
- do not modify product semantics;
- do not touch production aliases.

## Acceptance

F1 slice passes only if:

1. exact source SHA is recorded;
2. Vercel preview reaches `READY`;
3. build logs show web-only build scope;
4. no Expo/mobile build is accidentally used as Vercel web authority;
5. no product/domain invariant changes;
6. resulting receipt states exactly what the preview proves and does not prove.

## Non-goals

- merging PR #8;
- production release;
- Supabase mutation;
- Railway redeploy;
- EAS/mobile release;
- Photoroom live-provider certification;
- reworking 3D UX;
- reopening stack decisions.

## Authority

Current authority:

`READ / RECOVER / WRITE PERSONAL_KNOWLEDGE B0 ARTIFACTS`

Future Wardrobe source mutation:

`PENDING EXACT F1 ACTION AUTHORITY`

Deployment/promotion:

`NOT AUTHORIZED`

Merge/release:

`NOT AUTHORIZED`

## Evidence preserved

Historical receipts remain usable only at their exact recorded identities.

External operational state is revalidated fresh before any gate is promoted.

## After the first slice

If Vercel exact-state preview passes:

```text
Vercel gate
  ↓
reconcile Railway exact RC1 worker state
  ↓
restore/revalidate Supabase staging continuation
  ↓
remaining automated/device/provider gates
  ↓
independent review
```

If the web-only Vercel slice does not close the failure, remain in TEST/PROVE and update the contract from executed evidence rather than widening scope.
