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
import dataclasses
from types import UnionType
from typing import Any

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema, Version
from openepd.model.validation.common import validate_version_compatibility, validate_version_format
from openepd.model.validation.quantity import ExternalValidationConfig, QuantityValidator
from openepd.model.versioning import WithExtVersionMixin


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
            msg = f"Class {self.__class__} must declare an extension version"
            raise ValueError(msg)
        Version.parse_version(self._EXT_VERSION)  # validate format correctness
        super().__init__(**{"ext_version": self._EXT_VERSION, **data})

    _version_format_validator = pyd.validator("ext_version", allow_reuse=True, check_fields=False)(
        validate_version_format
    )
    _version_major_match_validator = pyd.validator("ext_version", allow_reuse=True, check_fields=False)(
        validate_version_compatibility("_EXT_VERSION")
    )


def setup_external_validators(quantity_validator: QuantityValidator):
    """Set the implementation unit validator for specs."""
    ExternalValidationConfig.QUANTITY_VALIDATOR = quantity_validator


@dataclasses.dataclass(kw_only=True)
class CodegenSpec:
    """
    Specification for codegen when generating RangeSpecs from normal specs.

    See openepd.mode.specs.README.md for details.
    """

    exclude_from_codegen: bool = False
    override_type: type | UnionType
