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
from openepd.model.specs.generated.enums import FireProtectionPipingMaterial, PipingAnsiSchedule, PlumbingPipingMaterial
from openepd.model.validation.quantity import LengthMStr, validate_unit_factory


class BathtubsV1(BaseOpenEpdHierarchicalSpec):
    """Bathtubs performance specification."""

    _EXT_VERSION = "1.0"


class FaucetsV1(BaseOpenEpdHierarchicalSpec):
    """Faucets performance specification."""

    _EXT_VERSION = "1.0"


class OtherPlumbingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Other plumbing fixtures performance specification."""

    _EXT_VERSION = "1.0"


class WaterClosetsV1(BaseOpenEpdHierarchicalSpec):
    """Water closets performance specification."""

    _EXT_VERSION = "1.0"


class FireProtectionPipingV1(BaseOpenEpdHierarchicalSpec):
    """Fire protection piping performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    piping_diameter: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    mass_per_unit_length: str | None = pyd.Field(default=None, description="", example="1 kg / m")
    piping_ansi_schedule: PipingAnsiSchedule | None = pyd.Field(default=None, description="", example="5")
    fire_protection_piping_material: FireProtectionPipingMaterial | None = pyd.Field(
        default=None, description="", example="PVC"
    )

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))
    _piping_diameter_is_quantity_validator = pyd.validator("piping_diameter", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _mass_per_unit_length_is_quantity_validator = pyd.validator("mass_per_unit_length", allow_reuse=True)(
        validate_unit_factory("kg / m")
    )


class FireSprinklersV1(BaseOpenEpdHierarchicalSpec):
    """Fire sprinklers performance specification."""

    _EXT_VERSION = "1.0"


class StorageTanksV1(BaseOpenEpdHierarchicalSpec):
    """Storage tanks performance specification."""

    _EXT_VERSION = "1.0"


class WaterHeatersV1(BaseOpenEpdHierarchicalSpec):
    """Water heaters performance specification."""

    _EXT_VERSION = "1.0"


class PlumbingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Plumbing fixtures performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Bathtubs: BathtubsV1 | None = None
    Faucets: FaucetsV1 | None = None
    OtherPlumbingFixtures: OtherPlumbingFixturesV1 | None = None
    WaterClosets: WaterClosetsV1 | None = None


class FireSuppressionV1(BaseOpenEpdHierarchicalSpec):
    """Fire suppression performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    FireProtectionPiping: FireProtectionPipingV1 | None = None
    FireSprinklers: FireSprinklersV1 | None = None


class PipingV1(BaseOpenEpdHierarchicalSpec):
    """Piping performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    piping_diameter: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    mass_per_unit_length: str | None = pyd.Field(default=None, description="", example="1 kg / m")
    piping_ansi_schedule: PipingAnsiSchedule | None = pyd.Field(default=None, description="", example="5")
    plumbing_piping_material: PlumbingPipingMaterial | None = pyd.Field(default=None, description="", example="PVC")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))
    _piping_diameter_is_quantity_validator = pyd.validator("piping_diameter", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _mass_per_unit_length_is_quantity_validator = pyd.validator("mass_per_unit_length", allow_reuse=True)(
        validate_unit_factory("kg / m")
    )


class PlumbingEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Plumbing equipment performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    StorageTanks: StorageTanksV1 | None = None
    WaterHeaters: WaterHeatersV1 | None = None


class PlumbingV1(BaseOpenEpdHierarchicalSpec):
    """Plumbing performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PlumbingFixtures: PlumbingFixturesV1 | None = None
    FireSuppression: FireSuppressionV1 | None = None
    Piping: PipingV1 | None = None
    PlumbingEquipment: PlumbingEquipmentV1 | None = None