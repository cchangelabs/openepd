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
__all__ = [
    "MANUFACTURER_DESCRIPTION",
    "PLANT_DESCRIPTION",
    "Ec3EpdExtension",
    "Epd",
    "EpdFactory",
    "EpdPreview",
    "EpdPreviewV0",
    "EpdRef",
    "EpdV0",
    "EpdWithDeps",
    "EpdWithDepsV0",
]

import pydantic

from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes
from openepd.model.declaration import (
    DEVELOPER_DESCRIPTION,
    PROGRAM_OPERATOR_DESCRIPTION,
    THIRD_PARTY_VERIFIER_DESCRIPTION,
    BaseDeclaration,
)
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org
from openepd.model.specs.singular import Specs
from openepd.model.versioning import OpenEpdVersions, Version

# Import light versions here for compatibility reasons so they are available from the same import location
from .light.epd import MANUFACTURER_DESCRIPTION, PLANT_DESCRIPTION, Ec3EpdExtension, EpdRef  # noqa: F401
from .light.epd import EpdPreviewV0 as EpdPreviewV0Light


class EpdPreviewV0(EpdPreviewV0Light):
    specs: Specs = pydantic.Field(  # type: ignore[assignment]
        default_factory=Specs,  # type: ignore[arg-type]
        description="Data structure(s) describing performance specs of product. Unique for each material type.",
    )


EpdPreview = EpdPreviewV0


class EpdV0(WithLciaMixin, EpdPreviewV0, title="EPD (Full)"):
    """Represent an EPD."""

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "epd"

    @pydantic.field_validator("compliance", mode="before")
    def validate_compliance(cls, v: list | None):
        """Handle correctly None values for compliance field."""
        if v is None:
            return []
        return v

    @pydantic.field_validator("includes", mode="before")
    def validate_includes(cls, v: list | None):
        """Handle correctly None values for includes field."""
        if v is None:
            return []
        return v


Epd = EpdV0


class EpdWithDepsV0(EpdV0, title="EPD (with Dependencies)"):
    """
    Expanded version of the EPD.

    Contains related entities - orgs - with full fields, to support object matching in implementations.
    For now the implementation matches the above EpdV0 entity, but they will diverge as normal Epd would have
    some required fields in Org (like web_domain), and WithDeps would not.
    """

    manufacturer: Org | None = pydantic.Field(description=MANUFACTURER_DESCRIPTION, default=None)  # type: ignore[assignment]
    epd_developer: Org | None = pydantic.Field(description=DEVELOPER_DESCRIPTION, default=None)  # type: ignore[assignment]
    program_operator: Org | None = pydantic.Field(description=PROGRAM_OPERATOR_DESCRIPTION, default=None)  # type: ignore[assignment]
    third_party_verifier: Org | None = pydantic.Field(description=THIRD_PARTY_VERIFIER_DESCRIPTION, default=None)  # type: ignore[assignment]


EpdWithDeps = EpdWithDepsV0


class EpdFactory(BaseDocumentFactory[BaseDeclaration]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = OpenEpdDoctypes.Epd
    VERSION_MAP: dict[Version, type[BaseDeclaration]] = {OpenEpdVersions.Version0: EpdV0}
