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
__all__ = ("AggregatesRangeV1",)

import pydantic

from openepd.model.common import RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import AggregateGradation, AggregateWeightClassification
from openepd.model.specs.singular.aggregates import AggregateApplication
from openepd.model.validation.quantity import AmountRangeLengthMm

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class AggregatesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Construction Aggregates.

    Includes sand, gravel, crushed stone, etc. for use as bases, ballasts, or as a component in concrete or asphalt.

    Range version.
    """

    _EXT_VERSION = "1.0"

    recycled_content: RangeRatioFloat | None = pydantic.Field(
        default=None, description="Percent of total mass that is recycled aggregate"
    )
    nominal_max_size: AmountRangeLengthMm | None = pydantic.Field(
        default=None,
        description="Nominal maximum aggregate size is defined as one sieve size smaller than the maximum aggregate size. The maximum aggregate size is defined as the smallest sieve size that requires 100% passing.",
    )
    weight_classification: list[AggregateWeightClassification] | None = pydantic.Field(default=None)
    gradation: list[AggregateGradation] | None = pydantic.Field(default=None)
    manufactured: bool | None = pydantic.Field(
        default=None,
        description="Aggregate produced via expansion or sintering at high temperatures of the following materials: clay, shale, slate, perlite, vermiculite, or slag. Typically used to produce lightweight aggregate",
    )
    slag: bool | None = pydantic.Field(
        default=None,
        description="Pelletized, foamed, and granulated blast furnace slag can be used as construction aggregate.",
    )
    application: AggregateApplication | None = None
