# Source analysis

Inspected public release HEAD: `20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36`.

## Verified observations

- [AGENTS.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/AGENTS.md): Canonical agent policy, authority, provenance and worktree practices.
- [CLAUDE.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/CLAUDE.md): Thin pointer to the canonical instructions.
- [REVIEW.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/REVIEW.md): Reviewer-specific regression contracts.
- [docs/testing.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/docs/testing.md): Distinct hermetic PR, clean-install, real-model and manual tiers.
- [.github/workflows/provenance-check.yml](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/.github/workflows/provenance-check.yml): Statement-presence gate, not license verification.
- [.github/pull_request_template.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/.github/pull_request_template.md): Mandatory provenance section.
- [skills/libreyolo-port-model/SKILL.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/skills/libreyolo-port-model/SKILL.md): Task-oriented agent procedure.
- [skills/libreyolo-verify-training/SKILL.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/skills/libreyolo-verify-training/SKILL.md): Dedicated training verification guidance.
- [docs/adr/0001-multi-task-architecture.md](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/docs/adr/0001-multi-task-architecture.md): Persistent architecture decisions.
- [Makefile](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/Makefile): Named developer operations.

## Our adaptations

This starter generalizes policy, skill routing, evidence tiers and provenance checks.
It deliberately does not carry model families, dev/release promotion branches,
GPU runner credentials, paid review services or upstream-specific deployment paths.
The ML acceptance matrix and minimal standard-library checks are recommendations.

## Inference limits

Public files demonstrate agent-oriented engineering, not which model authored
which code or the private orchestration and prompts used by maintainers. This
checkout was inspected, not installed or executed; no LibreYOLO test pass is claimed.

## Verified software stack additions

- [pyproject.toml](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/pyproject.toml): pytest, xdist, timeout, Ruff and ty dev group; PyTorch ecosystem is separate runtime scope.
- [greptile.json](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/greptile.json): external review integration configuration.
- [use-codex skill](https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/skills/use-codex/SKILL.md): explicit Claude-to-Codex delegation, optional CLI/plugin/MCP routes.
- `.agents/skills` and `.claude/skills` point to shared canonical skills upstream.
- The actual dev nightly uses Modal; see integrations/modal/README.md for pinned source links.

Template adaptations: generated copies instead of symlinks, frozen uv.lock, bounded
two-worker gate, strict small-project typing, disabled description rewriting in
the optional Greptile profile, and manual-only GPU CI. None imply SaaS login or
cloud execution was performed.
