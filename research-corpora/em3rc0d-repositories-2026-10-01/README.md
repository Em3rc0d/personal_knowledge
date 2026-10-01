# EM3RC0D Repository Estate — 2026-10-01

Status: **MK0 SOURCE CORPUS / NO AUTOMATIC PROMOTION**

This corpus freezes the identity of the repository estate selected for cross-system mining.

It does **not** make source code, README claims, external forks or generated summaries canonical knowledge merely by placing them under `personal_knowledge`.

## Why this exists

The repository estate now contains product systems, engineering frameworks, runtime primitives, distribution systems and external donor forks. This corpus gives them one reproducible source boundary:

```text
repository
  → pinned commit
  → source receipt
  → optional immutable materialization
  → quarry / system view
  → comparison / contradiction
  → MK gate
  → promoted knowledge
```

## Scope

- Destination/self: `Em3rc0d/personal_knowledge` is intentionally excluded from recursive capture.
- First-party sources: may be materialized as exact source snapshots.
- MIT forks: may be materialized only with their license/provenance preserved.
- Mixed-license sources: default to `POINTER_ONLY`.
- No nested `.git/` directories are stored.
- A materialized tree is evidence, not a working copy.
- Operational development stays in each original repository.

## Files

- `SOURCES.json` — machine-readable registry and exact SHAs.
- `sources/*.md` — human-readable receipts.
- `tools/materialize.py` — deterministic snapshot materializer.
- `upstream/` — generated snapshot destination; created by the materializer, never edited manually.
- `../../em3rc0d-foundry/systems/` — synthesized current views and cross-system relationships.

## Materialization

From the root of `personal_knowledge`:

```bash
python research-corpora/em3rc0d-repositories-2026-10-01/tools/materialize.py --all
```

By default the tool refuses `POINTER_ONLY` sources such as `skills`.

A successful materialization verifies the pinned commit, exports the Git tree without `.git/`, and writes a receipt beside the snapshot.

## Truth boundary

`SOURCE_PRESENT != INSPECTED != UNDERSTOOD != PROMOTED != PRODUCTION_READY`.

The current corpus is an intake and reproducibility layer. Canonical conclusions belong in the relevant domain after evidence-backed promotion.
