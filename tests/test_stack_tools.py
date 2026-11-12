import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_doctor_reports_missing_clis_without_executing_them():
    env = dict(os.environ, PATH="")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/stack_doctor.py"), "--json"],
        env=env,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["external_clis"]["codex"]["available"] is False
    assert data["external_clis"]["greptile"]["authentication"] == "not checked"


def test_discovery_adapters_copy_and_detect_drift():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        skill = root / "skills" / "example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("example")
        command = [sys.executable, str(ROOT / "scripts/sync_skills.py"), "--root", str(root)]
        assert subprocess.run(command + ["--check"], capture_output=True).returncode == 1
        assert subprocess.run(command, capture_output=True).returncode == 0
        assert (root / ".agents/skills/example/SKILL.md").read_text() == "example"
        assert (root / ".claude/skills/example/SKILL.md").read_text() == "example"
        assert subprocess.run(command + ["--check"], capture_output=True).returncode == 0
        (root / ".claude/skills/example/SKILL.md").write_text("stale")
        assert subprocess.run(command + ["--check"], capture_output=True).returncode == 1


def test_discovery_refuses_empty_source():
    with tempfile.TemporaryDirectory() as tmp:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/sync_skills.py"), "--root", tmp],
            capture_output=True,
        )
        assert result.returncode == 2
        assert b"No canonical skills" in result.stderr
