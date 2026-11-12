# Test tiers and evidence

## Implemented starter checks

`make check` verifies skill-discovery mirrors, runs Ruff and ty, then runs
pytest with xdist (two workers) and 60-second per-test timeouts. The PR gate
excludes explicit network, external_data, gpu and integration markers. Its
autouse socket guard prevents external in-process connections; it is not an OS
sandbox and does not intercept networking in arbitrary spawned subprocesses.
CI isolation remains necessary for untrusted code. `make smoke` builds a
wheel, installs it in a fresh temporary venv and invokes its console entry point
from outside the checkout. These do not test ML models. `make test-gpu` explicitly selects the optional
synthetic CUDA overfit example, which fails if dependencies/hardware are absent.
It was not executed during core validation.

## Recommended ML project additions (not implemented here)

| Tier | Evidence | Must define before running |
|---|---|---|
| Dataset contract | shapes, labels, splits, leakage, invalid samples | schema and split identity |
| Architecture | output shape, finite loss/gradients, parameter invariants | supported inputs and expected invariants |
| Single-batch overfit | actual loss/metric improvement | seed, batch, budget, threshold |
| Learning smoke | tiny real training run outperforms baseline | dataset digest, baseline, tolerance |
| Numerical parity | reference implementation or checkpoint outputs | upstream revision and tolerances |
| Export/runtime | exported model executes representative inputs | backend/version/hardware |
| Performance | latency/memory/accuracy | warmup, percentiles, batch and device |
| Release | clean install, upgrade/rollback, actual user path | immutable build and reviewer |

Record command, exit code, selected/passed/failed/skipped counts, code revision,
dirty-tree changes, seed, hardware and relevant dataset/model hashes. Never call
an unexecuted tier passing. Use synthetic fixtures for fast PR gates and separately
provision costly real-model runs. This matrix extends the observed upstream
patterns; it is a recommendation, not proof LibreYOLO implements every row.
