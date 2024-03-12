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
from enum import StrEnum

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import OpenEPDUnit
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.standard import Standard
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, validate_unit_factory


class SteelMakingRoute(BaseOpenEpdSchema):
    """Steel making route."""

    bof: bool | None = pyd.Field(default=None, description="Basic oxygen furnace")
    eaf: bool | None = pyd.Field(default=None, description="Electric arc furnace")
    ohf: bool | None = pyd.Field(default=None, description="Open hearth furnace")


class SteelComposition(StrEnum):
    """Steel composition enum."""

    CARBON = "Carbon"
    ALLOY = "Alloy"
    STAINLESS = "Stainless"
    TOOL = "Tool"
    OTHER = "Other"


class FabricatedOptionsMixin(pyd.BaseModel):
    """Fabricated options mixin."""

    _EXT_VERSION = "1.0"

    fabricated: bool | None = pyd.Field(default=None, description="Fabricated")


class WireMeshSteelV1(BaseOpenEpdHierarchicalSpec):
    """Spec for wire mesh steel."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema, FabricatedOptionsMixin):
        """Wire Mesh Options."""

        pass

    options: Options = pyd.Field(description="Rebar Steel options", default_factory=Options)


class RebarGrade(StrEnum):
    """Rebar grade enum."""

    USA_60_KSI = "60 ksi"
    USA_75_KIS = "75 ksi"
    USA_80_KSI = "80 ksi"
    USA_90_KSI = "90 ksi"
    USA_100_KSI = "100 ksi"
    USA_120_KSI = "120 ksi"
    USA_40_KSI = "40 ksi"
    USA_50_KSI = "50 ksi"

    METRIC_420_MPA = "420 Mpa"
    METRIC_520_MPA = "520 Mpa"
    METRIC_550_MPA = "550 Mpa"
    METRIC_620_MPA = "620 Mpa"
    METRIC_690_MPA = "690 MPa"
    METRIC_830_MPA = "830 Mpa"
    METRIC_280_MPA = "280 MPa"
    METRIC_350_MPA = "350 Mpa"


class RebarSteelV1(BaseOpenEpdHierarchicalSpec):
    """Rebar steel spec."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema, FabricatedOptionsMixin):
        """Rebar Steel Options."""

        epoxy: bool | None = pyd.Field(default=None, description="Epoxy Coated")

    options: Options = pyd.Field(description="Rebar Steel options", default_factory=Options)

    steel_rebar_grade: RebarGrade | None = pyd.Field(default=None, description="Rebar steel grade")
    steel_rebar_diameter_min: LengthMmStr | None = pyd.Field(default=None, description="Minimum rebar diameter")
    _steel_rebar_diameter_min = pyd.validator("steel_rebar_diameter_min", allow_reuse=True)(
        validate_unit_factory(OpenEPDUnit.m)
    )

    steel_rebar_bending_pin_max: float | None = pyd.Field(
        default=None, description="Maximum rebar bending pin in diameters of this rebar", example=6.2
    )
    steel_rebar_ts_ys_ratio_max: float | None = pyd.Field(
        default=None, description="Max ratio of ultimate tensile to yield tensile strength"
    )


class PlateSteelV1(BaseOpenEpdHierarchicalSpec):
    """Plate Steel Spec."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema, FabricatedOptionsMixin):
        """Plate Steel Options."""

        pass

    options: Options = pyd.Field(description="Plate Steel options", default_factory=Options)


class HollowV1(BaseOpenEpdHierarchicalSpec):
    """Hollow Sections Spec."""

    _EXT_VERSION = "1.0"

    class Options(FabricatedOptionsMixin, BaseOpenEpdSchema):
        """Hollow Sections Options."""

        pass

    options: Options = pyd.Field(description="Hollow Steel options", default_factory=Options)


class HotRolledV1(BaseOpenEpdHierarchicalSpec):
    """Hot Rolled spec."""

    _EXT_VERSION = "1.0"

    class Options(FabricatedOptionsMixin, BaseOpenEpdSchema):
        """Hot Rolled options."""

        pass

    options: Options = pyd.Field(description="Hollow Steel options", default_factory=Options)


class SteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel spec."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema):
        """Steel spec options."""

        galvanized: bool | None = pyd.Field(default=None, description="Galvanized")
        cold_finished: bool | None = pyd.Field(default=None, description="Cold Finished")

    form_factor: str | None = pyd.Field(description="Product's form factor", example="Steel >> RebarSteel")
    steel_composition: SteelComposition | None = pyd.Field(default=None, description="Basic chemical composition")
    recycled_content: RatioFloat | None = pyd.Field(
        default=None,
        example=0.3,
        description="Scrap steel inputs from other processes.  Includes "
        "Post-Consumer content, if any.  This percentage may be "
        "used to evaluate the EPD w.r.t. targets or limits that are"
        " different for primary and recycled content.",
    )
    ASTM: list[Standard] = pyd.Field(description="ASTM standard to which this product complies", default_factory=list)
    SAE: list[Standard] = pyd.Field(
        description="AISA/SAE standard to which this product complies", default_factory=list
    )
    EN: list[Standard] = pyd.Field(description="EN 10027 number(s)", default_factory=list)

    options: Options | None = pyd.Field(description="Steel options", default_factory=Options)
    making_route: SteelMakingRoute | None = pyd.Field(default=None, description="Steel making route")

    # Nested specs

    WireMeshSteel: WireMeshSteelV1 | None = None
    RebarSteel: RebarSteelV1 | None = None
    PlateSteel: PlateSteelV1 | None = None
    Hollow: HollowV1 | None = None
    HotRolled: HotRolledV1 | None = None
