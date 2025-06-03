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
    "CementGroutRangeV1",
    "ConcretePavingRangeV1",
    "ConcreteRangeV1",
    "FlowableFillRangeV1",
    "OilPatchRangeV1",
    "ReadyMixRangeV1",
    "ShotcreteRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from typing import Literal

from openepd.compat.pydantic import pyd
from openepd.model.common import RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.concrete import Cementitious, ConcreteTypicalApplication
from openepd.model.specs.enums import AciExposureClass, CsaExposureClass, EnExposureClass
from openepd.model.validation.quantity import (
    AmountRangeLengthInch,
    AmountRangeLengthMm,
    AmountRangeMass,
    AmountRangePressureMpa,
)


class CementGroutRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cement grout performance specification.

    Cement grouting is a slurry that is placed as a flowable liquid. It is an effective material
    for filling and strengthening granular soils, voids in rocks, foundation underpinnings, and
    other underground voids. Also called structural grout, these materials typically impart
    significant compressive strength to the system.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ConcretePavingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Concrete paving.

    Range version.
    """

    _EXT_VERSION = "1.0"

    flexion_strength: AmountRangePressureMpa | None = pyd.Field(default=None, description="Concrete flexural strength.")


class FlowableFillRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Flowable fill performance specification.

    Flowable fill is a slurry that is placed as a flowable liquid (high slump) and sets with no
    compaction. It is often used in tight or restricted access areas where placing and compacting
    fill is difficult. Applications include filling large voids such as abandoned underground storage
    tanks, basements, tunnels, mines, and sewers. It can also be used as paving sub-base, bridge
    abutment, and retaining wall backfill.

    Also called Controlled Density Fill (CDF) or Controlled Low Strength Materials (CLSMs). These materials typically
    have compressive strengths under 1200 psi.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OilPatchRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Petroleum Industry Cement Slurry.

    Concretes for use in creation, maintenance, and decommissioning of petroleum extraction wells and similar
    applications. Includes foamed cement; often called cement in the drilling industry. Differs from
    flowable fill and grout in that it contains no sand or other aggregates.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ReadyMixRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Concretes to be mixed and then poured on-site.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ShotcreteRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Concretes sprayed on a target.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherConcreteRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other Concrete.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CellularConcreteRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cellular concrete is typically composed of cementitious material, water, and pre-formed foam with air entrainment.

    Such a product is a homogeneous void or cell structure.
    It is self-compacting and can be pumped over extensive heights and distances.
    """

    _EXT_VERSION = "1.0"


class ConcreteRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Concrete.

    A composite material composed of fine and coarse aggregate bonded together with a fluid cement (cement paste) that
    hardens over time.

    Range version.
    """

    _EXT_VERSION = "1.1"

    lightweight: bool | None = pyd.Field(default=None, description="Product is lightweight")
    strength_28d: AmountRangePressureMpa | None = pyd.Field(default=None, description="Concrete strength after 28 days")
    strength_other: AmountRangePressureMpa | None = pyd.Field(
        default=None, description="A strength spec which is to be reached later other 28 days (e.g. 42d)"
    )
    strength_other_d: Literal[3, 7, 14, 42, 56, 72, 96, 120] | None = pyd.Field(
        default=None, description="Test Day for strength_other"
    )
    slump: AmountRangeLengthInch | None = pyd.Field(default=None, description="")
    min_slump: AmountRangeLengthInch | None = pyd.Field(default=None, description="Minimum test slump")
    max_slump: AmountRangeLengthInch | None = pyd.Field(default=None, description="")
    min_pipeline_size: AmountRangeLengthMm | None = pyd.Field(default=None, description="Minimum pipeline size")
    w_c_ratio: RangeRatioFloat | None = pyd.Field(default=None, description="Ratio of water to cement")
    air_entrain: bool | None = pyd.Field(default=None, description="Air Entrainment")
    co2_entrain: bool | None = pyd.Field(default=None, description="CO2 Curing")
    self_consolidating: bool | None = pyd.Field(default=None, description="Self Compacting")
    white_cement: bool | None = pyd.Field(default=None, description="White Cement")
    plc: bool | None = pyd.Field(default=None, description="Portland Limestone Cement")
    finishable: bool | None = pyd.Field(default=None, description="Finishable")
    fiber_reinforced: bool | None = pyd.Field(default=None, description="fiber_reinforced")
    cementitious: Cementitious | None = pyd.Field(
        default=None, description="List of cementitious materials, and proportion by mass"
    )
    aggregate_size_max: AmountRangeLengthMm | None = pyd.Field(
        default=None,
        description="The smallest sieve size for which the entire amount of aggregate is able to pass. Parameter describes diameter of aggregate",
    )
    cement_content: AmountRangeMass | None = pyd.Field(default=None)
    aci_exposure_classes: list[AciExposureClass] | None = pyd.Field(
        default=None, description="List of ACI exposure classes"
    )
    csa_exposure_classes: list[CsaExposureClass] | None = pyd.Field(
        default=None, description="List of CSA exposure classes"
    )
    en_exposure_classes: list[EnExposureClass] | None = pyd.Field(
        default=None, description="List of EN exposure classes"
    )
    typical_application: ConcreteTypicalApplication | None = pyd.Field(default=None, description="Typical Application")
    CementGrout: CementGroutRangeV1 | None = None
    ConcretePaving: ConcretePavingRangeV1 | None = None
    FlowableFill: FlowableFillRangeV1 | None = None
    OilPatch: OilPatchRangeV1 | None = None
    ReadyMix: ReadyMixRangeV1 | None = None
    Shotcrete: ShotcreteRangeV1 | None = None
    OtherConcrete: OtherConcreteRangeV1 | None = None
    CellularConcrete: CellularConcreteRangeV1 | None = None
