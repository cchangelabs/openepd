#
#  Copyright 2023 by C Change Labs Inc. www.c-change-labs.com
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
import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Measurement


class EolScenario(BaseOpenEpdSchema):
    """
    A scenario for end-of-life.

    If a particular implementation commits to a specific scenario, then that value can be used;
    otherwise the outcomes can be statistically combined.
    """

    name: str = pyd.Field(
        max_length=40,
        example="Landfill",
        description="A brief text description of the scenario, preferably from list eol_scenario_names",
    )
    likelihood: float | None = pyd.Field(
        description="The weigting of this scenario used in the C1 .. C4 dataset. For example, the overall C1 shoudl be "
        "equal to weighted sum of C1 from all the scenarios, weighted by likelihood.",
        example=0.33,
    )
    C1: Measurement | None = pyd.Field(description="Deconstruction and Demolition under this scenario")
    C2: Measurement | None = pyd.Field(description="Transport to waste processing or disposal under this scenario.")
    C3: Measurement | None = pyd.Field(description="Waste Processing under this scenario")
    C4: Measurement | None = pyd.Field(description="Disposal under this scenario")
    D: Measurement | None = pyd.Field(
        description="Potential net benefits from reuse, recycling, and/or energy recovery beyond "
        "the system boundary under this scenario"
    )


class ScopeSet(BaseOpenEpdSchema):
    """
    A set of scopes, such as A1..A5, B1..B7, C1..C4, D, etc.

    Any scopes with no entry are considered 'measure not declared' (null) rather than zero.
    The 'unit' field must be consistent across all scopes in a single scopeset.
    """

    A1A2A3: Measurement | None = pyd.Field(description="Sum of A1..A3")
    A1: Measurement | None = pyd.Field(description="Raw Material Supply")
    A2: Measurement | None = pyd.Field(description="Transport to Manufacturing")
    A3: Measurement | None = pyd.Field(description="Manufacturing")
    A4: Measurement | None = pyd.Field(description="Transport to Construction")
    A5: Measurement | None = pyd.Field(description="Construction")
    B1: Measurement | None = pyd.Field(description="Use impacts over Reference Service Life (Predicted)")
    B1_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B1 is evaluated, in years. "
        "For example, an impact of 1.23 kgCO2e per year for ten years could be B1=1.23kgCO2e, "
        "B1_years=1.0 or  B1=12.3kgCO2e, B1_years=10.0",
    )
    B2: Measurement | None = pyd.Field(description="Predicted Maintenance Impacts over Reference Service Life")
    B2_years: float | None = pyd.Field(
        gt=0, lt=11, description="Predicted Maintenance Impacts over Reference Service Life"
    )
    B3: Measurement | None = pyd.Field(description="Predicted Repair impacts over Reference Service Life")
    B3_years: float | None = pyd.Field(gt=0, lt=11, description="Timeframe over which B3 is evaluated, in years")
    B4: Measurement | None = pyd.Field(
        description="Predicted Replacement Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR."
    )
    B4_years: float | None = pyd.Field(gt=0, lt=11, description="Timeframe over which B4 is evaluated, in years")
    B5: Measurement | None = pyd.Field(
        description="Predicted Refurbishment Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR."
    )
    B5_years: float | None = pyd.Field(gt=0, lt=11, description="Timeframe over which B5 is evaluated, in years")
    B6: Measurement | None = pyd.Field(description="Predicted Impacts related to Operational Energy Use")
    B6_years: float | None = pyd.Field(gt=0, lt=11, description="Timeframe over which B6 is evaluated, in years")
    B7: Measurement | None = pyd.Field(description="Predicted Impacts related to Operational Water Use")
    B7_years: float | None = pyd.Field(gt=0, lt=11, description="Timeframe over which B7 is evaluated, in years")
    C_scenarios: list[EolScenario] | None = pyd.Field(
        description="A list of possible end-of-life scenarios, "
        "for use in analyses where the end-of-life can be predicted."
    )
    C1: Measurement | None = pyd.Field(description="Deconstruction and Demolition")
    C2: Measurement | None = pyd.Field(description="Transport to waste processing or disposal.")
    C3: Measurement | None = pyd.Field(description="Waste Processing")
    C4: Measurement | None = pyd.Field(description="Disposal")
    D: Measurement | None = pyd.Field(
        description="Potential net benefits from reuse, recycling, and/or energy recovery beyond the system boundary."
    )


class ImpactSet(BaseOpenEpdSchema):
    """A set of impacts, such as GWP, ODP, AP, EP, POCP, EP-marine, EP-terrestrial, EP-freshwater, etc."""

    gwp: ScopeSet | None = pyd.Field(
        description="GWP100, calculated per IPCC guidelines.  If any CO2 removals are "
        "part of this figure, the gwp-fossil, gwp-bioganic, gwp-luluc, an "
        "gwp-nonCO2 fields are required, as is "
        "kg_C_biogenic_per_declared_unit."
    )
    odp: ScopeSet | None = pyd.Field(description="Ozone Depletion Potential")
    ap: ScopeSet | None = pyd.Field(description="Acidification Potential")
    ep: ScopeSet | None = pyd.Field(
        description="Eutrophication Potential in Marine Ecosystems. Has the same meaning as ep-marine."
    )
    pocp: ScopeSet | None = pyd.Field(description="Photochemical Smog (Ozone) creation potential")
    ep_marine: ScopeSet | None = pyd.Field(alias="ep-marine", description="Has the same meaning as 'ep'")
    ep_fresh: ScopeSet | None = pyd.Field(
        alias="ep-fresh", description="Eutrophication Potential in Freshwater Ecosystems"
    )
    ep_terr: ScopeSet | None = pyd.Field(
        alias="ep-terr", description="Eutrophication Potential in Terrestrial Ecosystems"
    )
    gwp_biogenic: ScopeSet | None = pyd.Field(
        alias="gwp-biogenic",
        description="Net GWP from removals of atmospheric CO2 into biomass and  emissions of CO2 from biomass sources. "
        "To be counted as negative, CO2 removals must be closely linked to production in "
        "operational control (i.e. no purchased offsets), time (within three years of production) and "
        "space (similar biome).  They must not have been sold, committed, or credited to any other "
        "product.  Harvesting from native forests is handled under GWP_luluc for EN15804.",
    )
    gwp_luluc: ScopeSet | None = pyd.Field(
        alias="gwp-luluc",
        description="Climate change effects related to land use and land use change, for example biogenic carbon "
        "exchanges resulting from deforestation or other soil activities (including soil carbon "
        "emissions). All related emissions for native forests are included under this category. "
        "Uptake for native forests is set to 0 kgCO2 for EN15804.",
    )
    gwp_nonCO2: ScopeSet | None = pyd.Field(
        alias="gwp-nonCO2",
        description="GWP from non-CO2, non-fossil sources, such as livestock-sourced CH4 and agricultural N2O.",
    )


class ResourceUseSet(BaseOpenEpdSchema):
    """A set of resource use indicators, such as RPRec, RPRm, etc."""

    RPRec: ScopeSet | None = pyd.Field(
        description="Renewable primary resources used as energy carrier (fuel). "
        "First use bio-based materials used as an energy source. Hydropower, solar and wind power used "
        "in the technosphere are also included in this indicator"
    )
    RPRm: ScopeSet | None = pyd.Field(
        description="Renewable primary resources with energy content used as material. "
        "First use biobased materials used as materials (e.g. wood, hemp, etc.)."
    )


class OutputFlowSet(BaseOpenEpdSchema):
    """A set of output flows, such as waste, emissions, etc."""

    hwd: ScopeSet | None = pyd.Field(description="Hazardous waste disposed")
