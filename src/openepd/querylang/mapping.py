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
from __future__ import annotations

from collections.abc import Iterable, Iterator

import pydantic as pyd

from openepd.utils.reflection import FieldNameMatcher, is_field_matched

from .dto import FieldMappingDto


def is_field_matched_by_def(field_def: FieldMappingDto, matcher: FieldNameMatcher, delimiter: str) -> bool:
    """
    Check if a field mapping matches the given matcher.

    :param field_def: The field mapping definition to check.
    :param matcher: The matcher to compare against (can be a string, regex pattern, or callable).
    :param delimiter: The delimiter used to extract the short field name from the full field name.

    :return: True if the field matches the matcher, False otherwise.
    """
    return is_field_matched(field_def.lang_field_name, field_def.lang_field_name.rsplit(delimiter, 2)[-1], matcher)


class FieldMappingLibrary:
    def __init__(self, field_mappings: dict[str, FieldMappingDto], delimiter: str = ".") -> None:
        self._field_mappings = field_mappings
        self._delimiter = delimiter

    @classmethod
    def from_list(cls, mappings: list[FieldMappingDto]) -> FieldMappingLibrary:
        mapping_dict = {fm.lang_field_name: fm for fm in mappings}
        return cls(mapping_dict)

    @classmethod
    def from_json(cls, json_str: str) -> FieldMappingLibrary:
        mappings = pyd.TypeAdapter(list[FieldMappingDto]).validate_json(json_str)
        return cls.from_list(mappings)

    @property
    def delimiter(self) -> str:
        return self._delimiter

    def get_by_name(self, name: str) -> FieldMappingDto | None:
        return self._field_mappings.get(name)

    def add(self, field_mapping: FieldMappingDto) -> None:
        self._field_mappings[field_mapping.lang_field_name] = field_mapping

    def get_first(self, matcher: FieldNameMatcher) -> FieldMappingDto | None:
        for fd in self._field_mappings.values():
            if is_field_matched_by_def(fd, matcher, self.delimiter):
                return fd
        return None

    def filter(self, *matchers: FieldNameMatcher) -> list[FieldMappingDto]:
        result: dict[str, FieldMappingDto] = {}
        for fd in self._field_mappings.values():
            if any(is_field_matched_by_def(fd, matcher, self.delimiter) for matcher in matchers):
                result[fd.lang_field_name] = fd
        return list(result.values())

    def override(
        self,
        matcher: FieldNameMatcher,
        target_field_name: str | None = None,
        datatype: str | None = None,
        description: str | None = None,
        supported_operators: list[str] | None = None,
    ) -> None:
        fm = self.get_first(matcher)
        if not fm:
            raise KeyError(f"Field mapping '{matcher}' not found.")
        if target_field_name is not None:
            fm.target_field_name = target_field_name
        if datatype is not None:
            fm.datatype = datatype
        if supported_operators is not None:
            fm.supported_operators = supported_operators
        if description is not None:
            fm.description = description

    def override_all(
        self,
        matchers: Iterable[FieldNameMatcher],
        target_field_name: str | None = None,
        datatype: str | None = None,
        description: str | None = None,
        supported_operators: list[str] | None = None,
    ) -> None:
        for m in matchers:
            self.override(
                m,
                target_field_name=target_field_name,
                datatype=datatype,
                description=description,
                supported_operators=supported_operators,
            )

    def exclude(self, *matchers: FieldNameMatcher) -> None:
        for matcher in matchers:
            to_delete: list[str] = []
            for fd in self._field_mappings.values():
                if is_field_matched_by_def(fd, matcher, self.delimiter):
                    to_delete.append(fd.lang_field_name)
            for name in to_delete:
                del self._field_mappings[name]

    def keep_only(self, matchers: set[FieldNameMatcher]) -> None:
        to_remove = []
        for fd in self._field_mappings.values():
            short_name = fd.lang_field_name.rsplit(self.delimiter, 2)[-1]
            if not any(is_field_matched(fd.lang_field_name, short_name, matcher) for matcher in matchers):
                to_remove.append(fd.lang_field_name)
        for name in to_remove:
            del self._field_mappings[name]

    def clone(self) -> FieldMappingLibrary:
        cloned_mappings = {name: fm.model_copy() for name, fm in self._field_mappings.items()}
        return FieldMappingLibrary(cloned_mappings)

    def to_list(self) -> list[FieldMappingDto]:
        return list(self._field_mappings.values())

    def __iter__(self) -> Iterator[FieldMappingDto]:
        return iter(self._field_mappings.values())
