"""Report locally installed tools without invoking agents or reading credentials."""

import argparse
import importlib.metadata
import json
import shutil


def report() -> dict:
    packages = {}
    for name in ("pytest", "pytest-xdist", "pytest-timeout", "ruff", "ty"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    return {
        "python_packages": packages,
        "external_clis": {
            name: {"available": shutil.which(name) is not None, "authentication": "not checked"}
            for name in ("uv", "git", "gh", "claude", "codex", "greptile", "modal", "hf")
        },
        "note": "Presence is not authentication, compatibility, or service validation.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()
    print(json.dumps(report(), indent=2))
