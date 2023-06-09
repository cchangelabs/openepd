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
from enum import StrEnum

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
    gwp_fossil: ScopeSet | None = pyd.Field(
        alias="gwp-fossil",
        description="Climate change effects due to greenhouse gas emissions originating from the oxidation or "
        "reduction of fossil fuels or materials containing fossil carbon. [Source: EN15804]",
    )


class LCIAMethod(StrEnum):
    """A list of available LCA methods."""

    UNKNOWN = "Unknown LCIA"
    TRACI_2_1 = "TRACI 2.1"
    TRACI_2_0 = "TRACI 2.0"
    TRACI_1_0 = "TRACI 1.0"
    IPCC_AR5 = "IPCC AR5"
    EF_3_0 = "EF 3.0"
    EF_3_1 = "EF 3.1"
    EF_2_0 = "EF 2.0"
    EN_15978_2011 = "EN 15978:2011"
    USETOX_2_12 = "USEtox 2.12"
    CML_2016 = "CML 2016"
    CML_2012 = "CML 2012"
    CML_2007 = "CML 2007"
    CML_2001 = "CML 2001"
    CML_1992 = "CML 1992"
    RECIPE_2016 = "ReCiPe 2016"
    RECIPE_2008 = "ReCiPe 2008"

    @classmethod
    def is_method_supported(cls, method_name: str | None) -> bool:
        """Return True if the method is supported, False otherwise."""
        if method_name is None:
            return False
        try:
            cls(method_name)
        except ValueError:
            return False
        return True

    @classmethod
    def get_by_name(cls, d_name: str | None) -> "LCIAMethod":
        """Return the LCIAMethod enum value for the given name, or UNKNOWN if not found."""
        if d_name is None:
            return cls.UNKNOWN
        try:
            return cls(d_name)
        except ValueError:
            return cls.UNKNOWN


class Impacts(dict[LCIAMethod, ImpactSet]):
    """List of environmental impacts, compiled per one of the standard Impact Assessment methods."""

    def set_unknown_lcia(self, impact_set: ImpactSet):
        """Set the impact set as an unknown LCIA method."""
        self[LCIAMethod.UNKNOWN] = impact_set

    def set_impact_set(self, lcia_method: LCIAMethod | str | None, impact_set: ImpactSet):
        """
        Set the impact set for the given LCIA method.

        If the LCIA method is None, set it as an unknown LCIA method.
        """
        if lcia_method is None:
            self.set_unknown_lcia(impact_set)
        else:
            if isinstance(lcia_method, str):
                lcia_method = LCIAMethod.get_by_name(lcia_method)
            self[lcia_method] = impact_set

    def available_methods(self) -> set[LCIAMethod]:
        """Return a list of available LCIA methods."""
        return set(self.keys())


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
    rpre: ScopeSet | None = pyd.Field(description="Renewable primary energy resources as energy")
    nrpre: ScopeSet | None = pyd.Field(description="Non-renewable primary resources as energy (fuel)")
    nrprm: ScopeSet | None = pyd.Field(description="Non-renewable primary resources as material")
    fw: ScopeSet | None = pyd.Field(description="Use of net fresh water")
    sm: ScopeSet | None = pyd.Field(description="Use of secondary materials")
    rsf: ScopeSet | None = pyd.Field(description="Use of renewable secondary materials")
    nrsf: ScopeSet | None = pyd.Field(description="Use of non-renewable secondary fuels")
    re: ScopeSet | None = pyd.Field(description="Renewable energy resources")
    pere: ScopeSet | None = pyd.Field(
        description="Use of renewable primary energy excluding renewable primary energy resources used as raw materials"
    )
    perm: ScopeSet | None = pyd.Field(description="Use of renewable primary energy resources used as raw materials")
    pert: ScopeSet | None = pyd.Field(description="Total use of renewable primary energy resources")
    penre: ScopeSet | None = pyd.Field(
        description="Use of non-renewable primary energy excluding "
        "non-renewable primary energy resources used as raw materials"
    )
    penrm: ScopeSet | None = pyd.Field(
        description="Use of non-renewable primary energy resources used as raw materials"
    )
    penrt: ScopeSet | None = pyd.Field(description="Total use of non-renewable primary energy resources")


class OutputFlowSet(BaseOpenEpdSchema):
    """A set of output flows, such as waste, emissions, etc."""

    twd: ScopeSet | None = pyd.Field(description="Total waste disposed")
    hwd: ScopeSet | None = pyd.Field(description="Hazardous waste disposed")
    nhwd: ScopeSet | None = pyd.Field(description="Non-hazardous waste disposed")
    rwd: ScopeSet | None = pyd.Field(description="Radioactive waste disposed")
    hlrw: ScopeSet | None = pyd.Field(description="High level radioactive waste disposed")
    illrw: ScopeSet | None = pyd.Field(description="Intermediate level radioactive waste disposed")
    cru: ScopeSet | None = pyd.Field(description="Components for re-use")
    mr: ScopeSet | None = pyd.Field(description="Recycled materials")
    mfr: ScopeSet | None = pyd.Field(description="Materials for recycling")
    mer: ScopeSet | None = pyd.Field(description="Materials for energy recovery")
    ee: ScopeSet | None = pyd.Field(description="Exported energy")
    eh: ScopeSet | None = pyd.Field(description="Exported heat")
