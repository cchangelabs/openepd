#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import LengthMStr, validate_unit_factory

from .enums import *

UnknownStrTypeHandleMe = str


class AluminiumSidingV1(BaseOpenEpdHierarchicalSpec):
    """Aluminium siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class SteelSidingV1(BaseOpenEpdHierarchicalSpec):
    """Steel siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class ZincSidingV1(BaseOpenEpdHierarchicalSpec):
    """Zinc siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class ShingleAndShakeSidingV1(BaseOpenEpdHierarchicalSpec):
    """Shingle and shake siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class MetalSidingV1(BaseOpenEpdHierarchicalSpec):
    """Metal siding performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AluminiumSiding: AluminiumSidingV1 | None = None
    SteelSiding: SteelSidingV1 | None = None
    ZincSiding: ZincSidingV1 | None = None


class CompositionSidingV1(BaseOpenEpdHierarchicalSpec):
    """Composition siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class FiberCementSidingV1(BaseOpenEpdHierarchicalSpec):
    """Fiber cement siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class InsulatedVinylSidingV1(BaseOpenEpdHierarchicalSpec):
    """Insulated vinyl siding performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    vinyl_siding_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _vinyl_siding_thickness_is_quantity_validator = pyd.validator("vinyl_siding_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class PlywoodSidingV1(BaseOpenEpdHierarchicalSpec):
    """Plywood siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class PolypropyleneSidingV1(BaseOpenEpdHierarchicalSpec):
    """Polypropylene siding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class SolidWoodSidingV1(BaseOpenEpdHierarchicalSpec):
    """Solid wood siding performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ShingleAndShakeSiding: ShingleAndShakeSidingV1 | None = None


class VinylSidingV1(BaseOpenEpdHierarchicalSpec):
    """Vinyl siding performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    vinyl_siding_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _vinyl_siding_thickness_is_quantity_validator = pyd.validator("vinyl_siding_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class SidingV1(BaseOpenEpdHierarchicalSpec):
    """Siding performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    siding_insulated: bool | None = pyd.Field(default=None, description="", example="True")
    siding_ventilated: bool | None = pyd.Field(default=None, description="", example="True")
    siding_paint_or_stain_required: bool | None = pyd.Field(default=None, description="", example="True")
    siding_r_value: str | None = pyd.Field(default=None, description="", example="1 K * m2 / W")
    siding_form_factor: SidingFormFactor | None = pyd.Field(default=None, description="", example="Lap")

    _siding_r_value_is_quantity_validator = pyd.validator("siding_r_value", allow_reuse=True)(
        validate_unit_factory("K * m2 / W")
    )

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
    cladding_r_value: str | None = pyd.Field(default=None, description="", example="1 K * m2 / W")
    cladding_insulating_material: CladdingInsulatingMaterial | None = pyd.Field(
        default=None, description="", example="No Insulation"
    )

    _cladding_r_value_is_quantity_validator = pyd.validator("cladding_r_value", allow_reuse=True)(
        validate_unit_factory("K * m2 / W")
    )


class InsulatedWallPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Insulated wall panels performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cladding_r_value: str | None = pyd.Field(default=None, description="", example="1 K * m2 / W")
    cladding_insulating_material: CladdingInsulatingMaterial | None = pyd.Field(
        default=None, description="", example="No Insulation"
    )

    _cladding_r_value_is_quantity_validator = pyd.validator("cladding_r_value", allow_reuse=True)(
        validate_unit_factory("K * m2 / W")
    )


class RoofPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Roof panels performance specification."""

    _EXT_VERSION = "1.0"

    pass


class StoneCladdingV1(BaseOpenEpdHierarchicalSpec):
    """Stone cladding performance specification."""

    _EXT_VERSION = "1.0"

    pass


class WallPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Wall panels performance specification."""

    _EXT_VERSION = "1.0"

    pass


class CladdingV1(BaseOpenEpdHierarchicalSpec):
    """Cladding performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    cladding_facing_material: CladdingFacingMaterial | None = pyd.Field(default=None, description="", example="Steel")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))

    # Nested specs:
    Siding: SidingV1 | None = None
    InsulatedRoofPanels: InsulatedRoofPanelsV1 | None = None
    InsulatedWallPanels: InsulatedWallPanelsV1 | None = None
    RoofPanels: RoofPanelsV1 | None = None
    StoneCladding: StoneCladdingV1 | None = None
    WallPanels: WallPanelsV1 | None = None
