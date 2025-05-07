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
__all__ = (
    "AluminiumSidingRangeV1",
    "CladdingRangeV1",
    "CompositionSidingRangeV1",
    "FiberCementSidingRangeV1",
    "InsulatedRoofPanelsRangeV1",
    "InsulatedVinylSidingRangeV1",
    "InsulatedWallPanelsRangeV1",
    "MetalSidingRangeV1",
    "PlywoodSidingRangeV1",
    "PolypropyleneSidingRangeV1",
    "RoofPanelsRangeV1",
    "ShingleAndShakeSidingRangeV1",
    "SidingRangeV1",
    "SolidWoodSidingRangeV1",
    "SteelSidingRangeV1",
    "StoneCladdingRangeV1",
    "VinylSidingRangeV1",
    "WallPanelsRangeV1",
    "ZincSidingRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CladdingFacingMaterial, CladdingInsulatingMaterial, SidingFormFactor
from openepd.model.validation.quantity import AmountRangeLengthMm, AmountRangeRValue


class AluminiumSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exterior siding product made primarily from aluminium.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SteelSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exterior siding product made primarily from steel.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ZincSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exterior siding product made primarily from zinc.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ShingleAndShakeSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Shingle & shake siding.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MetalSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exterior siding product made of metal such as steel, aluminum, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    AluminiumSiding: AluminiumSidingRangeV1 | None = None
    SteelSiding: SteelSidingRangeV1 | None = None
    ZincSiding: ZincSidingRangeV1 | None = None


class CompositionSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Composite wood siding composed of wood wafers and resin.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FiberCementSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Composite siding product made of cement and cellulose fibers.

    Range version.
    """

    _EXT_VERSION = "1.0"


class InsulatedVinylSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Vinyl cladding product integrated with manufacturer-installed insulation.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")


class PlywoodSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Siding made of plywood boards.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PolypropyleneSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exterior wall cladding made from polypropylene, which may contain fillers or reinforcements.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SolidWoodSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Siding products made of wood including shingle & shake siding.

    Range version.
    """

    _EXT_VERSION = "1.0"

    ShingleAndShakeSiding: ShingleAndShakeSidingRangeV1 | None = None


class VinylSidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exterior wall cladding made principally from rigid polyvinyl chloride (PVC).

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")


class SidingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Long narrow products for exterior wall face of building.

    Typically made of, e.g., metal, solid wood, plywood, plastic, composition, fiber cement, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    insulated: bool | None = pyd.Field(default=None, description="")
    ventilated: bool | None = pyd.Field(default=None, description="")
    paint_or_stain_required: bool | None = pyd.Field(default=None, description="")
    r_value: AmountRangeRValue | None = pyd.Field(default=None, description="")
    form_factor: list[SidingFormFactor] | None = pyd.Field(default=None, description="")
    MetalSiding: MetalSidingRangeV1 | None = None
    CompositionSiding: CompositionSidingRangeV1 | None = None
    FiberCementSiding: FiberCementSidingRangeV1 | None = None
    InsulatedVinylSiding: InsulatedVinylSidingRangeV1 | None = None
    PlywoodSiding: PlywoodSidingRangeV1 | None = None
    PolypropyleneSiding: PolypropyleneSidingRangeV1 | None = None
    SolidWoodSiding: SolidWoodSidingRangeV1 | None = None
    VinylSiding: VinylSidingRangeV1 | None = None


class InsulatedRoofPanelsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Insulated roof panels performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

    r_value: AmountRangeRValue | None = pyd.Field(default=None, description="")
    insulating_material: list[CladdingInsulatingMaterial] | None = pyd.Field(default=None, description="")


class InsulatedWallPanelsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Insulated wall panels performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

    r_value: AmountRangeRValue | None = pyd.Field(default=None, description="")
    insulating_material: list[CladdingInsulatingMaterial] | None = pyd.Field(default=None, description="")


class RoofPanelsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Roof panels performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class StoneCladdingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Stone cladding performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WallPanelsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wall panels performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CladdingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cladding performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    facing_material: list[CladdingFacingMaterial] | None = pyd.Field(default=None, description="")
    Siding: SidingRangeV1 | None = None
    InsulatedRoofPanels: InsulatedRoofPanelsRangeV1 | None = None
    InsulatedWallPanels: InsulatedWallPanelsRangeV1 | None = None
    RoofPanels: RoofPanelsRangeV1 | None = None
    StoneCladding: StoneCladdingRangeV1 | None = None
    WallPanels: WallPanelsRangeV1 | None = None
