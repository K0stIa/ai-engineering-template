# Free-first software choices

Checked against public project metadata and primary documentation on **2026-11-12**.
The default stack favors widely adopted open-source tools that run locally without
subscriptions. Optional services remain off unless the owner deliberately enables
them. Software being open source does not make model inference, hosting, GPUs,
storage, network transfer or electricity free.

## Recommended baseline

Keep **uv + pytest/xdist/timeout + Ruff + ty + Git + human review** as the default.
Use the supplied GitHub CI within your account's applicable quota. Start with one
AI coding client you already use, rather than installing multiple orchestration
systems. If a free/self-hostable AI PR reviewer becomes necessary, evaluate
PR-Agent before adding a paid review service. Add experiment tracking only when
real experiments need comparison.

## Implemented core

Star counts below are point-in-time signals of attention, not quality scores,
active-user counts, security guarantees or evidence that every feature works.
The links point to the actual projects and their license/documentation surfaces.

| Tool | Role here | License / cost boundary | Observed GitHub stars |
|---|---|---|---:|
| [uv](https://github.com/astral-sh/uv) | Environment, dependency lock, build runner | MIT or Apache-2.0; local use requires no subscription | 91,924 |
| [Ruff](https://github.com/astral-sh/ruff) | Lint and formatting | MIT; local | 51,202 |
| [ty](https://github.com/astral-sh/ty) | Type checking | MIT; local; upstream labels it beta | 20,062 |
| [pytest](https://github.com/pytest-dev/pytest) | Test execution and fixtures | MIT; local | 14,686 |
| [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) | Parallel test workers | MIT; local | 1,934 |
| [pytest-timeout](https://github.com/pytest-dev/pytest-timeout) | Bound individual tests | MIT; local | 262 |
| [setuptools](https://github.com/pypa/setuptools) | Package build backend | MIT; local | 2,871 |
| [Git](https://github.com/git/git) | Changes, branches and worktrees | GPLv2 tool; running Git does not relicense your repository | 64,273 |

Specialist pytest plugins naturally have smaller audiences than the parent test
framework. Their role, compatibility and direct upstream use are better reasons
for inclusion than demanding equal star counts. ty is included to match the
observed LibreYOLO stack; if maturity becomes more important than matching that
choice, [Pyright](https://github.com/microsoft/pyright) is a separate MIT alternative
(15,743 observed stars), not currently installed here.

The committed `uv.lock` records exact resolved versions. License information
above describes these projects generally; review the actual version and bundled
notices when distributing a product. Direct primary license sources include
[uv's license section](https://github.com/astral-sh/uv#license),
[Git COPYING](https://github.com/git/git/blob/master/COPYING) and
[Pyright LICENSE](https://github.com/microsoft/pyright/blob/main/LICENSE.txt).

## Optional tools and what is actually connected

| Tool | Recommendation | State in this repository | Cost / permission boundary |
|---|---|---|---|
| [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions) | Reuse the same checks in PRs | Workflow files supplied; hosted runs must be checked on the actual pushed revision | Standard public-repository usage and private-repository quotas have different billing rules; do not assume unlimited free private CI |
| [GitHub CLI](https://github.com/cli/cli) | Convenient human-authorized PR operations | Doctor detects presence; no login or GitHub settings setup | MIT CLI, 46,972 stars; GitHub service permissions/plan are separate |
| [Codex CLI](https://github.com/openai/codex) | Optional coding/independent review client | AGENTS and skill-discovery adapter supplied; no model calls configured | Apache-2.0 client; model/service access can require payment or existing entitlement |
| [Claude Code](https://code.claude.com/docs/en/overview) | Optional coding client matching upstream workflow | CLAUDE entry point and discovery adapter supplied | Do not describe it as a free open-source inference service; account/model terms apply |
| [PR-Agent](https://github.com/The-PR-Agent/pr-agent) | First optional AI PR-review candidate for a free-first stack | Not installed or connected | MIT project, 15,965 stars; self-hostable, but hosted models or local inference still consume resources |
| [Greptile](https://www.greptile.com/pricing) | Optional upstream-matching hosted reviewer, not the default | Conservative config example only | Free allowances/qualified OSS offers exist; it is not unrestricted free OSS and may require paid credits |
| [PyTorch](https://github.com/pytorch/pytorch) | Add when implementing actual models | Optional requirements and an unrun synthetic CUDA overfit example | BSD-style license with bundled notices, 105,445 stars; hardware/compute costs remain |
| [Hugging Face Hub library](https://github.com/huggingface/huggingface_hub) | Optional model/data artifact client | Optional requirements only, no account/token/download/upload | Apache-2.0 client, 4,041 stars; hosted storage/compute terms and artifact licenses are separate |
| [Modal](https://modal.com/pricing) | Optional managed GPU CI matching upstream nightly design | Adoption guide only; no account, token, schedule or job | Free compute allotment is bounded; subsequent usage can be billed |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Evaluate only if a separate agent workspace/orchestrator is needed | Not installed; not verified as part of LibreYOLO's committed process | MIT project metadata, 93,271 stars; hosted/enterprise/model offerings have separate terms |

The [PyTorch license file](https://github.com/pytorch/pytorch/blob/main/LICENSE)
contains BSD-style redistribution terms and additional notices. Do not infer a
single blanket right to redistribute every dataset or model weight from it.

### Free alternative to a hosted AI reviewer

Begin with the supplied `REVIEW.md`, reproducible tests and human review: no model
service is required. For automation, PR-Agent is community-maintained and supports
multiple model backends; a local model can avoid a paid API, but still requires
hardware and validation that its review quality is sufficient. Its OSS project is
not the same product as Qodo's commercial platform. See the
[PR-Agent documentation](https://docs.pr-agent.ai/) before choosing deployment,
repository token permissions and data-sharing scope. Nothing is activated here.

Do not silently substitute an external AI reviewer merely because a command is
installed. Repository contents may leave your machine, so confirm destination
and scope first. Reviews are advice, not merge authorization.

## What was deliberately not added

- A second type checker, a second test runner or duplicate formatting hooks.
- A paid reviewer, cloud GPU scheduler, hosted dashboard or secret-bearing MCP
  configuration enabled by default.
- A large agent orchestrator without a demonstrated need.
- Claims that Pi, OpenCode, PR-Agent, OpenHands, Potato or a vector memory system
  were observed as LibreYOLO's actual development stack.
- A claim that running the starter's small test suite validates a real ML model.

This keeps the core cheap and understandable. Add tools only when they close an
observed workflow gap and can be tested in the project's actual environment.

## Evidence and freshness

Popularity snapshots came from the unauthenticated GitHub REST repository
metadata endpoint `https://api.github.com/repos/<owner>/<repo>` for the linked
projects. License conclusions use primary repository metadata/license files.
Prices and quotas are deliberately linked rather than frozen as promises:
[GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions),
[Greptile pricing](https://www.greptile.com/pricing), and
[Modal pricing](https://modal.com/pricing).

Recheck terms and access before enabling a service. Presence on this list is not
an installation, account connection, subscription or endorsement of every feature.
