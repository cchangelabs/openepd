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
from enum import StrEnum

# Enums used


class AhuZoneControl(StrEnum):
    """
    Ahu zone control.

     - Single Zone: Single Zone
     - Multi Zone: Multi Zone

    """

    SINGLE_ZONE = "Single Zone"
    MULTI_ZONE = "Multi Zone"


class UtilityPipingMaterial(StrEnum):
    """
    Utility piping material.

     - PVC: PVC
     - PEX: PEX
     - HDPE: HDPE
     - Galvanized Steel: Galvanized Steel
     - Cast iron: Cast iron
     - PVCO: PVCO
     - Ductile Iron: Ductile Iron
     - Steel: Steel
     - Reinforced Concrete: Reinforced Concrete
     - Unreinforced Concrete: Unreinforced Concrete
     - Fiberglass: Fiberglass
     - PP: PP
     - Stainless Steel: Stainless Steel
     - Other: Other

    """

    PVC = "PVC"
    PEX = "PEX"
    HDPE = "HDPE"
    GALVANIZED_STEEL = "Galvanized Steel"
    CAST_IRON = "Cast iron"
    PVCO = "PVCO"
    DUCTILE_IRON = "Ductile Iron"
    STEEL = "Steel"
    REINFORCED_CONCRETE = "Reinforced Concrete"
    UNREINFORCED_CONCRETE = "Unreinforced Concrete"
    FIBERGLASS = "Fiberglass"
    PP = "PP"
    STAINLESS_STEEL = "Stainless Steel"
    OTHER = "Other"


class ResilientFlooringThickness(StrEnum):
    """
    Resilient flooring thickness.

     - ≤ 2mm: ≤ 2mm
     - ~ 2.5mm: ~ 2.5mm
     - ~ 3.2mm: ~ 3.2mm
     - ~ 4mm: ~ 4mm
     - ~ 4.5mm: ~ 4.5mm
     - ~ 5mm: ~ 5mm
     - ~ 5.5mm: ~ 5.5mm
     - ~ 6mm: ~ 6mm
     - ~ 8mm: ~ 8mm
     - ≥ 10mm: ≥ 10mm

    """

    _2MM = "≤ 2mm"
    _2_5MM = "~ 2.5mm"
    _3_2MM = "~ 3.2mm"
    _4MM = "~ 4mm"
    _4_5MM = "~ 4.5mm"
    _5MM = "~ 5mm"
    _5_5MM = "~ 5.5mm"
    _6MM = "~ 6mm"
    _8MM = "~ 8mm"
    _10MM = "≥ 10mm"


class CablingFireRating(StrEnum):
    """
    Cabling fire rating.

     - CMP: CMP
     - CMR: CMR
     - CMG: CMG
     - CM: CM
     - OFNP/CP: OFNP/CP
     - OFNR/CR: OFNR/CR

    """

    CMP = "CMP"
    CMR = "CMR"
    CMG = "CMG"
    CM = "CM"
    OFNP_CP = "OFNP/CP"
    OFNR_CR = "OFNR/CR"


class ElevatorsBuildingRise(StrEnum):
    """
    Elevators building rise.

     - Low-rise: Low-rise
     - Mid-rise: Mid-rise
     - High-rise: High-rise

    """

    LOW_RISE = "Low-rise"
    MID_RISE = "Mid-rise"
    HIGH_RISE = "High-rise"


class ResilientFlooringMaterial(StrEnum):
    """
    Resilient flooring material.

     - VCT: VCT
     - LVT: LVT
     - Rubber: Rubber
     - Linoleum: Linoleum
     - Cork: Cork
     - Rigid: Rigid
     - Vinyl: Vinyl
     - SVT: SVT
     - Composite: Composite
     - Other: Other

    """

    VCT = "VCT"
    LVT = "LVT"
    RUBBER = "Rubber"
    LINOLEUM = "Linoleum"
    CORK = "Cork"
    RIGID = "Rigid"
    VINYL = "Vinyl"
    SVT = "SVT"
    COMPOSITE = "Composite"
    OTHER = "Other"


class AirFiltersMediaType(StrEnum):
    """
    Air filters media type.

     - Acrylic: Acrylic
     - Activated Carbon / Charcoal: Activated Carbon / Charcoal
     - Aluminum Screen Wire: Aluminum Screen Wire
     - Electrostatic: Electrostatic
     - Fiberglass: Fiberglass
     - Paper: Paper
     - Polyurethane Foam: Polyurethane Foam
     - Polyester: Polyester
     - Poly / Cotton Nonwoven Media: Poly / Cotton Nonwoven Media

    """

    ACRYLIC = "Acrylic"
    ACTIVATED_CARBON_OR_CHARCOAL = "Activated Carbon / Charcoal"
    ALUMINUM_SCREEN_WIRE = "Aluminum Screen Wire"
    ELECTROSTATIC = "Electrostatic"
    FIBERGLASS = "Fiberglass"
    PAPER = "Paper"
    POLYURETHANE_FOAM = "Polyurethane Foam"
    POLYESTER = "Polyester"
    POLY_COTTON_NONWOVEN_MEDIA = "Poly / Cotton Nonwoven Media"


class GypsumFireRating(StrEnum):
    """
    Gypsum fire rating.

     - -: -
     - X: X
     - C: C
     - F: F

    """

    _ = "-"
    X = "X"
    C = "C"
    F = "F"


class MembraneRoofingReinforcement(StrEnum):
    """
    Membrane roofing reinforcement.

     - Polyester: Polyester
     - Fiberglass: Fiberglass
     - None: None
     - Other: Other

    """

    POLYESTER = "Polyester"
    FIBERGLASS = "Fiberglass"
    NONE = "None"
    OTHER = "Other"


class AirFiltersMervRating(StrEnum):
    """
    Air filters merv rating.

     - MERV 1: MERV 1
     - MERV 2: MERV 2
     - MERV 3: MERV 3
     - MERV 4: MERV 4
     - MERV 5: MERV 5
     - MERV 6: MERV 6
     - MERV 7: MERV 7
     - MERV 8: MERV 8
     - MERV 9: MERV 9
     - MERV 10: MERV 10
     - MERV 11: MERV 11
     - MERV 12: MERV 12
     - MERV 13: MERV 13
     - MERV 14: MERV 14
     - MERV 15: MERV 15
     - MERV 16: MERV 16
     - HEPA: HEPA

    """

    MERV_1 = "MERV 1"
    MERV_2 = "MERV 2"
    MERV_3 = "MERV 3"
    MERV_4 = "MERV 4"
    MERV_5 = "MERV 5"
    MERV_6 = "MERV 6"
    MERV_7 = "MERV 7"
    MERV_8 = "MERV 8"
    MERV_9 = "MERV 9"
    MERV_10 = "MERV 10"
    MERV_11 = "MERV 11"
    MERV_12 = "MERV 12"
    MERV_13 = "MERV 13"
    MERV_14 = "MERV 14"
    MERV_15 = "MERV 15"
    MERV_16 = "MERV 16"
    HEPA = "HEPA"


class PduTechnology(StrEnum):
    """
    Pdu technology.

     - Basic: Basic
     - Intelligent: Intelligent
     - Intelligent with Outlet Control: Intelligent with Outlet Control
     - Intelligent with Outlet Monitoring: Intelligent with Outlet Monitoring
     - Outlet Control and Monitoring: Outlet Control and Monitoring

    """

    BASIC = "Basic"
    INTELLIGENT = "Intelligent"
    INTELLIGENT_WITH_OUTLET_CONTROL = "Intelligent with Outlet Control"
    INTELLIGENT_WITH_OUTLET_MONITORING = "Intelligent with Outlet Monitoring"
    OUTLET_CONTROL_AND_MONITORING = "Outlet Control and Monitoring"


class IntumescentFireproofingMaterialType(StrEnum):
    """
    Intumescent fireproofing material type.

     - Epoxy: Epoxy
     - Water-based: Water-based
     - Solvent-based: Solvent-based

    """

    EPOXY = "Epoxy"
    WATER_BASED = "Water-based"
    SOLVENT_BASED = "Solvent-based"


class AccessFlooringCoreMaterial(StrEnum):
    """
    Access flooring core material.

     - Cementitious: Cementitious
     - Wood: Wood
     - Other: Other
     - Concrete: Concrete
     - Hollow: Hollow

    """

    CEMENTITIOUS = "Cementitious"
    WOOD = "Wood"
    OTHER = "Other"
    CONCRETE = "Concrete"
    HOLLOW = "Hollow"


class BuriedPipingType(StrEnum):
    """
    Buried piping type.

     - Water Utilities: Water Utilities
     - Sanitary Sewer: Sanitary Sewer
     - Storm Drainage: Storm Drainage
     - Fuel Distribution: Fuel Distribution

    """

    WATER_UTILITIES = "Water Utilities"
    SANITARY_SEWER = "Sanitary Sewer"
    STORM_DRAINAGE = "Storm Drainage"
    FUEL_DISTRIBUTION = "Fuel Distribution"


class RackType(StrEnum):
    """
    Rack type.

     - Cabinet: Cabinet
     - Rack: Rack
     - Enclosure: Enclosure

    """

    CABINET = "Cabinet"
    RACK = "Rack"
    ENCLOSURE = "Enclosure"


class FoamType(StrEnum):
    """
    Foam type.

     - Open-Cell: Open-Cell
     - Closed-Cell: Closed-Cell

    """

    OPEN_CELL = "Open-Cell"
    CLOSED_CELL = "Closed-Cell"


class FrameMaterial(StrEnum):
    """
    Frame material.

     - Vinyl: Vinyl
     - Aluminium: Aluminium
     - Steel: Steel
     - Wood: Wood
     - Fiberglass: Fiberglass
     - Composite: Composite
     - None: None
     - Other: Other

    """

    VINYL = "Vinyl"
    ALUMINIUM = "Aluminium"
    STEEL = "Steel"
    WOOD = "Wood"
    FIBERGLASS = "Fiberglass"
    COMPOSITE = "Composite"
    NONE = "None"
    OTHER = "Other"


class PipingAnsiSchedule(StrEnum):
    """
    Piping ansi schedule.

     - 5: 5
     - 10: 10
     - 20: 20
     - 30: 30
     - 40: 40
     - 60: 60
     - 80: 80
     - 100: 100
     - 120: 120
     - 140: 140
     - 160: 160

    """

    ANSI_SCHEDULE_5 = "5"
    ANSI_SCHEDULE_10 = "10"
    ANSI_SCHEDULE_20 = "20"
    ANSI_SCHEDULE_30 = "30"
    ANSI_SCHEDULE_40 = "40"
    ANSI_SCHEDULE_60 = "60"
    ANSI_SCHEDULE_80 = "80"
    ANSI_SCHEDULE_100 = "100"
    ANSI_SCHEDULE_120 = "120"
    ANSI_SCHEDULE_140 = "140"
    ANSI_SCHEDULE_160 = "160"


class CmuWeightClassification(StrEnum):
    """
    Cmu weight classification.

     - Normal: Normal
     - Medium: Medium
     - Light: Light

    """

    NORMAL = "Normal"
    MEDIUM = "Medium"
    LIGHT = "Light"


class CementEn197_1(StrEnum):
    """
    CementEn197 1.

     - CEM I: CEM I
     - CEM II/A-S: CEM II/A-S
     - CEM II/A-P: CEM II/A-P
     - CEM II/A-Q: CEM II/A-Q
     - CEM II/A-V: CEM II/A-V
     - CEM II/A-W: CEM II/A-W
     - CEM II/A-T: CEM II/A-T
     - CEM II/A-L: CEM II/A-L
     - CEM II/A-LL: CEM II/A-LL
     - CEM II/A-M: CEM II/A-M
     - CEM II/A-D: CEM II/A-D
     - CEM II/B-S: CEM II/B-S
     - CEM II/B-P: CEM II/B-P
     - CEM II/B-Q: CEM II/B-Q
     - CEM II/B-V: CEM II/B-V
     - CEM II/B-W: CEM II/B-W
     - CEM II/B-T: CEM II/B-T
     - CEM II/B-L: CEM II/B-L
     - CEM II/B-LL: CEM II/B-LL
     - CEM II/B-M: CEM II/B-M
     - CEM II/C: CEM II/C
     - CEM III/A: CEM III/A
     - CEM III/B: CEM III/B
     - CEM III/C: CEM III/C
     - CEM IV/A: CEM IV/A
     - CEM IV/B: CEM IV/B
     - CEM V/A: CEM V/A
     - CEM V/B: CEM V/B

    """

    CEM_I = "CEM I"
    CEM_II_A_S = "CEM II/A-S"
    CEM_II_A_P = "CEM II/A-P"
    CEM_II_A_Q = "CEM II/A-Q"
    CEM_II_A_V = "CEM II/A-V"
    CEM_II_A_W = "CEM II/A-W"
    CEM_II_A_T = "CEM II/A-T"
    CEM_II_A_L = "CEM II/A-L"
    CEM_II_A_LL = "CEM II/A-LL"
    CEM_II_A_M = "CEM II/A-M"
    CEM_II_A_D = "CEM II/A-D"
    CEM_II_B_S = "CEM II/B-S"
    CEM_II_B_P = "CEM II/B-P"
    CEM_II_B_Q = "CEM II/B-Q"
    CEM_II_B_V = "CEM II/B-V"
    CEM_II_B_W = "CEM II/B-W"
    CEM_II_B_T = "CEM II/B-T"
    CEM_II_B_L = "CEM II/B-L"
    CEM_II_B_LL = "CEM II/B-LL"
    CEM_II_B_M = "CEM II/B-M"
    CEM_II_C = "CEM II/C"
    CEM_III_A = "CEM III/A"
    CEM_III_B = "CEM III/B"
    CEM_III_C = "CEM III/C"
    CEM_IV_A = "CEM IV/A"
    CEM_IV_B = "CEM IV/B"
    CEM_V_A = "CEM V/A"
    CEM_V_B = "CEM V/B"


class CsaA3001(StrEnum):
    """
    Csa a3001.

     - A3001 GU: A3001 GU
     - A3001 HE: A3001 HE
     - A3001 MS: A3001 MS
     - A3001 HS: A3001 HS

    """

    A3001_GU = "A3001 GU"
    A3001_HE = "A3001 HE"
    A3001_MS = "A3001 MS"
    A3001_HS = "A3001 HS"


class BoilerConfiguration(StrEnum):
    """
    Boiler configuration.

     - Hot water: Hot water
     - Steam: Steam

    """

    HOT_WATER = "Hot water"
    STEAM = "Steam"


class FloorBoxCoverMaterial(StrEnum):
    """
    Floor box cover material.

     - Brass: Brass
     - Aluminum: Aluminum
     - Other Metallic: Other Metallic
     - Non-metallic: Non-metallic
     - Heavy Duty: Heavy Duty
     - None (box only): None (box only)

    """

    BRASS = "Brass"
    ALUMINUM = "Aluminum"
    OTHER_METALLIC = "Other Metallic"
    NON_METALLIC = "Non-metallic"
    HEAVY_DUTY = "Heavy Duty"
    NONE = "None (box only)"


class SteelComposition(StrEnum):
    """
    Steel composition.

     - Carbon: Carbon
     - Alloy: Alloy
     - Stainless: Stainless
     - Tool: Tool
     - Other: Other

    """

    CARBON = "Carbon"
    ALLOY = "Alloy"
    STAINLESS = "Stainless"
    TOOL = "Tool"
    OTHER = "Other"


class CeilingPanelFireRating(StrEnum):
    """
    Ceiling panel fire rating.

     - Class A: Class A
     - Class B: Class B
     - Class C: Class C
     - Class D: Class D

    """

    CLASS_A = "Class A"
    CLASS_B = "Class B"
    CLASS_C = "Class C"
    CLASS_D = "Class D"


class SheetConstruction(StrEnum):
    """
    Sheet construction.

     - Homogeneous: Homogeneous
     - Heterogeneous: Heterogeneous

    """

    HOMOGENEOUS = "Homogeneous"
    HETEROGENEOUS = "Heterogeneous"


class FloorBoxMaterial(StrEnum):
    """
    Floor box material.

     - Metallic Box: Metallic Box
     - Non-metallic Box: Non-metallic Box
     - None (cover only): None (cover only)

    """

    METALLIC_BOX = "Metallic Box"
    NON_METALLIC_BOX = "Non-metallic Box"
    NONE = "None (cover only)"


class FireProtectionPipingMaterial(StrEnum):
    """
    Fire protection piping material.

     - PVC: PVC
     - Copper: Copper
     - PEX: PEX
     - HDPE: HDPE
     - Ductile Iron: Ductile Iron
     - Steel: Steel

    """

    PVC = "PVC"
    COPPER = "Copper"
    PEX = "PEX"
    HDPE = "HDPE"
    DUCTILE_IRON = "Ductile Iron"
    STEEL = "Steel"


class MechanicalRefrigerants(StrEnum):
    """
    Mechanical refrigerants.

     - R11: R11
     - R22: R22
     - R407c: R407c
     - R410a: R410a
     - R134a: R134a
     - R32: R32
     - R1234yf: R1234yf
     - R1234ze: R1234ze
     - R290: R290
     - R744: R744
     - R717: R717
     - R718: R718

    """

    R11 = "R11"
    R22 = "R22"
    R407C = "R407c"
    R410A = "R410a"
    R134A = "R134a"
    R32 = "R32"
    R1234YF = "R1234yf"
    R1234ZE = "R1234ze"
    R290 = "R290"
    R744 = "R744"
    R717 = "R717"
    R718 = "R718"


class RacewaysMaterial(StrEnum):
    """
    Raceways material.

     - Aluminum: Aluminum
     - Steel: Steel
     - Non-metallic: Non-metallic

    """

    ALUMINUM = "Aluminum"
    STEEL = "Steel"
    NON_METALLIC = "Non-metallic"


class CountertopMaterial(StrEnum):
    """
    Countertop material.

     - Stone: Stone
     - Concrete: Concrete
     - Plastic: Plastic
     - Glass: Glass
     - Wood: Wood
     - Metal: Metal
     - Ceramic: Ceramic
     - Other: Other

    """

    STONE = "Stone"
    CONCRETE = "Concrete"
    PLASTIC = "Plastic"
    GLASS = "Glass"
    WOOD = "Wood"
    METAL = "Metal"
    CERAMIC = "Ceramic"
    OTHER = "Other"


class SteelRebarGrade(StrEnum):
    """
    Steel rebar grade.

     - 60 ksi: 60 ksi
     - 75 ksi: 75 ksi
     - 80 ksi: 80 ksi
     - 90 ksi: 90 ksi
     - 100 ksi: 100 ksi
     - 120 ksi: 120 ksi
     - 40 ksi: 40 ksi
     - 50 ksi: 50 ksi

    """

    _60_KSI = "60 ksi"
    _75_KSI = "75 ksi"
    _80_KSI = "80 ksi"
    _90_KSI = "90 ksi"
    _100_KSI = "100 ksi"
    _120_KSI = "120 ksi"
    _40_KSI = "40 ksi"
    _50_KSI = "50 ksi"


class AsphaltGradation(StrEnum):
    """
    Asphalt gradation.

     - Gap-graded: Gap-graded
     - Open-graded: Open-graded
     - Dense-graded: Dense-graded

    """

    GAP_GRADED = "Gap-graded"
    OPEN_GRADED = "Open-graded"
    DENSE_GRADED = "Dense-graded"


class RoofCoverBoardsFacing(StrEnum):
    """
    Roof cover boards facing.

     - Paper: Paper
     - Glass mat: Glass mat
     - Fiberglass: Fiberglass
     - Other: Other

    """

    PAPER = "Paper"
    GLASS_MAT = "Glass mat"
    FIBERGLASS = "Fiberglass"
    OTHER = "Other"


class PlumbingPipingMaterial(StrEnum):
    """
    Plumbing piping material.

     - PVC: PVC
     - Copper: Copper
     - PEX: PEX
     - HDPE: HDPE
     - Galvanized Steel: Galvanized Steel
     - Cast iron: Cast iron
     - Stainless Steel: Stainless Steel

    """

    PVC = "PVC"
    COPPER = "Copper"
    PEX = "PEX"
    HDPE = "HDPE"
    GALVANIZED_STEEL = "Galvanized Steel"
    CAST_IRON = "Cast iron"
    STAINLESS_STEEL = "Stainless Steel"


class AccessFlooringStringers(StrEnum):
    """
    Access flooring stringers.

     - Standard: Standard
     - Heavy-duty: Heavy-duty
     - None: None

    """

    STANDARD = "Standard"
    HEAVY_DUTY = "Heavy-duty"
    NONE = "None"


class ResilientFlooringFormFactor(StrEnum):
    """
    Resilient flooring form factor.

     - Loose Lay: Loose Lay
     - Gluedown: Gluedown
     - Underlayment: Underlayment
     - Interlocking: Interlocking
     - Self Adhering: Self Adhering
     - Tile: Tile
     - Sheet: Sheet
     - Other: Other

    """

    LOOSE_LAY = "Loose Lay"
    GLUEDOWN = "Gluedown"
    UNDERLAYMENT = "Underlayment"
    INTERLOCKING = "Interlocking"
    SELF_ADHERING = "Self Adhering"
    TILE = "Tile"
    SHEET = "Sheet"
    OTHER = "Other"


class EnergySource(StrEnum):
    """
    Energy source.

     - Grid: Grid
     - Wind: Wind
     - Solar: Solar
     - Hydro: Hydro
     - Biomass: Biomass
     - Coal: Coal
     - Natgas: Natgas
     - Nuclear: Nuclear
     - Other: Other

    """

    GRID = "Grid"
    WIND = "Wind"
    SOLAR = "Solar"
    HYDRO = "Hydro"
    BIOMASS = "Biomass"
    COAL = "Coal"
    NATGAS = "Natgas"
    NUCLEAR = "Nuclear"
    OTHER = "Other"


class CablingCategory(StrEnum):
    """
    Cabling category.

     - Cat7: Cat7
     - Cat6A: Cat6A
     - Cat6: Cat6
     - Cat5/5e: Cat5/5e
     - Cat3: Cat3
     - Coax: Coax
     - Fiber: Fiber
     - Other: Other

    """

    CAT7 = "Cat7"
    CAT6A = "Cat6A"
    CAT6 = "Cat6"
    CAT5_CAT5e = "Cat5/5e"
    CAT3 = "Cat3"
    COAX = "Coax"
    FIBER = "Fiber"
    OTHER = "Other"


class MechanicalInstallation(StrEnum):
    """
    Mechanical installation.

     - Indoor: Indoor
     - Outdoor: Outdoor

    """

    INDOOR = "Indoor"
    OUTDOOR = "Outdoor"


class DeckingBoardMaterial(StrEnum):
    """
    Decking board material.

     - Wood: Wood
     - Composite: Composite
     - Vinyl: Vinyl
     - Aluminum: Aluminum
     - Other: Other

    """

    WOOD = "Wood"
    COMPOSITE = "Composite"
    VINYL = "Vinyl"
    ALUMINUM = "Aluminum"
    OTHER = "Other"


class BoilerEquipmentFuelType(StrEnum):
    """
    Boiler equipment fuel type.

     - Coal: Coal
     - Electric: Electric
     - Natural Gas: Natural Gas
     - Propane: Propane
     - Oil: Oil
     - Wood: Wood
     - Other: Other

    """

    COAL = "Coal"
    ELECTRIC = "Electric"
    NATURAL_GAS = "Natural Gas"
    PROPANE = "Propane"
    OIL = "Oil"
    WOOD = "Wood"
    OTHER = "Other"


class Spacer(StrEnum):
    """
    Spacer.

     - Aluminium: Aluminium
     - Stainless steel: Stainless steel
     - Plastic and stainless steel: Plastic and stainless steel
     - Thermoplastic: Thermoplastic
     - Foam: Foam
     - Stainless steel or tin plate U-channel: Stainless steel or tin plate U-channel
     - Plastic: Plastic

    """

    ALUMINIUM = "Aluminium"
    STAINLESS_STEEL = "Stainless steel"
    PLASTIC_AND_STAINLESS_STEEL = "Plastic and stainless steel"
    THERMOPLASTIC = "Thermoplastic"
    FOAM = "Foam"
    STAINLESS_STEEL_OR_TIN_PLATE_U_CHANNEL = "Stainless steel or tin plate U-channel"
    PLASTIC = "Plastic"


class HvacHeatExchangersType(StrEnum):
    """
    Hvac heat exchangers type.

     - Shell and Tube: Shell and Tube
     - Plate: Plate
     - Finned Tube: Finned Tube
     - Double-Pipe: Double-Pipe
     - Plate-Fin: Plate-Fin
     - Spiral: Spiral

    """

    SHELL_AND_TUBE = "Shell and Tube"
    PLATE = "Plate"
    FINNED_TUBE = "Finned Tube"
    DOUBLE_PIPE = "Double-Pipe"
    PLATE_FIN = "Plate-Fin"
    SPIRAL = "Spiral"


class HeatPumpType(StrEnum):
    """
    Heat pump type.

     - Air-to-Water: Air-to-Water
     - Water-to-Water: Water-to-Water

    """

    AIR_TO_WATER = "Air-to-Water"
    WATER_TO_WATER = "Water-to-Water"


class RoofCoverBoardsMaterial(StrEnum):
    """
    Roof cover boards material.

     - Gypsum Fiber: Gypsum Fiber
     - Gypsum: Gypsum
     - Wood Fiber: Wood Fiber
     - Cement: Cement
     - Polyiso: Polyiso
     - Perlite: Perlite
     - Asphaltic: Asphaltic
     - Mineral Fiber: Mineral Fiber
     - Plywood/OSB: Plywood/OSB
     - Other: Other

    """

    GYPSUM_FIBER = "Gypsum Fiber"
    GYPSUM = "Gypsum"
    WOOD_FIBER = "Wood Fiber"
    CEMENT = "Cement"
    POLYISO = "Polyiso"
    PERLITE = "Perlite"
    ASPHALTIC = "Asphaltic"
    MINERAL_FIBER = "Mineral Fiber"
    PLYWOOD_OSB = "Plywood/OSB"
    OTHER = "Other"


class CablingJacketMaterial(StrEnum):
    """
    Cabling jacket material.

     - PVC: PVC
     - FEP: FEP
     - LSHF: LSHF
     - PVDF: PVDF
     - Polyolefin: Polyolefin
     - Other: Other

    """

    PVC = "PVC"
    FEP = "FEP"
    LSHF = "LSHF"
    PVDF = "PVDF"
    POLYOLEFIN = "Polyolefin"
    OTHER = "Other"


class CeilingPanelCoreMaterial(StrEnum):
    """
    Ceiling panel core material.

     - Fiberglass: Fiberglass
     - Mineral Fiber: Mineral Fiber
     - Wood: Wood
     - Aluminium: Aluminium
     - Steel: Steel
     - Other: Other

    """

    FIBERGLASS = "Fiberglass"
    MINERAL_FIBER = "Mineral Fiber"
    WOOD = "Wood"
    ALUMINIUM = "Aluminium"
    STEEL = "Steel"
    OTHER = "Other"


class CableTraysMaterial(StrEnum):
    """
    Cable trays material.

     - Stainless Steel: Stainless Steel
     - Electroplated Zinc: Electroplated Zinc
     - Hot Dip Galvanized: Hot Dip Galvanized

    """

    STAINLESS_STEEL = "Stainless Steel"
    ELECTROPLATED_ZINC = "Electroplated Zinc"
    HOT_DIP_GALVANIZED = "Hot Dip Galvanized"


class InsulationIntendedApplication(StrEnum):
    """
    Insulation intended application.

     - Wall & General: Wall & General
     - Exterior Wall: Exterior Wall
     - Roof: Roof
     - Below Grade: Below Grade
     - Duct: Duct
     - Other: Other

    """

    WALL_GENERAL = "Wall & General"
    EXTERIOR_WALL = "Exterior Wall"
    ROOF = "Roof"
    BELOW_GRADE = "Below Grade"
    DUCT = "Duct"
    OTHER = "Other"


class SprayFireproofingDensity(StrEnum):
    """
    Spray fireproofing density.

     - Standard: Standard
     - Medium: Medium
     - High: High

    """

    STANDARD = "Standard"
    MEDIUM = "Medium"
    HIGH = "High"


class ElevatorsUsageIntensity(StrEnum):
    """
    Elevators usage intensity.

     - Very low: Very low
     - Low: Low
     - Medium: Medium
     - High: High
     - Very high: Very high
     - Extremely high: Extremely high

    """

    VERY_LOW = "Very low"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very high"
    EXTREMELY_HIGH = "Extremely high"


class CladdingFacingMaterial(StrEnum):
    """
    Cladding facing material.

     - Steel: Steel
     - Stone: Stone
     - Aluminium: Aluminium
     - Other: Other

    """

    STEEL = "Steel"
    STONE = "Stone"
    ALUMINIUM = "Aluminium"
    OTHER = "Other"


class WallBaseMaterial(StrEnum):
    """
    Wall base material.

     - Rubber: Rubber
     - Vinyl: Vinyl
     - Other: Other

    """

    RUBBER = "Rubber"
    VINYL = "Vinyl"
    OTHER = "Other"


class SprayFireproofingMaterialType(StrEnum):
    """
    Spray fireproofing material type.

     - Gypsum-based: Gypsum-based
     - Portland: Portland
     - Gypsum and Portland: Gypsum and Portland

    """

    GYPSUM_BASED = "Gypsum-based"
    PORTLAND_CEMENT_BASED = "Portland"
    GYPSUM_AND_PORTLAND_CEMENT_BASED = "Gypsum and Portland"


class MasonryCementAstmC91Type(StrEnum):
    """
    Masonry cement astm c91 type.

     - Type N: Type N
     - Type S: Type S
     - Type O: Type O
     - Type M: Type M

    """

    TYPE_N = "Type N"
    TYPE_S = "Type S"
    TYPE_O = "Type O"
    TYPE_M = "Type M"


class CementAstmType(StrEnum):
    """
    Cement astm type.

     - C150 Type I: C150 Type I
     - C150 Type I/II: C150 Type I/II
     - C150 Type III: C150 Type III
     - C150 Type IV: C150 Type IV
     - C150 Type II/V: C150 Type II/V
     - C595 PLC: C595 PLC
     - C595 Blended: C595 Blended

    """

    C150_TYPE_I = "C150 Type I"
    C150_TYPE_I_II = "C150 Type I/II"
    C150_TYPE_III = "C150 Type III"
    C150_TYPE_IV = "C150 Type IV"
    C150_TYPE_II_V = "C150 Type II/V"
    C595_PLC = "C595 PLC"
    C595_BLENDED = "C595 Blended"


class CmuBlockType(StrEnum):
    """
    Cmu block type.

     - Gray: Gray
     - Architectural: Architectural

    """

    GRAY = "Gray"
    ARCHITECTURAL = "Architectural"


class CarpetYarnType(StrEnum):
    """
    Carpet yarn type.

     - Nylon 6,6: Nylon 6,6
     - Nylon 6: Nylon 6
     - Wool: Wool
     - Recycled PET: Recycled PET
     - Polyester (PET): Polyester (PET)
     - Olefin: Olefin

    """

    NYLON_6_6 = "Nylon 6,6"
    NYLON_6 = "Nylon 6"
    WOOL = "Wool"
    RECYCLED_PET = "Recycled PET"
    POLYESTER_PET = "Polyester (PET)"
    OLEFIN = "Olefin"


class Alloy(StrEnum):
    """
    Alloy.

     - 1xxx: 1xxx
     - 2xxx: 2xxx
     - 3xxx: 3xxx
     - 4xxx: 4xxx
     - 5xxx: 5xxx
     - 6xxx: 6xxx
     - 7xxx: 7xxx
     - 8xxx: 8xxx
     - 1xx.x: 1xx.x
     - 2xx.x: 2xx.x
     - 3xx.x: 3xx.x
     - 4xx.x: 4xx.x
     - 5xx.x: 5xx.x
     - 7xx.x: 7xx.x
     - 8xx.x: 8xx.x
     - 9xx.x: 9xx.x

    """

    _1XXX = "1xxx"
    _2XXX = "2xxx"
    _3XXX = "3xxx"
    _4XXX = "4xxx"
    _5XXX = "5xxx"
    _6XXX = "6xxx"
    _7XXX = "7xxx"
    _8XXX = "8xxx"
    _1XX_X = "1xx.x"
    _2XX_X = "2xx.x"
    _3XX_X = "3xx.x"
    _4XX_X = "4xx.x"
    _5XX_X = "5xx.x"
    _7XX_X = "7xx.x"
    _8XX_X = "8xx.x"
    _9XX_X = "9xx.x"


class IntendedApplication(StrEnum):
    """
    Intended application.

     - Res: Res
     - Com: Com
     - Ind: Ind

    """

    RES = "Res"
    COM = "Com"
    IND = "Ind"


class WoodFlooringFabrication(StrEnum):
    """
    Wood Flooring Fabrication.

     - Solid hardwood: Solid hardwood
     - Engineered hardwood: Engineered hardwood
     - Bamboo: Bamboo
     - Parquet: Parquet
     - Cork: Cork

    """

    SOLID_HARDWOOD = "Solid hardwood"
    ENGINEERED_HARDWOOD = "Engineered hardwood"
    BAMBOO = "Bamboo"
    PARQUET = "Parquet"
    CORK = "Cork"


class CompositeLumberFabrication(StrEnum):
    """
    Composite Lumber Fabrication.

     - LVL: LVL
     - Bonded Strand: Bonded Strand
    """

    LVL = "LVL"
    BONDED_STRAND = "Bonded Strand"


class MassTimberFabrication(StrEnum):
    """
    Composite Lumber Fabrication.

     - CLT: CLT
     - GLT: GLT
     - NLT: NLT
     - DLT: DLT
    """

    CLT = "CLT"
    GLT = "GLT"
    NLT = "NLT"
    DLT = "DLT"


class SheathingPanelsFabrication(StrEnum):
    """
    Sheathing Panels Fabrication.

     - Plywood: Plywood
     - OSB: OSB
     - Fiberboard: Fiberboard
    """

    PLYWOOD = "Plywood"
    OSB = "OSB"
    FIBERBOARD = "Fiberboard"


class AllFabrication(StrEnum):
    """
    Wood fabrication enumeration.

     - Plywood: Plywood
     - OSB: OSB
     - Fiberboard: Fiberboard
     - CLT: CLT
     - GLT: GLT
     - NLT: NLT
     - DLT: DLT
     - LVL: LVL
     - Bonded Strand: Bonded Strand
     - Solid hardwood: Solid hardwood
     - Engineered hardwood: Engineered hardwood
     - Bamboo: Bamboo
     - Parquet: Parquet
     - Cork: Cork
    """

    PLYWOOD = "Plywood"
    OSB = "OSB"
    FIBERBOARD = "Fiberboard"
    CLT = "CLT"
    GLT = "GLT"
    NLT = "NLT"
    DLT = "DLT"
    LVL = "LVL"
    BONDED_STRAND = "Bonded Strand"
    SOLID_HARDWOOD = "Solid hardwood"
    ENGINEERED_HARDWOOD = "Engineered hardwood"
    BAMBOO = "Bamboo"
    PARQUET = "Parquet"
    CORK = "Cork"


class AsphaltMixType(StrEnum):
    """
    Asphalt mix type.

     - WMA: WMA
     - HMA: HMA

    """

    WMA = "WMA"
    HMA = "HMA"


class EngineeredTimberSpecies(StrEnum):
    """Engineered Timber species."""

    ALASKA_CEDAR = "Alaska Cedar"
    DOUGLAS_FIR_LARCH = "Douglas Fir-Larch"
    BLACK_SPRUCE = "Black Spruce"
    WHITE_SPRUCE = "White Spruce"
    RED_SPRUCE = "Red Spruce"
    GRAND_FIR = "Grand Fir"
    WHITE_FIR = "White Fir"
    WESTERN_HEMLOCK = "Western Hemlock"
    CALIFORNIA_RED_FIR = "California Red Fir"
    NOBLE_FIR = "Noble Fir"
    PACIFIC_SILVER_FIR = "Pacific Silver Fir"
    DOUGLAS_FIR = "Douglas Fir"
    JACK_PINE = "Jack Pine"
    IDAHO_WHITE_PINE = "Idaho White Pine"
    MOUNTAIN_HEMLOCK = "Mountain Hemlock"
    ALPINE_FIR = "Alpine Fir"
    LODGEPOLE_PINE = "Lodgepole Pine"
    PONDEROSA_PINE = "Ponderosa Pine"
    SUGAR_PINE = "Sugar Pine"
    WESTERN_RED_CEDAR = "Western Red Cedar"
    ENGELMANN_SPRUCE = "Engelmann Spruce"
    DOUGLAS_FIR_SOUTH = "Douglas Fir South"
    WESTERN_LARCH = "Western Larch"
    BALSAM_FIR = "Balsam Fir"
    LOBLOLLY_PINE = "Loblolly Pine"
    SHORTLEAF_PINE = "Shortleaf Pine"
    LONGLEAF_PINE = "Longleaf Pine"
    SLASH_PINE = "Slash Pine"
    SITKA_SPRUCE = "Sitka Spruce"
    NORWAY_PINE = "Norway Pine"
    SHAGBARK_HICKORY = "Shagbark Hickory"
    MOCKERNUT_HICKORY = "Mockernut Hickory"
    PIGNUT_HICKORY = "Pignut Hickory"
    NUTMEG_HICKORY = "Nutmeg Hickory"
    AMERICAN_BEECH = "American Beech"
    WATER_HICKORY = "Water Hickory"
    YELLOW_BIRCH = "Yellow Birch"
    SWEET_BIRCH = "Sweet Birch"
    WHITE_ASH = "White Ash"
    BITTERNUT_HICKORY = "Bitternut Hickory"
    SHELLBARK_HICKORY = "Shellbark Hickory"
    NORTHERN_RED_OAK = "Northern Red Oak"
    WHITE_OAK = "White Oak"
    PECAN_HICKORY = "Pecan Hickory"
    WATER_OAK = "Water Oak"
    BLACK_MAPLE = "Black Maple"
    POST_OAK = "Post Oak"
    SCARLET_OAK = "Scarlet Oak"
    SWEETGUM_OAK = "Sweetgum Oak"
    PIN_OAK = "Pin Oak"
    SOUTHERN_RED_OAK = "Southern Red Oak"
    MIXED_OAK = "Mixed Oak"
    CHESTNUT_OAK = "Chestnut Oak"
    SWAMP_WHITE_OAK = "Swamp White Oak"
    BUR_OAK = "Bur Oak"
    BLACK_OAK = "Black Oak"
    SWAMP_CHESTNUT_OAK = "Swamp Chestnut Oak"
    RED_MAPLE = "Red Maple"
    CHERRYBARK_OAK = "Cherrybark Oak"
    LIVE_OAK = "Live Oak"
    OVERCUP_OAK = "Overcup Oak"
    LAUREL_OAK = "Laurel Oak"
    ROCK_ELM = "Rock Elm"
    YELLOW_POPLAR = "Yellow Poplar"
    AMERICAN_ELM = "American Elm"
    BLACK_ASH = "Black Ash"
    WATER_TUPULO = "Water Tupulo"
    SILVER_MAPLE = "Silver Maple"
    BIGTOOTH_ASPEN = "Bigtooth Aspen"
    EASTERN_COTTONWOOD = "Eastern Cottonwood"
    SUGAR_MAPLE = "Sugar Maple"
    QUAKING_ASPEN = "Quaking Aspen"


class WoodFlooringTimberSpecies(StrEnum):
    """
    Engineered Timber species.

     - Oak: Oak
     - Maple: Maple
     - Cherry: Cherry
     - Walnut: Walnut
     - Ash: Ash
     - Mahogany: Mahogany
     - Hickory: Hickory
     - Teak: Teak
     - Jarrah: Jarrah
     - Mesquite: Mesquite
     - Bamboo: Bamboo

    """

    OAK = "Oak"
    MAPLE = "Maple"
    CHERRY = "Cherry"
    WALNUT = "Walnut"
    ASH = "Ash"
    MAHOGANY = "Mahogany"
    HICKORY = "Hickory"
    TEAK = "Teak"
    JARRAH = "Jarrah"
    MESQUITE = "Mesquite"
    BAMBOO = "Bamboo"


class SawnTimberSpecies(StrEnum):
    """
    Sawn Timber species.

     - Alaska Cedar: Alaska Cedar
     - Alaska Hemlock: Alaska Hemlock
     - Alaska Spruce: Alaska Spruce
     - Alaska Yellow Cedar: Alaska Yellow Cedar
     - Aspen: Aspen
     - Baldcypress: Baldcypress
     - Balsam Fir: Balsam Fir
     - Beech-Birch-Hickory: Beech-Birch-Hickory
     - Coast Sitka Spruce: Coast Sitka Spruce
     - Coast Species: Coast Species
     - Cottonwood: Cottonwood
     - Douglas Fir-Larch: Douglas Fir-Larch
     - Douglas Fir-Larch (North): Douglas Fir-Larch (North)
     - Douglas Fir-South: Douglas Fir-South
     - Eastern Hemlock: Eastern Hemlock
     - Eastern Hemlock-Balsam Fir: Eastern Hemlock-Balsam Fir
     - Eastern Hemlock-Tamarack: Eastern Hemlock-Tamarack
     - Eastern Hemlock-Tamarack (North): Eastern Hemlock-Tamarack (North)
     - Eastern Softwoods: Eastern Softwoods
     - Eastern Spruce: Eastern Spruce
     - Eastern White Pine: Eastern White Pine
     - Eastern White Pine (North): Eastern White Pine (North)
     - Hem-Fir: Hem-Fir
     - Hem-Fir (North): Hem-Fir (North)
     - Mixed Maple: Mixed Maple
     - Mixed Oak: Mixed Oak
     - Mixed Southern Pine: Mixed Southern Pine
     - Mountain Hemlock: Mountain Hemlock
     - Northern Pine: Northern Pine
     - Northern Red Oak: Northern Red Oak
     - Northern Species: Northern Species
     - Northern White Cedar: Northern White Cedar
     - Ponderosa Pine: Ponderosa Pine
     - Red Maple: Red Maple
     - Red Oak: Red Oak
     - Red Pine: Red Pine
     - Redwood: Redwood
     - Sitka Spruce: Sitka Spruce
     - Southern Pine: Southern Pine
     - Spruce-Pine-Fir: Spruce-Pine-Fir
     - Scots Pine: Scots Pine
     - Spruce-Pine-Fir (South): Spruce-Pine-Fir (South)
     - Western Cedars: Western Cedars
     - Western Cedars (North): Western Cedars (North)
     - Western Hemlock: Western Hemlock
     - Western Hemlock (North): Western Hemlock (North)
     - Western White Pine: Western White Pine
     - Western Woods: Western Woods
     - White Oak: White Oak
     - Yellow Cedar: Yellow Cedar
     - Yellow Poplar: Yellow Poplar

    """

    ALASKA_CEDAR = "Alaska Cedar"
    ALASKA_HEMLOCK = "Alaska Hemlock"
    ALASKA_SPRUCE = "Alaska Spruce"
    ALASKA_YELLOW_CEDAR = "Alaska Yellow Cedar"
    ASPEN = "Aspen"
    BALDCYPRESS = "Baldcypress"
    BALSAM_FIR = "Balsam Fir"
    BEECH_BIRCH_HICKORY = "Beech-Birch-Hickory"
    COAST_SITKA_SPRUCE = "Coast Sitka Spruce"
    COAST_SPECIES = "Coast Species"
    COTTONWOOD = "Cottonwood"
    DOUGLAS_FIR_LARCH = "Douglas Fir-Larch"
    DOUGLAS_FIR_LARCH_NORTH = "Douglas Fir-Larch (North)"
    DOUGLAS_FIR_SOUTH = "Douglas Fir-South"
    EASTERN_HEMLOCK = "Eastern Hemlock"
    EASTERN_HEMLOCK_BALSAM_FIR = "Eastern Hemlock-Balsam Fir"
    EASTERN_HEMLOCK_TAMARACK = "Eastern Hemlock-Tamarack"
    EASTERN_HEMLOCK_TAMARACK_NORTH = "Eastern Hemlock-Tamarack (North)"
    EASTERN_SOFTWOODS = "Eastern Softwoods"
    EASTERN_SPRUCE = "Eastern Spruce"
    EASTERN_WHITE_PINE = "Eastern White Pine"
    EASTERN_WHITE_PINE_NORTH = "Eastern White Pine (North)"
    HEM_FIR = "Hem-Fir"
    HEM_FIR_NORTH = "Hem-Fir (North)"
    MIXED_MAPLE = "Mixed Maple"
    MIXED_OAK = "Mixed Oak"
    MIXED_SOUTHERN_PINE = "Mixed Southern Pine"
    MOUNTAIN_HEMLOCK = "Mountain Hemlock"
    NORTHERN_PINE = "Northern Pine"
    NORTHERN_RED_OAK = "Northern Red Oak"
    NORTHERN_SPECIES = "Northern Species"
    NORTHERN_WHITE_CEDAR = "Northern White Cedar"
    PONDEROSA_PINE = "Ponderosa Pine"
    RED_MAPLE = "Red Maple"
    RED_OAK = "Red Oak"
    RED_PINE = "Red Pine"
    REDWOOD = "Redwood"
    SITKA_SPRUCE = "Sitka Spruce"
    SOUTHERN_PINE = "Southern Pine"
    SPRUCE_PINE_FIR = "Spruce-Pine-Fir"
    SCOTS_PINE = "Scots Pine"
    SPRUCE_PINE_FIR_SOUTH = "Spruce-Pine-Fir (South)"
    WESTERN_CEDARS = "Western Cedars"
    WESTERN_CEDARS_NORTH = "Western Cedars (North)"
    WESTERN_HEMLOCK = "Western Hemlock"
    WESTERN_HEMLOCK_NORTH = "Western Hemlock (North)"
    WESTERN_WHITE_PINE = "Western White Pine"
    WESTERN_WOODS = "Western Woods"
    WHITE_OAK = "White Oak"
    YELLOW_CEDAR = "Yellow Cedar"
    YELLOW_POPLAR = "Yellow Poplar"


class AllTimberSpecies(StrEnum):
    """
    All timber species.

     - Oak: Oak
     - Maple: Maple
     - Cherry: Cherry
     - Walnut: Walnut
     - Ash: Ash
     - Mahogany: Mahogany
     - Hickory: Hickory
     - Teak: Teak
     - Jarrah: Jarrah
     - Mesquite: Mesquite
     - Bamboo: Bamboo
     - Alaska Cedar: Alaska Cedar
     - Alaska Hemlock: Alaska Hemlock
     - Alaska Spruce: Alaska Spruce
     - Alaska Yellow Cedar: Alaska Yellow Cedar
     - Aspen: Aspen
     - Baldcypress: Baldcypress
     - Balsam Fir: Balsam Fir
     - Beech-Birch-Hickory: Beech-Birch-Hickory
     - Coast Sitka Spruce: Coast Sitka Spruce
     - Coast Species: Coast Species
     - Cottonwood: Cottonwood
     - Douglas Fir-Larch: Douglas Fir-Larch
     - Douglas Fir-Larch (North): Douglas Fir-Larch (North)
     - Douglas Fir-South: Douglas Fir-South
     - Eastern Hemlock: Eastern Hemlock
     - Eastern Hemlock-Balsam Fir: Eastern Hemlock-Balsam Fir
     - Eastern Hemlock-Tamarack: Eastern Hemlock-Tamarack
     - Eastern Hemlock-Tamarack (North): Eastern Hemlock-Tamarack (North)
     - Eastern Softwoods: Eastern Softwoods
     - Eastern Spruce: Eastern Spruce
     - Eastern White Pine: Eastern White Pine
     - Eastern White Pine (North): Eastern White Pine (North)
     - Hem-Fir: Hem-Fir
     - Hem-Fir (North): Hem-Fir (North)
     - Mixed Maple: Mixed Maple
     - Mixed Oak: Mixed Oak
     - Mixed Southern Pine: Mixed Southern Pine
     - Mountain Hemlock: Mountain Hemlock
     - Northern Pine: Northern Pine
     - Northern Red Oak: Northern Red Oak
     - Northern Species: Northern Species
     - Northern White Cedar: Northern White Cedar
     - Ponderosa Pine: Ponderosa Pine
     - Red Maple: Red Maple
     - Red Oak: Red Oak
     - Red Pine: Red Pine
     - Redwood: Redwood
     - Sitka Spruce: Sitka Spruce
     - Southern Pine: Southern Pine
     - Spruce-Pine-Fir: Spruce-Pine-Fir
     - Scots Pine: Scots Pine
     - Spruce-Pine-Fir (South): Spruce-Pine-Fir (South)
     - Western Cedars: Western Cedars
     - Western Cedars (North): Western Cedars (North)
     - Western Hemlock: Western Hemlock
     - Western Hemlock (North): Western Hemlock (North)
     - Western White Pine: Western White Pine
     - Western Woods: Western Woods
     - White Oak: White Oak
     - Yellow Cedar: Yellow Cedar
     - Yellow Poplar: Yellow Poplar

    """

    OAK = "Oak"
    MAPLE = "Maple"
    CHERRY = "Cherry"
    WALNUT = "Walnut"
    ASH = "Ash"
    MAHOGANY = "Mahogany"
    HICKORY = "Hickory"
    TEAK = "Teak"
    JARRAH = "Jarrah"
    MESQUITE = "Mesquite"
    BAMBOO = "Bamboo"
    ALASKA_CEDAR = "Alaska Cedar"
    ALASKA_HEMLOCK = "Alaska Hemlock"
    ALASKA_SPRUCE = "Alaska Spruce"
    ALASKA_YELLOW_CEDAR = "Alaska Yellow Cedar"
    ASPEN = "Aspen"
    BALDCYPRESS = "Baldcypress"
    BALSAM_FIR = "Balsam Fir"
    BEECH_BIRCH_HICKORY = "Beech-Birch-Hickory"
    COAST_SITKA_SPRUCE = "Coast Sitka Spruce"
    COAST_SPECIES = "Coast Species"
    COTTONWOOD = "Cottonwood"
    DOUGLAS_FIR_LARCH = "Douglas Fir-Larch"
    DOUGLAS_FIR_LARCH_NORTH = "Douglas Fir-Larch (North)"
    DOUGLAS_FIR_SOUTH = "Douglas Fir-South"
    EASTERN_HEMLOCK = "Eastern Hemlock"
    EASTERN_HEMLOCK_BALSAM_FIR = "Eastern Hemlock-Balsam Fir"
    EASTERN_HEMLOCK_TAMARACK = "Eastern Hemlock-Tamarack"
    EASTERN_HEMLOCK_TAMARACK_NORTH = "Eastern Hemlock-Tamarack (North)"
    EASTERN_SOFTWOODS = "Eastern Softwoods"
    EASTERN_SPRUCE = "Eastern Spruce"
    EASTERN_WHITE_PINE = "Eastern White Pine"
    EASTERN_WHITE_PINE_NORTH = "Eastern White Pine (North)"
    HEM_FIR = "Hem-Fir"
    HEM_FIR_NORTH = "Hem-Fir (North)"
    MIXED_MAPLE = "Mixed Maple"
    MIXED_OAK = "Mixed Oak"
    MIXED_SOUTHERN_PINE = "Mixed Southern Pine"
    MOUNTAIN_HEMLOCK = "Mountain Hemlock"
    NORTHERN_PINE = "Northern Pine"
    NORTHERN_RED_OAK = "Northern Red Oak"
    NORTHERN_SPECIES = "Northern Species"
    NORTHERN_WHITE_CEDAR = "Northern White Cedar"
    PONDEROSA_PINE = "Ponderosa Pine"
    RED_MAPLE = "Red Maple"
    RED_OAK = "Red Oak"
    RED_PINE = "Red Pine"
    REDWOOD = "Redwood"
    SITKA_SPRUCE = "Sitka Spruce"
    SOUTHERN_PINE = "Southern Pine"
    SPRUCE_PINE_FIR = "Spruce-Pine-Fir"
    SCOTS_PINE = "Scots Pine"
    SPRUCE_PINE_FIR_SOUTH = "Spruce-Pine-Fir (South)"
    WESTERN_CEDARS = "Western Cedars"
    WESTERN_CEDARS_NORTH = "Western Cedars (North)"
    WESTERN_HEMLOCK = "Western Hemlock"
    WESTERN_HEMLOCK_NORTH = "Western Hemlock (North)"
    WESTERN_WHITE_PINE = "Western White Pine"
    WESTERN_WOODS = "Western Woods"
    WHITE_OAK = "White Oak"
    YELLOW_CEDAR = "Yellow Cedar"
    YELLOW_POPLAR = "Yellow Poplar"


class HardwareFunction(StrEnum):
    """
    Hardware function.

     - Lock: Lock
     - Hinge: Hinge
     - Handle: Handle
     - Operator: Operator
     - Balance: Balance
     - Other: Other

    """

    LOCK = "Lock"
    HINGE = "Hinge"
    HANDLE = "Handle"
    OPERATOR = "Operator"
    BALANCE = "Balance"
    OTHER = "Other"


class AccessFlooringFinishMaterial(StrEnum):
    """
    Access flooring finish material.

     - Linoleum: Linoleum
     - Vinyl: Vinyl
     - HPL: HPL
     - Solid hardwood: Solid hardwood
     - Engineered hardwood: Engineered hardwood
     - Poured Terrazzo: Poured Terrazzo
     - Epoxy Terrazzo: Epoxy Terrazzo
     - Concrete Terrazzo: Concrete Terrazzo
     - Rubber: Rubber
     - Porcelain: Porcelain
     - Other: Other
     - None: None

    """

    LINOLEUM = "Linoleum"
    VINYL = "Vinyl"
    HPL = "HPL"
    SOLID_HARDWOOD = "Solid hardwood"
    ENGINEERED_HARDWOOD = "Engineered hardwood"
    POURED_TERRAZZO = "Poured Terrazzo"
    EPOXY_TERRAZZO = "Epoxy Terrazzo"
    CONCRETE_TERRAZZO = "Concrete Terrazzo"
    RUBBER = "Rubber"
    PORCELAIN = "Porcelain"
    OTHER = "Other"
    NONE = "None"


class AccessFlooringSeismicRating(StrEnum):
    """
    Access flooring seismic rating.

     - Type 0: Type 0
     - Type 1: Type 1
     - Type 2: Type 2
     - Type 3: Type 3
     - Type 4: Type 4
     - Type 5: Type 5

    """

    TYPE_0 = "Type 0"
    TYPE_1 = "Type 1"
    TYPE_2 = "Type 2"
    TYPE_3 = "Type 3"
    TYPE_4 = "Type 4"
    TYPE_5 = "Type 5"


class CarpetManufactureType(StrEnum):
    """
    Carpet manufacture type.

     - Tufted: Tufted
     - Needlefelt: Needlefelt

    """

    TUFTED = "Tufted"
    NEEDLEFELT = "Needlefelt"


class AdmixtureEffects(StrEnum):
    """
    Admixture effects.

     - Air Entrainer: Air Entrainer
     - Water Reducer: Water Reducer
     - Retarding: Retarding
     - Accelerating: Accelerating
     - Superplasticizer: Superplasticizer
     - Corrosion Inhibitor: Corrosion Inhibitor
     - Shrinkage Control: Shrinkage Control
     - Other: Other

    """

    AIR_ENTRAINER = "Air Entrainer"
    WATER_REDUCER = "Water Reducer"
    RETARDING = "Retarding"
    ACCELERATING = "Accelerating"
    SUPERPLASTICIZER = "Superplasticizer"
    CORROSION_INHIBITOR = "Corrosion Inhibitor"
    SHRINKAGE_CONTROL = "Shrinkage Control"
    OTHER = "Other"


class TextilesFabricType(StrEnum):
    """
    Textiles fabric type.

     - Leather: Leather
     - Cotton: Cotton
     - Wool: Wool
     - Polyester: Polyester
     - Acrylic: Acrylic
     - Nylon: Nylon
     - HMW Polymer: HMW Polymer
     - Other Plant Fiber: Other Plant Fiber
     - Mineral Fiber: Mineral Fiber
     - Other Synthetic Fiber: Other Synthetic Fiber

    """

    LEATHER = "Leather"
    COTTON = "Cotton"
    WOOL = "Wool"
    POLYESTER = "Polyester"
    ACRYLIC = "Acrylic"
    NYLON = "Nylon"
    HMW_POLYMER = "HMW Polymer"
    OTHER_PLANT_FIBER = "Other Plant Fiber"
    MINERAL_FIBER = "Mineral Fiber"
    OTHER_SYNTHETIC_FIBER = "Other Synthetic Fiber"


class GypsumFacing(StrEnum):
    """
    Gypsum facing.

     - Paper: Paper
     - Glass mat: Glass mat

    """

    PAPER = "Paper"
    GLASS_MAT = "Glass mat"


class InsulatingMaterial(StrEnum):
    """
    Insulating material.

     - Mineral Wool: Mineral Wool
     - Cellulose: Cellulose
     - Fiberglass: Fiberglass
     - XPS: XPS
     - GPS: GPS
     - Polyisocyanurate: Polyisocyanurate
     - Expanded Polyethylene: Expanded Polyethylene
     - EPS: EPS
     - Other: Other

    """

    MINERAL_WOOL = "Mineral Wool"
    CELLULOSE = "Cellulose"
    FIBERGLASS = "Fiberglass"
    XPS = "XPS"
    GPS = "GPS"
    POLYISOCYANURATE = "Polyisocyanurate"
    EXPANDED_POLYETHYLENE = "Expanded Polyethylene"
    EPS = "EPS"
    OTHER = "Other"


class ThermalSeparation(StrEnum):
    """
    Thermal separation.

     - Aluminium: Aluminium
     - Steel: Steel
     - Thermally Improved Metal: Thermally Improved Metal
     - Thermally Broken Metal: Thermally Broken Metal
     - Nonmetal: Nonmetal

    """

    ALUMINIUM = "Aluminium"
    STEEL = "Steel"
    THERMALLY_IMPROVED_METAL = "Thermally Improved Metal"
    THERMALLY_BROKEN_METAL = "Thermally Broken Metal"
    NONMETAL = "Nonmetal"


class CementScm(StrEnum):
    """
    Cement scm.

     - ggbs: ggbs
     - flyAsh: flyAsh
     - natPoz: natPoz
     - siFume: siFume
     - gg45: gg45
     - mk: mk
     - CaCO3: CaCO3
     - other: other

    """

    GGBS = "ggbs"
    FLYASH = "flyAsh"
    NATPOZ = "natPoz"
    SIFUME = "siFume"
    GG45 = "gg45"
    MK = "mk"
    CACO3 = "CaCO3"
    OTHER = "other"


class C1157(StrEnum):
    """
    C1157.

     - GU: GU
     - HE: HE
     - MS: MS
     - HS: HS
     - MH: MH
     - LH: LH

    """

    GU = "GU"
    HE = "HE"
    MS = "MS"
    HS = "HS"
    MH = "MH"
    LH = "LH"


class AhuAirflowControl(StrEnum):
    """
    Ahu airflow control.

     - CAV: CAV
     - VAV: VAV

    """

    CAV = "CAV"
    VAV = "VAV"


class CarpetFormFactor(StrEnum):
    """
    Carpet form factor.

     - Tiles: Tiles
     - Broadloom: Broadloom

    """

    TILES = "Tiles"
    BROADLOOM = "Broadloom"


class CladdingInsulatingMaterial(StrEnum):
    """
    Cladding insulating material.

     - No Insulation: No Insulation
     - Mineral Wool: Mineral Wool
     - Gypsum: Gypsum
     - EPS: EPS
     - XPS: XPS
     - GPS: GPS
     - Polyiso: Polyiso
     - PE: PE
     - Other: Other

    """

    NO_INSULATION = "No Insulation"
    MINERAL_WOOL = "Mineral Wool"
    GYPSUM = "Gypsum"
    EPS = "EPS"
    XPS = "XPS"
    GPS = "GPS"
    POLYISO = "Polyiso"
    PE = "PE"
    OTHER = "Other"


class SidingFormFactor(StrEnum):
    """
    Siding form factor.

     - Lap: Lap
     - Vertical: Vertical
     - Shake & Shingle: Shake & Shingle

    """

    LAP = "Lap"
    VERTICAL = "Vertical"
    SHAKE_SHINGLE = "Shake & Shingle"


class FloorBoxFloorMaterial(StrEnum):
    """
    Floor box floor material.

     - Concrete: Concrete
     - Wood: Wood
     - Other: Other

    """

    CONCRETE = "Concrete"
    WOOD = "Wood"
    OTHER = "Other"
