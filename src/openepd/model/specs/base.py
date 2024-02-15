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
from typing import Any, NamedTuple

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import WithExtVersionMixin


class SpecVersion(NamedTuple):
    """Version of the spec."""

    major: int
    minor: int


def parse_ext_version(ext_version: str) -> SpecVersion:
    """Parse the extension version.

    :param ext_version: The extension version.
    :return: A tuple of major and minor version numbers.
    """
    splits = ext_version.split(".", 1) if isinstance(ext_version, str) else None
    if len(splits) != 2:
        raise ValueError(f"Invalid extension version: {ext_version}")
    if not splits[0].isdigit() or not splits[1].isdigit():
        raise ValueError(f"Invalid extension version: {ext_version}")
    return SpecVersion(major=int(splits[0]), minor=int(splits[1]))


class BaseOpenEpdSpec(BaseOpenEpdSchema):
    """Base class for all OpenEPD specs."""

    class Config:
        use_enum_values = False  # we need to store enums as strings and not values


class BaseOpenEpdHierarchicalSpec(BaseOpenEpdSpec, WithExtVersionMixin):
    """Base class for new specs (hierarchical, versioned)."""

    def __init__(self, **data: Any) -> None:
        # ensure that all the concrete spec objects fail on creations if they dont have _EXT_VERSION declared to
        # something meaningful
        if not hasattr(self, "_EXT_VERSION") or self._EXT_VERSION is None:
            raise ValueError(f"Class {self.__class__} must declare an extension version")
        parse_ext_version(self._EXT_VERSION)  # validate format correctness
        super().__init__(**{"ext_version": self._EXT_VERSION, **data})

    @pyd.validator("ext_version", check_fields=False)
    def check_ext_version(cls, v: str) -> str:
        """Ensure that the extension version is valid."""
        parse_ext_version(v)  # will raise an error if not valid
        return v

    @pyd.validator("ext_version", check_fields=False)
    def validate_ext_version_compatibility(cls, v: str) -> str:
        """Ensure that the extension version is the same as the class version."""
        if parse_ext_version(v).major != parse_ext_version(cls._EXT_VERSION).major:
            raise ValueError(f"Extension version {v} does not match class version {cls._EXT_VERSION}")
        return v
