# How this repository works

This is a repository-level operating system for engineering work, not an
always-running autonomous agent service. Its purpose is to make work explicit,
keep AI changes small, and require reproducible evidence before human acceptance.

## The loop

```text
Human goal and acceptance criteria
                |
                v
Task brief + relevant architecture/decision records
                |
                v
One agent + one isolated branch/worktree
                |
                v
Failing regression -> implementation -> local checks
                |
                v
Review actual diff + reproduce important behavior
                |
                v
Pull request: evidence, limitations, provenance, rollback
                |
                v
GitHub CI + human decision -> merge -> separately approved release
```

No step sends code to an AI service, creates an issue, opens a PR, purchases GPU
capacity or publishes a package automatically. Start your chosen agent yourself,
or explicitly authorize the assistant to do that work.

## Who owns what

| Participant | Responsibility | Does not imply |
|---|---|---|
| Human owner | Goal, scope, risk, external-service permissions, acceptance and release decisions | Every routine code choice needs another approval |
| Implementing agent | Inspect actual code, maintain a focused diff, test and explain evidence | Its own summary proves success |
| Reviewer | Check contracts and diff, reproduce key failures, challenge evidence | Another model's approval replaces human authority |
| CI | Run deterministic checks on the submitted revision | All hardware, real models or production paths were tested |
| Repository documents | Preserve decisions and interfaces for future sessions | A vector database or automatic long-term memory is installed |

For a small change one person can implement and review. For risky changes use an
independent reviewer. A second AI review is optional and must use an authorized
service; a human review of diff and test results is the free default.

## Where each kind of information belongs

| Location | Purpose |
|---|---|
| `README.md` | First-run commands and navigation |
| `AGENTS.md` | Canonical rules for coding agents and authority boundaries |
| `CLAUDE.md` | Claude entry point pointing to the canonical policy |
| `skills/` | Canonical task procedures, not background-running agents |
| `.agents/skills/`, `.claude/skills/` | Generated discovery mirrors for compatible agents |
| `REVIEW.md` | Reviewer-specific criteria and common false-positive risks |
| `docs/architecture.md` | Public interfaces, modules, data flow and trust boundaries |
| `docs/adr/` | Durable architecture decisions and trade-offs |
| `docs/templates/` | Task brief, experiment card and review report starters |
| `tests/` | Executable behavior checks |
| `scripts/` | Repository tooling: provenance, skill sync, doctor and wheel smoke |
| `artifacts/` | Local/JUnit evidence, ignored by Git and optionally uploaded by CI |
| `.github/` | CI workflows and pull-request form |
| `integrations/` | Explicit optional service/hardware configuration and guidance |

Edit a canonical skill, then run `make agents-sync`. `make check` detects stale
mirrors. Do not make three independent copies of the same policy by editing the
mirrors separately.

## First project setup

1. Clone your new repository, not the LibreYOLO source repository.
2. Install uv from its official installation guide; run `make setup`.
3. Run `make doctor`. It reports locally available executables/packages without
   invoking agents, logging in, reading tokens or validating service access.
4. Run `make check` and `make smoke` before changing anything. This establishes a
   baseline on your machine.
5. Rename `ai_project`, its console entry point, tests and project metadata.
6. Replace the demo with the smallest real user workflow. Define contracts in
   `docs/architecture.md` and add a task-specific acceptance test.
7. Configure branch protection and required CI checks in GitHub yourself, if
   wanted. Merely adding workflow YAML does not configure repository protection.

The template deliberately keeps one `main` branch. LibreYOLO's `dev` -> `release`
flow is an optional organizational choice, not required for one developer.

## Example: ask an agent to add a feature

Copy `docs/templates/task.md`, fill in the goal and acceptance criteria, then:

```sh
git worktree add ../my-feature -b feature/my-feature main
cd ../my-feature
uv sync --frozen --dev
```

Give the agent this brief:

> Read AGENTS.md and the task brief. Inspect the existing implementation and
> affected contracts. Add a failing regression, implement the smallest change,
> run make check and the required runtime tier, and report commands, results and
> unverified behavior. Do not publish, merge or use external services unless
> explicitly authorized.

After implementation:

```sh
make check
make smoke
git diff --check
git diff --stat
```

Inspect the actual diff. For changes to shared code, run representative consuming
workflows. For ML changes, use the test matrix below, not only the demo unit suite.
Only then commit and prepare a PR with provenance and evidence. Use explicit
selected-file staging when the worktree contains unrelated changes.

## What each green check actually proves

| Command | Evidence | Important limit |
|---|---|---|
| `make agents-check` | Discovery mirrors match canonical files | Agent discovery has not been exercised inside every client version |
| `make lint` | Ruff checks and formatting pass | Style/static diagnostics do not prove correct behavior |
| `make typecheck` | ty accepts package/repository scripts | Optional GPU dependencies and arbitrary future code are not all covered |
| `make test-pr` | Selected offline CPU tests execute with timeout and parallel workers | Real models, external data, network and GPU tiers are excluded |
| `make smoke` | Built wheel installs and CLI runs outside checkout | Demo CLI behavior is not a production acceptance test |
| `make build` | Source distribution and wheel can be built | Nothing is uploaded to a package index |
| `make test-gpu` | Explicit optional CUDA synthetic overfit example | Not run by default; not proof of a real model's quality |

The socket guard blocks external connections in the test process. It is not an
OS sandbox and cannot police arbitrary subprocesses. Keep untrusted PR execution
away from credentials and sensitive runners.

## ML-specific workflow

Use `docs/templates/experiment.md` before a training experiment. Record the code,
data and model identities, seed, device, baseline, metric and a bounded budget.
Add progressively more expensive evidence:

1. Dataset schema/split and leakage checks.
2. Shape, finite loss/gradient and architecture invariants.
3. A single-batch overfit experiment.
4. A small real learning run against a baseline.
5. Export/runtime parity and target-device measurements.
6. Representative full evaluation before release.

These are recommended additions, not all implemented template capabilities. The
optional PyTorch test is a small synthetic example. A skipped, missing-data or
unavailable-hardware test must remain unverified rather than being called passed.

## Release and handoff

Use `skills/prepare-release`. Record the exact revision, clean/dirty working tree,
artifact hashes, commands, exit statuses, test counts and known omissions. Run the
actual install/upgrade/rollback path appropriate to your product. Human approval
and separately authorized publishing remain required. No release token or
publishing workflow is installed by this template.
