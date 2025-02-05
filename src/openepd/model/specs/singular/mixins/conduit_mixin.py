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
__all__ = ["ConduitMixin"]

from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdSpec
from openepd.model.specs.enums import ConduitMaterial
from openepd.model.validation.quantity import LengthMmStr


class ConduitMixin(BaseOpenEpdSpec):
    """
    Properties of a conduit.

    Those properties are the same for communication and electrical conduits.
    """

    nominal_diameter: LengthMmStr | None = pyd.Field(
        default=None,
        description="Nominal Diameter is also known as the mean or average outside diameter.",
        example="100 mm",
    )
    outer_diameter: LengthMmStr | None = pyd.Field(
        default=None,
        description="The measurement of the distance of a straight line between points on the outer walls of the pipe.",
        example="100 mm",
    )
    inner_diameter: LengthMmStr | None = pyd.Field(
        default=None,
        description="The measurement of the distance of a straight line between points on the inner walls of the pipe.",
        example="100 mm",
    )
    wall_thickness: LengthMmStr | None = pyd.Field(
        default=None, description="Conduit wall thickness.", example="100 mm"
    )

    material: ConduitMaterial | None = pyd.Field(default=None, description="Material of the conduit.", example="PVC")
