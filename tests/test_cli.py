import json
import subprocess
import sys
import unittest


class CliTest(unittest.TestCase):
    def test_status(self):
        result = subprocess.run(
            [sys.executable, "-m", "ai_project"], text=True, capture_output=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"status": "ok", "version": "0.1.0"})
