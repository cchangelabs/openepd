#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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
from enum import StrEnum
from typing import Annotated

import pydantic

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.org import Org


class SoftwarePrimaryFunction(StrEnum):
    EPD_GENERATOR = "EPD Generator"
    """Software that directly generates environmental product declarations that are fully or partly pre-verified."""
    LCA_ANALYSIS = "LCA Analysis"
    """
    Software that calculates full sets of LCI indicators for processes or products, 
    but does not directly generate a preverified EPD.
    """
    BILL_OF_QUANTITIES = "Bill of Quantities"
    """Software that generates quantities and types of materials, but not the impacts of those materials."""
    OTHER = "Other"
    """Software not described by a defined value in this list."""


class ResourceObject(BaseOpenEpdSchema):
    guid: str | None = pydantic.Field(
        description=(
            "The guid of this resource on the current system.  An openEPD system MUST create a guid for a "
            "newly defined resource that lacks a guid.  If a resource is created via API, and contains a guid, "
            "the receiving system SHOULD use the existing GUID.  "
        ),
        examples=["40888d44-916d-4220-8353-dcdbc4e38d1b"],
        default=None,
    )
    owner: Org | None = pydantic.Field(
        description="The owner or publisher.",
        default=None,
    )
    alt_ids: list[str] | None = pydantic.Field(
        max_length=255,
        description=(
            "A list of IDs by which this resource is also referred.  "
            "When merging duplicate resource records, one guid should be retained and the other should be "
            "appended to alt_ids.  When synchronizing resources from a data source, an openEPD system SHOULD "
            "adopt the guid used in the data source, and either delete its own guid or append its own guid to alt_ids.  "
            "When connecting to multiple sources, implementers are advised to merge alt_ids lists "
            "rather than overwriting the entire list."
        ),
        examples=[["4a90591d-1a40-40e3-b72f-e5853d286b15", "0cddd245-a2c6-477b-afc1-3070ddf0ef9b"]],
        default=None,
    )
    name: str | None = pydantic.Field(
        max_length=200,
        description=(
            "Title or name of this software, database, or other reference. Avoid adding the name of the owner "
            "to the name (e.g. '911' rather than 'Porsche 911'), and do not add the version here.  "
        ),
        examples=["LCA for Experts"],
        default=None,
    )
    alt_names: list[Annotated[str, pydantic.Field(max_length=200)]] | None = pydantic.Field(
        max_length=255,
        description=(
            "List of alternate names that refer to this object.  "
            "These are useful in helping other databases recognize the object."
        ),
        default=None,
        examples=[["GaBi"]],
    )
    version: str | None = pydantic.Field(
        max_length=40,
        description=(
            "Version ID provided by publishers. Do not include static prefixes like 'v' or 'ver.'"
            "If there is no version ID, an issue date in the format YYYY-MM-DD or in ISO date format is acceptable."
            "Version IDs SHOULD be such that the most recent version is last in an ascending alphabetic search."
            "The combination (name, version) SHOULD be unique."
        ),
        examples=["2.3.0"],
        default=None,
    )
    link: str | None = pydantic.Field(
        max_length=200,
        description="URL of a web page providing access to the resource.",
        examples=["https://asphaltepd.org/epd/d/aRU5Po/"],
        default=None,
    )


class DatabaseResource(ResourceObject):
    pass


class SoftwareResource(ResourceObject):
    primary_function: SoftwarePrimaryFunction | None = pydantic.Field(
        description="The primary function of this software.",
        default=None,
    )
