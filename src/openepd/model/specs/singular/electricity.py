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


class ElectricityV1(BaseOpenEpdHierarchicalSpec):
    """Electrical equipment and components and supplies."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Electricity",
        display_name="Electricity",
        description="Electrical equipment and components and supplies",
        masterformat="48 00 00 Electrical Power Generation Manufacturers",
        declared_unit=Amount(qty=1, unit="kWh"),
    )
