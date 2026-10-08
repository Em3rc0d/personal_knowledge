#!/usr/bin/env python3
"""Offline, source-pinned context-footprint experiment (no LLM/network/CI calls).

Measures the exact UTF-8 bytes and optional tokenizer counts of fixed, curated
document sets. It does NOT measure billed tokens, retrieval effectiveness,
answer quality, execution time, or agent/tool overhead.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def git_blob_sha(data: bytes) -> str:
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def within_repo(repo_root: Path, path: str) -> Path:
    if not isinstance(path, str) or not path or "\\" in path or path.startswith("/"):
        raise ValueError(f"invalid relative path: {path!r}")
    if ".." in Path(path).parts:
        raise ValueError(f"path traversal: {path!r}")
    candidate = (repo_root / path).resolve()
    if not candidate.is_relative_to(repo_root.resolve()) or not candidate.is_file():
        raise ValueError(f"missing/outside-repo file: {path!r}")
    return candidate


def read_pinned(repo_root: Path, blobs: dict[str, str]) -> dict[str, bytes]:
    content: dict[str, bytes] = {}
    for path, expected_sha in blobs.items():
        data = within_repo(repo_root, path).read_bytes()
        actual_sha = git_blob_sha(data)
        if actual_sha != expected_sha:
            raise ValueError(
                f"STALE_SOURCE {path}: expected blob {expected_sha}, found {actual_sha}. "
                "Do not compare against a silently changed corpus."
            )
        content[path] = data
    return content


def count_side(paths: list[str], files: dict[str, bytes], encoder: object | None) -> dict:
    data = [files[path] for path in paths]
    result = {
        "document_count": len(paths),
        "utf8_bytes": sum(len(item) for item in data),
        "whitespace_words": sum(len(re.findall(r"\S+", item.decode("utf-8"))) for item in data),
    }
    result["tokenizer_tokens"] = (
        sum(len(encoder.encode(item.decode("utf-8"))) for item in data)
        if encoder is not None else None
    )
    return result


def measure(spec: dict, root: Path, encoder: object | None = None) -> dict:
    if spec.get("schema") != "context-retrieval-measurement/v1":
        raise ValueError("unsupported manifest schema")
    blobs = spec.get("source_blobs")
    cases = spec.get("cases")
    if not isinstance(blobs, dict) or not blobs or not isinstance(cases, list) or not cases:
        raise ValueError("manifest must contain pinned source_blobs and cases")
    files = read_pinned(root, blobs)
    results = []
    seen_ids: set[str] = set()
    for case in cases:
        case_id = case["id"]
        baseline = case["baseline"]
        selective = case["selective"]
        required = case["required_evidence"]
        anchors = case["anchors"]
        if case_id in seen_ids or not baseline or not selective:
            raise ValueError(f"{case_id}: duplicate ID or empty document list")
        seen_ids.add(case_id)
        if len(baseline) != len(set(baseline)) or len(selective) != len(set(selective)):
            raise ValueError(f"{case_id}: duplicate document path")
        if not set(selective).issubset(baseline):
            raise ValueError(f"{case_id}: selected documents are not a subset of baseline")
        if not set(required).issubset(selective):
            raise ValueError(f"{case_id}: required evidence omitted by selective route")
        if not set(baseline).issubset(files):
            raise ValueError(f"{case_id}: corpus lacks a pinned source document")
        for anchor in anchors:
            if anchor["path"] not in required or anchor["text"] not in files[anchor["path"]].decode("utf-8"):
                raise ValueError(f"{case_id}: required evidence anchor absent: {anchor}")
        broad = count_side(baseline, files, encoder)
        narrow = count_side(selective, files, encoder)
        if broad["utf8_bytes"] == 0:
            raise ValueError(f"{case_id}: empty baseline")
        pct = round(100 * (broad["utf8_bytes"] - narrow["utf8_bytes"]) / broad["utf8_bytes"], 2)
        token_pct = None
        if encoder is not None and broad["tokenizer_tokens"]:
            token_pct = round(
                100 * (broad["tokenizer_tokens"] - narrow["tokenizer_tokens"]) /
                broad["tokenizer_tokens"], 2
            )
        results.append({
            "case_id": case_id,
            "question": case["question"],
            "baseline": broad,
            "selective": narrow,
            "utf8_bytes_reduction_pct": pct,
            "tokenizer_tokens_reduction_pct": token_pct,
            "evidence_presence_gate": "PASS",
            "answer_quality": "NOT_EVALUATED",
            "billed_tokens_saved": None,
        })
    return {
        "schema": "context-retrieval-result/v1",
        "source_reference_commit": spec["reference_commit"],
        "source_integrity": "PASS",
        "route_type": "MANUALLY_CURATED_ORACLE",
        "comparison": "fixed-document-input-only",
        "cases": results,
        "billed_tokens_saved": None,
        "time_saved": None,
        "answer_quality": "NOT_EVALUATED",
    }


def main() -> int:
    default_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=default_root)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("cases.json"))
    parser.add_argument("--encoding", default="none", help="none (stdlib) or tiktoken encoding, e.g. o200k_base")
    parser.add_argument("--json-out", type=Path, help="Optional results path; no file is written by default")
    args = parser.parse_args()
    encoder = None
    if args.encoding != "none":
        try:
            import tiktoken
            encoder = tiktoken.get_encoding(args.encoding)
        except (ImportError, Exception) as exc:
            parser.error(f"tokenizer unavailable ({exc}); no token claim was produced")
    try:
        spec = json.loads(args.manifest.read_text(encoding="utf-8"))
        result = measure(spec, args.repo_root.resolve(), encoder)
    except (ValueError, KeyError, OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"FAIL CLOSED: {exc}", file=sys.stderr)
        return 2
    result["tokenizer_encoding"] = args.encoding if encoder is not None else None
    print("Case | Broad bytes | Selective bytes | Byte reduction | Evidence")
    for c in result["cases"]:
        print(f"{c['case_id']} | {c['baseline']['utf8_bytes']} | "
              f"{c['selective']['utf8_bytes']} | "
              f"{c['utf8_bytes_reduction_pct']:.2f}% | {c['evidence_presence_gate']}")
    if encoder is None:
        print("TOKEN COUNTS: UNKNOWN (no tokenizer). BILLED TOKENS: UNKNOWN.")
    else:
        print(f"TOKEN COUNTS: local {args.encoding} source-text counts only. "
              "BILLED TOKENS: UNKNOWN.")
    print("ANSWER QUALITY: NOT_EVALUATED. ROUTE SELECTION: MANUALLY CURATED.")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Receipt: {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
