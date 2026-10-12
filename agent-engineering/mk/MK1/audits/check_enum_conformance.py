#!/usr/bin/env python3
"""Bounded static check of MK1 normalized enum scalars. Python stdlib only.

Not a YAML parser, execution proof, semantic grader, or production certificate.
Use the exact representative set from the MK1 registry, not the historical REC-012
deterministic control, which is intentionally not a materialized agent record.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RECORDS = (
    "REC-001-minimal-while-loop.md",
    "REC-002-hitl-approval.md",
    "REC-003-trace-evaluation-harness.md",
    "REC-004-generated-code-browser-e2e.md",
    "REC-007-social-publication.md",
    "REC-008-document-data-egress.md",
    "REC-009-database-authority.md",
    "REC-010-reflection-adaptation.md",
    "REC-011-memory-lifecycle-contrast.md",
    "REC-012-external-agent-scaling.md",
    "REC-013-mcp-revision-drift.md",
)
BLOCK = re.compile(r"^\x60{3}yaml\s*\n(.*?)^\x60{3}\s*$", re.MULTILINE | re.DOTALL)
SECTION = re.compile(r"^([a-z][a-z_]+):\s*$")
FIELD = re.compile(r"^  ([a-z][a-z_]+):\s*(.*)$")


def yaml_blocks(document: str) -> list[str]:
    return BLOCK.findall(document)


def enum_fields(schema: str) -> dict[str, list[str]]:
    blocks = yaml_blocks(schema)
    if not blocks:
        raise ValueError("Missing YAML schema block")
    section = ""
    enums: dict[str, list[str]] = {}
    for line in blocks[0].splitlines():
        head = SECTION.match(line)
        if head:
            section = head.group(1)
            continue
        entry = FIELD.match(line)
        if entry and " | " in entry.group(2):
            enums[f"{section}.{entry.group(1)}"] = [
                option.strip() for option in entry.group(2).split(" | ")
            ]
    if not enums:
        raise ValueError("No enumerated schema fields")
    return enums


def check_record(document: str, enums: dict[str, list[str]], name: str) -> tuple[int, list[dict[str, object]]]:
    candidates = [b for b in yaml_blocks(document) if "\ncontrol:" in b and "\ncapabilities:" in b]
    if len(candidates) != 1:
        return 0, [{"record": name, "error": "expected one primary classification YAML block", "count": len(candidates)}]
    section = ""
    checked = 0
    problems: list[dict[str, object]] = []
    for line_number, line in enumerate(candidates[0].splitlines(), start=1):
        head = SECTION.match(line)
        if head:
            section = head.group(1)
            continue
        field = FIELD.match(line)
        if not field:
            continue
        key = f"{section}.{field.group(1)}"
        if key not in enums:
            continue
        checked += 1
        # Annotation comments are not part of the scalar; do not remove '#'
        # inside an intentionally quoted value.
        value = re.split(r"\s+#", field.group(2), maxsplit=1)[0].strip().strip('"').strip("'")
        if value not in enums[key]:
            problems.append({
                "record": name, "classification_yaml_line": line_number,
                "field": key, "value": value, "allowed": enums[key],
            })
    return checked, problems


def run(root: Path) -> dict[str, object]:
    mk = root / "agent-engineering" / "mk" / "MK1"
    enums = enum_fields((mk / "CLASSIFICATION_SCHEMA.md").read_text(encoding="utf-8"))
    paths = [mk / "records" / filename for filename in RECORDS]
    paths.append(root / "agent-engineering" / "systems" / "strands" / "CLASSIFICATION.md")
    checked = 0
    problems: list[dict[str, object]] = []
    for path in paths:
        amount, issues = check_record(path.read_text(encoding="utf-8"), enums, path.name)
        checked += amount
        problems.extend(issues)
    return {
        "scope": "MK1 representative normalized YAML scalar enumerations only",
        "schema": "mk1-draft-2026-09-16.1",
        "records": len(paths), "enum_dimensions": len(enums),
        "enum_scalars_checked": checked,
        "violations": problems, "violation_count": len(problems),
        "not_tested": ["YAML syntax in all fences", "semantic evidence decisions",
                       "child-agent effective permissions / PA-06", "production behavior"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[4])
    args = parser.parse_args()
    report = run(args.repo_root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["violation_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
