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
from collections.abc import Callable, Generator
from enum import StrEnum
import re
from typing import Annotated, Any

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.validation.numbers import RatioFloat

DATA_URL_REGEX = r"^data:([-\w]+\/[-+\w.]+)?(;?\w+=[-\w]+)*(;base64)?,.*$"
"""
Regular expression pattern for matching Data URLs.

A Data URL is a URI scheme that allows you to embed small data items inline 
in web pages as if they were external resources.
The pattern matches the following format: data:[<media-type>][;base64],<data>
"""


class Amount(BaseOpenEpdSchema):
    """A value-and-unit pairing for amounts that do not have an uncertainty."""

    qty: float | None = pyd.Field(description="How much of this in the amount.", ge=0, default=None)
    unit: str | None = pyd.Field(description="Which unit.  SI units are preferred.", example="kg", default=None)

    @pyd.root_validator
    def check_qty_or_unit(cls, values: dict[str, Any]):
        """Ensure that qty or unit is provided."""
        if values.get("qty") is None and values.get("unit") is None:
            msg = "Either qty or unit must be provided."
            raise ValueError(msg)
        return values

    def to_quantity_str(self):
        """Return a string representation of the amount."""
        return f"{self.qty or ''} {self.unit or 'str'}".strip()


class Distribution(StrEnum):
    """
    Distribution of the measured value.

    * log-normal: Probability distribution of any random parameter whose natural log is normally distributed (the
      PDF is gaussian).
    * normal: Probability distribution of any random parameter whose value is normally distributed around the mean
      (the PDF is gaussian).
    * Continuous uniform probability distribution between minimum value and maximum value and "0" probability beyond
      these.
    * Probability distribution of any random parameter between minimum value and maximum value with the highest
      probability at the average value of minimum plus maximum value. Linear change of probability between minimum,
      maximum and average value.
    * Means Impact is not known, but with >95% certainty the true value is below the declared value.
      So [1e-6,"kgCFC11e",0,"max"] means the ODP was not exactly measured, but it is guaranteed to be below
      1E-6 kg CO2e.  It is acceptable to treat a 'max' distribution a normal or lognormal distribution with variation
      0.1%.  This is conservative, because the 'max' value is usually much greater than the true impact.
    """

    LOG_NORMAL = "log-normal"
    NORMAL = "normal"
    UNIFORM = "uniform"
    TRIANGULAR = "triangular"
    MAX = "max"


class Measurement(BaseOpenEpdSchema):
    """A scientific value with units and uncertainty."""

    mean: float = pyd.Field(description="Mean (expected) value of the measurement")
    unit: str | None = pyd.Field(description="Measurement unit")
    rsd: pyd.PositiveFloat | None = pyd.Field(
        description="Relative standard deviation, i.e. standard_deviation/mean", default=None
    )
    dist: Distribution | None = pyd.Field(
        description="Statistical distribution of the measurement error.", default=None
    )


class IngredientEvidenceTypeEnum(StrEnum):
    """Supported types of evidence for indirect ingredient."""

    PRODUCT_EPD = "Product EPD"


class Ingredient(BaseOpenEpdSchema):
    """
    An ingredient of a product.

    The Ingredients list gives the core data references and quantities. This list is used to document supply-chain
    transparency, such as the EPDs of major components (e.g. cement in concrete, or recycled steel
    in hot-rolled sections).

    Since the exact ingredients may be viewed as a proprietary information by Manufacturers, this schema also allows
    to pass some data about ingredient about explicitly saying what it is. Further, this data can be used to
    calculate the supply chain specificity of the product and uncertainty adjusted factor. For this option, use
    gwp_fraction, citation and evidence_type.
    """

    qty: float | None = pyd.Field(
        description="Number of declared units of this consumed. Negative values indicate an outflow."
    )
    link: pyd.AnyUrl | None = pyd.Field(
        description="Link to this object's OpenEPD declaration. An OpenIndustryEPD or OpenLCI link is also acceptable.",
        default=None,
    )

    gwp_fraction: RatioFloat | None = pyd.Field(
        default=None,
        description="Fraction of product's A1-A3 GWP this flow represents.  This value, along with the specificity of "
        "the reference, are used to caclulate supply chain specificity.",
    )
    evidence_type: IngredientEvidenceTypeEnum | None = pyd.Field(
        default=None, description="Type of evidence used, which can be used to calculate degree of specificity"
    )
    citation: str | None = pyd.Field(default=None, description="Text citation describing the data source ")

    @pyd.root_validator(skip_on_failure=True)
    def _validate_evidence(cls, values: dict[str, Any]) -> dict[str, Any]:
        # gwp_fraction should be backed by some type of evidence (fraction coming from product EPD etc) to be accounted
        # for in the calculation of uncertainty
        if values.get("gwp_fraction"):
            if not values.get("evidence_type"):
                msg = "evidence_type is required if gwp_fraction is provided"
                raise ValueError(msg)
            if not (values.get("citation") or values.get("link")):
                msg = "link or citation is required if gwp_fraction is provided"
                raise ValueError(msg)

        return values


class LatLng(BaseOpenEpdSchema):
    """A latitude and longitude."""

    lat: float = pyd.Field(description="Latitude", example=47.6062)
    lng: float = pyd.Field(description="Longitude", example=-122.3321)


class Location(BaseOpenEpdSchema):
    """A location on the Earth's surface."""

    pluscode: str | None = pyd.Field(default=None, description="Open Location code of this location")
    latlng: LatLng | None = pyd.Field(default=None, description="Latitude and longitude of this location")
    address: str | None = pyd.Field(default=None, description="Text address, preferably geocoded")
    country: str | None = pyd.Field(default=None, description="2-alpha country code")
    jurisdiction: str | None = pyd.Field(
        default=None, description="Province, State, or similar subdivision below the level of a country"
    )


ATTACHMENT_KNOWN_KEYS: dict[str, str] = {
    "OpenEPD": "A Product EPD in OpenEPD format",
    "openEPD": "Equivalent to OpenEPD",
    "ILCD_EPD": "A Product EPD in ILCD+EPD format.  An underscore is used in place of '+' for compatability purposes.",
    "OpenIndustryEPD": "An Industry EPD in OpenEPD format",
    "openIndustryEPD": "Equivalent to OpenIndustryEPD",
    "LCA_Model": "An underlying LCA model from which one could replicate these EPD results, in LCA Commons 2.0 format",
    "LCA_Report": "An underlying LCA report, in PDF or other document format",
    "lca_software": "A url, optionally with an #anchor tag, pointing to the version of the software used, generally one provided by the software vendor. ",
    "lca_dataset_reference": "A URL link to an lca dataset used in the analysis.  Multiple dataset references can be added by appending a number or string after _reference, e.g. lca_dataset_reference_3 or lca_dataset_reference_steel",
    "EPD": "Environmental Product Declaration, verified by a third party, not in OpenEPD format.",
    "IndustryEPD": "EPD for an industry, sector, or group of companies, not in OpenEPD format.",
    "Datasheet": "A technical data sheet describing the product.",
    "PCR": "Product Category Rules for EPD generation",
    "Contact_Us": "A url to contact.  May be an email (mailto:) link.",
    "URL": "A link to a relevant resource.  No particular format is specified.  Each URL should be uniquely named. ",
    "VOC": "Volatile Organic Compound declaration",
    "HPD": "Material Health Product Declaration",
    "PEF": "Product Environmental Footprint (without 3rd party verification)",
    "MSDS": "Material Safety Data Sheet",
    "Developer": "Link to the website of the group who performed the LCA and/or prepared the EPD.",
}


class AttachmentDict(dict[str, pyd.AnyUrl]):
    """Special form of dict for attachments."""

    @classmethod
    def __modify_schema__(cls, field_schema: dict[str, Any], field: pyd.fields.ModelField | None):
        # This may be generalized later to combine, for example, enum descriptions and field descriptions to provide
        # a better result.
        field_description = field.field_info.description if field else ""
        if field_description:
            field_description = field_description.strip()
            if not field_description.endswith("."):
                field_description += "."
            field_description += " "

        field_schema["description"] = field_description + "Extra properties of string -> URL allowed."
        field_schema["properties"] = {
            k: {"type": "string", "format": "uri", "description": v} for k, v in ATTACHMENT_KNOWN_KEYS.items()
        }
        field_schema["additionalProperties"] = True


class WithAttachmentsMixin(pyd.BaseModel):
    """Mixin for objects that can have attachments."""

    attachments: AttachmentDict = pyd.Field(
        description="Dict of URLs relevant to this entry",
        example={
            "Contact Us": "https://www.c-change-labs.com/en/contact-us/",
            "LinkedIn": "https://www.linkedin.com/company/c-change-labs/",
        },
        default=None,
    )

    def set_attachment(self, name: str, url: str):
        """Set an attachment."""
        if self.attachments is None:
            self.attachments = {}  # type: ignore
        self.attachments[name] = url  # type: ignore

    def set_attachment_if_any(self, name: str, url: str | None):
        """Set an attachment if url is not None."""
        if url is not None:
            self.set_attachment(name, url)


class WithAltIdsMixin(pyd.BaseModel):
    """Mixin for objects that can have alt_ids."""

    alt_ids: dict[Annotated[str, pyd.Field(max_length=200)], str] | None = pyd.Field(
        description="Dict identifiers for this entry.",
        example={
            "oekobau.dat": "bdda4364-451f-4df2-a68b-5912469ee4c9",
        },
        default=None,
    )

    def set_alt_id(self, domain_name: str, value: str):
        """Set an alt_id."""
        if self.alt_ids is None:
            self.alt_ids = {}
        self.alt_ids[domain_name] = value

    def set_alt_id_if_any(self, domain_name: str, value: str | None):
        """Set an alt_id if value is not None."""
        if value is not None:
            self.set_alt_id(domain_name, value)


class OpenEPDUnit(StrEnum):
    """OpenEPD allowed units."""

    kg = "kg"
    m2 = "m2"
    m = "m"
    M2_RSI = "m2 * RSI"
    MJ = "MJ"
    t_km = "t * km"
    MPa = "MPa"
    item = "item"
    W = "W"
    use = "use"
    degree_c = "°C"
    kg_co2 = "kgCO2e"
    hour = "hour"


class RangeBase(BaseOpenEpdSchema):
    """Base class for range types having min and max and order between them."""

    @pyd.root_validator
    def _validate_range_bounds(cls, values: dict[str, Any]) -> dict[str, Any]:
        min_boundary = values.get("min")
        max_boundary = values.get("max")
        if min_boundary is not None and max_boundary is not None and min_boundary > max_boundary:
            msg = "Max should be greater than min"
            raise ValueError(msg)
        return values


class RangeFloat(RangeBase):
    """Structure representing a range of floats."""

    min: float | None = pyd.Field(default=None, example=3.1)
    max: float | None = pyd.Field(default=None, example=5.8)


class RangeInt(RangeBase):
    """Structure representing a range of ints1."""

    min: int | None = pyd.Field(default=None, example=2)
    max: int | None = pyd.Field(default=None, example=3)


class RangeRatioFloat(RangeFloat):
    """Range of ratios (0-1 to 0-10)."""

    min: float | None = pyd.Field(default=None, example=0.2, ge=0, le=1)
    max: float | None = pyd.Field(default=None, example=0.65, ge=0, le=1)


class RangeAmount(RangeFloat):
    """Structure representing a range of quantities."""

    unit: str | None = pyd.Field(default=None, description="Unit of the range.")


class EnumGroupingAware:
    """
    Mixin for enums to support groups.

    With the groups, enum can group its values into more than one groups, so that the validator higher in code can check
    for mutual exclusivity, for example that only one value from the group is permitted at the same time.
    """

    @classmethod
    def get_groupings(cls) -> list[list]:
        """Return logical groupings of the values."""
        return []


class DataUrl(str):
    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[str], str], None, None]:
        def validator(v: str) -> str:
            if re.compile(DATA_URL_REGEX).match(v):
                return v
            msg = "Value must be a valid dataUrl"
            raise ValueError(msg)

        yield validator
