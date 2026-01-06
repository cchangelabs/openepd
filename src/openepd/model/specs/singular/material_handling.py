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
from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class ConveyorsV1(BaseOpenEpdHierarchicalSpec):
    """
    Machinery and tools designed to move materials within a facility, both manually and automatically.

    This includes various types of conveyors such as belt, roller, and overhead conveyors.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Conveyors",
        display_name="Conveyors",
        historical_names=["Material Handling >> Conveyors"],
        description="Machinery and tools designed to move materials within a facility, both manually and automatically. This includes various types of conveyors such as belt, roller, and overhead conveyors.",
        masterformat="41 21 00 Conveyors",
        declared_unit=Amount(qty=1, unit="m"),
    )


class MaterialHandlingV1(BaseOpenEpdHierarchicalSpec):
    """
    Material handling.

    Equipment and supplies for moving, storing, administering, and protecting materials during the handling process.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MaterialHandling",
        display_name="Material Processing and Handling",
        short_name="Material Handling",
        historical_names=["Material Handling"],
        description="Equipment and supplies for moving, storing, administering, and protecting materials during the handling process.",
        masterformat="41 00 00 Material Processing and Handling",
    )

    # Nested specs:
    Conveyors: ConveyorsV1 | None = None
