---
name: adding-new-openepd-categories
description: "Adding new categories to OpenEPD repository"
---

# Adding new categories skill

Use this skill when tasked with adding new category to OpenEPD repository.

1. Extend `spec_maping` to the correct place in the project hierarchy. Search for `src.openepd.model.specs.singular` and `src.openepd.model.specs.range` folders.
2. Add a new spec material types there. Name it after `db_name` of the category. For example, if you have `DoorsAndFrames` category, add next specifications: `DoorsAndFramesV1` into `singular` folder and `DoorsAndFramesRangeV1` into `range` folder. This classes should be a child of `BaseOpenEpdHierarchicalSpec` class.
3. Add `_EXT_VERSION` . The newly created V1 category should be `1.0`.
4. Add `_CATEGORY_META` .
```python
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.category import CategoryMeta

class DoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """Doors (the operable part) and frames (what holds the door proper)."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="DoorsAndFrames",
        display_name="Doors and Frames",
        historical_names=["Openings >> Doors and Frames"],
        description="Doors (the operable part) and frames (what holds the door proper)",
        masterformat="08 10 00 Doors and Frames",
        declared_unit=Amount(qty=1, unit="item"),
    )
```
5. Add the specification as a child of its parent specification. If the parent spec already exists, bump its minor 
version; no version bump is needed when adding both the parent and child in the same change.
    
```python
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

class WoodDoorsV1(BaseOpenEpdHierarchicalSpec):
  """Wood doors performance specification."""

  _EXT_VERSION = "1.0"

class DoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
  """Doors (the operable part) and frames (what holds the door proper)."""

  _EXT_VERSION = "1.1"
  
  WoodDoors: WoodDoorsV1 | None = None
``` 
    
```python
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

class WoodDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wood doors performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

class DoorsAndFramesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Doors (the operable part) and frames (what holds the door proper).

    Range version.
    """

    _EXT_VERSION = "1.1"

    WoodDoors: WoodDoorsRangeV1 | None = None
```
    
6. Add properties to a specification. Declare them as pydantic fields. Use semantic types for material properties - see 
`LengthMmStr` vs `LengthInchStr`. If needed, add more semantic types like these. 
7. Add accurate documentation, realistic example, etc. Example:
    
```python
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import LengthMmStr

class DoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
  """Doors (the operable part) and frames (what holds the door proper)."""

  _EXT_VERSION = "1.1"

  # Own fields:
  height: LengthMmStr | None = pyd.Field(default=None, example="1200 mm")
  width: LengthMmStr | None = pyd.Field(default=None, example="600 mm")

  # Nested specs:
  WoodDoors: WoodDoorsV1 | None = None
```
    
```python
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import AmountRangeLengthMm

class DoorsAndFramesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Doors (the operable part) and frames (what holds the door proper).

    Range version.
    """

    _EXT_VERSION = "1.0"

    height: AmountRangeLengthMm | None = pyd.Field(default=None)
    width: AmountRangeLengthMm | None = pyd.Field(default=None)
    
    # Nested specs:
    WoodDoors: WoodDoorsRangeV1 | None = None
```
    
8. For semantic groups of properties, extract them into the separate sub-object. For example, concrete model has 
`typical_application_vrt` , `typical_application_hrz` and so on boolean flags, but openepd model has 
`typical_application: TypicalApplication` which is a separate sub-object.
9. Run `make codegen-category-tree` to generate the category tree. 
Check that the new category is present in `src/openepd/category/generated.py` 