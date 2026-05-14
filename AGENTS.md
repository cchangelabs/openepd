# AGENTS.md — AI Coding Agent Guide for openepd

## Project Overview

Python library (v7.x, Pydantic v2) for the [openEPD](https://www.buildingtransparency.org/programs/openepd/) data
format — Environmental Product Declarations for building materials. Provides Pydantic models, an API client, a bundle
format, and a hierarchical category system.

## Architecture

- **`src/openepd/model/`** — Pydantic data models. All models inherit from `BaseOpenEpdSchema` (in `model/base.py`),
  which extends `pydantic.BaseModel` with `to_serializable()`, `to_json()`, `to_dict()`, and `revalidate()`. Key domain
  models: `Epd`, `Pcr`, `Org`, `Plant`, `Standard`, `GenericEstimate`, `IndustryEpd`.
- **`src/openepd/model/specs/`** — Material extension specs in two parallel trees:
    - `specs/singular/` — Per-EPD specs (e.g., `SteelV1`). Inherit `BaseOpenEpdHierarchicalSpec`, must declare
      `_EXT_VERSION` and `_CATEGORY_META`.
    - `specs/range/` — **Auto-generated** from singular specs via `make codegen`. Do NOT edit these by hand.
    - See `src/openepd/model/specs/README.md` for type-mapping rules and `CodegenSpec` annotation overrides.
- **`src/openepd/api/`** — Sync HTTP API client. `SyncHttpClient` (base_sync_client.py) wraps `requests` with
  retry/throttle. Domain APIs (e.g., `EpdApi`, `PcrApi`) are `BaseApiMethodGroup` subclasses, lazily instantiated via
  properties on `OpenEpdApiClientSync`.
- **`src/openepd/bundle/`** — Read/write `.epb` bundle files containing multiple openEPD objects + related blobs.
- **`src/openepd/category/`** — Hierarchical category tree. `generated.py` is **auto-generated** — use
  `make codegen-category-tree`.
- **`src/openepd/model/validation/`** — Custom Pydantic validators for quantities, enums, numbers.
- **`src/openepd/model/geography.py`** — **Auto-generated** geography enum. Use `make codegen`.

## Key Commands

```bash
make setup          # Create venv, install deps, set up pre-commit hooks
make test           # Run ALL tests with pytest (discovered from src/, files named test_*.py)
make lint           # Run ruff lint + mypy + format check
make format         # Auto-format with ruff (import sort + formatter)
make codegen        # Regenerate geography enum + range specs, then apply copyright + format
make codegen-category-tree  # Regenerate category tree module
```

**Testing workflow**: After making changes, first run only the specific test file related to the change to verify it
works (e.g., `pytest src/openepd/model/tests/test_epd.py -v`). Once the targeted test passes, run the full suite with
`make test` to check for regressions.

## Conventions & Patterns

- **Line length**: 120 characters (enforced by Ruff in the standard workflow).
- **Python version**: 3.11+ only. Use modern type hints (`list[str]`, `str | None`, not `Optional`/`List`).
- **Tests**: Co-located with source under `src/`, e.g., `src/openepd/model/tests/test_epd.py`. Write all tests using
  the `unittest` framework and `unittest.TestCase` classes (do not use other test frameworks). Tests must be executed
  with `pytest` (via `make test`) for convenience, but test implementations must use `unittest` conventions. Test files
  are excluded from the published package.
- **Spec naming**: `{SpecName}V{major}` for singular, `{SpecName}RangeV{major}` for range. Each spec class requires
  `_EXT_VERSION = "X.Y"` and `_CATEGORY_META = CategoryMeta(...)`.
- **Serialization defaults**: `exclude_none=True`, `exclude_unset=True`, `by_alias=True` — set in
  `BaseOpenEpdSchema.to_serializable()`.
- **API method groups**: Each domain (epd, pcr, org, etc.) lives in `api/{domain}/sync_api.py` and extends
  `BaseApiMethodGroup`. Add new domain APIs as properties on `OpenEpdApiClientSync`.
- **Commit messages**: Follow [Conventional Commits](https://www.conventionalcommits.org/) — version bumps are automated
  via `commitizen`.
- **Copyright header**: All `.py` files must have the Apache 2.0 header (applied via `make copyright`).
- **Generated files — do not edit manually**: `model/geography.py`, `model/specs/range/*.py`, `category/generated.py`.
