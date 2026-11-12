"""Build and install a wheel outside the source tree, without inherited PYTHONPATH."""

import json
import os
import subprocess
import sys
import tempfile
import venv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
env = dict(os.environ)
env.pop("PYTHONPATH", None)
with tempfile.TemporaryDirectory(prefix="ai-template-smoke-") as temporary:
    temp = Path(temporary)
    wheels = temp / "wheels"
    subprocess.run(
        [sys.executable, "-m", "pip", "wheel", "--no-deps", "--wheel-dir", str(wheels), str(root)],
        check=True,
        env=env,
    )
    artifacts = list(wheels.glob("*.whl"))
    if len(artifacts) != 1:
        raise RuntimeError(f"Expected one wheel, got {len(artifacts)}")
    venv.create(temp / "env", with_pip=True)
    bindir = temp / "env" / ("Scripts" if os.name == "nt" else "bin")
    python = bindir / ("python.exe" if os.name == "nt" else "python")
    executable = bindir / ("ai-project.exe" if os.name == "nt" else "ai-project")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--no-index", "--no-deps", str(artifacts[0])],
        check=True,
        cwd=temp,
        env=env,
    )
    result = subprocess.run(
        [str(executable)], check=True, capture_output=True, text=True, cwd=temp, env=env
    )
    if json.loads(result.stdout) != {"status": "ok", "version": "0.1.0"}:
        raise RuntimeError("Unexpected installed CLI result")
    print("PASS: installed-wheel CLI executed outside checkout.")
