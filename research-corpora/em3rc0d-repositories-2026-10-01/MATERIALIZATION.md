# Materialization contract

The source receipts are committed immediately. Full source trees are intentionally generated from the pinned SHAs rather than maintained as mutable nested repositories.

## Invariants

1. Checkout must resolve to the exact SHA in `SOURCES.json`.
2. `.git/` must never be copied into `upstream/`.
3. Existing snapshot directories are immutable unless `--force` is explicitly supplied.
4. `POINTER_ONLY` sources fail closed.
5. External-license snapshots preserve repository license files and the source receipt.
6. Materialization does not promote any source statement to EM3RC0D canon.
7. Refreshing a repository requires a new corpus date or an explicit versioned refresh record; do not silently move a pinned SHA.
