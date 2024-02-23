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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.standard import Standard
from openepd.model.validation.numbers import RatioFloat


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

    fabricated: bool | None = pyd.Field(default=None, description="Fabricated")


class WireMeshSteelV1(BaseOpenEpdHierarchicalSpec):
    """Spec for wire mesh steel."""

    class Options(BaseOpenEpdSchema, FabricatedOptionsMixin):
        """Wire Mesh Options."""

        pass

    options: Options = pyd.Field(description="Rebar Steel options", default_factory=Options)


class RebarSteelV1(BaseOpenEpdHierarchicalSpec):
    """Rebar steel spec."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema, FabricatedOptionsMixin):
        """Rebar Steel Options."""

        epoxy: bool | None = pyd.Field(default=None, description="Epoxy Coated")

    options: Options = pyd.Field(description="Rebar Steel options", default_factory=Options)


class PlateSteelV1(BaseOpenEpdHierarchicalSpec):
    """Plate Steel Spec."""

    class Options(BaseOpenEpdSchema, FabricatedOptionsMixin):
        """Plate Steel Options."""

        pass

    options: Options = pyd.Field(description="Plate Steel options", default_factory=Options)


class HollowV1(BaseOpenEpdHierarchicalSpec):
    """Hollow Sections Spec."""

    class Options(FabricatedOptionsMixin, BaseOpenEpdSchema):
        """Hollow Sections Options."""

        pass

    options: Options = pyd.Field(description="Hollow Steel options", default_factory=Options)


class HotRolledV1(BaseOpenEpdHierarchicalSpec):
    """Hot Rolled spec."""

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
