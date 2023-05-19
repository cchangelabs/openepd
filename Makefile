VIRTUAL_ENV_PATH=venv
SKIP_VENV="${NO_VENV}"
SHELL := /bin/bash
PYTHON := python3.11
SRC_ROOT := ./src

.DEFAULT_GOAL := pre_commit

FORMAT_PATH := $(SRC_ROOT)
LINT_PATH := $(SRC_ROOT)
MYPY_PATH := $(SRC_ROOT)

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
		$(PYTHON) -m pip install -r ./requirements-dev.txt; \
		poetry install --all-extras; \
	)

deps-lock:
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

black:
	@( \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Running Black code formatter..."; \
       black $(FORMAT_PATH); \
       \
       echo "DONE: Black"; \
    )

black-check:
	@( \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       set -e; \
       echo "Running Black format check..."; \
       black --check $(FORMAT_PATH); \
       \
       echo "DONE: Black format check"; \
    )

isort:
	@( \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Running isort formatter..."; \
       isort $(FORMAT_PATH); \
       \
       echo "DONE: isort formatter"; \
    )

isort-check:
	@( \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       set -e; \
       echo "Running isort validation..."; \
       isort --check $(FORMAT_PATH); \
       \
       echo "DONE: isort validation"; \
    )

format: isort black
check-format: isort-check black-check

flake8:
	@( \
       set -e; \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Running Flake8 checks..."; \
       flake8 $(LINT_PATH) --count --statistics; \
       echo "DONE: Flake8"; \
    )

mypy:
	@( \
       set -e; \
       if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
       echo "Running MyPy checks..."; \
       mypy $(MYPY_PATH); \
       echo "DONE: MyPy"; \
    )

lint: flake8 mypy check-format

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
		poetry publish -r ec3; \
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
		cz bump --changelog; \
		echo "DONE: Preparing release"; \
	)

print-version:
	@( \
		if [ -z $(SKIP_VENV) ]; then source $(VIRTUAL_ENV_PATH)/bin/activate; fi; \
		cz version --project; \
	)
