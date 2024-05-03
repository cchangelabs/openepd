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
from typing import Literal

from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.concrete import Cementitious, ConcreteTypicalApplication
from openepd.model.specs.generated.enums import AciExposureClass, CsaExposureClass, EnExposureClass
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import (
    LengthInchStr,
    LengthMmStr,
    MassKgStr,
    PressureMPaStr,
    validate_unit_factory,
)


class CementGroutV1(BaseOpenEpdHierarchicalSpec):
    """
    Cement grout performance specification.

    Cement grouting is a slurry that is placed as a flowable liquid. It is an effective material
    for filling and strengthening granular soils, voids in rocks, foundation underpinnings, and
    other underground voids. Also called structural grout, these materials typically impart
    significant compressive strength to the system.
    """

    _EXT_VERSION = "1.0"


class ConcretePavingV1(BaseOpenEpdHierarchicalSpec):
    """Concrete paving."""

    _EXT_VERSION = "1.0"

    # Own fields:
    flexion_strength: PressureMPaStr | None = pyd.Field(
        default=None, description="Concrete flexural strength.", example="30 MPa"
    )

    _concrete_flexion_strength_is_quantity_validator = pyd.validator("flexion_strength", allow_reuse=True)(
        validate_unit_factory("MPa")
    )


class FlowableFillV1(BaseOpenEpdHierarchicalSpec):
    """
    Flowable fill performance specification.

    Flowable fill is a slurry that is placed as a flowable liquid (high slump) and sets with no
    compaction. It is often used in tight or restricted access areas where placing and compacting
    fill is difficult. Applications include filling large voids such as abandoned underground storage
    tanks, basements, tunnels, mines, and sewers. It can also be used as paving sub-base, bridge
    abutment, and retaining wall backfill.

    Also called Controlled Density Fill (CDF) or Controlled Low Strength Materials (CLSMs). These materials typically
    have compressive strengths under 1200 psi.
    """

    _EXT_VERSION = "1.0"


class OilPatchV1(BaseOpenEpdHierarchicalSpec):
    """
    Petroleum Industry Cement Slurry.

    Concretes for use in creation, maintenance, and decommissioning of petroleum extraction wells and similar
    applications. Includes foamed cement; often called cement in the drilling industry. Differs from
    flowable fill and grout in that it contains no sand or other aggregates.
    """

    _EXT_VERSION = "1.0"


class ReadyMixV1(BaseOpenEpdHierarchicalSpec):
    """Concretes to be mixed and then poured on-site."""

    _EXT_VERSION = "1.0"


class ShotcreteV1(BaseOpenEpdHierarchicalSpec):
    """Concretes sprayed on a target."""

    _EXT_VERSION = "1.0"


class ConcreteV1(BaseOpenEpdHierarchicalSpec):
    """
    Concrete.

    A composite material composed of fine and coarse aggregate bonded together with a fluid cement (cement paste) that
    hardens over time.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    lightweight: bool | None = pyd.Field(default=None, description="Product is lightweight", example=True)

    strength_28d: PressureMPaStr | None = pyd.Field(
        default=None, description="Concrete strength after 28 days", example="1 MPa"
    )
    strength_other: PressureMPaStr | None = pyd.Field(
        default=None,
        description="A strength spec which is to be reached later other 28 days (e.g. 42d)",
        example="30 MPa",
    )
    strength_other_d: Literal[3, 7, 14, 42, 56, 72, 96, 120] | None = pyd.Field(
        default=None, description="Test Day for strength_other", example=42
    )

    slump: LengthInchStr | None = pyd.Field(default=None, description="", example="2 in")
    min_slump: LengthInchStr | None = pyd.Field(default=None, description="Minimum test slump", example="2 in")
    max_slump: LengthInchStr | None = pyd.Field(default=None, description="", example="2 in")

    min_pipeline_size: LengthMmStr | None = pyd.Field(
        default=None, description="Minimum pipeline size", example="200 mm"
    )
    w_c_ratio: RatioFloat | None = pyd.Field(
        default=None, description="Ratio of water to cement", example=0.5, ge=0, le=1
    )
    air_entrain: bool | None = pyd.Field(default=None, description="Air Entrainment", example=True)
    co2_entrain: bool | None = pyd.Field(default=None, description="CO2 Curing", example=True)
    self_consolidating: bool | None = pyd.Field(default=None, description="Self Compacting", example=True)
    white_cement: bool | None = pyd.Field(default=None, description="White Cement", example=True)
    plc: bool | None = pyd.Field(default=None, description="Portland Limestone Cement", example=True)
    finishable: bool | None = pyd.Field(default=None, description="Finishable", example=True)
    fiber_reinforced: bool | None = pyd.Field(default=None, description="fiber_reinforced", example=True)

    cementitious: Cementitious | None = pyd.Field(
        default=None, description="List of cementitious materials, and proportion by mass"
    )

    aggregate_size_max: LengthMmStr | None = pyd.Field(
        default=None,
        description="The smallest sieve size for which the entire amount of aggregate is able to pass. "
        "Parameter describes diameter of aggregate",
        example="8 mm",
    )
    cement_content: MassKgStr | None = pyd.Field(default=None, example="1 kg")

    aci_exposure_classes: list[AciExposureClass] | None = pyd.Field(
        default=None, description="List of ACI exposure classes", example=["aci.F0"]
    )
    csa_exposure_classes: list[CsaExposureClass] | None = pyd.Field(
        default=None, description="List of CSA exposure classes", example=["csa.C-2"]
    )
    en_exposure_classes: list[EnExposureClass] | None = pyd.Field(
        default=None, description="List of EN exposure classes", example=["en206.X0"]
    )
    typical_application: ConcreteTypicalApplication | None = pyd.Field(default=None, description="Typical Application")

    # Nested specs:
    CementGrout: CementGroutV1 | None = None
    ConcretePaving: ConcretePavingV1 | None = None
    FlowableFill: FlowableFillV1 | None = None
    OilPatch: OilPatchV1 | None = None
    ReadyMix: ReadyMixV1 | None = None
    Shotcrete: ShotcreteV1 | None = None
