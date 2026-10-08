#!/usr/bin/env python3
"""Standard-library unit tests; no network, paid APIs or Github Actions."""

import tempfile
import unittest
from pathlib import Path

from measure import git_blob_sha, measure, within_repo


class ContextMeasurementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.a = b"MK1 requires REC-012.\n"
        self.b = b"Reference receipt without extra facts.\n"
        (self.root / "docs").mkdir()
        (self.root / "docs/a.md").write_bytes(self.a)
        (self.root / "docs/b.md").write_bytes(self.b)
        self.spec = {
            "schema": "context-retrieval-measurement/v1",
            "reference_commit": "fixture",
            "source_blobs": {
                "docs/a.md": git_blob_sha(self.a),
                "docs/b.md": git_blob_sha(self.b),
            },
            "cases": [{
                "id": "fixture",
                "question": "What blocks MK1?",
                "baseline": ["docs/a.md", "docs/b.md"],
                "selective": ["docs/a.md"],
                "required_evidence": ["docs/a.md"],
                "anchors": [{"path": "docs/a.md", "text": "REC-012"}],
            }],
        }

    def tearDown(self):
        self.temp.cleanup()

    def test_curated_route_reduces_input_without_token_claim(self):
        result = measure(self.spec, self.root)
        case = result["cases"][0]
        self.assertEqual(case["evidence_presence_gate"], "PASS")
        self.assertEqual(case["selective"]["utf8_bytes"], len(self.a))
        self.assertEqual(case["baseline"]["utf8_bytes"], len(self.a) + len(self.b))
        self.assertGreater(case["utf8_bytes_reduction_pct"], 0)
        self.assertIsNone(case["billed_tokens_saved"])
        self.assertIsNone(case["baseline"]["tokenizer_tokens"])
        self.assertEqual(case["answer_quality"], "NOT_EVALUATED")

    def test_stale_source_fails_closed(self):
        (self.root / "docs/a.md").write_text("REC-012 was changed", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "STALE_SOURCE"):
            measure(self.spec, self.root)

    def test_missing_evidence_fails_closed(self):
        self.spec["cases"][0]["required_evidence"] = ["docs/b.md"]
        with self.assertRaisesRegex(ValueError, "required evidence omitted"):
            measure(self.spec, self.root)

    def test_missing_anchor_fails_closed(self):
        self.spec["cases"][0]["anchors"][0]["text"] = "fabricated"
        with self.assertRaisesRegex(ValueError, "anchor absent"):
            measure(self.spec, self.root)

    def test_path_traversal_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "path traversal"):
            within_repo(self.root, "../escaped.txt")

    def test_non_subset_route_fails_closed(self):
        self.spec["cases"][0]["baseline"] = ["docs/b.md"]
        with self.assertRaisesRegex(ValueError, "not a subset"):
            measure(self.spec, self.root)


if __name__ == "__main__":
    unittest.main()
