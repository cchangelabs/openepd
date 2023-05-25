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
from typing import Annotated

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema


class Amount(BaseOpenEpdSchema):
    """A value-and-unit pairing for amounts that do not have an uncertainty."""

    qty: float | None = pyd.Field(description="How much of this in the amount.")
    unit: str = pyd.Field(description="Which unit.  SI units are preferred.", example="kg")


class Measurement(BaseOpenEpdSchema):
    """A scientific value with units and uncertainty."""

    mean: float = pyd.Field(description="Mean (expected) value of the measurement")
    unit: str = pyd.Field(description="Measurement unit")
    rsd: pyd.PositiveFloat = pyd.Field(description="Relative standard deviation, i.e. standard_deviation/mean")
    dist: str | None = pyd.Field(description="Statistical distribution of the measurement error.")


class ExternalIdentification(BaseOpenEpdSchema):  # TODO: NEW Object, not in the spec
    """Represent an external identification of an object."""

    id: str
    version: str | None


class ExternallyIdentifiableMixin:  # TODO: NEW Object, not in the spec
    """Mixin for objects that can be identified externally."""

    identified: dict[str, ExternalIdentification] = pyd.Field(description="The external identification of the object.")


class WithAttachmentsMixin:
    """Mixin for objects that can have attachments."""

    attachments: dict[Annotated[str, pyd.constr(max_length=200)], pyd.AnyUrl] | None = pyd.Field(
        description="Dict of URLs relevant to this entry",
        example={
            "Contact Us": "https://www.c-change-labs.com/en/contact-us/",
            "LinkedIn": "https://www.linkedin.com/company/c-change-labs/",
        },
        default=None,
    )
