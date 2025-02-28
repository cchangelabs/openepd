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
from typing import ClassVar

import pydantic

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.enums import SteelComposition
from openepd.model.specs.singular import BaseCompatibilitySpec
from openepd.model.specs.singular.steel import SteelMakingRoute
from openepd.model.standard import Standard
from openepd.model.validation.quantity import PressureMPaStr


class SteelOldOptions(BaseOpenEpdSchema):
    """Legacy Steel options model."""

    cold_finished: bool | None = pydantic.Field(
        default=None,
        description="Cold Finished",
        examples=[True],
    )
    galvanized: bool | None = pydantic.Field(
        default=None,
        description="Galvanized",
        examples=[True],
    )
    epoxy: bool | None = pydantic.Field(
        default=None,
        description="Epoxy Coated",
        examples=[True],
    )
    steel_fabricated: bool | None = pydantic.Field(default=None, examples=[True], description="Fabricated")


class SteelOldSpec(BaseCompatibilitySpec):
    """Legacy Steel spec."""

    COMPATIBILITY_SPECS_KEY_OLD: ClassVar[str] = "steel"
    COMPATIBILITY_SPECS_KEY_NEW: ClassVar[str] = "Steel"
    COMPATIBILITY_MAPPING: ClassVar[dict[str, str]] = {
        "steel.steel_composition": "Steel.composition",
        "steel.Fy": "Steel.yield_tensile_str",
        "steel.making_route": "Steel.making_route",
        "steel.ASTM": "Steel.astm_standards",
        "steel.EN": "Steel.en_standards",
        "steel.SAE": "Steel.sae_standards",
        "steel.options.cold_finished": "Steel.cold_finished",
        "steel.options.galvanized": "Steel.galvanized",
        "steel.options.epoxy": "Steel.RebarSteel.epoxy_coated",  # moved to sub-spec
        "steel.options.steel_fabricated": "Steel.RebarSteel.fabricated",
        # last one is tricky as fabricated might be in multiple cases; thus limited support
    }
    form_factor: str | None = pydantic.Field(default=None, description="Product's form factor, read-only.")
    steel_composition: SteelComposition | None = pydantic.Field(
        default=None,
        description="Basic chemical composition. Generally the ASTM or EN grade is a subcategory of one of these.",
        examples=["Carbon"],
    )
    Fy: PressureMPaStr | None = pydantic.Field(
        default=None,
        description="Minimum Yield Strength",
        examples=["2000 psi"],
    )
    making_route: SteelMakingRoute | None = pydantic.Field(
        default=None, description="List of true/false properties for steelmaking route"
    )
    ASTM: list[Standard] | None = pydantic.Field(
        default=None, description="ASTM standard(s) to which this product complies."
    )
    SAE: list[Standard] | None = pydantic.Field(
        default=None, description="AISA/SAE standard(s) to which this product complies."
    )
    EN: list[Standard] | None = pydantic.Field(default=None, description="EN 10027 number(s).")
    options: SteelOldOptions | None = pydantic.Field(default=None, description="List of true/false properties")
