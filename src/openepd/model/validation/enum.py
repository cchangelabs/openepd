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
from collections.abc import Callable
from typing import Any

from openepd.model.common import EnumGroupingAware


def exclusive_groups_validator_factory(enum_type: type[EnumGroupingAware]) -> Callable[[type, Any], Any]:
    """
    Create an exclusive groups validator.

    If we have a certain enum TheEnum, and a field of list[TheEnum], where list can contain only one value of each of
    the groups, this validator should be used. For example, ACI exposure classes for concrete specify various
    parameters such as water resistance, chemical resistance, etc., and the list of classes can have 0 or 1 from each
    group.

    :param enum_type:Enum type which supports groupings.
    :return:value, or raises ValueError if not allowed combination is given.
    """

    def enum_exclusive_grouping_validator(cls, value: list | None) -> list | None:
        for grouping in enum_type.get_groupings():
            matching_from_group = [v for v in (value or []) if v in grouping]
            if len(matching_from_group) > 1:
                msg = f"Values {', '.join(matching_from_group)} are not allowed together."
                raise ValueError(msg)

        return value

    return enum_exclusive_grouping_validator
