#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CladdingFacingMaterial, CladdingInsulatingMaterial, SidingFormFactor
from openepd.model.validation.quantity import LengthMmStr, LengthMStr, RValueStr, validate_quantity_unit_factory


class AluminiumSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made primarily from aluminium."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AluminiumSiding",
        display_name="Aluminium Siding",
        short_name="Aluminium",
        historical_names=["Cladding >> Siding >> Metal >> Aluminium"],
        description="Exterior siding product made primarily from aluminium.",
        masterformat="07 46 16 Aluminum Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SteelSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made primarily from steel."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SteelSiding",
        display_name="Steel Siding",
        short_name="Steel",
        historical_names=["Cladding >> Siding >> Metal >> Steel"],
        description="Exterior siding product made primarily from steel.",
        masterformat="07 46 19 Steel Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class ZincSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made primarily from zinc."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ZincSiding",
        display_name="Zinc Siding",
        short_name="Zinc",
        historical_names=["Cladding >> Siding >> Metal >> Zinc"],
        description="Exterior siding product made primarily from zinc.",
        masterformat="07 46 21 Zinc Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class ShingleAndShakeSidingV1(BaseOpenEpdHierarchicalSpec):
    """Shingle & shake siding."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ShingleAndShakeSiding",
        display_name="Shingle and Shake Siding",
        short_name="Shingle and Shake",
        historical_names=["Cladding >> Siding >> Solid Wood >> Shingle and Shake"],
        description="Shingle & shake siding.",
        masterformat="07 46 24 Wood Shingle and Shake Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class MetalSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior siding product made of metal such as steel, aluminum, etc."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MetalSiding",
        display_name="Metal Siding",
        short_name="Metal",
        historical_names=["Cladding >> Siding >> Metal"],
        description="Exterior siding product made of metal such as steel, aluminum, etc.",
        masterformat="07 46 00 Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Nested specs:
    AluminiumSiding: AluminiumSidingV1 | None = None
    SteelSiding: SteelSidingV1 | None = None
    ZincSiding: ZincSidingV1 | None = None


class CompositionSidingV1(BaseOpenEpdHierarchicalSpec):
    """Composite wood siding composed of wood wafers and resin."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CompositionSiding",
        display_name="Composition Siding",
        short_name="Composition",
        historical_names=["Cladding >> Siding >> Composition"],
        description="Composite wood siding composed of wood wafers and resin.",
        masterformat="07 46 43 Composition Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class FiberCementSidingV1(BaseOpenEpdHierarchicalSpec):
    """Composite siding product made of cement and cellulose fibers."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FiberCementSiding",
        display_name="Fiber-cement Siding",
        short_name="Fiber-cement",
        historical_names=["Cladding >> Siding >> Fiber-cement"],
        description="Composite siding product made of cement and cellulose fibers.",
        masterformat="07 46 46 Fiber-Cement Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class InsulatedVinylSidingV1(BaseOpenEpdHierarchicalSpec):
    """Vinyl cladding product integrated with manufacturer-installed insulation."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="InsulatedVinylSiding",
        display_name="Insulated Siding",
        short_name="Insulated Vinyl",
        historical_names=["Cladding >> Siding >> Insulated Vinyl"],
        description="Vinyl cladding product integrated with manufacturer-installed insulation.",
        masterformat="07 46 00 Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["1 mm"])

    @pydantic.field_validator("thickness", mode="before")
    def _vinyl_siding_thickness_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("m")(cls, value)


class PlywoodSidingV1(BaseOpenEpdHierarchicalSpec):
    """Siding made of plywood boards."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PlywoodSiding",
        display_name="Plywood Siding",
        short_name="Plywood",
        historical_names=["Cladding >> Siding >> Plywood"],
        description="Siding made of plywood boards.",
        masterformat="07 46 29 Plywood Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class PolypropyleneSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior wall cladding made from polypropylene, which may contain fillers or reinforcements."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PolypropyleneSiding",
        display_name="Polypropylene Siding",
        short_name="Polypropylene",
        historical_names=["Cladding >> Siding >> Polypropylene"],
        description="Exterior wall cladding made from polypropylene, which may contain fillers or reinforcements.",
        masterformat="07 46 00 Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SolidWoodSidingV1(BaseOpenEpdHierarchicalSpec):
    """Siding products made of wood including shingle & shake siding."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SolidWoodSiding",
        display_name="Solid Wood Siding",
        short_name="Solid Wood",
        historical_names=["Cladding >> Siding >> Solid Wood"],
        description="Siding products made of wood including shingle & shake siding.",
        masterformat="07 46 23 Wood Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Nested specs:
    ShingleAndShakeSiding: ShingleAndShakeSidingV1 | None = None


class VinylSidingV1(BaseOpenEpdHierarchicalSpec):
    """Exterior wall cladding made principally from rigid polyvinyl chloride (PVC)."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="VinylSiding",
        display_name="Vinyl Siding",
        short_name="Vinyl",
        historical_names=["Cladding >> Siding >> Vinyl"],
        description="Exterior wall cladding made principally from rigid polyvinyl chloride (PVC).",
        masterformat="07 46 00 Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="Siding",
        display_name="Siding",
        alt_names=["Rainscreen", "Shingle", "Shakes", "Residential Siding", "Facade", "HPL Boards"],
        description="Long narrow products for exterior wall face of building, made of, e.g., metal, solid wood, plywood, plastic, composition, fiber cement, etc.",
        masterformat="07 46 00 Siding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="InsulatedRoofPanels",
        display_name="Insulated Roof Panels",
        historical_names=["Cladding >> Insulated Roof Panels"],
        description="Insulated metal panel (IMP) for roof applications",
        masterformat="07 41 00 Roof Panels",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    r_value: RValueStr | None = pydantic.Field(default=None, description="")
    insulating_material: CladdingInsulatingMaterial | None = pydantic.Field(
        default=None, description="", examples=["No Insulation"]
    )


class InsulatedWallPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Insulated wall panels performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="InsulatedWallPanels",
        display_name="Insulated Wall Panels",
        alt_names=["Metal Composite Panels", "Insulated Panel", "Structural Insulated Panel", "Wall Panel System"],
        historical_names=["Cladding >> Insulated Wall Panels"],
        description="Insulated metal panel (IMP) for exterior wall applications",
        masterformat="07 42 00 Wall Panels",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    r_value: RValueStr | None = pydantic.Field(default=None, description="")
    insulating_material: CladdingInsulatingMaterial | None = pydantic.Field(
        default=None, description="", examples=["No Insulation"]
    )


class RoofPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Roof panels performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="RoofPanels",
        display_name="Roof Panels",
        historical_names=["Cladding >> Roof Panels"],
        description="Solid roofing panels for exterior face of building, made typically of metal, wood, plastic, or composite materials",
        masterformat="07 41 00 Roof Panels",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class StoneCladdingV1(BaseOpenEpdHierarchicalSpec):
    """Stone cladding performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="StoneCladding",
        display_name="Stone Cladding",
        alt_names=["Exterior Stone Cladding"],
        historical_names=["Cladding >> Stone Cladding"],
        description="Exterior stone cladding supported by masonry, steel studs, or other support system",
        masterformat="04 42 00 Stone Cladding",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class WallPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Wall panels performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WallPanels",
        display_name="Wall Panels",
        alt_names=["Metal Cladding"],
        historical_names=["Cladding >> Wall Panels"],
        description="Solid panels for exterior wall face of building, made of, e.g., metal, wood, tile, terra cotta, cementitious materials, or composite materials",
        masterformat="07 42 00 Wall Panels",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class CladdingV1(BaseOpenEpdHierarchicalSpec):
    """Cladding performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Cladding",
        display_name="Cladding",
        alt_names=["Panels"],
        description="Nonstructural materials used primarily on the outside of buildings",
        masterformat="07 40 00 Roofing and Siding Panels",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

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
