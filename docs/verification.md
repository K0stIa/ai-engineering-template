# Validation record

## Software-stack upgrade

Linux, Python 3.12.14. Installed through `uv sync --dev`; committed uv.lock.

- `uv lock --check`: passed.
- `make check`: discovery adapter consistency, Ruff lint and formatting, ty,
  then 11 pytest cases passed using two xdist workers and 60-second timeouts.
- New doctor/discovery tests observed failing before implementation, then passing.
- `make doctor`: reported local availability without invoking external agent CLIs
  or accessing credentials. CLI presence is not authentication or compatibility.
- `make smoke`: passed; wheel installed and console entry point executed outside
  the source checkout without inherited PYTHONPATH.

Not run: GitHub-hosted CI, Python 3.10 matrix, Windows/macOS, GPU overfit example,
real models/training, Greptile, Claude, Codex model calls, Modal or Hugging Face.
No external account, token, paid run, remote branch or publication was configured.
The optional GPU workflow is disabled unless explicitly enabled on a trusted runner.

## Initial starter baseline

The original baseline passed 8 standard-library tests, compileall and clean-wheel
smoke. The upgraded pytest gate subsumes those tests; do not use the old count as
current stack evidence. Initial non-venv pip install was blocked by a read-only
user site; isolated virtual environment setup succeeded.

## Process documentation update (2026-11-12)

`make check` re-run: 11/11 selected tests passed; Ruff, formatting, ty and skill
mirror checks passed. `make smoke` passed again. Local Markdown links in README
and docs resolved; `git diff --check` passed. Tool popularity/license metadata and
service-cost boundaries were checked against the primary sources linked from
`docs/tool-selection.md`. This does not validate external-service integration.
