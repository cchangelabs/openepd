#
#  Copyright 2025 by C Change Labs Inc. www.c-change-labs.com
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CladdingFacingMaterial, CladdingInsulatingMaterial, SidingFormFactor
from openepd.model.validation.quantity import LengthMmStr, LengthMStr, RValueStr, validate_quantity_unit_factory


class AluminiumSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made primarily from aluminium."""

    _EXT_VERSION = "1.0"


class SteelSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made primarily from steel."""

    _EXT_VERSION = "1.0"


class ZincSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made primarily from zinc."""

    _EXT_VERSION = "1.0"


class ShingleAndShakeSidingV1(BaseOpenEpdHierarchicalSpec):
    """Shingle & shake siding."""

    _EXT_VERSION = "1.0"


class MetalSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made of metal such as steel, aluminum, etc."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AluminiumSiding: AluminiumSidingV1 | None = None
    SteelSiding: SteelSidingV1 | None = None
    ZincSiding: ZincSidingV1 | None = None


class CompositionSidingV1(BaseOpenEpdHierarchicalSpec):
    """Composite wood siding composed of wood wafers and resin."""

    _EXT_VERSION = "1.0"


class FiberCementSidingV1(BaseOpenEpdHierarchicalSpec):
    """Composite siding product made of cement and cellulose fibers."""

    _EXT_VERSION = "1.0"


class InsulatedVinylSidingV1(BaseOpenEpdHierarchicalSpec):
    """Vinyl cladding product integrated with manufacturer-installed insulation."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["1 mm"])

    @pydantic.field_validator("thickness", mode="before")
    def _vinyl_siding_thickness_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("m")(cls, value)


class PlywoodSidingV1(BaseOpenEpdHierarchicalSpec):
    """Siding made of plywood boards."""

    _EXT_VERSION = "1.0"


class PolypropyleneSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior wall cladding made from polypropylene, which may contain fillers or reinforcements."""

    _EXT_VERSION = "1.0"


class SolidWoodSidingV1(BaseOpenEpdHierarchicalSpec):
    """Siding products made of wood including shingle & shake siding."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ShingleAndShakeSiding: ShingleAndShakeSidingV1 | None = None


class VinylSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior wall cladding made principally from rigid polyvinyl chloride (PVC)."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["5 mm"])

    @pydantic.field_validator("thickness")
    def _vinyl_siding_thickness_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("m")(cls, value)


class SidingV1(BaseOpenEpdHierarchicalSpec):
    """
    Long narrow products for exterior wall face of building.

    Typically made of, e.g., metal, solid wood, plywood, plastic, composition, fiber cement, etc.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    insulated: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    ventilated: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    paint_or_stain_required: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    r_value: RValueStr | None = pydantic.Field(default=None, description="")
    form_factor: SidingFormFactor | None = pydantic.Field(default=None, description="", examples=["Lap"])

    # Nested specs:
    MetalSiding: MetalSidingV1 | None = None
    CompositionSiding: CompositionSidingV1 | None = None
    FiberCementSiding: FiberCementSidingV1 | None = None
    InsulatedVinylSiding: InsulatedVinylSidingV1 | None = None
    PlywoodSiding: PlywoodSidingV1 | None = None
    PolypropyleneSiding: PolypropyleneSidingV1 | None = None
    SolidWoodSiding: SolidWoodSidingV1 | None = None
    VinylSiding: VinylSidingV1 | None = None


class InsulatedRoofPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Insulated roof panels performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    r_value: RValueStr | None = pydantic.Field(default=None, description="")
    insulating_material: CladdingInsulatingMaterial | None = pydantic.Field(
        default=None, description="", examples=["No Insulation"]
    )


class InsulatedWallPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Insulated wall panels performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    r_value: RValueStr | None = pydantic.Field(default=None, description="")
    insulating_material: CladdingInsulatingMaterial | None = pydantic.Field(
        default=None, description="", examples=["No Insulation"]
    )


class RoofPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Roof panels performance specification."""

    _EXT_VERSION = "1.0"


class StoneCladdingV1(BaseOpenEpdHierarchicalSpec):
    """Stone cladding performance specification."""

    _EXT_VERSION = "1.0"


class WallPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Wall panels performance specification."""

    _EXT_VERSION = "1.0"


class CladdingV1(BaseOpenEpdHierarchicalSpec):
    """Cladding performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])
    facing_material: CladdingFacingMaterial | None = pydantic.Field(default=None, description="", examples=["Steel"])

    @pydantic.field_validator("thickness")
    def _thickness_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("m")(cls, value)

    # Nested specs:
    Siding: SidingV1 | None = None
    InsulatedRoofPanels: InsulatedRoofPanelsV1 | None = None
    InsulatedWallPanels: InsulatedWallPanelsV1 | None = None
    RoofPanels: RoofPanelsV1 | None = None
    StoneCladding: StoneCladdingV1 | None = None
    WallPanels: WallPanelsV1 | None = None
