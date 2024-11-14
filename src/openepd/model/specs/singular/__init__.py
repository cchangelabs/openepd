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
from typing import Any, ClassVar

from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.singular.accessories import AccessoriesV1
from openepd.model.specs.singular.aggregates import AggregatesV1
from openepd.model.specs.singular.aluminium import AluminiumV1
from openepd.model.specs.singular.asphalt import AsphaltV1
from openepd.model.specs.singular.bulk_materials import BulkMaterialsV1
from openepd.model.specs.singular.cast_decks_and_underlayment import CastDecksAndUnderlaymentV1
from openepd.model.specs.singular.cladding import CladdingV1
from openepd.model.specs.singular.cmu import CMUV1
from openepd.model.specs.singular.concrete import ConcreteV1
from openepd.model.specs.singular.conveying_equipment import ConveyingEquipmentV1
from openepd.model.specs.singular.deprecated import BaseCompatibilitySpec, get_safely, set_safely
from openepd.model.specs.singular.deprecated.concrete import ConcreteOldSpec
from openepd.model.specs.singular.deprecated.steel import SteelOldSpec
from openepd.model.specs.singular.electrical import ElectricalV1
from openepd.model.specs.singular.electrical_transmission_and_distribution_equipment import (
    ElectricalTransmissionAndDistributionEquipmentV1,
)
from openepd.model.specs.singular.electricity import ElectricityV1
from openepd.model.specs.singular.finishes import FinishesV1
from openepd.model.specs.singular.fire_and_smoke_protection import FireAndSmokeProtectionV1
from openepd.model.specs.singular.furnishings import FurnishingsV1
from openepd.model.specs.singular.grouting import GroutingV1
from openepd.model.specs.singular.manufacturing_inputs import ManufacturingInputsV1
from openepd.model.specs.singular.masonry import MasonryV1
from openepd.model.specs.singular.material_handling import MaterialHandlingV1
from openepd.model.specs.singular.mechanical import MechanicalV1
from openepd.model.specs.singular.mechanical_insulation import MechanicalInsulationV1
from openepd.model.specs.singular.network_infrastructure import NetworkInfrastructureV1
from openepd.model.specs.singular.openings import OpeningsV1
from openepd.model.specs.singular.other_electrical_equipment import OtherElectricalEquipmentV1
from openepd.model.specs.singular.other_materials import OtherMaterialsV1
from openepd.model.specs.singular.plumbing import PlumbingV1
from openepd.model.specs.singular.precast_concrete import PrecastConcreteV1
from openepd.model.specs.singular.sheathing import SheathingV1
from openepd.model.specs.singular.steel import SteelV1
from openepd.model.specs.singular.thermal_moisture_protection import ThermalMoistureProtectionV1
from openepd.model.specs.singular.utility_piping import UtilityPipingV1
from openepd.model.specs.singular.wood import WoodV1
from openepd.model.specs.singular.wood_joists import WoodJoistsV1

__all__ = ("Specs",)


class Specs(BaseOpenEpdHierarchicalSpec):
    """Material specific specs."""

    COMPATIBILITY_SPECS: ClassVar[list[type[BaseCompatibilitySpec]]] = [ConcreteOldSpec, SteelOldSpec]

    _EXT_VERSION = "1.0"

    # Nested specs:
    CMU: CMUV1 | None = None
    Masonry: MasonryV1 | None = None
    Steel: SteelV1 | None = None
    NetworkInfrastructure: NetworkInfrastructureV1 | None = None
    Finishes: FinishesV1 | None = None
    ManufacturingInputs: ManufacturingInputsV1 | None = None
    Accessories: AccessoriesV1 | None = None
    ElectricalTransmissionAndDistributionEquipment: ElectricalTransmissionAndDistributionEquipmentV1 | None = None
    Aggregates: AggregatesV1 | None = None
    ThermalMoistureProtection: ThermalMoistureProtectionV1 | None = None
    Mechanical: MechanicalV1 | None = None
    Aluminium: AluminiumV1 | None = None
    Cladding: CladdingV1 | None = None
    FireAndSmokeProtection: FireAndSmokeProtectionV1 | None = None
    PrecastConcrete: PrecastConcreteV1 | None = None
    Asphalt: AsphaltV1 | None = None
    OtherMaterials: OtherMaterialsV1 | None = None
    Plumbing: PlumbingV1 | None = None
    Electrical: ElectricalV1 | None = None
    UtilityPiping: UtilityPipingV1 | None = None
    BulkMaterials: BulkMaterialsV1 | None = None
    CastDecksAndUnderlayment: CastDecksAndUnderlaymentV1 | None = None
    Concrete: ConcreteV1 | None = None
    Sheathing: SheathingV1 | None = None
    Furnishings: FurnishingsV1 | None = None
    Wood: WoodV1 | None = None
    ConveyingEquipment: ConveyingEquipmentV1 | None = None
    MaterialHandling: MaterialHandlingV1 | None = None
    Openings: OpeningsV1 | None = None
    Electricity: ElectricityV1 | None = None
    Grouting: GroutingV1 | None = None
    MechanicalInsulation: MechanicalInsulationV1 | None = None
    OtherElectricalEquipment: OtherElectricalEquipmentV1 | None = None
    WoodJoists: WoodJoistsV1 | None = None

    # historical backward-compatible specs
    concrete: ConcreteOldSpec | None = None
    steel: SteelOldSpec | None = None

    @pyd.root_validator(pre=True)
    def _ensure_backward_compatibiltiy(cls, values: dict[str, Any]) -> dict[str, Any]:
        """
        Restore the functionality for backward-compatible specs.

        Originally, we used to have 'concrete' and 'steel' specs non-hierarchical and manually maintained. Since we
        introduced hierarchical specs, there is a need to retain the key mapping to the old structure.

        :return: modified values
        """
        for compat_spec in cls.COMPATIBILITY_SPECS:
            if (
                compat_spec.COMPATIBILITY_SPECS_KEY_OLD not in values
                and compat_spec.COMPATIBILITY_SPECS_KEY_NEW not in values
            ):
                continue
            for old_key_spec, new_key_spec in compat_spec.COMPATIBILITY_MAPPING.items():
                has_new_spec, new_value = get_safely(values, new_key_spec)

                # new value is set, we should not override it but should return it in old spec
                if has_new_spec:
                    set_safely(values, old_key_spec, new_value)
                    continue

                has_old_spec, old_value = get_safely(values, old_key_spec)
                # nothing to back
                if not has_old_spec:
                    continue
                set_safely(values, new_key_spec, old_value)
        return values
