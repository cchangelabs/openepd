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
from typing import Any, ClassVar

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema


class BaseCompatibilitySpec(BaseOpenEpdSchema):
    """
    Base class for compatibility (legacy) specs.

    See Specs model for implementation.
    """

    COMPATIBILITY_SPECS_KEY_OLD: ClassVar[str]
    COMPATIBILITY_SPECS_KEY_NEW: ClassVar[str]
    COMPATIBILITY_MAPPING: ClassVar[dict[str, str]]


def get_safely(d: dict, path: str) -> tuple[bool, Any]:
    """
    Get a value from a mixed object via dotted path.

    Mixed object can be a combination of dicts and pydatnic Models on any hierarchy.
    :param d: source dict/object to search in
    :param path: dotted path in object like specs.Concrete.strength_28d
    :return: tuple (WasFound, Value). First element tells if value was found, second - the value itself.
    """
    path_elements = path.split(".")
    current: Any = d
    for p in path_elements:
        match current:
            case dict():
                if p not in current:
                    return False, None
                current = current.get(p)
            case pyd.BaseModel() as model:
                if not hasattr(current, p) or p not in model.__fields_set__:
                    return False, None
                current = getattr(current, p)
            case _:
                return False, None

    return True, current


def set_safely(d: dict, path: str, value: Any) -> None:
    """
    Safely set an element in a dict.

    Warning: this is asymmetric compared to get_safely, since it sets value in a dict, not in pydantic model object.

    :param d: source dict/object to set value in
    :param path: dotted path in object like specs.Concrete.strength_28d
    :param value: value to set
    :return: None
    """
    path_elements = path.split(".")
    current = d
    for p in path_elements[:-1]:
        if current.get(p) is None:
            current[p] = {}
        current = current[p]

    current[path_elements[-1]] = value
