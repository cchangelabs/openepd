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
__all__ = ["ScopePhases"]


from enum import StrEnum

from openepd.utils.functional import classproperty


# noinspection PyMethodParameters
class ScopePhases(StrEnum):
    """Container of common way to specify known scope phases under OpenEPD standard."""

    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A1A2A3 = "A1A2A3"
    A4 = "A4"
    A5 = "A5"

    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    B4 = "B4"
    B5 = "B5"
    B6 = "B6"
    B7 = "B7"

    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"

    D = "D"

    @classproperty
    def a1a2a3(cls) -> str:
        return cls.A1A2A3.lower()

    @classproperty
    def a1(cls) -> str:
        return cls.A1.lower()

    @classproperty
    def a2(cls) -> str:
        return cls.A2.lower()

    @classproperty
    def a3(cls) -> str:
        return cls.A3.lower()

    @classproperty
    def a4(cls) -> str:
        return cls.A4.lower()

    @classproperty
    def a5(cls) -> str:
        return cls.A5.lower()

    @classproperty
    def b1(cls) -> str:
        return cls.B1.lower()

    @classproperty
    def b2(cls) -> str:
        return cls.B2.lower()

    @classproperty
    def b3(cls) -> str:
        return cls.B3.lower()

    @classproperty
    def b4(cls) -> str:
        return cls.B4.lower()

    @classproperty
    def b5(cls) -> str:
        return cls.B5.lower()

    @classproperty
    def b6(cls) -> str:
        return cls.B6.lower()

    @classproperty
    def b7(cls) -> str:
        return cls.B7.lower()

    @classproperty
    def c1(cls) -> str:
        return cls.C1.lower()

    @classproperty
    def c2(cls) -> str:
        return cls.C2.lower()

    @classproperty
    def c3(cls) -> str:
        return cls.C3.lower()

    @classproperty
    def c4(cls) -> str:
        return cls.C4.lower()

    @classproperty
    def d(cls) -> str:
        return cls.D.lower()

    @classmethod
    def a_scopes(cls, *, lowercase: bool = False) -> tuple[str, ...]:
        result = (ScopePhases.A1A2A3, ScopePhases.A1, ScopePhases.A2, ScopePhases.A3, ScopePhases.A4, ScopePhases.A5)
        if lowercase:
            return cls._lowercase(result)
        return result

    @classmethod
    def b_scopes(cls, *, lowercase: bool = False) -> tuple[str, ...]:
        result = (
            ScopePhases.B1,
            ScopePhases.B2,
            ScopePhases.B3,
            ScopePhases.B4,
            ScopePhases.B5,
            ScopePhases.B6,
            ScopePhases.B7,
        )
        if lowercase:
            return cls._lowercase(result)

        return result

    @classmethod
    def c_scopes(cls, *, lowercase: bool = False) -> tuple[str, ...]:
        result = (ScopePhases.C1, ScopePhases.C2, ScopePhases.C3, ScopePhases.C4)
        if lowercase:
            return cls._lowercase(result)
        return result

    @classmethod
    def d_scopes(cls, *, lowercase: bool = False) -> tuple[str, ...]:
        result = (ScopePhases.D,)
        if lowercase:
            return cls._lowercase(result)
        return result

    @classmethod
    def all_scopes(cls, *, lowercase: bool = False) -> tuple[str, ...]:
        result = cls.a_scopes() + cls.b_scopes() + cls.c_scopes() + cls.d_scopes()
        if lowercase:
            return cls._lowercase(result)
        return result

    @classmethod
    def _lowercase(cls, scopes: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(scope.lower() for scope in scopes)
