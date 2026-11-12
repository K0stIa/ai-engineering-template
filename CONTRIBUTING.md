# Contributing

Use Python 3.10 or newer. Install uv, then run `make setup` and `make check`.
Setup installs the frozen dev toolchain from uv.lock. `make smoke` builds and installs a wheel into a
temporary clean environment (build dependencies may require network access).

Edit canonical skills/ and run `make agents-sync`; never edit generated adapters.

Use one branch and one PR per coherent change. Record actual evidence and
limitations using the PR template. Do not copy unrelated LibreYOLO product code.
Follow the authority boundaries in AGENTS.md. Human review owns merge decisions.

For model work, extend docs/testing.md with project-specific datasets, metrics,
thresholds and hardware before implementing acceptance tests. The demo package
proves only that this template builds, installs and runs.
