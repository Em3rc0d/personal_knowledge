#!/usr/bin/env python3
"""Materialize exact repository snapshots from SOURCES.json.

No Git metadata is copied. POINTER_ONLY sources fail closed.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent
REGISTRY = CORPUS / "SOURCES.json"
UPSTREAM = CORPUS / "upstream"


def run(*args: str, cwd: Path | None = None) -> str:
    proc = subprocess.run(args, cwd=cwd, check=True, text=True, capture_output=True)
    return proc.stdout.strip()


def safe_extract(archive: Path, target: Path) -> None:
    target_resolved = target.resolve()
    with tarfile.open(archive, "r") as tf:
        for member in tf.getmembers():
            dest = (target / member.name).resolve()
            if target_resolved not in dest.parents and dest != target_resolved:
                raise RuntimeError(f"unsafe archive path: {member.name}")
        tf.extractall(target)


def load_sources() -> list[dict]:
    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return payload["sources"]


def materialize(source: dict, force: bool) -> None:
    slug = source["slug"]
    policy = source["policy"]
    if policy == "POINTER_ONLY":
        raise RuntimeError(f"{slug}: POINTER_ONLY; full materialization is intentionally blocked")

    target = UPSTREAM / slug
    receipt = CORPUS / "materialized" / f"{slug}.json"

    if target.exists():
        if not force:
            raise RuntimeError(f"{slug}: snapshot already exists; use --force only for deliberate rebuild")
        shutil.rmtree(target)

    url = f"https://github.com/{source['repo']}.git"
    sha = source["sha"]

    with tempfile.TemporaryDirectory(prefix=f"em3rc0d-{slug}-") as tmp:
        checkout = Path(tmp) / "repo"
        archive = Path(tmp) / "snapshot.tar"

        run("git", "init", str(checkout))
        run("git", "remote", "add", "origin", url, cwd=checkout)
        run("git", "fetch", "--depth", "1", "origin", sha, cwd=checkout)
        resolved = run("git", "rev-parse", "FETCH_HEAD", cwd=checkout)
        if resolved != sha:
            raise RuntimeError(f"{slug}: expected {sha}, resolved {resolved}")

        run("git", "archive", "--format=tar", f"--output={archive}", resolved, cwd=checkout)
        target.mkdir(parents=True, exist_ok=False)
        safe_extract(archive, target)

    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps({
        "schema": "em3rc0d.materialization-receipt.v1",
        "slug": slug,
        "repository": source["repo"],
        "sha": sha,
        "policy": policy,
        "path": str(target.relative_to(CORPUS)),
        "git_metadata_copied": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"PASS {slug} @ {sha}")


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true")
    group.add_argument("--repo", action="append", default=[])
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    sources = load_sources()
    selected = sources if args.all else [s for s in sources if s["slug"] in set(args.repo)]
    if not selected:
        raise SystemExit("no matching repositories")

    failures = []
    for source in selected:
        try:
            materialize(source, args.force)
        except Exception as exc:
            failures.append((source["slug"], str(exc)))
            print(f"BLOCKED {source['slug']}: {exc}")

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
