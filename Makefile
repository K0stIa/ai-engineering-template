UV ?= uv
RUN := $(UV) run --no-sync
WORKERS ?= 2
.PHONY: setup test test-pr test-gpu check smoke lint format typecheck agents-sync agents-check doctor build
setup:
	$(UV) sync --frozen --dev
agents-sync:
	$(RUN) python scripts/sync_skills.py
agents-check:
	$(RUN) python scripts/sync_skills.py --check
doctor:
	$(RUN) python scripts/stack_doctor.py --json
format:
	$(RUN) ruff format src scripts tests
lint:
	$(RUN) ruff check src scripts tests
	$(RUN) ruff format --check src scripts tests
typecheck:
	$(RUN) ty check src scripts
# CI and local checks share one command. Expensive/unavailable tiers are explicit.
test: test-pr
test-pr:
	AI_PROJECT_PR_GATE=1 $(RUN) pytest tests -m "not network and not external_data and not gpu and not integration" -n $(WORKERS) --dist loadfile --junitxml=artifacts/pr-tests.xml
test-gpu:
	$(RUN) pytest tests/e2e -m gpu --timeout=300 --junitxml=artifacts/gpu-tests.xml
check: agents-check lint typecheck test-pr
smoke:
	$(RUN) python scripts/install_smoke.py
build:
	$(UV) build
