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
from typing import ClassVar, Literal

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.concrete import Cementitious, ConcreteTypicalApplication
from openepd.model.specs.enums import AciExposureClass, CsaExposureClass, EnExposureClass
from openepd.model.specs.singular import BaseCompatibilitySpec
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthInchStr, PressureMPaStr


class ConcreteOptions(BaseOpenEpdSchema):
    """Legacy Concrete options model."""

    lightweight: bool | None = pyd.Field(
        default=None, description="Lightweight. True if < 120lb/ft3 or 1900 kg/m3", example=True
    )
    scc: bool | None = pyd.Field(default=None, description="Self Compacting", example=True)
    finishable: bool | None = pyd.Field(default=None, description="Finishable", example=True)
    air: bool | None = pyd.Field(default=None, description="Air Entrainment", example=True)
    co2_entrain: bool | None = pyd.Field(
        default=None, description="CO2 Curing. Uses intentionally entrained CO2.", example=True
    )
    white_cement: bool | None = pyd.Field(default=None, description="White Cement", example=True)
    plc: bool | None = pyd.Field(default=None, description="Portland Limestone Cement", example=True)
    fiber_reinforced: bool | None = pyd.Field(default=None, description="fiber_reinforced", example=True)


class ConcreteOldSpec(BaseCompatibilitySpec):
    """Old version of the Concrete spec, please use Concrete hierarchical version instead."""

    COMPATIBILITY_SPECS_KEY_OLD: ClassVar[str] = "concrete"
    COMPATIBILITY_SPECS_KEY_NEW: ClassVar[str] = "Concrete"
    COMPATIBILITY_MAPPING: ClassVar[dict[str, str]] = {
        "concrete.strength_28d": "Concrete.strength_28d",
        "concrete.slump": "Concrete.min_slump",
        "concrete.strength_other": "Concrete.strength_other",
        "concrete.strength_other_d": "Concrete.strength_other_d",
        "concrete.w_c_ratio": "Concrete.w_c_ratio",
        "concrete.aci_exposure_classes": "Concrete.aci_exposure_classes",
        "concrete.csa_exposure_classes": "Concrete.csa_exposure_classes",
        "concrete.en_exposure_classes": "Concrete.en_exposure_classes",
        "concrete.application": "Concrete.typical_application",
        "concrete.options.lightweight": "Concrete.lightweight",
        "concrete.options.scc": "Concrete.self_consolidating",
        "concrete.options.finishable": "Concrete.finishable",
        "concrete.options.air": "Concrete.air_entrain",
        "concrete.options.co2_entrain": "Concrete.co2_entrain",
        "concrete.options.white_cement": "Concrete.white_cement",
        "concrete.options.plc": "Concrete.plc",
        "concrete.options.fiber_reinforced": "Concrete.fiber_reinforced",
        "concrete.cementitious": "Concrete.cementitious",
    }

    strength_28d: PressureMPaStr | None = pyd.Field(
        default=None, description="Compressive Strength at 28 days", example="1 MPa"
    )
    slump: LengthInchStr | None = pyd.Field(default=None, description="Minimum test slump", example="2 in")
    strength_other: PressureMPaStr | None = pyd.Field(
        default=None,
        description="One additional strength, which can be early (e.g. 3d) or late (e.g. 96d)",
        example="30 MPa",
    )
    strength_other_d: Literal[3, 7, 14, 42, 56, 72, 96, 120] | None = pyd.Field(
        default=None,
        description="Days for the strength field above. Required IF strength_other is provided.",
        example=42,
    )
    w_c_ratio: RatioFloat | None = pyd.Field(
        default=None, description="Ratio of water to cement", example=0.5, ge=0, le=1
    )
    aci_exposure_classes: list[AciExposureClass] | None = pyd.Field(
        default=None, description="List of ACI318-19 exposure classes this product meets", example=["aci.F0"]
    )
    csa_exposure_classes: list[CsaExposureClass] | None = pyd.Field(
        default=None, description="List of CSA A23.1 exposure classes this product meets", example=["csa.C-2"]
    )
    en_exposure_classes: list[EnExposureClass] | None = pyd.Field(
        default=None, description="List of EN206 exposure classes this product meets", example=["en206.X0"]
    )
    application: ConcreteTypicalApplication | None = pyd.Field(default=None, description="Typical Application")
    options: ConcreteOptions | None = pyd.Field(default=None, description="List of true/false properties")
    cementitious: Cementitious | None = pyd.Field(
        default=None, description="List of cementitious materials, and proportion by mass"
    )
