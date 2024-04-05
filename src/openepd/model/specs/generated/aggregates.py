#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import AggregateGradation, AggregateWeightClassification
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr


class AggregatesV1(BaseOpenEpdHierarchicalSpec):
    """Aggregates performance specification."""

    _EXT_VERSION = "1.0"
    """Construction Aggregates, including sand, gravel, crushed stone, etc.
    for use as bases, ballasts, or as a component in concrete or asphalt"""

    # Own fields:
    recycled_aggregate: RatioFloat | None = pyd.Field(
        example="0.3", default=None, description="Percent of total mass that is recycled aggregate"
    )
    aggregate_nominal_max_size: LengthMmStr | None = pyd.Field(
        default=None,
        example="10 mm",
        description="Nominal maximum aggregate size is defined as one sieve size smaller than the maximum "
        "aggregate size. "
        "The maximum aggregate size is defined as the smallest sieve size that requires 100% passing.",
    )
    aggregate_weight_classification: AggregateWeightClassification | None = pyd.Field(
        example=AggregateWeightClassification.HEAVY_WEIGHT, default=None
    )
    aggregate_gradation: AggregateGradation | None = pyd.Field(example=AggregateGradation.GAP, default=None)
    manufactured: bool | None = pyd.Field(
        default=None,
        description="Aggregate produced via expansion or sintering at high temperatures of the following materials: "
        "clay, shale, slate, perlite, vermiculite, or slag. Typically used to produce lightweight aggregate",
    )
    slag: bool | None = pyd.Field(
        default=None,
        description="Pelletized, foamed, and granulated blast furnace slag can be used as construction aggregate.",
    )

    # Aggregates applications
    concrete: bool | None = pyd.Field(default=None, description="Aggregates used in concrete and masonry applications")
    asphalt: bool | None = pyd.Field(
        default=None, description="Aggregates used in bituminous paving and surface applications"
    )
    unbound: bool | None = pyd.Field(default=None)