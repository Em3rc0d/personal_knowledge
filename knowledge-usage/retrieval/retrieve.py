#!/usr/bin/env python3
"""Deterministic local Markdown section search. Candidates, not verified answers.

No network, API, embeddings or model calls. Entire Markdown sections are kept
intact; an oversized high-priority section blocks instead of being truncated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

SKIP_DIRS = frozenset({".git", ".github", "node_modules", ".venv", "venv", "__pycache__", "research-corpora", "dist", "build"})
STOP = frozenset("a al algo and are as at be but by con de del do el en es for from how in is it la las lo los of on or para por que qué se should the to un una use usando we what which with y ya about como cómo esta este su sus mi me no not esto entre dentro our can do qué cuál fue qué hay".split())
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
WORD = re.compile(r"[a-z0-9]+(?:[-.][a-z0-9]+)*")
FENCE = re.compile(r"^\s*(\x60{3,}|~{3,})")


def terms(value: str) -> list[str]:
    norm = unicodedata.normalize("NFKD", value.casefold())
    norm = "".join(ch for ch in norm if not unicodedata.combining(ch))
    return [w for w in WORD.findall(norm) if w not in STOP and len(w) > 1]


@dataclass(frozen=True)
class Section:
    path: str
    headings: tuple[str, ...]
    first_line: int
    last_line: int
    content: str
    sha256: str


def parse_sections(path: str, data: bytes) -> list[Section]:
    # Reject files that cannot be safely represented as UTF-8 Markdown.
    lines = data.decode("utf-8").splitlines(keepends=True)
    sections: list[Section] = []
    heading_chain: list[str] = []
    stack_depth = 0
    fence_char = ""
    fence_width = 0
    start = 0

    def save(end: int) -> None:
        fragment = "".join(lines[start:end]).strip("\n")
        if not fragment.strip():
            return
        if all(not row.strip() or HEADING.match(row) for row in fragment.splitlines()):
            return  # Avoid title-only segments with no claim or evidence.
        sections.append(Section(path=path, headings=tuple(heading_chain), first_line=start + 1,
                                last_line=end, content=fragment, sha256=hashlib.sha256(data).hexdigest()))

    for i, line in enumerate(lines):
        f = FENCE.match(line)
        if f:
            marker = f.group(1)
            if not fence_char:
                fence_char, fence_width = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_width:
                fence_char, fence_width = "", 0
            continue
        if fence_char:
            continue
        h = HEADING.match(line)
        if h:
            save(i)
            depth, name = len(h.group(1)), h.group(2).strip()
            if depth <= stack_depth:
                heading_chain[:] = heading_chain[:depth - 1]
            elif depth > stack_depth + 1:
                # Ragged heading hierarchy; preserve known ancestor without inventing levels.
                pass
            if len(heading_chain) >= depth:
                heading_chain[:] = heading_chain[:depth - 1]
            heading_chain.append(name)
            stack_depth = depth
            start = i
    save(len(lines))
    return sections


def enumerate_docs(root: Path, scope: str) -> list[Path]:
    base = (root / scope).resolve()
    if not base.is_relative_to(root.resolve()) or not base.is_dir():
        raise ValueError("scope must be an existing directory inside the repository")
    found = []
    skip = SKIP_DIRS if scope == "." else SKIP_DIRS - {"research-corpora"}
    for path in base.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part in skip or part.startswith(".") for part in rel.parts[:-1]):
            continue
        resolved = path.resolve()
        if not resolved.is_relative_to(root.resolve()):
            continue  # no symlink traversal into external/untrusted files
        if path.is_file():
            found.append(path)
    return sorted(found)


def importance(path: str, mode: str) -> int:
    p = path.lower()
    if mode == "current":
        if p.endswith("/status.md") or p == "status.md":
            return 8
        if "/systems/" in p or p.endswith("/llm_context.md"):
            return 5
        if "/mk/" in p:
            return 2
        if "/quarries/" in p or "/mining-site/" in p:
            return -3
    if mode == "evidence":
        if "/mining-site/" in p or "/quarries/" in p:
            return 5
    return 0


def score_section(section: Section, query_terms: list[str], mode: str) -> int:
    if not query_terms:
        return 0
    p = set(terms(section.path.replace("/", " ").replace("_", " ")))
    h = set(terms(" ".join(section.headings)))
    body = set(terms(section.content))
    matched = 0
    score = 0
    for q in set(query_terms):
        contribution = (12 if q in p else 0) + (9 if q in h else 0) + (2 if q in body else 0)
        score += contribution
        matched += bool(contribution)
    if not matched:
        return 0
    # Prioritize covering the question, not verbosity or keyword repetition.
    score += 10 * matched * matched // len(set(query_terms))
    if matched == len(set(query_terms)):
        score += 9
    score += importance(section.path, mode)
    return max(0, score)


def retrieve(repo_root: Path, query: str, scope: str = ".", mode: str = "current",
             max_chars: int = 6000, max_sections: int = 3) -> dict:
    if not (80 <= max_chars <= 100_000):
        raise ValueError("max_chars must be between 80 and 100000")
    if not (1 <= max_sections <= 25):
        raise ValueError("max_sections must be between 1 and 25")
    if mode not in {"current", "evidence", "discover"}:
        raise ValueError("invalid mode")
    q = terms(query)
    if not q:
        raise ValueError("query has no searchable terms")
    root = repo_root.resolve()
    if not root.is_dir():
        raise ValueError("repository root missing")
    ranked: list[tuple[int, Section]] = []
    scanned = 0
    for path in enumerate_docs(root, scope):
        rel = path.relative_to(root).as_posix()
        data = path.read_bytes()
        scanned += 1
        if len(data) > 1_000_000:
            continue  # oversized file requires explicit manual source inspection
        for section in parse_sections(rel, data):
            s = score_section(section, q, mode)
            if s > 0:
                ranked.append((s, section))
    ranked.sort(key=lambda x: (-x[0], x[1].path, x[1].first_line))
    chosen: list[dict] = []
    omitted_oversize: list[dict] = []
    used = 0
    for s, sec in ranked:
        if len(chosen) >= max_sections:
            break
        # Include source and headings in the budget, not just body.
        header = f"[{sec.path}:{sec.first_line}-{sec.last_line}] " + " > ".join(sec.headings) + "\n"
        amount = len(header) + len(sec.content)
        if amount + used > max_chars:
            omitted_oversize.append({"path": sec.path, "lines": [sec.first_line, sec.last_line],
                                     "required_chars": amount, "score": s})
            # Do not silently replace a top-ranked unreturned source with lower-ranked evidence.
            if not chosen:
                break
            continue
        chosen.append({"path": sec.path, "start_line": sec.first_line, "end_line": sec.last_line,
                       "heading_path": list(sec.headings), "git_revision": "NOT_PINNED",
                       "sha256": sec.sha256, "score": s, "text": sec.content})
        used += amount
    status = "CANDIDATES_ONLY" if chosen else ("BUDGET_BLOCKED" if omitted_oversize else "NO_MATCH")
    if chosen and omitted_oversize:
        status = "PARTIAL_CANDIDATES_EXPANSION_REQUIRED"
    return {"status": status, "query": query, "scope": scope, "mode": mode,
            "scanned_documents": scanned, "budget_chars": max_chars, "used_chars": used,
            "results": chosen, "blocked_sections": omitted_oversize[:5],
            "answer_verified": False, "billed_token_savings": None,
            "warning": "Candidate retrieval only; confirm authority, contradictions, freshness and complete evidence before answering."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Original question; quote when it contains spaces")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--scope", default=".", help="Restrict to directory, e.g. agent-engineering")
    parser.add_argument("--mode", choices=["current", "evidence", "discover"], default="current")
    parser.add_argument("--max-chars", type=int, default=6000)
    parser.add_argument("--max-sections", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = retrieve(args.repo_root, args.query, args.scope, args.mode,
                          args.max_chars, args.max_sections)
    except (ValueError, OSError, UnicodeError) as exc:
        parser.exit(2, f"FAIL CLOSED: {exc}\n")
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"STATUS: {result['status']} | {result['used_chars']}/{result['budget_chars']} chars "
              f"| documents scanned {result['scanned_documents']}")
        for item in result["results"]:
            print(f"\nSOURCE: {item['path']}:{item['start_line']}-{item['end_line']} "
                  f"(sha256:{item['sha256'][:12]})")
            print(item["text"])
        if result["blocked_sections"]:
            print("\nBLOCKED HIGH-RELEVANCE SECTIONS: " + json.dumps(result["blocked_sections"]))
        print("\nCANDIDATES ONLY: validate authority, freshness, competing evidence and answer quality.")
    return 0 if result["status"] == "CANDIDATES_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
