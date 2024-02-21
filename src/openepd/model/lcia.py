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
        default=None,
    )
    C1: Measurement | None = pyd.Field(
        description="Deconstruction and Demolition under this scenario",
        default=None,
    )
    C2: Measurement | None = pyd.Field(
        description="Transport to waste processing or disposal under this scenario.",
        default=None,
    )
    C3: Measurement | None = pyd.Field(
        description="Waste Processing under this scenario",
        default=None,
    )
    C4: Measurement | None = pyd.Field(
        description="Disposal under this scenario",
        default=None,
    )
    D: Measurement | None = pyd.Field(
        description="Potential net benefits from reuse, recycling, and/or energy recovery beyond "
        "the system boundary under this scenario",
        default=None,
    )


class ScopeSet(BaseOpenEpdSchema):
    """
    A set of scopes, such as A1..A5, B1..B7, C1..C4, D, etc.

    Any scopes with no entry are considered 'measure not declared' (null) rather than zero.
    The 'unit' field must be consistent across all scopes in a single scopeset.
    """

    A1A2A3: Measurement | None = pyd.Field(
        description="Sum of A1..A3",
        default=None,
    )
    A1: Measurement | None = pyd.Field(
        description="Raw Material Supply",
        default=None,
    )
    A2: Measurement | None = pyd.Field(
        description="Transport to Manufacturing",
        default=None,
    )
    A3: Measurement | None = pyd.Field(
        description="Manufacturing",
        default=None,
    )
    A4: Measurement | None = pyd.Field(
        description="Transport to Construction",
        default=None,
    )
    A5: Measurement | None = pyd.Field(
        description="Construction",
        default=None,
    )
    B1: Measurement | None = pyd.Field(
        description="Use impacts over Reference Service Life (Predicted)",
        default=None,
    )
    B1_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B1 is evaluated, in years. "
        "For example, an impact of 1.23 kgCO2e per year for ten years could be B1=1.23kgCO2e, "
        "B1_years=1.0 or  B1=12.3kgCO2e, B1_years=10.0",
        default=None,
    )
    B2: Measurement | None = pyd.Field(
        description="Predicted Maintenance Impacts over Reference Service Life",
        default=None,
    )
    B2_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Predicted Maintenance Impacts over Reference Service Life",
        default=None,
    )
    B3: Measurement | None = pyd.Field(
        description="Predicted Repair impacts over Reference Service Life",
        default=None,
    )
    B3_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B3 is evaluated, in years",
        default=None,
    )
    B4: Measurement | None = pyd.Field(
        description="Predicted Replacement Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR.",
        default=None,
    )
    B4_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B4 is evaluated, in years",
        default=None,
    )
    B5: Measurement | None = pyd.Field(
        description="Predicted Refurbishment Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR.",
        default=None,
    )
    B5_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B5 is evaluated, in years",
        default=None,
    )
    B6: Measurement | None = pyd.Field(
        description="Predicted Impacts related to Operational Energy Use",
        default=None,
    )
    B6_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B6 is evaluated, in years",
        default=None,
    )
    B7: Measurement | None = pyd.Field(
        description="Predicted Impacts related to Operational Water Use",
        default=None,
    )
    B7_years: float | None = pyd.Field(
        gt=0,
        lt=11,
        description="Timeframe over which B7 is evaluated, in years",
        default=None,
    )
    C_scenarios: list[EolScenario] | None = pyd.Field(
        description="A list of possible end-of-life scenarios, "
        "for use in analyses where the end-of-life can be predicted.",
        default=None,
    )
    C1: Measurement | None = pyd.Field(
        description="Deconstruction and Demolition",
        default=None,
    )
    C2: Measurement | None = pyd.Field(
        description="Transport to waste processing or disposal.",
        default=None,
    )
    C3: Measurement | None = pyd.Field(
        description="Waste Processing",
        default=None,
    )
    C4: Measurement | None = pyd.Field(
        description="Disposal",
        default=None,
    )
    D: Measurement | None = pyd.Field(
        default=None,
        description="Potential net benefits from reuse, recycling, and/or energy recovery beyond the system boundary.",
    )


class ImpactSet(BaseOpenEpdSchema):
    """A set of impacts, such as GWP, ODP, AP, EP, POCP, EP-marine, EP-terrestrial, EP-freshwater, etc."""

    gwp: ScopeSet | None = pyd.Field(
        default=None,
        description="GWP100, calculated per IPCC guidelines.  If any CO2 removals are "
        "part of this figure, the gwp-fossil, gwp-bioganic, gwp-luluc, an "
        "gwp-nonCO2 fields are required, as is "
        "kg_C_biogenic_per_declared_unit.",
    )
    odp: ScopeSet | None = pyd.Field(default=None, description="Ozone Depletion Potential")
    ap: ScopeSet | None = pyd.Field(default=None, description="Acidification Potential")
    ep: ScopeSet | None = pyd.Field(
        default=None, description="Eutrophication Potential in Marine Ecosystems. Has the same meaning as ep-marine."
    )
    pocp: ScopeSet | None = pyd.Field(default=None, description="Photochemical Smog (Ozone) creation potential")
    ep_marine: ScopeSet | None = pyd.Field(alias="ep-marine", default=None, description="Has the same meaning as 'ep'")
    ep_fresh: ScopeSet | None = pyd.Field(
        alias="ep-fresh", default=None, description="Eutrophication Potential in Freshwater Ecosystems"
    )
    ep_terr: ScopeSet | None = pyd.Field(
        alias="ep-terr", default=None, description="Eutrophication Potential in Terrestrial Ecosystems"
    )
    gwp_biogenic: ScopeSet | None = pyd.Field(
        alias="gwp-biogenic",
        default=None,
        description="Net GWP from removals of atmospheric CO2 into biomass and  emissions of CO2 from biomass sources. "
        "To be counted as negative, CO2 removals must be closely linked to production in "
        "operational control (i.e. no purchased offsets), time (within three years of production) and "
        "space (similar biome).  They must not have been sold, committed, or credited to any other "
        "product.  Harvesting from native forests is handled under GWP_luluc for EN15804.",
    )
    gwp_luluc: ScopeSet | None = pyd.Field(
        alias="gwp-luluc",
        default=None,
        description="Climate change effects related to land use and land use change, for example biogenic carbon "
        "exchanges resulting from deforestation or other soil activities (including soil carbon "
        "emissions). All related emissions for native forests are included under this category. "
        "Uptake for native forests is set to 0 kgCO2 for EN15804.",
    )
    gwp_nonCO2: ScopeSet | None = pyd.Field(
        alias="gwp-nonCO2",
        default=None,
        description="GWP from non-CO2, non-fossil sources, such as livestock-sourced CH4 and agricultural N2O.",
    )
    gwp_fossil: ScopeSet | None = pyd.Field(
        alias="gwp-fossil",
        default=None,
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


class Impacts(pyd.BaseModel):
    """List of environmental impacts, compiled per one of the standard Impact Assessment methods."""

    __root__: dict[LCIAMethod, ImpactSet]

    def set_unknown_lcia(self, impact_set: ImpactSet):
        """Set the impact set as an unknown LCIA method."""
        self.__root__[LCIAMethod.UNKNOWN] = impact_set

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
            self.__root__[lcia_method] = impact_set

    def replace_lcia_method(self, lcia_method: LCIAMethod, new_lcia_method: LCIAMethod) -> None:
        """
        Replace the LCIA method.

        If the there is no impact set for the given LCIA method, do nothing.
        """
        impact_set = self.get_impact_set(lcia_method)
        if impact_set is None:
            return None
        self.set_impact_set(new_lcia_method, impact_set)
        del self.__root__[lcia_method]

    def get_impact_set(
        self, lcia_method: LCIAMethod | str | None, default_val: ImpactSet | None = None
    ) -> ImpactSet | None:
        """Return the impact set for the given LCIA method."""
        if lcia_method is None:
            return self.__root__.get(LCIAMethod.UNKNOWN, default_val)
        if isinstance(lcia_method, str):
            lcia_method = LCIAMethod.get_by_name(lcia_method)
        return self.__root__.get(lcia_method, default_val)

    def available_methods(self) -> set[LCIAMethod]:
        """Return a list of available LCIA methods."""
        return set(self.__root__.keys())

    def as_dict(self) -> dict[LCIAMethod, ImpactSet]:
        """Return the impacts as a dictionary."""
        return self.__root__


class ResourceUseSet(BaseOpenEpdSchema):
    """A set of resource use indicators, such as RPRec, RPRm, etc."""

    RPRec: ScopeSet | None = pyd.Field(
        description="Renewable primary resources used as energy carrier (fuel). "
        "First use bio-based materials used as an energy source. Hydropower, solar and wind power used "
        "in the technosphere are also included in this indicator",
        default=None,
    )
    RPRm: ScopeSet | None = pyd.Field(
        description="Renewable primary resources with energy content used as material. "
        "First use biobased materials used as materials (e.g. wood, hemp, etc.).",
        default=None,
    )
    rpre: ScopeSet | None = pyd.Field(
        description="Renewable primary energy resources as energy",
        default=None,
    )
    nrpre: ScopeSet | None = pyd.Field(
        description="Non-renewable primary resources as energy (fuel)",
        default=None,
    )
    nrprm: ScopeSet | None = pyd.Field(
        description="Non-renewable primary resources as material",
        default=None,
    )
    fw: ScopeSet | None = pyd.Field(
        description="Use of net fresh water",
        default=None,
    )
    sm: ScopeSet | None = pyd.Field(
        description="Use of secondary materials",
        default=None,
    )
    rsf: ScopeSet | None = pyd.Field(
        description="Use of renewable secondary materials",
        default=None,
    )
    nrsf: ScopeSet | None = pyd.Field(
        description="Use of non-renewable secondary fuels",
        default=None,
    )
    re: ScopeSet | None = pyd.Field(
        description="Renewable energy resources",
        default=None,
    )
    pere: ScopeSet | None = pyd.Field(
        description="Use of renewable primary energy excluding renewable primary energy resources used as raw materials",
        default=None,
    )
    perm: ScopeSet | None = pyd.Field(
        description="Use of renewable primary energy resources used as raw materials",
        default=None,
    )
    pert: ScopeSet | None = pyd.Field(
        description="Total use of renewable primary energy resources",
        default=None,
    )
    penre: ScopeSet | None = pyd.Field(
        description="Use of non-renewable primary energy excluding "
        "non-renewable primary energy resources used as raw materials",
        default=None,
    )
    penrm: ScopeSet | None = pyd.Field(
        description="Use of non-renewable primary energy resources used as raw materials",
        default=None,
    )
    penrt: ScopeSet | None = pyd.Field(
        description="Total use of non-renewable primary energy resources",
        default=None,
    )


class OutputFlowSet(BaseOpenEpdSchema):
    """A set of output flows, such as waste, emissions, etc."""

    twd: ScopeSet | None = pyd.Field(
        description="Total waste disposed",
        default=None,
    )
    hwd: ScopeSet | None = pyd.Field(
        description="Hazardous waste disposed",
        default=None,
    )
    nhwd: ScopeSet | None = pyd.Field(
        description="Non-hazardous waste disposed",
        default=None,
    )
    rwd: ScopeSet | None = pyd.Field(
        description="Radioactive waste disposed",
        default=None,
    )
    hlrw: ScopeSet | None = pyd.Field(
        description="High level radioactive waste disposed",
        default=None,
    )
    illrw: ScopeSet | None = pyd.Field(
        description="Intermediate level radioactive waste disposed",
        default=None,
    )
    cru: ScopeSet | None = pyd.Field(
        description="Components for re-use",
        default=None,
    )
    mr: ScopeSet | None = pyd.Field(
        description="Recycled materials",
        default=None,
    )
    mfr: ScopeSet | None = pyd.Field(
        description="Materials for recycling",
        default=None,
    )
    mer: ScopeSet | None = pyd.Field(
        description="Materials for energy recovery",
        default=None,
    )
    ee: ScopeSet | None = pyd.Field(
        description="Exported energy",
        default=None,
    )
    eh: ScopeSet | None = pyd.Field(
        description="Exported heat",
        default=None,
    )
