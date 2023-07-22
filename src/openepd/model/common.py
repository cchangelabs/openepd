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
from typing import Annotated, Any

import pydantic as pyd
from pydantic import BaseModel, model_validator

from openepd.model.base import BaseOpenEpdSchema


class Amount(BaseOpenEpdSchema):
    """A value-and-unit pairing for amounts that do not have an uncertainty."""

    qty: float | None = pyd.Field(description="How much of this in the amount.", default=None)
    unit: str | None = pyd.Field(
        description="Which unit.  SI units are preferred.",
        default=None,
        json_schema_extra=dict(example="kg"),
    )

    @model_validator(mode="before")
    def check_qty_or_unit(cls, values: dict[str, Any]):
        """Ensure that qty or unit is provided."""
        if values["qty"] is None and values["unit"] is None:
            raise ValueError("Either qty or unit must be provided.")
        return values

    def to_quantity_str(self):
        """Return a string representation of the amount."""
        return f"{self.qty or ''} {self.unit or 'str'}".strip()


class Measurement(BaseOpenEpdSchema):
    """A scientific value with units and uncertainty."""

    mean: float = pyd.Field(description="Mean (expected) value of the measurement")
    unit: str = pyd.Field(description="Measurement unit")
    rsd: pyd.PositiveFloat | None = pyd.Field(
        description="Relative standard deviation, i.e. standard_deviation/mean", default=None
    )
    dist: str | None = pyd.Field(description="Statistical distribution of the measurement error.", default=None)


class Ingredient(BaseOpenEpdSchema):
    """
    An ingredient of a product.

    The Ingredients list gives the core data references and quantities. This list is used to document supply-chain
    transparency, such as the EPDs of major components (e.g. cement in concrete, or recycled steel
    in hot-rolled sections).
    """

    qty: float | None = pyd.Field(
        description="Number of declared units of this consumed. Negative values indicate an outflow."
    )
    link: pyd.AnyUrl | None = pyd.Field(
        description="Link to this object's OpenEPD declaration. "
        "An OpenIndustryEPD or OpenLCI link is also acceptable.",
        default=None,
    )


class LatLng(BaseOpenEpdSchema):
    """A latitude and longitude."""

    lat: float = pyd.Field(description="Latitude", json_schema_extra=dict(example=47.6062))
    lng: float = pyd.Field(description="Longitude", json_schema_extra=dict(example=-122.3321))


class Location(BaseOpenEpdSchema):
    """A location on the Earth's surface."""

    pluscode: str | None = pyd.Field(default=None, description="Open Location code of this location")
    latlng: LatLng | None = pyd.Field(default=None, description="Latitude and longitude of this location")
    address: str | None = pyd.Field(default=None, description="Text address, preferably geocoded")
    country: str | None = pyd.Field(default=None, description="2-alpha country code")
    jurisdiction: str | None = pyd.Field(
        default=None, description="Province, State, or similar subdivision below the level of a country"
    )


class WithAttachmentsMixin(BaseModel):
    """Mixin for objects that can have attachments."""

    attachments: dict[Annotated[str, pyd.Field(max_length=200)], pyd.AnyUrl] | None = pyd.Field(
        description="Dict of URLs relevant to this entry",
        default=None,
        json_schema_extra={
            "example": {
                "Contact Us": "https://www.c-change-labs.com/en/contact-us/",
                "LinkedIn": "https://www.linkedin.com/company/c-change-labs/",
            }
        },
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


class WithAltIdsMixin(BaseModel):
    """Mixin for objects that can have alt_ids."""

    alt_ids: dict[Annotated[str, pyd.Field(max_length=200)], str] | None = pyd.Field(
        description="Dict identifiers for this entry.",
        default=None,
        json_schema_extra=dict(
            example={
                "oekobau.dat": "bdda4364-451f-4df2-a68b-5912469ee4c9",
            }
        ),
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
