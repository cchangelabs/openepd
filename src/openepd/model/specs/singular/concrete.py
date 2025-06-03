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
from typing import Annotated, Literal

import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, CodegenSpec
from openepd.model.specs.concrete import Cementitious, ConcreteTypicalApplication
from openepd.model.specs.enums import AciExposureClass, CsaExposureClass, EnExposureClass
from openepd.model.validation.enum import exclusive_groups_validator_factory
from openepd.model.validation.quantity import (
    LengthInchStr,
    LengthMmStr,
    MassKgStr,
    PressureMPaStr,
    validate_quantity_unit_factory,
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
    flexion_strength: PressureMPaStr | None = pydantic.Field(
        default=None, description="Concrete flexural strength.", examples=["30 MPa"]
    )

    @pydantic.field_validator("flexion_strength", mode="before", check_fields=False)
    def _validate_flexion_strength(cls, value):
        return validate_quantity_unit_factory("MPa")(cls, value)


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


class CellularConcreteV1(BaseOpenEpdHierarchicalSpec):
    """
    Cellular concrete is typically composed of cementitious material, water, and pre-formed foam with air entrainment.

    Such a product is a homogeneous void or cell structure.
    It is self-compacting and can be pumped over extensive heights and distances.
    """

    _EXT_VERSION = "1.0"


class OtherConcreteV1(BaseOpenEpdHierarchicalSpec):
    """
    Other Concrete Products.

    Other types of concrete products that are not captured by existing concrete categories.
    Could include products such as patching concrete or additives
    """

    _EXT_VERSION = "1.0"


class ConcreteV1(BaseOpenEpdHierarchicalSpec):
    """
    Concrete.

    A composite material composed of fine and coarse aggregate bonded together with a fluid cement (cement paste) that
    hardens over time.
    """

    _EXT_VERSION = "1.1"

    # Own fields:
    lightweight: bool | None = pydantic.Field(
        default=None,
        description="Product is lightweight",
        examples=[True],
    )

    strength_28d: PressureMPaStr | None = pydantic.Field(
        default=None, description="Concrete strength after 28 days", examples=["1 MPa"]
    )
    strength_other: PressureMPaStr | None = pydantic.Field(
        default=None,
        description="A strength spec which is to be reached later other 28 days (e.g. 42d)",
        examples=["30 MPa"],
    )
    strength_other_d: Annotated[
        Literal[3, 7, 14, 42, 56, 72, 96, 120] | None,
        CodegenSpec(override_type=Literal[3, 7, 14, 42, 56, 72, 96, 120]),
    ] = pydantic.Field(default=None, description="Test Day for strength_other", examples=[42])

    slump: LengthInchStr | None = pydantic.Field(default=None, description="", examples=["2 in"])
    min_slump: LengthInchStr | None = pydantic.Field(default=None, description="Minimum test slump", examples=["2 in"])
    max_slump: LengthInchStr | None = pydantic.Field(default=None, description="", examples=["2 in"])

    min_pipeline_size: LengthMmStr | None = pydantic.Field(
        default=None, description="Minimum pipeline size", examples=["200 mm"]
    )
    w_c_ratio: float | None = pydantic.Field(
        default=None, description="Ratio of water to cement", examples=[0.5], ge=0, le=1
    )
    air_entrain: bool | None = pydantic.Field(
        default=None,
        description="Air Entrainment",
        examples=[True],
    )
    co2_entrain: bool | None = pydantic.Field(
        default=None,
        description="CO2 Curing",
        examples=[True],
    )
    self_consolidating: bool | None = pydantic.Field(
        default=None,
        description="Self Compacting",
        examples=[True],
    )
    white_cement: bool | None = pydantic.Field(
        default=None,
        description="White Cement",
        examples=[True],
    )
    plc: bool | None = pydantic.Field(
        default=None,
        description="Portland Limestone Cement",
        examples=[True],
    )
    finishable: bool | None = pydantic.Field(
        default=None,
        description="Finishable",
        examples=[True],
    )
    fiber_reinforced: bool | None = pydantic.Field(
        default=None,
        description="fiber_reinforced",
        examples=[True],
    )

    cementitious: Cementitious | None = pydantic.Field(
        default=None,
        description="List of cementitious materials, and proportion by mass",
    )

    aggregate_size_max: LengthMmStr | None = pydantic.Field(
        default=None,
        description="The smallest sieve size for which the entire amount of aggregate is able to pass. "
        "Parameter describes diameter of aggregate",
        examples=["8 mm"],
    )
    cement_content: MassKgStr | None = pydantic.Field(default=None, examples=["1 kg"])

    aci_exposure_classes: list[AciExposureClass] | None = pydantic.Field(
        default=None, description="List of ACI exposure classes", examples=[["aci.F0"]]
    )
    csa_exposure_classes: list[CsaExposureClass] | None = pydantic.Field(
        default=None, description="List of CSA exposure classes", examples=[["csa.C-2"]]
    )
    en_exposure_classes: list[EnExposureClass] | None = pydantic.Field(
        default=None, description="List of EN exposure classes", examples=[["en206.X0"]]
    )
    typical_application: ConcreteTypicalApplication | None = pydantic.Field(
        default=None, description="Typical Application"
    )

    # Nested specs:
    CementGrout: CementGroutV1 | None = None
    ConcretePaving: ConcretePavingV1 | None = None
    FlowableFill: FlowableFillV1 | None = None
    OilPatch: OilPatchV1 | None = None
    ReadyMix: ReadyMixV1 | None = None
    Shotcrete: ShotcreteV1 | None = None
    OtherConcrete: OtherConcreteV1 | None = None
    CellularConcrete: CellularConcreteV1 | None = None

    @pydantic.field_validator("aci_exposure_classes", mode="before", check_fields=False)
    def _validate_aci_exposure_classes(cls, value):
        return exclusive_groups_validator_factory(AciExposureClass)(cls, value)

    @pydantic.field_validator("en_exposure_classes", mode="before", check_fields=False)
    def _validate_en_exposure_classes(cls, value):
        return exclusive_groups_validator_factory(EnExposureClass)(cls, value)

    @pydantic.field_validator("csa_exposure_classes", mode="before", check_fields=False)
    def _validate_csa_exposure_classes(cls, value):
        return exclusive_groups_validator_factory(CsaExposureClass)(cls, value)
