VIRTUAL_ENV_PATH=venv
SKIP_VENV="${NO_VENV}"
SHELL := /bin/bash
PYTHON := python3.11
SRC_ROOT := ./src
POETRY_GROUPS := dev

.DEFAULT_GOAL := pre_commit

FORMAT_PATH := $(SRC_ROOT)
LINT_PATH := $(SRC_ROOT)
MYPY_PATH := $(SRC_ROOT)

# Helper function to activate virtual environment if not skipped
define activate_venv
  if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi;
endef

pre_commit: pre_commit_hook lint

pre_commit_hook:
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		pre-commit run --all --hook-stage=commit; \
	)

verify-prerequisites:
	@(development/ensure-dependencies.sh)

setup: verify-prerequisites venv deps
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		pre-commit install; \
		echo "Pre-commit hooks installed" \
		echo "DONE: setup" \
	)

deps:
	@( \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		poetry install --all-extras --no-root; \
	)

# Synchronize installed dependencies to match the lock file
.PHONY: deps-sync
deps-sync:
	@( \
		$(call activate_venv) \
		set -e; \
		echo "Syncing dependencies..."; \
		poetry install --all-extras --no-root --sync --with "$(POETRY_GROUPS)"; \
		echo "DONE: all dependencies are synchronized"; \
	)

deps-lock:
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		poetry lock --no-update; \
	)

deps-update:
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		poetry lock; \
	)

.PHONY: venv
venv:
	@( \
	  	set -e; \
		$(PYTHON) -m venv $(VIRTUAL_ENV_PATH); \
		source ./venv/bin/activate; \
	)

copyright:
	@( \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Applying copyright..."; \
       for p in $(FORMAT_PATH); do \
       	 licenseheaders -t ./development/copyright.tmpl -E ".py" -cy -d $$p; \
       done; \
       echo "DISABLED: copyright"; \
    )

.PHONY: ruff-fix-pyupgrade
ruff-fix-pyupgrade:
	@( \
	   $(call activate_venv) \
       echo "Applying pyupgrade..."; \
       ruff check --select UP --fix; \
       echo "DONE: pyupgrade"; \
    )

.PHONY: ruff-fix-pyupgrade-unsafe
ruff-fix-pyupgrade-unsafe:
	@( \
	   $(call activate_venv) \
	   echo "Applying pyupgrade..."; \
	   ruff check --select UP --fix --unsafe-fixes; \
	   echo "DONE: pyupgrade"; \
	)

ruff-format:
	@( \
	   $(call activate_venv) \
	   echo "Running Ruff code formatter..."; \
	   ruff format $(FORMAT_PATH); \
	   echo "DONE: Ruff"; \
	)

ruff-format-check:
	@( \
	   $(call activate_venv) \
	   echo "Running Ruff format check..."; \
	   ruff format --diff $(FORMAT_PATH) || exit 1; \
	   echo "DONE: Ruff"; \
	)

ruff-import-sort:
	@( \
	   $(call activate_venv) \
	   echo "Running Ruff import sort..."; \
	   ruff check --select I --fix; \
	   echo "DONE: Ruff"; \
	)

ruff-import-sort-check:
	@( \
	   $(call activate_venv) \
	   echo "Running Ruff import sort..."; \
	   ruff check --select I || exit 1; \
	   echo "DONE: Ruff"; \
	)

ruff-lint:
	@( \
	   $(call activate_venv) \
	   echo "Running Ruff link..."; \
	   ruff check $(LINT_PATH) || exit 1; \
	   echo "DONE: Ruff"; \
	)

format: ruff-import-sort ruff-format
check-format: ruff-import-sort-check ruff-format-check

mypy:
	@( \
       set -e; \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Running MyPy checks..."; \
       mypy $(MYPY_PATH); \
       echo "DONE: MyPy"; \
    )

lint: ruff-lint mypy check-format

build:
	@( \
		echo "Building packages"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		rm -rf dist/*; \
		poetry build; \
		echo "DONE: Building packages"; \
	)

publish: build
	@( \
		echo "Publishing packages"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		poetry publish; \
		echo "DONE: Publishing packages"; \
	)

test-publish: build
	@( \
		echo "Publishing packages to the TEST PYPI"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		poetry publish -r test-pypi; \
		echo "DONE: Publishing packages (TEST PYPI)"; \
	)

private-publish: build
	@( \
		echo "Publishing packages"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		poetry publish  --repository private; \
		echo "DONE: Publishing packages"; \
	)
coverage:
	@( \
		echo "Running coverage"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		coverage run --source $(SRC_ROOT)/cqd_etl -m pytest; \
		coverage html; \
		echo "DONE: Coverage"; \
	)

test:
	@( \
		echo "Running tests"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		echo pytest -v --cov-report term-missing --cov=$(SRC_ROOT)/cqd_etl; \
		pytest -v; \
		echo "DONE: Tests"; \
	)

changelog:
	@( \
		echo "Generating changelog"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		cz changelog --incremental; \
		echo "DONE: Changelog"; \
	)

print-changelog:
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		cz changelog --dry-run --incremental; \
	)

release:
	@( \
		echo "Preparing release"; \
		set -e; \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		cz bump --yes --changelog; \
		echo "DONE: Preparing release"; \
	)

print-version:
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		cz version --project; \
	)

codegen-internal:
	@( \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Generating code..."; \
       python ./tools/openepd/codegen/generate_geography_enum.py > ./src/openepd/model/geography.py; \
       PYTHONPATH=$PYTHONPATH:./src python ./tools/openepd/codegen/generate_range_spec_models.py openepd.model.specs.singular ./src/openepd/model/specs/range; \
       \
       echo "DONE: Generating code"; \
    )

codegen: codegen-internal isort copyright format
