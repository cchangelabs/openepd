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
import abc
from enum import StrEnum

from ..querylang.operators import BaseQueryLangOperator, BaseScalarOperator
from ..querylang.types import ScalarArgType
from .errors import MaterialFilterError


class BaseMfOperator(BaseQueryLangOperator, metaclass=abc.ABCMeta):
    """Marker base for MF operators."""

    pass


class BaseMfScalarOperator(BaseScalarOperator, BaseMfOperator, metaclass=abc.ABCMeta):
    """Base class for Material Filter scalar operators."""

    pass


class SupportedOperators(StrEnum):
    EQ = "eq"
    NOT_EQ = "not_eq"
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    LIKE = "like"
    NOT_LIKE = "not_like"
    TARGET = "target"
    MIN = "min"
    MAX = "max"
    IN = "in"
    NOT_IN = "not_in"
    IS_SET = "is_set"
    NOT_IS_SET = "not_is_set"


class ExactQlOperator(BaseMfScalarOperator):
    """
    Matches if target value equals an argument.

    For number or unit types:
      Matches if argument - 1% >= target value <= argument + 1%
    For string type:
      Matches if target value == argument
    """

    NAME = SupportedOperators.EQ
    SYMBOLS = ["=", "=="]


class GtQlOperator(BaseMfScalarOperator):
    """Matches if target value is greater than an argument."""

    NAME = SupportedOperators.GT
    SYMBOLS = [">"]


class GteQlOperator(BaseMfScalarOperator):
    """Matches if target value is greater than or equals an argument."""

    NAME = SupportedOperators.GTE
    SYMBOLS = [">="]


class LtQlOperator(BaseMfScalarOperator):
    """Matches if target value is less than an argument."""

    NAME = SupportedOperators.LT
    SYMBOLS = ["<"]


class LteQlOperator(BaseMfScalarOperator):
    """Matches if target value is less than or equals an argument."""

    NAME = SupportedOperators.LTE
    SYMBOLS = ["<="]


class LikeQlOperator(BaseMfScalarOperator):
    """Matches if the target value contains the argument. Case Insensitive."""

    NAME = SupportedOperators.LIKE
    SYMBOLS = ["~"]

    def sanitize_arg(self, val: ScalarArgType) -> ScalarArgType:
        if isinstance(val, str):
            return val
        msg = f"Invalid argument type for {self.NAME} operator. Expected str, got: {val!r}"
        raise MaterialFilterError(msg)


class NotLikeQlOperator(BaseMfScalarOperator):
    """Matches if the target value does not contain the argument. Case Insensitive."""

    NAME = SupportedOperators.NOT_LIKE
    SYMBOLS = ["!~"]

    def sanitize_arg(self, val: ScalarArgType) -> ScalarArgType:
        if isinstance(val, str):
            return val
        msg = f"Invalid argument type for {self.NAME} operator. Expected str, got: {val!r}"
        raise MaterialFilterError(msg)


class TargetQlOperator(BaseMfScalarOperator):
    """Matches if argument - 10% >= target value <= argument + 10%."""

    NAME = SupportedOperators.TARGET
    SYMBOLS = ["~="]


class MinQlOperator(BaseMfScalarOperator):
    """Matches if target value >= argument - 1%."""

    NAME = SupportedOperators.MIN
    SYMBOLS = [">~"]


class MaxQlOperator(BaseMfScalarOperator):
    """Matches if target value <= argument + 1%."""

    NAME = SupportedOperators.MAX
    SYMBOLS = ["<~"]


class InQlOperator(BaseMfOperator):
    """
    Matches if target value is in a list of arguments.

    If target value is a scalar type then matches if target value is IN the argument list.
    If target value is an array type then matches if target value intersects the argument list.
    """

    NAME = SupportedOperators.IN
    IS_MULTI_ARG = True


class NotInQlOperator(BaseMfOperator):
    """
    Matches if target value is not in a list of arguments.

    If target value is a scalar type then matches if target value is NOT IN the argument list.
    If target value is an array type then matches if target value DOES NOT intersect the argument list.
    """

    NAME = SupportedOperators.NOT_IN
    IS_MULTI_ARG = True
