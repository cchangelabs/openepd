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

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.generated.accessories import AccessoriesV1
from openepd.model.specs.generated.aggregates import AggregatesV1
from openepd.model.specs.generated.aluminium import AluminiumV1
from openepd.model.specs.generated.asphalt import AsphaltV1
from openepd.model.specs.generated.bulk_materials import BulkMaterialsV1
from openepd.model.specs.generated.cast_decks_and_underlayment import CastDecksAndUnderlaymentV1
from openepd.model.specs.generated.cladding import CladdingV1
from openepd.model.specs.generated.cmu import CMUV1
from openepd.model.specs.generated.concrete import ConcreteV1
from openepd.model.specs.generated.conveying_equipment import ConveyingEquipmentV1
from openepd.model.specs.generated.electrical import ElectricalV1
from openepd.model.specs.generated.electrical_transmission_and_distribution_equipment import (
    ElectricalTransmissionAndDistributionEquipmentV1,
)
from openepd.model.specs.generated.electricity import ElectricityV1
from openepd.model.specs.generated.finishes import FinishesV1
from openepd.model.specs.generated.fire_and_smoke_protection import FireAndSmokeProtectionV1
from openepd.model.specs.generated.furnishings import FurnishingsV1
from openepd.model.specs.generated.grouting import GroutingV1
from openepd.model.specs.generated.manufacturing_inputs import ManufacturingInputsV1
from openepd.model.specs.generated.masonry import MasonryV1
from openepd.model.specs.generated.material_handling import MaterialHandlingV1
from openepd.model.specs.generated.mechanical import MechanicalV1
from openepd.model.specs.generated.mechanical_insulation import MechanicalInsulationV1
from openepd.model.specs.generated.network_infrastructure import NetworkInfrastructureV1
from openepd.model.specs.generated.openings import OpeningsV1
from openepd.model.specs.generated.other_electrical_equipment import OtherElectricalEquipmentV1
from openepd.model.specs.generated.other_materials import OtherMaterialsV1
from openepd.model.specs.generated.plumbing import PlumbingV1
from openepd.model.specs.generated.precast_concrete import PrecastConcreteV1
from openepd.model.specs.generated.sheathing import SheathingV1
from openepd.model.specs.generated.steel import SteelV1
from openepd.model.specs.generated.thermal_moisture_protection import ThermalMoistureProtectionV1
from openepd.model.specs.generated.utility_piping import UtilityPipingV1
from openepd.model.specs.generated.wood import WoodV1
from openepd.model.specs.generated.wood_joists import WoodJoistsV1


class Specs(BaseOpenEpdSchema):
    """Material specific specs."""

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
