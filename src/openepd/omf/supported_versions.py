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
from enum import Enum

from ..querylang.dto import VersionInfo
from .dto import MfFieldSet
from .errors import MaterialFilterError


class SupportedMaterialFilterVersionsEnum(Enum):
    """
    Enum of Material Filter versions supported by the system.

    An enum class listing all the supported versions the system can work with. The enum value is the version info object
    which can be matched against the MaterialFilterQuery.

    Exhaustiveness check should be used when making a branched code working with different version, in such a way our
    static type checker will raise a flag when we are missing a newly created case somewhere in the code.

    Example:
        ```
        mf_version = SupportedMaterialFilterVersionsEnum.get_by_version_info(mf.get_version())

        if mf_version is SupportedMaterialFilterVersionsEnum.V2_0:
            return self.__translate_mf2_query_to_oldstyle_kwargs(mf)
        else:
            assert_never(mf_version)
        ```
    Not using `match` with enums since there is an unclear handling of execution paths in mypy, see
    https://github.com/python/mypy/issues/12010

    This will fail static type checker when a new version is added to the enum, and we will be forced to add a new case.

    For places where we work with the version info object, exhaustiveness check is needed.
    For the places where we create the new MaterialFilter objects,
    things will not break when we add a new version to the enum (which is correct), but
    things will break when we delete the old one from the enum.

    All-in-all this matches very well with the notion of 'this is an enum of versions supported by the system'.

    """

    OMF_V2_0 = VersionInfo(major=2, minor=0, fieldset=MfFieldSet.OPEN_MATERIAL_FILTER)

    @classmethod
    def get_by_version_info(cls, v: VersionInfo) -> "SupportedMaterialFilterVersionsEnum":
        """
        Get the version enum form raw VersionInfo object.

        :param v:
        :return: version enum
        """
        match = next((e for e in cls if e.value == v), None)
        if not match:
            msg = f"Unsupported version {v}"
            raise MaterialFilterError(msg)

        return match
