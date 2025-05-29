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
__all__ = [
    "SpecsRange",
]


from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

from .accessories import AccessoriesRangeV1
from .aggregates import AggregatesRangeV1
from .aluminium import AluminiumRangeV1
from .asphalt import AsphaltRangeV1
from .bulk_materials import BulkMaterialsRangeV1
from .cast_decks_and_underlayment import CastDecksAndUnderlaymentRangeV1
from .cladding import CladdingRangeV1
from .cmu import CMURangeV1
from .concrete import ConcreteRangeV1
from .conveying_equipment import ConveyingEquipmentRangeV1
from .electrical import ElectricalRangeV1
from .electrical_transmission_and_distribution_equipment import ElectricalTransmissionAndDistributionEquipmentRangeV1
from .electricity import ElectricityRangeV1
from .exterior_improvements import ExteriorImprovementsRangeV1
from .finishes import FinishesRangeV1
from .fire_and_smoke_protection import FireAndSmokeProtectionRangeV1
from .furnishings import FurnishingsRangeV1
from .grouting import GroutingRangeV1
from .manufacturing_inputs import ManufacturingInputsRangeV1
from .masonry import MasonryRangeV1
from .material_handling import MaterialHandlingRangeV1
from .mechanical import MechanicalRangeV1
from .mechanical_insulation import MechanicalInsulationRangeV1
from .network_infrastructure import NetworkInfrastructureRangeV1
from .openings import OpeningsRangeV1
from .other_electrical_equipment import OtherElectricalEquipmentRangeV1
from .other_materials import OtherMaterialsRangeV1
from .plumbing import PlumbingRangeV1
from .precast_concrete import PrecastConcreteRangeV1
from .sheathing import SheathingRangeV1
from .steel import SteelRangeV1
from .thermal_moisture_protection import ThermalMoistureProtectionRangeV1
from .utility_piping import UtilityPipingRangeV1
from .wood import WoodRangeV1
from .wood_joists import WoodJoistsRangeV1


class SpecsRange(BaseOpenEpdHierarchicalSpec):
    """
    Material specific specs.

    Range version.
    """

    _EXT_VERSION = "1.0"

    CMU: CMURangeV1 | None = None
    Masonry: MasonryRangeV1 | None = None
    Steel: SteelRangeV1 | None = None
    NetworkInfrastructure: NetworkInfrastructureRangeV1 | None = None
    Finishes: FinishesRangeV1 | None = None
    ManufacturingInputs: ManufacturingInputsRangeV1 | None = None
    Accessories: AccessoriesRangeV1 | None = None
    ElectricalTransmissionAndDistributionEquipment: ElectricalTransmissionAndDistributionEquipmentRangeV1 | None = None
    Aggregates: AggregatesRangeV1 | None = None
    ThermalMoistureProtection: ThermalMoistureProtectionRangeV1 | None = None
    Mechanical: MechanicalRangeV1 | None = None
    Aluminium: AluminiumRangeV1 | None = None
    Cladding: CladdingRangeV1 | None = None
    FireAndSmokeProtection: FireAndSmokeProtectionRangeV1 | None = None
    PrecastConcrete: PrecastConcreteRangeV1 | None = None
    Asphalt: AsphaltRangeV1 | None = None
    OtherMaterials: OtherMaterialsRangeV1 | None = None
    Plumbing: PlumbingRangeV1 | None = None
    Electrical: ElectricalRangeV1 | None = None
    UtilityPiping: UtilityPipingRangeV1 | None = None
    BulkMaterials: BulkMaterialsRangeV1 | None = None
    CastDecksAndUnderlayment: CastDecksAndUnderlaymentRangeV1 | None = None
    Concrete: ConcreteRangeV1 | None = None
    Sheathing: SheathingRangeV1 | None = None
    Furnishings: FurnishingsRangeV1 | None = None
    Wood: WoodRangeV1 | None = None
    ConveyingEquipment: ConveyingEquipmentRangeV1 | None = None
    MaterialHandling: MaterialHandlingRangeV1 | None = None
    Openings: OpeningsRangeV1 | None = None
    Electricity: ElectricityRangeV1 | None = None
    Grouting: GroutingRangeV1 | None = None
    MechanicalInsulation: MechanicalInsulationRangeV1 | None = None
    OtherElectricalEquipment: OtherElectricalEquipmentRangeV1 | None = None
    WoodJoists: WoodJoistsRangeV1 | None = None
    ExteriorImprovements: ExteriorImprovementsRangeV1 | None = None
