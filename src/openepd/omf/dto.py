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
from enum import Enum, StrEnum
import logging
import re
from typing import Final, TypeVar, Union

import pydantic as pyd

from openepd.utils.none_raises import none_raises

from ..querylang.dto import PragmaDto, VersionInfo
from ..querylang.types import ArgCommentType, ArgType
from .errors import MaterialFilterError
from .operators import SupportedOperators

logger = logging.getLogger(__name__)


class MfFieldSet(str, Enum):
    OPEN_MATERIAL_FILTER = "open_mf"


VERSION_PRAGMA_NAMES: dict[MfFieldSet, tuple[str]] = {
    MfFieldSet.OPEN_MATERIAL_FILTER: ("oMF",),
}


_VERSION_PRAGMA_NAMES_HASHMAP: dict[str, MfFieldSet] = {}
for field_set, names in VERSION_PRAGMA_NAMES.items():
    for n in names:
        n = n.upper()
        if n in _VERSION_PRAGMA_NAMES_HASHMAP:
            msg = f"Duplicate version pragma name: {n}. It already describes {_VERSION_PRAGMA_NAMES_HASHMAP[n]}"
            raise MaterialFilterError(msg)
        _VERSION_PRAGMA_NAMES_HASHMAP[n] = field_set

_VERSION_REGEX = re.compile(r"(\d+\.\d+)(\/\d+)?")

PRAGMA_LCIA: Final[str] = "lcia"
"""
Pragma for LCIA method. It is used to specify the LCIA method for the material filter.
"""

T = TypeVar("T", bound=ArgType)


class MfPredicate(pyd.BaseModel):
    model_config = pyd.ConfigDict(use_enum_values=False, populate_by_name=True)

    field: str
    operator: str = pyd.Field(alias="op")
    arg: ArgType = pyd.Field(union_mode="smart")
    arg_comment: ArgCommentType | None = None

    def get_arg_or_throw(self, arg_type: type[T]) -> T:
        if not isinstance(self.arg, arg_type):
            msg = f"Expected arg of type {arg_type}, got {self.arg}"
            raise MaterialFilterError(msg)
        return self.arg


class MfBooleanOp(StrEnum):
    AND = "and"
    OR = "or"
    NOT = "not"
    NONE = "none"


class MfExpression(pyd.BaseModel):
    """
    Boolean expression tree.

    type:
      - 'none' : leaf predicate
      - 'and'  : conjunction, children length >= 2
      - 'or'   : disjunction, children length >= 2
      - 'not'  : negation, children length == 1
    """

    type: MfBooleanOp = MfBooleanOp.NONE
    pred: MfPredicate | None = None
    children: list["MfExpression"] | None = None

    @classmethod
    def create_predicate_expression(cls, predicate: MfPredicate) -> "MfExpression":
        return MfExpression(type=MfBooleanOp.NONE, pred=predicate)

    @classmethod
    def create_not_expression(cls, expr: "MfExpression | None") -> "MfExpression":
        return MfExpression(type=MfBooleanOp.NOT, children=[expr] if expr is not None else [])

    @classmethod
    def create_and_expression(cls, *exprs: "MfExpression") -> "MfExpression":
        normalized_exprs: list[MfExpression] = [
            cls.create_predicate_expression(x) if isinstance(x, MfPredicate) else x  # type: ignore[arg-type]
            for x in exprs or []
        ]
        return MfExpression(type=MfBooleanOp.AND, children=normalized_exprs)

    @classmethod
    def create_or_expression(cls, *exprs: Union["MfExpression", MfPredicate]) -> "MfExpression":
        normalized_exprs: list[MfExpression] = [
            cls.create_predicate_expression(x) if isinstance(x, MfPredicate) else x for x in exprs or []
        ]
        return MfExpression(type=MfBooleanOp.OR, children=normalized_exprs)

    @classmethod
    def create_predicate(
        cls, field: str, arg: ArgType, op: str = SupportedOperators.EQ, arg_comment: ArgCommentType | None = None
    ):
        return MfPredicate(field=field, op=op, arg=arg, arg_comment=arg_comment)  # type: ignore[call-arg]

    def add_not_expression(self, expr: "MfExpression | None") -> "MfExpression":
        new_expr = self.create_not_expression(expr)
        if self.children is None:
            self.children = []
        self.children.append(new_expr)
        return new_expr

    def add_or_expression(self, expr: list["MfExpression"]) -> "MfExpression":
        new_expr = self.create_or_expression(*expr)
        if self.children is None:
            self.children = []
        self.children.append(new_expr)
        return new_expr

    def add_and_expression(self, exprs: list["MfExpression"]) -> "MfExpression":
        new_expr = self.create_and_expression(*exprs)
        if self.children is None:
            self.children = []
        self.children.append(new_expr)
        return new_expr

    def add_predicate(
        self, field: str, arg: ArgType, op: str = SupportedOperators.EQ, arg_comment: ArgCommentType | None = None
    ) -> "MfExpression":
        self.add_predicates([self.create_predicate(field=field, op=op, arg=arg, arg_comment=arg_comment)])
        return self

    def add_predicates(self, predicates: list[MfPredicate]) -> "MfExpression":
        if self.type == MfBooleanOp.NONE:
            msg = "Cannot add predicates to a leaf expression"
            raise ValueError(msg)
        if self.type == MfBooleanOp.NOT and len(predicates) != 1:
            msg = "NOT expression can only have one child predicate"
            raise ValueError(msg)
        if self.children is None:
            self.children = []
        self.children.extend([self.create_predicate_expression(x) for x in predicates])
        return self

    def get_predicate(self, field_name: str, operator: str) -> MfPredicate | None:
        for ex in self.children:  # type: ignore[union-attr]
            if ex.type == MfBooleanOp.NONE and ex.pred and ex.pred.field == field_name and ex.pred.operator == operator:
                return ex.pred
        return None

    def get_predicates_by_field(self, field_name: str) -> list[MfPredicate]:
        result: list[MfPredicate] = []
        for ex in self.children:  # type: ignore[union-attr]
            if ex.type == MfBooleanOp.NONE and ex.pred and ex.pred.field == field_name:
                result.append(ex.pred)
        return result

    def remove_predicate(self, to_remove: MfPredicate) -> "MfExpression":
        for ex in self.children:  # type: ignore[union-attr]
            if ex.type == MfBooleanOp.NONE and ex.pred and ex.pred == to_remove:
                self.children.remove(ex)  # type: ignore[union-attr]
                break
        return self


class MaterialFilter(pyd.BaseModel):
    pragma: list[PragmaDto]
    filter: MfExpression = pyd.Field(default_factory=lambda: MfExpression(type=MfBooleanOp.AND, children=[]))

    @staticmethod
    def format_full_version(fieldset_version: VersionInfo, lang_version: int) -> str:
        return f"{fieldset_version.format_version()}/{lang_version}"

    @classmethod
    def get_version_from_pragma(cls, pragma: list[PragmaDto]) -> VersionInfo | None:
        for x in pragma:
            if cls.is_version_pragma(x):
                current_field_set = _VERSION_PRAGMA_NAMES_HASHMAP[x.name.upper()]
                version_components = cls.__parse_version_arg(x)
                return VersionInfo.from_string(current_field_set, none_raises(version_components.group(1)))
        return None

    @classmethod
    def is_version_pragma(cls, pragma: PragmaDto) -> bool:
        if pragma.name.upper() in _VERSION_PRAGMA_NAMES_HASHMAP:
            return True
        return False

    @classmethod
    def get_lang_version_from_pragma(cls, pragma: list[PragmaDto]) -> int | None:
        """
        Return language version or None if no language version pragma is found.

        Example of the language version pragma: xMF("2.0/4"). In this example language version is 4.
        """
        for x in pragma:
            if cls.is_version_pragma(x):
                version_components = cls.__parse_version_arg(x)
                lang_version_component = version_components.group(2)
                if lang_version_component is None:
                    return None
                return int(lang_version_component[1:])
        return None

    def get_version(self) -> VersionInfo:
        version = self.get_version_from_pragma(self.pragma)
        if version is not None:
            return version
        else:
            msg = "Query doesn't represent material filter. No valid version pragma found."
            raise MaterialFilterError(msg)

    def get_lang_version(self) -> int | None:
        return self.get_lang_version_from_pragma(self.pragma)

    def get_pragma(self, pragma_name: str) -> PragmaDto | None:
        """Return pragma with given name or None if not found."""
        for x in self.pragma:
            if x.name == pragma_name:
                return x
        return None

    def get_lcia(self) -> str | None:
        """
        Return LCIA method for given material filter.

        :return: LCIA method string or none if not given
        """
        lcia_pragma = self.get_pragma(PRAGMA_LCIA)
        if lcia_pragma is None:
            return None

        assert len(lcia_pragma.args) == 1
        lcia_method = lcia_pragma.args[0]
        assert isinstance(lcia_method, str)
        return lcia_method

    def set_lcia(self, lcia_method: str) -> None:
        """
        Set or update the LCIA method pragma for this material filter.

        :param lcia_method: The LCIA method string to set.
        """
        # Remove any existing lcia pragma
        self.pragma = [p for p in self.pragma if p.name != PRAGMA_LCIA]
        # Add the new lcia pragma
        self.pragma.append(PragmaDto(name=PRAGMA_LCIA, args=[lcia_method]))

    @classmethod
    def __parse_version_arg(cls, x: PragmaDto) -> re.Match:
        if len(x.args) != 1 or not isinstance(x.args[0], str):
            msg = f"Invalid version pragma {x.name}. It must have one str argument holding version."
            raise MaterialFilterError(msg)
        version_components = _VERSION_REGEX.fullmatch(x.args[0])
        if not version_components:
            msg = f"Invalid version pragma {x.name}. Invalid version format."
            raise MaterialFilterError(msg)
        return version_components


class MaterialFilterOutputFormat(StrEnum):
    Json = "json"
    String = "string"
