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
from collections.abc import Generator
from enum import StrEnum
from typing import Any, ClassVar, Self, cast

import pydantic
from pydantic.annotated_handlers import GetJsonSchemaHandler
from pydantic.json_schema import GenerateJsonSchema
from pydantic_core import CoreSchema

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Measurement
from openepd.model.validation.quantity import ExternalValidationConfig


class EolScenario(BaseOpenEpdSchema):
    """
    A scenario for end-of-life.

    If a particular implementation commits to a specific scenario, then that value can be used;
    otherwise the outcomes can be statistically combined.
    """

    name: str = pydantic.Field(
        max_length=40,
        examples=["Landfill"],
        description="A brief text description of the scenario, preferably from list eol_scenario_names",
    )
    likelihood: float | None = pydantic.Field(
        description="The weigting of this scenario used in the C1 .. C4 dataset. For example, the overall C1 shoudl be "
        "equal to weighted sum of C1 from all the scenarios, weighted by likelihood.",
        examples=[0.33],
        default=None,
    )
    C1: Measurement | None = pydantic.Field(
        description="Deconstruction and Demolition under this scenario",
        default=None,
    )
    C2: Measurement | None = pydantic.Field(
        description="Transport to waste processing or disposal under this scenario.",
        default=None,
    )
    C3: Measurement | None = pydantic.Field(
        description="Waste Processing under this scenario",
        default=None,
    )
    C4: Measurement | None = pydantic.Field(
        description="Disposal under this scenario",
        default=None,
    )
    D: Measurement | None = pydantic.Field(
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

    allowed_units: ClassVar[str | tuple[str, ...] | None] = None

    A1A2A3: Measurement | None = pydantic.Field(
        description="Sum of A1..A3",
        default=None,
    )
    A1: Measurement | None = pydantic.Field(
        description="Raw Material Supply",
        default=None,
    )
    A2: Measurement | None = pydantic.Field(
        description="Transport to Manufacturing",
        default=None,
    )
    A3: Measurement | None = pydantic.Field(
        description="Manufacturing",
        default=None,
    )
    A4: Measurement | None = pydantic.Field(
        description="Transport to Construction",
        default=None,
    )
    A5: Measurement | None = pydantic.Field(
        description="Construction",
        default=None,
    )
    B1: Measurement | None = pydantic.Field(
        description="Use impacts over Reference Service Life (Predicted)",
        default=None,
    )
    B1_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Timeframe over which B1 is evaluated, in years. "
        "For example, an impact of 1.23 kgCO2e per year for ten years could be B1=1.23kgCO2e, "
        "B1_years=1.0 or  B1=12.3kgCO2e, B1_years=10.0",
        default=None,
    )
    B2: Measurement | None = pydantic.Field(
        description="Predicted Maintenance Impacts over Reference Service Life",
        default=None,
    )
    B2_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Predicted Maintenance Impacts over Reference Service Life",
        default=None,
    )
    B3: Measurement | None = pydantic.Field(
        description="Predicted Repair impacts over Reference Service Life",
        default=None,
    )
    B3_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Timeframe over which B3 is evaluated, in years",
        default=None,
    )
    B4: Measurement | None = pydantic.Field(
        description="Predicted Replacement Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR.",
        default=None,
    )
    B4_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Timeframe over which B4 is evaluated, in years",
        default=None,
    )
    B5: Measurement | None = pydantic.Field(
        description="Predicted Refurbishment Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR.",
        default=None,
    )
    B5_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Timeframe over which B5 is evaluated, in years",
        default=None,
    )
    B6: Measurement | None = pydantic.Field(
        description="Predicted Impacts related to Operational Energy Use",
        default=None,
    )
    B6_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Timeframe over which B6 is evaluated, in years",
        default=None,
    )
    B7: Measurement | None = pydantic.Field(
        description="Predicted Impacts related to Operational Water Use",
        default=None,
    )
    B7_years: float | None = pydantic.Field(
        gt=0,
        lt=100,
        description="Timeframe over which B7 is evaluated, in years",
        default=None,
    )
    C_scenarios: list[EolScenario] | None = pydantic.Field(
        description="A list of possible end-of-life scenarios, "
        "for use in analyses where the end-of-life can be predicted.",
        default=None,
    )
    C1: Measurement | None = pydantic.Field(
        description="Deconstruction and Demolition",
        default=None,
    )
    C2: Measurement | None = pydantic.Field(
        description="Transport to waste processing or disposal.",
        default=None,
    )
    C3: Measurement | None = pydantic.Field(
        description="Waste Processing",
        default=None,
    )
    C4: Measurement | None = pydantic.Field(
        description="Disposal",
        default=None,
    )
    D: Measurement | None = pydantic.Field(
        default=None,
        description="Potential net benefits from reuse, recycling, and/or energy recovery beyond the system boundary.",
    )

    model_config = pydantic.ConfigDict(from_attributes=True)

    @pydantic.model_validator(mode="after")
    def _unit_validator(self) -> Self:
        all_units = set()

        for k in self.__class__.model_fields:
            v = getattr(self, k, None)
            if isinstance(v, Measurement):
                all_units.add(v.unit)

        if not self.allowed_units:
            # For unknown units - only units should be the same across all measurements (textually)
            if len(all_units) > 1:
                msg = "All scopes and measurements should be expressed in the same unit."
                raise ValueError(msg)
        else:
            # might be multiple variations of the same unit (kgCFC-11e, kgCFC11e)
            if len(all_units) > 1 and ExternalValidationConfig.QUANTITY_VALIDATOR:
                all_units_list = list(all_units)
                first = all_units_list[0]
                for unit in all_units_list[1:]:
                    ExternalValidationConfig.QUANTITY_VALIDATOR.validate_same_dimensionality(first, unit)

        # can correctly validate unit
        if self.allowed_units is not None and len(all_units) == 1 and ExternalValidationConfig.QUANTITY_VALIDATOR:
            unit = next(iter(all_units))
            allowed_units = self.allowed_units if isinstance(self.allowed_units, tuple) else (self.allowed_units,)

            matched_unit = False
            for allowed_unit in allowed_units:
                try:
                    ExternalValidationConfig.QUANTITY_VALIDATOR.validate_same_dimensionality(unit, allowed_unit)
                    matched_unit = True
                except ValueError:
                    ...
            if not matched_unit:
                msg = f"'{', '.join(allowed_units)}' is only allowed unit for this scopeset. Provided '{unit}'"
                raise ValueError(msg)

        return self


class ScopesetByNameBase(BaseOpenEpdSchema, extra="allow"):
    """Base class for the data structures presented as typed name:scopeset mapping ."""

    def get_scopeset_names(self, exclude_none: bool = False, only_standard: bool = False) -> list[str]:
        """
        Get the names of scopesets which have been set by model (not defaults).

        :param exclude_none: If True, exclude scopesets with None values.
        :param only_standard: If True, include only standard scopesets (those defined in model_fields_set).
        :return: set of names, for example ['gwp', 'odp']
        """
        result = []
        for f in self.model_fields_set:
            if f in ("ext",):
                continue
            field = self.__class__.model_fields.get(f)
            # field can be explicitly specified, or can be an unknown impact covered by extra='allow'
            result.append(field.alias if field and field.alias else f)

        # add extra fields
        if not only_standard and self.model_extra:
            for name in self.model_extra.keys():
                if name not in result:
                    result.append(name)

        if exclude_none:
            # filter out names with None values
            result = [name for name in result if self.get_scopeset_by_name(name) is not None]

        return result

    def set_scopeset_by_name(self, name: str, scopeset: ScopeSet | None) -> None:
        """
        Set scopeset by name.

        :param name: The name of the scopeset.
        :param scopeset: The scopeset to set.
        """
        # check known impacts first
        for f_name, f in self.__class__.model_fields.items():
            if f.alias == name:
                setattr(self, f_name, scopeset)
                return
            if f_name == name:
                setattr(self, f_name, scopeset)
                return
        # probably unknown impact, coming from 'extra' fields
        setattr(self, name, scopeset)

    def __getitem__(self, scopeset_name: str) -> ScopeSet:
        """Get scopeset by name or raise KeyError."""
        if not isinstance(scopeset_name, str):
            raise TypeError(f"Key must be a string, got {type(scopeset_name)}")
        result = self.get_scopeset_by_name(scopeset_name)
        if result is None:
            raise KeyError(f"Scopeset '{scopeset_name}' not found")
        return result

    def __setitem__(self, key: str, value: ScopeSet | None) -> None:
        """Set scopeset by name."""
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key)}")
        if value is not None and not isinstance(value, ScopeSet):
            raise TypeError(f"Value must be a ScopeSet, got {type(value)}")
        self.set_scopeset_by_name(key, value)

    def __contains__(self, item: str) -> bool:
        """Check if scopeset with the given name exists (was set and is not None)."""
        if not isinstance(item, str):
            return False
        return item in self.get_scopeset_names(exclude_none=True)

    def __iter__(self) -> Generator[tuple[str, ScopeSet], None, None]:
        """Iterate over existing (set and not None) scopesets and yield tuples of scopeset name and scopeset."""
        for name in self.get_scopeset_names(exclude_none=True):
            yield name, cast(ScopeSet, self.get_scopeset_by_name(name))

    def __len__(self) -> int:
        """Get the number of existing (set and not None) scopesets."""
        return len(self.get_scopeset_names(exclude_none=True))

    def items(self) -> list[tuple[str, ScopeSet]]:
        """Get all scopeset names and their values."""
        return [
            (name, cast(ScopeSet, self.get_scopeset_by_name(name)))
            for name in self.get_scopeset_names(exclude_none=True)
        ]

    def get_scopeset_by_name(self, name: str) -> ScopeSet | None:
        """
        Get scopeset by name.

        :param name: The name of the scopeset.
        :return: A scopeset if found, None otherwise
        """
        # check known impacts first
        for f_name, f in self.__class__.model_fields.items():
            if f.alias == name:
                return getattr(self, f_name)
            if f_name == name:
                return getattr(self, f_name)
        # probably unknown impact, coming from 'extra' fields
        return getattr(self, name, None)

    @pydantic.model_validator(mode="before")
    def _extra_scopeset_validator(cls, values: dict[str, Any]) -> dict[str, Any]:
        for f in values:
            # only interested in validating the extra fields
            if f in cls.model_fields:
                continue

            # extra impact of an unknown type - engage validation of ScopeSet
            extra_scopeset = values.get(f)
            match extra_scopeset:
                case ScopeSet():
                    continue
                case dict():
                    values[f] = ScopeSet(**extra_scopeset)
                case _:
                    msg = f"{f} must be a ScopeSet schema"
                    raise ValueError(msg)

        return values


class ScopeSetGwp(ScopeSet):
    """ScopeSet measured in kgCO2e."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kgCO2e"


class ScopeSetOdp(ScopeSet):
    """ScopeSet measured in kgCFC11e."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kgCFC11e"


class ScopeSetAp(ScopeSet):
    """ScopeSet measured in kgSO2e."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = ("kgSO2e", "molHe")


class ScopeSetEpNe(ScopeSet):
    """ScopeSet measured in kgNe."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kgNe"


class ScopeSetPocp(ScopeSet):
    """ScopeSet measured in kgO3e."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = ("kgO3e", "kgNMVOCe")


class ScopeSetEpFresh(ScopeSet):
    """ScopeSet measured in kgPO4e."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kgPO4e"


class ScopeSetEpTerr(ScopeSet):
    """ScopeSet measured in molNe."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "molNe"


class ScopeSetIrp(ScopeSet):
    """ScopeSet measured in kilo Becquerel equivalent of u235."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kBqU235e"


class ScopeSetCTUh(ScopeSet):
    """ScopeSet measured in CTUh."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "CTUh"


class ScopeSetM3Aware(ScopeSet):
    """ScopeSet measured in m3AWARE Water consumption by AWARE method."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "m3AWARE"


class ScopeSetCTUe(ScopeSet):
    """ScopeSet measured in CTUe."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "CTUe"


class ScopeSetKgSbe(ScopeSet):
    """ScopeSet measured in kgSbe."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kgSbe"


class ScopeSetDiseaseIncidence(ScopeSet):
    """ScopeSet measuring disease incidence measured in AnnualPerCapita (cases)."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "AnnualPerCapita"


class ScopeSetMass(ScopeSet):
    """ScopeSet measuring mass in kg."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "kg"


class ScopeSetVolume(ScopeSet):
    """ScopeSet measuring mass in kg."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "m3"


class ScopeSetMassOrVolume(ScopeSet):
    """ScopeSet measuring mass in kg OR volume in m3, example: radioactive waste."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = ("kg", "m3")


class ScopeSetEnergy(ScopeSet):
    """ScopeSet measuring mass in kg."""

    allowed_units: ClassVar[str | tuple[str, ...] | None] = "MJ"


class ImpactSet(ScopesetByNameBase):
    """A set of impacts, such as GWP, ODP, AP, EP, POCP, EP-marine, EP-terrestrial, EP-freshwater, etc."""

    gwp: ScopeSetGwp | None = pydantic.Field(
        default=None,
        description="GWP100, calculated per IPCC guidelines.  If any CO2 removals are "
        "part of this figure, the gwp-fossil, gwp-bioganic, gwp-luluc, an "
        "gwp-nonCO2 fields are required, as is "
        "kg_C_biogenic_per_declared_unit.",
    )
    odp: ScopeSetOdp | None = pydantic.Field(default=None, description="Ozone Depletion Potential")
    ap: ScopeSetAp | None = pydantic.Field(default=None, description="Acidification Potential")
    ep: ScopeSetEpNe | None = pydantic.Field(
        default=None,
        description="Eutrophication Potential in Marine Ecosystems. Has the same meaning as ep-marine.",
    )
    pocp: ScopeSetPocp | None = pydantic.Field(
        default=None, description="Photochemical Smog (Ozone) creation potential"
    )
    ep_marine: ScopeSetEpNe | None = pydantic.Field(
        alias="ep-marine", default=None, description="Has the same meaning as 'ep'"
    )
    ep_fresh: ScopeSetEpFresh | None = pydantic.Field(
        alias="ep-fresh",
        default=None,
        description="Eutrophication Potential in Freshwater Ecosystems",
    )
    ep_terr: ScopeSetEpTerr | None = pydantic.Field(
        alias="ep-terr",
        default=None,
        description="Eutrophication Potential in Terrestrial Ecosystems",
    )
    gwp_biogenic: ScopeSetGwp | None = pydantic.Field(
        alias="gwp-biogenic",
        default=None,
        description="Net GWP from removals of atmospheric CO2 into biomass and  emissions of CO2 from biomass sources. "
        "To be counted as negative, CO2 removals must be closely linked to production in "
        "operational control (i.e. no purchased offsets), time (within three years of production) and "
        "space (similar biome).  They must not have been sold, committed, or credited to any other "
        "product.  Harvesting from native forests is handled under GWP_luluc for EN15804.",
    )
    gwp_luluc: ScopeSetGwp | None = pydantic.Field(
        alias="gwp-luluc",
        default=None,
        description="Climate change effects related to land use and land use change, for example biogenic carbon "
        "exchanges resulting from deforestation or other soil activities (including soil carbon "
        "emissions). All related emissions for native forests are included under this category. "
        "Uptake for native forests is set to 0 kgCO2 for EN15804.",
    )
    gwp_nonCO2: ScopeSetGwp | None = pydantic.Field(
        alias="gwp-nonCO2",
        default=None,
        description="GWP from non-CO2, non-fossil sources, such as livestock-sourced CH4 and agricultural N2O.",
    )
    gwp_fossil: ScopeSetGwp | None = pydantic.Field(
        alias="gwp-fossil",
        default=None,
        description="Climate change effects due to greenhouse gas emissions originating from the oxidation or "
        "reduction of fossil fuels or materials containing fossil carbon. [Source: EN15804]",
    )
    WDP: ScopeSetM3Aware | None = pydantic.Field(
        default=None,
        description="Deprivation-weighted water consumption, calculated by the AWARE method "
        "(https://wulca-waterlca.org/aware/what-is-aware)",
    )
    PM: ScopeSetDiseaseIncidence | None = pydantic.Field(
        default=None,
        description="Potential incidence of disease due to particulate matter emissions.",
    )
    IRP: ScopeSetIrp | None = pydantic.Field(
        default=None,
        description="Potential ionizing radiation effect on human health, relative to U235.",
    )
    ETP_fw: ScopeSetCTUe | None = pydantic.Field(
        alias="ETP-fw",
        default=None,
        description="Ecotoxicity in freshwater, in potential Comparative Toxic Unit for ecosystems.",
    )
    HTP_c: ScopeSetCTUh | None = pydantic.Field(
        alias="HTP-c",
        default=None,
        description="Human toxicity, cancer effects in potential Comparative Toxic Units for humans.",
    )
    HTP_nc: ScopeSetCTUh | None = pydantic.Field(
        alias="HTP-nc",
        default=None,
        description="Human toxicity, noncancer effects in potential Comparative Toxic Units for humans.",
    )
    SQP: ScopeSet | None = pydantic.Field(
        default=None,
        description="Land use related impacts / Soil quality, in potential soil quality parameters.",
    )
    ADP_mineral: ScopeSetKgSbe | None = pydantic.Field(
        alias="ADP-mineral",
        default=None,
        description='Abiotic depletion potential for non-fossil resources. EN15804 calls this "ADP - minerals and metals".',
    )

    ADP_fossil: ScopeSetEnergy | None = pydantic.Field(
        alias="ADP-fossil",
        default=None,
        description="Abiotic depletion potential for fossil resources",
    )

    model_config = pydantic.ConfigDict(from_attributes=True)


class LCIAMethod(StrEnum):
    """A list of available LCA methods."""

    UNKNOWN = "Unknown LCIA"
    TRACI_2_2 = "TRACI 2.2"
    TRACI_2_1 = "TRACI 2.1"
    TRACI_2_0 = "TRACI 2.0"
    TRACI_1_0 = "TRACI 1.0"
    IPCC_AR5 = "IPCC AR5"
    IPCC_AR6 = "IPCC AR6"
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
    GWP_GHG = "GWP-GHG"
    LIME2 = "LIME2"

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


class Impacts(pydantic.RootModel[dict[LCIAMethod, ImpactSet]]):
    """List of environmental impacts, compiled per one of the standard Impact Assessment methods."""

    def set_unknown_lcia(self, impact_set: ImpactSet):
        """Set the impact set as an unknown LCIA method."""
        self.root[LCIAMethod.UNKNOWN] = impact_set

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
            self.root[lcia_method] = impact_set

    def replace_lcia_method(self, lcia_method: LCIAMethod, new_lcia_method: LCIAMethod) -> None:
        """
        Replace the LCIA method.

        If the there is no impact set for the given LCIA method, do nothing.
        """
        impact_set = self.get_impact_set(lcia_method)
        if impact_set is None:
            return None
        self.set_impact_set(new_lcia_method, impact_set)
        del self.root[lcia_method]

    def get_impact_set(
        self, lcia_method: LCIAMethod | str | None, default_val: ImpactSet | None = None
    ) -> ImpactSet | None:
        """Return the impact set for the given LCIA method."""
        if lcia_method is None:
            return self.root.get(LCIAMethod.UNKNOWN, default_val)
        if isinstance(lcia_method, str):
            lcia_method = LCIAMethod.get_by_name(lcia_method)
        return self.root.get(lcia_method, default_val)

    def available_methods(self) -> set[LCIAMethod]:
        """Return a list of available LCIA methods."""
        return set(self.root.keys())

    def as_dict(self) -> dict[LCIAMethod, ImpactSet]:
        """Return the impacts as a dictionary."""
        return self.root

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler, *, mode="validation"):
        # Get the base schema from the handler
        json_schema: dict[str, Any] = handler(core_schema)
        # Resolve the reference to get the actual ImpactSet schema
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema_generator: GenerateJsonSchema | None = None
        if hasattr(handler, "generate_json_schema") and handler.generate_json_schema:
            json_schema_generator = handler.generate_json_schema

        ref_template = ""
        if json_schema_generator and json_schema_generator.ref_template:
            ref_template = json_schema_generator.ref_template
        elif json_schema.get("propertyNames", {}).get("$ref") is not None:
            template_path, _ = json_schema.get("propertyNames", {}).get("$ref", "").rsplit("/", maxsplit=2)
            if template_path:
                ref_template = f"{template_path}/{{model}}"
        if not ref_template:
            ref_template = "#/components/schemas/{model}"

        # Get the ImpactSet reference dynamically
        impact_set_ref = None
        if (
            json_schema_generator
            and hasattr(json_schema_generator, "definitions")
            and json_schema_generator.definitions
        ):
            # Look for ImpactSet in the definitions
            for def_name, _ in json_schema_generator.definitions.items():
                if "ImpactSet" in def_name:
                    # Use the correct OpenAPI reference format
                    impact_set_ref = ref_template.format(model=def_name)
                    break

        # Fallback: use a generic reference if we can't find the specific one (
        if not impact_set_ref:
            impact_set_ref = ref_template.format(model="ImpactSet")

        # Update the schema with explicit properties for each LCIA method
        json_schema.update(
            {
                "type": "object",
                "properties": {
                    str(lm): {
                        "description": str(lm),
                        "allOf": [{"$ref": impact_set_ref}],
                    }
                    for lm in LCIAMethod
                },
            }
        )
        json_schema.pop("additionalProperties")

        return json_schema


class ResourceUseSet(ScopesetByNameBase):
    """A set of resource use indicators, such as RPRec, RPRm, etc."""

    RPRec: ScopeSetEnergy | None = pydantic.Field(
        description="Renewable primary resources used as energy carrier (fuel). "
        "First use bio-based materials used as an energy source. Hydropower, solar and wind power used "
        "in the technosphere are also included in this indicator",
        default=None,
    )
    RPRm: ScopeSetEnergy | None = pydantic.Field(
        description="Renewable primary resources with energy content used as material. "
        "First use biobased materials used as materials (e.g. wood, hemp, etc.).",
        default=None,
    )
    rpre: ScopeSetEnergy | None = pydantic.Field(
        description="Renewable primary energy resources as energy",
        default=None,
    )
    nrpre: ScopeSetEnergy | None = pydantic.Field(
        description="Non-renewable primary resources as energy (fuel)",
        default=None,
    )
    nrprm: ScopeSetEnergy | None = pydantic.Field(
        description="Non-renewable primary resources as material",
        default=None,
    )
    fw: ScopeSetVolume | None = pydantic.Field(
        description="Use of net fresh water",
        default=None,
    )
    sm: ScopeSetMass | None = pydantic.Field(
        description="Use of secondary materials",
        default=None,
    )
    rsf: ScopeSetEnergy | None = pydantic.Field(
        description="Use of renewable secondary materials",
        default=None,
    )
    nrsf: ScopeSetEnergy | None = pydantic.Field(
        description="Use of non-renewable secondary fuels",
        default=None,
    )
    re: ScopeSetEnergy | None = pydantic.Field(
        description="Renewable energy resources",
        default=None,
    )
    pere: ScopeSetEnergy | None = pydantic.Field(
        description="Use of renewable primary energy excluding renewable primary energy resources used as raw materials",
        default=None,
    )
    perm: ScopeSetEnergy | None = pydantic.Field(
        description="Use of renewable primary energy resources used as raw materials",
        default=None,
    )
    pert: ScopeSetEnergy | None = pydantic.Field(
        description="Total use of renewable primary energy resources",
        default=None,
    )
    penre: ScopeSetEnergy | None = pydantic.Field(
        description="Use of non-renewable primary energy excluding "
        "non-renewable primary energy resources used as raw materials",
        default=None,
    )
    penrm: ScopeSetEnergy | None = pydantic.Field(
        description="Use of non-renewable primary energy resources used as raw materials",
        default=None,
    )
    penrt: ScopeSetEnergy | None = pydantic.Field(
        description="Total use of non-renewable primary energy resources",
        default=None,
    )


class OutputFlowSet(ScopesetByNameBase):
    """A set of output flows, such as waste, emissions, etc."""

    twd: ScopeSetMass | None = pydantic.Field(
        description="Total waste disposed",
        default=None,
    )
    hwd: ScopeSetMass | None = pydantic.Field(
        description="Hazardous waste disposed",
        default=None,
    )
    nhwd: ScopeSetMass | None = pydantic.Field(
        description="Non-hazardous waste disposed",
        default=None,
    )
    rwd: ScopeSetMass | None = pydantic.Field(
        description="Radioactive waste disposed",
        default=None,
    )
    hlrw: ScopeSetMassOrVolume | None = pydantic.Field(
        description="High level radioactive waste disposed",
        default=None,
    )
    illrw: ScopeSetMassOrVolume | None = pydantic.Field(
        description="Intermediate level radioactive waste disposed",
        default=None,
    )
    cru: ScopeSetMass | None = pydantic.Field(
        description="Components for re-use",
        default=None,
    )
    mr: ScopeSetMass | None = pydantic.Field(
        description="Recycled materials",
        default=None,
    )
    mfr: ScopeSetMass | None = pydantic.Field(
        description="Materials for recycling",
        default=None,
    )
    mer: ScopeSetMass | None = pydantic.Field(
        description="Materials for energy recovery",
        default=None,
    )
    ee: ScopeSetEnergy | None = pydantic.Field(
        description="Exported energy",
        default=None,
    )
    eh: ScopeSetEnergy | None = pydantic.Field(
        description="Exported heat",
        default=None,
    )


class WithLciaMixin(BaseOpenEpdSchema):
    """Mixin for LCIA data."""

    impacts: Impacts | None = pydantic.Field(
        description="List of environmental impacts, compiled per one of the standard Impact Assessment methods",
        examples=[{"TRACI 2.1": {"gwp": {"A1A2A3": {"mean": 22.4, "unit": "kgCO2e"}}}}],
        default=None,
    )
    resource_uses: ResourceUseSet | None = pydantic.Field(
        description="Set of Resource Use Indicators, over various LCA scopes",
        examples=[{"RPRe": {"A1A2A3": {"mean": 12, "unit": "MJ", "rsd": 0.12}}}],
        default=None,
    )
    output_flows: OutputFlowSet | None = pydantic.Field(
        description="Set of Waste and Output Flow indicators which describe the waste categories "
        "and other material output flows derived from the LCI.",
        examples=[{"hwd": {"A1A2A3": {"mean": 2300, "unit": "kg", "rsd": 0.22}}}],
        default=None,
    )
