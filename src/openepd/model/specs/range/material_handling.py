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
    "ConveyorsRangeV1",
    "MaterialHandlingRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class ConveyorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Machinery and tools designed to move materials within a facility, both manually and automatically.

    This includes various types of conveyors such as belt, roller, and overhead conveyors.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MaterialHandlingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Material handling.

    Equipment and supplies for moving, storing, administering, and protecting materials during the handling process.

    Range version.
    """

    _EXT_VERSION = "1.0"

    Conveyors: ConveyorsRangeV1 | None = None
