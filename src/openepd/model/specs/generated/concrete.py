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
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMStr, MassKgStr, PressureMPaStr, validate_unit_factory

UnknownStrTypeHandleMe = str


class CementGroutV1(BaseOpenEpdHierarchicalSpec):
    """Cement grout performance specification."""

    _EXT_VERSION = "1.0"


class ConcretePavingV1(BaseOpenEpdHierarchicalSpec):
    """Concrete paving performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    concrete_flexion_strength: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")

    _concrete_flexion_strength_is_quantity_validator = pyd.validator("concrete_flexion_strength", allow_reuse=True)(
        validate_unit_factory("MPa")
    )


class FlowableFillV1(BaseOpenEpdHierarchicalSpec):
    """Flowable fill performance specification."""

    _EXT_VERSION = "1.0"


class OilPatchV1(BaseOpenEpdHierarchicalSpec):
    """Oil patch performance specification."""

    _EXT_VERSION = "1.0"


class ReadyMixV1(BaseOpenEpdHierarchicalSpec):
    """Ready mix performance specification."""

    _EXT_VERSION = "1.0"
    """Concretes that are mixed just before use, and then poured on-site into forms"""


class ShotcreteV1(BaseOpenEpdHierarchicalSpec):
    """Shotcrete performance specification."""

    _EXT_VERSION = "1.0"


class ConcreteV1(BaseOpenEpdHierarchicalSpec):
    """Concrete performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    lightweight: bool | None = pyd.Field(default=None, description="", example="True")
    concrete_compressive_strength_28d: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    cementitious: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueValidatedJSONProperty"
    )
    white_cement: bool | None = pyd.Field(default=None, description="", example="True")
    concrete_compressive_strength_other: PressureMPaStr | None = pyd.Field(
        default=None, description="", example="1 MPa"
    )
    concrete_compressive_strength_other_d: float | None = pyd.Field(default=None, description="", example="2.3")
    concrete_slump: LengthMStr | None = pyd.Field(default=None, description="", example="0.0254 m")
    concrete_min_slump: LengthMStr | None = pyd.Field(default=None, description="", example="0.0254 m")
    concrete_max_slump: LengthMStr | None = pyd.Field(default=None, description="", example="0.0254 m")
    concrete_min_pipeline_size: LengthMStr | None = pyd.Field(default=None, description="", example="0.0254 m")
    concrete_w_c_ratio: RatioFloat | None = pyd.Field(default=None, description="", example="0.5", ge=0, le=1)
    concrete_air_entrain: bool | None = pyd.Field(default=None, description="", example="True")
    concrete_co2_entrain: bool | None = pyd.Field(default=None, description="", example="True")
    concrete_self_consolidating: bool | None = pyd.Field(default=None, description="", example="True")
    plc: bool | None = pyd.Field(default=None, description="", example="True")
    finishable: bool | None = pyd.Field(default=None, description="", example="True")
    fiber_reinforced: bool | None = pyd.Field(default=None, description="", example="True")
    concrete_aggregate_size_max: LengthMStr | None = pyd.Field(default=None, description="", example="0.0254 m")
    concrete_cement_content: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    aci_exposure_classes: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueValidatedArrayPropertyGeneric"
    )
    csa_exposure_classes: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueValidatedArrayPropertyGeneric"
    )
    en_exposure_classes: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueValidatedArrayPropertyGeneric"
    )
    fnd: bool | None = pyd.Field(default=None, description="", example="True")
    sog: bool | None = pyd.Field(default=None, description="", example="True")
    hrz: bool | None = pyd.Field(default=None, description="", example="True")
    vrt_wall: bool | None = pyd.Field(default=None, description="", example="True")
    vrt_column: bool | None = pyd.Field(default=None, description="", example="True")
    vrt_other: bool | None = pyd.Field(default=None, description="", example="True")
    sht: bool | None = pyd.Field(default=None, description="", example="True")
    cdf: bool | None = pyd.Field(default=None, description="", example="True")
    sac: bool | None = pyd.Field(default=None, description="", example="True")
    pav: bool | None = pyd.Field(default=None, description="", example="True")
    oil: bool | None = pyd.Field(default=None, description="", example="True")
    grt: bool | None = pyd.Field(default=None, description="", example="True")
    ota: bool | None = pyd.Field(default=None, description="", example="True")

    _concrete_compressive_strength_28d_is_quantity_validator = pyd.validator(
        "concrete_compressive_strength_28d", allow_reuse=True
    )(validate_unit_factory("MPa"))
    _concrete_compressive_strength_other_is_quantity_validator = pyd.validator(
        "concrete_compressive_strength_other", allow_reuse=True
    )(validate_unit_factory("MPa"))
    _concrete_slump_is_quantity_validator = pyd.validator("concrete_slump", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_min_slump_is_quantity_validator = pyd.validator("concrete_min_slump", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_max_slump_is_quantity_validator = pyd.validator("concrete_max_slump", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_min_pipeline_size_is_quantity_validator = pyd.validator("concrete_min_pipeline_size", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_aggregate_size_max_is_quantity_validator = pyd.validator("concrete_aggregate_size_max", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _concrete_cement_content_is_quantity_validator = pyd.validator("concrete_cement_content", allow_reuse=True)(
        validate_unit_factory("kg")
    )

    # Nested specs:
    CementGrout: CementGroutV1 | None = None
    ConcretePaving: ConcretePavingV1 | None = None
    FlowableFill: FlowableFillV1 | None = None
    OilPatch: OilPatchV1 | None = None
    ReadyMix: ReadyMixV1 | None = None
    Shotcrete: ShotcreteV1 | None = None
