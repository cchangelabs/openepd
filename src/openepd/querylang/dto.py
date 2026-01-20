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

import abc
import datetime
from typing import Annotated, Any, Literal, NamedTuple, overload

import pydantic as pyd

from .errors import QueryLangError


class VersionInfo(NamedTuple):
    """Holds information about query language version."""

    major: int
    minor: int
    fieldset: str

    def __str__(self) -> str:
        return f"{self.fieldset}/{self.format_version()}"

    @classmethod
    @overload
    def from_string(cls, fieldset: str, val: None) -> None: ...

    @classmethod
    @overload
    def from_string(cls, fieldset: str, val: str) -> VersionInfo: ...

    @classmethod
    def from_string(cls, fieldset: str, val: str | None) -> VersionInfo | None:
        """
        Build new VersionInfo object from string.

        :raise: QueryLangError - if string is invalid.
        :returns: new VersionInfo if input value is valid and not `None` and `None` - if input is `None`.
        """
        if val is None:
            return None
        major, minor = val.split(".", maxsplit=1)
        try:
            return cls(int(major), int(minor), fieldset)
        except ValueError as e:
            raise QueryLangError("Invalid version: " + val) from e

    def format_version(self) -> str:
        return f"{self.major}.{self.minor}"


class ExpressionElement(pyd.BaseModel, metaclass=abc.ABCMeta):
    pass


class OperandDto(ExpressionElement):
    obj: Literal["arg"] = "arg"
    name: str
    type: str
    value: Any
    value_type: str | None = None


class OperatorDto(ExpressionElement):
    obj: Literal["op"] = "op"
    op: str
    operands: list[OperandOrOperator]


OperandOrOperator = Annotated[OperatorDto | OperandDto, pyd.Field(discriminator="obj")]
OperatorDto.model_rebuild()


class QueryLangQuery(pyd.BaseModel):
    tree: OperandOrOperator
    original_query: str


PragmaArg = str | int | bool | datetime.date


class PragmaDto(pyd.BaseModel):
    name: str
    args: list[PragmaArg] = pyd.Field(default_factory=list)


class FieldMappingDto(pyd.BaseModel):
    lang_field_name: str
    target_field_name: str
    container_type: str | None = None
    datatype: str
    description: str | None = None
    supported_operators: list[str] | None = None
    ext: dict[str, Any] = pyd.Field(default_factory=dict)
