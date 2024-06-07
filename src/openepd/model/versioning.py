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
from abc import ABC
from enum import ReprEnum
from typing import ClassVar, NamedTuple

from openepd.compat.pydantic import pyd


class WithExtVersionMixin(ABC, pyd.BaseModel):
    """Mixin for extensions supporting versions: recommended way."""

    _EXT_VERSION: ClassVar[str]
    """Exact version (major, minor) of the spec extension"""

    def __init_subclass__(cls):
        """Set the default value for the ext_version field from _EXT_VERSION class var."""
        super().__init_subclass__()
        if hasattr(cls, "_EXT_VERSION"):
            cls.__fields__["ext_version"].default = cls._EXT_VERSION

    # Note: default is set programmatically in __init_subclass__
    ext_version: str | None = pyd.Field(description="Extension version", example="3.22", default=None)


class Version(NamedTuple):
    """Version of the object or specification."""

    major: int
    minor: int

    @staticmethod
    def parse_version(version: str) -> "Version":
        """Parse the version of extension or the format.

        Version is expected to be major.minor

        :param version: The extension version.
        :return: A tuple of major and minor version numbers.
        """
        splits = version.split(".", 1) if isinstance(version, str) else None
        if len(splits) != 2:
            raise ValueError(f"Invalid version: {version}")
        if not splits[0].isdigit() or not splits[1].isdigit():
            raise ValueError(f"Invalid version: {version}")
        return Version(major=int(splits[0]), minor=int(splits[1]))

    def __str__(self) -> str:
        return self.as_str()

    def __repr__(self) -> str:
        return f"[Version] {self.as_str()}"

    def as_str(self) -> str:
        """Return the version as a string."""
        return f"{self.major}.{self.minor}"


class OpenEpdVersions(Version, ReprEnum):
    """
    Enum of supported openEPD versions.

    When adding a new version - make sure to add a new major version to the list of supported versions.
    When doing non-breaking change - update minor version in a corresponding enum value.
    """

    Version0 = Version(major=0, minor=1)

    @classmethod
    def get_supported_versions(cls) -> list[Version]:
        """Return a list of supported versions."""
        return [x.value for x in cls]

    @classmethod
    def supported_versions_str(cls, major_only: bool = False) -> str:
        """
        Return a comma separated list of the supported versions.

        This is a utility method, might be helpful for logging, building error messages, etc.

        :param major_only: If True, minor component will be replaced with 'x'. E.g. `2.x` instead of `2.1`
        """
        if major_only:
            return ", ".join(f"{x.major}.x" for x in cls.get_supported_versions())
        return ", ".join(str(x) for x in cls.get_supported_versions())

    @classmethod
    def get_most_recent_version(cls, branch: int | None = 0) -> Version:
        """
        Return the most recent version of the openEPD format.

        If branch is specified - returns the most recent version of the specified branch, otherwise returns
        the most recent version among all branches.
        """
        if branch is None:
            highest: Version = max(cls, key=lambda x: x.value.major)  # type: ignore
            if highest:
                return highest
        for x in cls:
            if x.value.major == branch:
                return x.value
        raise ValueError(
            f"No version {branch}.x is not supported. Supported versions are: {', '.join(str(x.value) for x in cls)}"
        )

    @classmethod
    def get_current(cls) -> Version:
        """Return the most recent stable version of the format."""
        return cls.get_most_recent_version()

    def __repr__(self):
        return f"[OpenEpdVesion] {self.name} - {self.value}"
