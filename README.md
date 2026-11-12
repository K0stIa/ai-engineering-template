# AI engineering template

A small, independent starter for AI-assisted Python/ML development, informed by
[LibreYOLO](https://github.com/LibreYOLO/libreyolo)'s public repository practices.
It is not a fork, an official LibreYOLO product, or a reconstruction of private prompts.

## Try it

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) first, then:

```sh
uv sync --frozen --dev
make doctor
make check
uv run ai-project
make smoke
```

The working stack is **uv + pytest/xdist/timeout + Ruff + ty + GitHub Actions**,
with Claude Code/Codex skill-discovery adapters. See [software stack and daily
loop](docs/software-stack.md) for core, optional external and hardware tiers.

Without Make, use the exact commands shown in Makefile with `uv run --no-sync`.
The GPU workflow and cloud/account integrations are not activated.

## Understand the workflow

- [How the repository works](docs/how-it-works.md): roles, files, daily agent loop,
  review, ML experiments and release handoff.
- [Connected software stack](docs/software-stack.md): what is implemented versus
  optional or not activated.
- [Free-first tool choices](docs/tool-selection.md): licenses, popularity evidence,
  service-cost boundaries and alternatives.
- [Task](docs/templates/task.md), [experiment](docs/templates/experiment.md) and
  [review](docs/templates/review.md) templates.

## Start a real project

1. Rename the distribution, package directory and CLI in pyproject.toml, src/ and tests/.
2. Replace the demo CLI with your first acceptance-tested feature.
3. Fill docs/architecture.md and record major decisions in docs/adr/.
4. Keep one canonical AGENTS.md; CLAUDE.md forwards to it.
5. Use the task-specific skills/ guides and PR evidence template.
6. Configure branch protection manually. CI files do not enable required checks.
7. Add real model/data/hardware tests when relevant; none are claimed by this starter.

## Included

- Agent and reviewer contracts; plan/review/release skills.
- Python packaging demo, hermetic unit checks and installed-wheel smoke test.
- Least-privilege GitHub CI and PR provenance-presence gate.
- [Source evidence](docs/source-analysis.md), [test tiers](docs/testing.md),
  [provenance](docs/provenance.md), and [adoption checklist](docs/adoption.md).

No paid tools, hosted GPUs, model downloads, auto-publishing or external agent
services are enabled. CI has not run until you push to your own repository.
