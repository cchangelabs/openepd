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
    """Cement grout performance specification."""

    _EXT_VERSION = "1.0"


class ConcretePavingV1(BaseOpenEpdHierarchicalSpec):
    """Concrete paving performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    flexion_strength: PressureMPaStr | None = pyd.Field(
        default=None, description="Paving flexion strength", example="30 MPa"
    )

    _concrete_flexion_strength_is_quantity_validator = pyd.validator("flexion_strength", allow_reuse=True)(
        validate_unit_factory("MPa")
    )


class FlowableFillV1(BaseOpenEpdHierarchicalSpec):
    """Flowable fill performance specification."""

    _EXT_VERSION = "1.0"


class OilPatchV1(BaseOpenEpdHierarchicalSpec):
    """Oil patch performance specification."""

    _EXT_VERSION = "1.0"


class ReadyMixV1(BaseOpenEpdHierarchicalSpec):
    """Concretes that are mixed just before use, and then poured on-site into forms."""

    _EXT_VERSION = "1.0"


class ShotcreteV1(BaseOpenEpdHierarchicalSpec):
    """Shotcrete performance specification."""

    _EXT_VERSION = "1.0"


class ConcreteV1(BaseOpenEpdHierarchicalSpec):
    """Concrete performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    lightweight: bool | None = pyd.Field(default=None, description="Lightweight", example=True)

    strength_28d: PressureMPaStr | None = pyd.Field(
        default=None, description="Concrete strength after 28 days", example="1 MPa"
    )
    strength_other: PressureMPaStr | None = pyd.Field(
        default=None,
        description="A strength spec which is to be reached later other 28 days (e.g. 42d)",
        example="30 MPa",
    )
    strength_other_d: Literal[3, 7, 14, 42, 56, 72, 96, 120] | None = pyd.Field(
        default=None, description="Test Day for the Late Strength", example=42
    )

    slump: LengthInchStr | None = pyd.Field(default=None, description="", example="2 in")
    min_slump: LengthInchStr | None = pyd.Field(default=None, description="Minimum test slump", example="2 in")
    max_slump: LengthInchStr | None = pyd.Field(default=None, description="", example="2 in")

    min_pipeline_size: LengthMmStr | None = pyd.Field(default=None, description="", example="200 mm")
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

    cementitious: Cementitious | None = pyd.Field(default=None, description="")

    aggregate_size_max: LengthMmStr | None = pyd.Field(default=None, description="", example="0.0254 m")
    cement_content: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    aci_exposure_classes: list[AciExposureClass] | None = pyd.Field(default=None, description="", example=["aci.F0"])
    csa_exposure_classes: list[CsaExposureClass] | None = pyd.Field(default=None, description="", example=["csa.C-2"])
    en_exposure_classes: list[EnExposureClass] | None = pyd.Field(default=None, description="", example=["en206.X0"])
    typical_application: ConcreteTypicalApplication | None = pyd.Field(default=None, description="Typical Application")

    _concrete_compressive_strength_28d_is_quantity_validator = pyd.validator("strength_28d", allow_reuse=True)(
        validate_unit_factory("MPa")
    )
    _concrete_compressive_strength_other_is_quantity_validator = pyd.validator("strength_other", allow_reuse=True)(
        validate_unit_factory("MPa")
    )
    _concrete_slump_is_quantity_validator = pyd.validator("slump", allow_reuse=True)(validate_unit_factory("m"))
    _concrete_min_slump_is_quantity_validator = pyd.validator("min_slump", allow_reuse=True)(validate_unit_factory("m"))
    _concrete_max_slump_is_quantity_validator = pyd.validator("max_slump", allow_reuse=True)(validate_unit_factory("m"))
    _concrete_min_pipeline_size_is_quantity_validator = pyd.validator("min_pipeline_size", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_aggregate_size_max_is_quantity_validator = pyd.validator("aggregate_size_max", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_cement_content_is_quantity_validator = pyd.validator("cement_content", allow_reuse=True)(
        validate_unit_factory("kg")
    )

    # Nested specs:
    CementGrout: CementGroutV1 | None = None
    ConcretePaving: ConcretePavingV1 | None = None
    FlowableFill: FlowableFillV1 | None = None
    OilPatch: OilPatchV1 | None = None
    ReadyMix: ReadyMixV1 | None = None
    Shotcrete: ShotcreteV1 | None = None
