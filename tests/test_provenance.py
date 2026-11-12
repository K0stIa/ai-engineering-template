import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProvenanceTest(unittest.TestCase):
    def check_body(self, text):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts/check_provenance.py")],
            input=text,
            text=True,
            capture_output=True,
        )

    def test_original_statement(self):
        self.assertEqual(
            self.check_body(
                "## Code provenance\nOriginal implementation for this project."
            ).returncode,
            0,
        )

    def test_missing_section(self):
        self.assertEqual(self.check_body("No provenance").returncode, 1)

    def test_comment_only(self):
        self.assertEqual(self.check_body("## Code provenance\n<!-- fill this -->").returncode, 1)

    def test_other_section_not_counted(self):
        self.assertEqual(self.check_body("## Code provenance\n## Tests\nPassed").returncode, 1)

    def test_heading_inside_comment_not_counted(self):
        self.assertEqual(
            self.check_body("<!--\n## Code provenance\n-->\nOther prose").returncode, 1
        )

    def test_case_and_crlf(self):
        self.assertEqual(
            self.check_body(
                "### CODE PROVENANCE\r\nOriginal work.\r\n## Tests\r\nPassed"
            ).returncode,
            0,
        )

    def test_placeholder_rejected(self):
        self.assertEqual(self.check_body("## Code provenance\nTODO").returncode, 1)
