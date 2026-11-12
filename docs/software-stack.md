# Software stack and daily development loop

This repository now installs a working development toolchain, not just policy
files. It generalizes the public LibreYOLO process pinned in source-analysis.md.

## Core: implemented and locally tested

| Layer | Software | This repository |
|---|---|---|
| Python environments and builds | uv, setuptools | `uv.lock`, `make setup`, `make build` |
| Test runner | pytest, pytest-xdist, pytest-timeout | bounded parallel PR gate and JUnit evidence |
| Lint and formatting | Ruff | `make lint`, `make format` |
| Type checking | ty | `make typecheck` |
| Agent discovery | Claude Code and Codex directory conventions | `.claude/skills/`, `.agents/skills/`, canonical `skills/` |
| Local workflow | Git branches/worktrees | feature worktree recipe below |
| Hosted CI | GitHub Actions | frozen environment, same `make check`, wheel smoke, artifacts |
| Provenance | PR body gate + human review | presence checker; no claim of legal verification |

The copied discovery directories are generated portability adapters. LibreYOLO
uses symlinks to the shared skills directory. We use synchronized copies to avoid
Windows symlink permissions. Edit only `skills/`, then run `make agents-sync`.
CI fails when adapters drift; the sync tool refuses unmanaged existing directories.

`uv.lock` is an intentional reproducibility addition: no lockfile was present in
the inspected LibreYOLO tree. Ruff/ty are stricter here because this small starter
does not need upstream PyTorch dynamic-attribute exceptions. Two workers are the
default rather than all machine cores to avoid surprising resource use.

## Daily loop

```sh
uv sync --frozen --dev
make doctor                  # reports presence, never logs in or invokes an agent
git worktree add ../feature-example -b feature/example main
# In that worktree: start your chosen agent, with the actual task and acceptance criteria.
make check                   # discovery + Ruff + ty + offline pytest gate
make smoke                   # real wheel installation outside checkout
# Inspect git diff, run relevant model/runtime tests, prepare PR with provenance.
```

A branch can use main directly. To adopt LibreYOLO's exact promotion pattern,
create dev as integration and release as public stable, retarget CI/protected
branches and PR base explicitly. This starter does not silently create remote
branches, enable branch protection, merge or release.

## Optional account-backed tools: configured or documented, not activated

### Claude Code and Codex

The repository discovery adapters and policy are installed; CLI installation,
account login and model calls are not. LibreYOLO's `skills/use-codex` describes
Claude Code delegating to Codex, with a human reconciling the result. Use
`skills/cross-model-review` here only when requested. No automatic model calls,
API keys, MCP registration, plugin installation or paid calls occur.

### Greptile

LibreYOLO has `greptile.json` and requires CLI review when available. Its observed
configuration enables description rewriting and status checks, disables comments.
Our opt-in file is `integrations/greptile/greptile.json`; it disables automatic
PR-description rewriting as a conservative template choice. Copy it to the root
only after deciding to enable Greptile and its repository permissions. Run
`greptile review --agent --branch <base>` only with authorization to transmit
that repository to the service. A local config does not install or authenticate it.

### GitHub CLI

`gh` is used by the upstream workflow/skills. It is detected by `make doctor`, not
installed or authenticated. Humans own PR publication, review submission, merge,
protected-branch settings and release approval.

### Hugging Face Hub and PyTorch

`integrations/ml/requirements.txt` defines a starting optional profile for Torch,
Torchvision, NumPy, Pillow, Hub and safetensors. Select and pin a compatible
Torch/Torchvision/CUDA combination for your hardware before adopting it. These
are upstream model/data tools, not required for ordinary template development.
No datasets, weights or tokens are bundled, downloaded or uploaded.

### GPU CI: self-hosted or Modal

The manual GPU workflow is disabled unless `ENABLE_GPU_TESTS=true` and a trusted
self-hosted runner labeled gpu is provided. It must not be enabled on untrusted
PRs. `make test-gpu` runs a synthetic overfit example; missing Torch/CUDA fails,
not skips. This is not proof of any real model's quality and was not run here.

LibreYOLO's actual dev nightly uses Modal, with explicit ref, bounded runtime,
GPU L4, result JSON and artifacts. We do not configure billing/secrets or schedule
cloud runs. See integrations/modal/README.md for the exact adoption boundary.
Vast.ai and Beam are documented upstream alternatives, not the observed nightly.

## Process additions versus upstream facts

PR-Agent, OpenHands, Pi, OpenCode, Potato, Opik and a vector wiki are not established
as part of LibreYOLO's committed process by this inspection. Do not represent them
as reconstructed stack components. They may be evaluated separately later.
