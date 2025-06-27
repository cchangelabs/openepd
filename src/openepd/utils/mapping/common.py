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
__all__ = (
    "BaseDataMapper",
    "KeyValueMapper",
    "ReferenceMapper",
    "RegexMapper",
    "SimpleDataMapper",
)

import abc
from collections.abc import Mapping
import re
from typing import Generic, TypeAlias, TypeVar, assert_never, cast

T = TypeVar("T")
K = TypeVar("K")


class BaseDataMapper(Generic[T, K], abc.ABC):
    """
    Base class for all data mappers.

    Data mappers are objects used to map some input values to output values of different types.

    Typical use case is mapping between different aliases of impact names with OpenEpd naming conventions.
    """

    @abc.abstractmethod
    def map(self, input_value: T, default_value: K | None, *, raise_if_missing: bool = False) -> K | None:
        """
        Map the input value to the output value.

        :param input_value: The input value to map.
        :param default_value: The default value to return if there is no mapping for the input value.
        :param raise_if_missing: Whether to raise an exception if there is no mapping for the input value.

        :raise ValueError: If there is no mapping for the input value and raise_if_missing is True.
        """
        pass


class SimpleDataMapper(BaseDataMapper[T, T], Generic[T]):
    """A data mapper that does not change the type of the input value."""

    DATABASE: Mapping[T, T] = {}

    def map(self, input_value: T, default_value: T | None, *, raise_if_missing: bool = False) -> T | None:
        """
        Map the input value to the output value.

        :param input_value: The input value to map.
        :param default_value: The default value to return if there is no mapping for the input value.
        :param raise_if_missing: Whether to raise an exception if there is no mapping for the input value.

        :raise ValueError: If there is no mapping for the input value and raise_if_missing is True.
        """
        if raise_if_missing and input_value not in self.DATABASE:
            msg = f"No mapping for input value: {input_value}"
            raise ValueError(msg)

        return self.DATABASE.get(input_value, default_value)


class KeyValueMapper(BaseDataMapper[str, T], Generic[T]):
    """
    A data mapper that maps input values to output values using keywords.

    List of values is expected to be a list string object or a list of objects easily castable to string.
    """

    KV: Mapping[str, list[T]] = {}

    def map(self, input_value: str, default_value: T | None, *, raise_if_missing: bool = False) -> T | None:
        """
        Map the input value to the output value using keywords.

        :param input_value: The input value to map.
        :param default_value: The default value to return if there is no mapping for input value.
        :param raise_if_missing: Whether to raise an exception if there is no mapping for the input value.

        :raise ValueError: If there is no mapping for the input value and raise_if_missing is True.
        """
        for impact_name, keywords in self.KV.items():
            for keyword in keywords:
                if str(keyword).strip().lower() in input_value.strip().lower():
                    return cast(T, impact_name)

        if raise_if_missing:
            msg = f"No mapping for input value: {input_value}"
            raise ValueError(msg)

        return default_value


class RegexMapper(BaseDataMapper[str, T], Generic[T]):
    """A data mapper that maps input values to output values using regex."""

    PATTERNS: dict[str, str] = {}
    _compiled_patterns: dict[str, re.Pattern]

    def __init__(self) -> None:
        self._compiled_patterns: dict[str, re.Pattern] = {
            key: re.compile(pattern, re.IGNORECASE) for key, pattern in self.PATTERNS.items()
        }

    def map(self, input_value: str, default_value: T | None, *, raise_if_missing: bool = False) -> T | None:
        """
        Map the input value to the output value using regex.

        :param input_value: The input value to map.
        :param default_value: The default value to return if there is no mapping for an input value.

        :param raise_if_missing: Whether to raise an exception if there is no mapping for the input value.

        :raise ValueError: If there is no mapping for the input value and raise_if_missing is True.
        """
        for impact_name, pattern in self._compiled_patterns.items():
            if pattern.search(input_value.strip().lower()):
                return cast(T, impact_name)

        if raise_if_missing:
            msg = f"No mapping for input value: {input_value}"
            raise ValueError(msg)

        return default_value


_TRmRules: TypeAlias = str | re.Pattern | list[str | re.Pattern]


class ReferenceMapper(BaseDataMapper[str, _TRmRules]):
    """
    A mapper that maps input values of any form to the expected value format.

    Expected values may be a value or a list of values. Values are expected to be a string object, regular expressions,
    or objects easily castable to string.
    """

    def map(self, input_value: str, default_value: str | None, *, raise_if_missing: bool = False) -> str | None:  # type: ignore[override]
        """
        Return specified key as a value if any of the values in the list matches the input value.

        :param input_value: value to be checked against the list of specified rules
        :param default_value: default value to return if no match is found
        :param raise_if_missing: whether to raise an exception if no match is found

        :return: mapped value if find any match, else default value

        :raise ValueError: if no match is found and raise_if_missing is True
        """
        for key, value in self.MAPPING.items():
            if not self._is_applied(input_value, value):
                continue
            return key

        if raise_if_missing:
            msg = f"No mapping for input value: {input_value}"
            raise ValueError(msg)

        return default_value

    def _is_applied(self, input_value: str, rules: _TRmRules) -> bool:
        if isinstance(rules, str | re.Pattern):
            return self._is_applied_to_item(input_value, rules)
        elif isinstance(rules, list):
            return any(self._is_applied_to_item(input_value, rule) for rule in rules)
        else:
            assert_never(rules)

    def _is_applied_to_item(self, input_value: str, rule: str | re.Pattern) -> bool:
        if isinstance(rule, str):
            return input_value.strip().lower() == rule.strip().lower()
        elif isinstance(rule, re.Pattern):
            return bool(rule.search(input_value.strip().lower()))
        else:
            assert_never(rule)

    MAPPING: Mapping[str, _TRmRules] = {}
