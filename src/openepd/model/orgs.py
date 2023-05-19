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
from typing import Annotated, Optional

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import ExternallyIdentifiableMixin


class Contact(BaseOpenEpdSchema):  # TODO: NEW Object, not in the spec
    """Contact information of a person or organization."""

    email: pyd.EmailStr | None = pyd.Field(description="Email", example="contact@c-change-labs.com", default=None)
    phone: str | None = pyd.Field(description="Phone number", example="+15263327352", default=None)
    website: pyd.AnyUrl | None = pyd.Field(
        description="Url of the website", example="http://buildingtransparency.org", default=None
    )


class Org(ExternallyIdentifiableMixin, BaseOpenEpdSchema):  # TODO: NEW Identifiable field, not in the spec
    """Represent an organization."""

    web_domain: str = pyd.Field(
        description="A web domain owned by organization. Typically is the org's home website address",
    )
    name: str = pyd.Field(max_length=200, description="Common name for organization", example="C Change Labs")
    alt_names: Annotated[list[str], pyd.conlist(pyd.constr(max_length=200), max_items=255)] | None = pyd.Field(
        description="List of other names for organization",
        example=["C-Change Labs", "C-Change Labs inc."],
        default=None,
    )
    # TODO: NEW field, not in the spec
    contacts: Contact | None = pyd.Field(description="Contact information of the organization", default=None)
    owner: Optional["Org"] = pyd.Field(description="Organization that controls this organization", default=None)
    subsidiaries: Annotated[list[str], pyd.conlist(pyd.constr(max_length=200), max_items=255)] | None = pyd.Field(
        description="Organizations controlled by this organization",
        example=["cqd.io", "supplychaincarbonpricing.org"],
        default=None,
    )
    attachments: dict[Annotated[str, pyd.constr(max_length=200)], pyd.AnyUrl] | None = pyd.Field(
        description="Dict of URLs relevant to this entry",
        example={
            "Contact Us": "https://www.c-change-labs.com/en/contact-us/",
            "LinkedIn": "https://www.linkedin.com/company/c-change-labs/",
        },
        default=None,
    )
