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
from typing import Annotated, Any, Callable, Type, TypeAlias

from openepd.compat.pydantic import pyd
from openepd.model.versioning import Version


def together_validator(field1: str, field2: Any, values: dict[str, Any]) -> Any:
    """Shared validator to ensure that two fields are provided together or not provided at all."""
    value1 = values.get(field1)
    value2 = values.get(field2)
    if value1 is not None and value2 is None or value1 is None and value2 is not None:
        raise ValueError(f"Both or neither {field1} and {field2} days must be provided together")


def validate_version_format(v: str) -> str:
    """Ensure that the extension version is valid."""
    Version.parse_version(v)  # will raise an error if not valid
    return v


def validate_version_compatibility(class_version_attribute_name: str) -> Callable[[Type, str], str]:
    """Ensure that the object which is passed for parsing and validation is compatible with the class."""

    # we need closure to pass property name, since actual class will only be available in runtime
    def internal_validate_version_compatibility(cls: Type, v: str) -> str:
        if not hasattr(cls, class_version_attribute_name):
            raise ValueError(f"Class {cls} must declare a class var extension var named {class_version_attribute_name}")

        class_version = getattr(cls, class_version_attribute_name)
        if Version.parse_version(v).major != Version.parse_version(class_version).major:
            raise ValueError(f"Extension version {v} does not match class version {class_version}")
        return v

    return internal_validate_version_compatibility


ReferenceStr: TypeAlias = Annotated[
    str,
    pyd.Field(description="Reference to another object", example="https://buildingtransparency.org/ec3/epds/1u7zsed8"),
]
