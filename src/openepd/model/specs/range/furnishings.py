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
__all__ = (
    "DemountablePartitionTrackRangeV1",
    "ChairsRangeV1",
    "CountertopsRangeV1",
    "DemountablePartitionsRangeV1",
    "OtherFurnishingsRangeV1",
    "StorageFurnitureRangeV1",
    "TablesRangeV1",
    "WorkSurfacesRangeV1",
    "FurnishingsRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CountertopMaterial
from openepd.model.validation.quantity import AmountRangeLengthMm


class DemountablePartitionTrackRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Track for modular partitions.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ChairsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Chairs.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CountertopsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Raised, flat, and horizontal surfaces often used in kitchens, bathrooms, and workrooms.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    countertop_material: list[CountertopMaterial] | None = pyd.Field(default=None, description="")


class DemountablePartitionsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Demountable partitions.

    Range version.
    """

    _EXT_VERSION = "1.0"

    DemountablePartitionTrack: DemountablePartitionTrackRangeV1 | None = None


class OtherFurnishingsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other furnishings.

    Range version.
    """

    _EXT_VERSION = "1.0"


class StorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Storage Furniture.

    Range version.
    """

    _EXT_VERSION = "1.0"


class TablesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Tables.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WorkSurfacesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Work surfaces.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FurnishingsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Home and office furnishings.

    Range version.
    """

    _EXT_VERSION = "1.0"

    Chairs: ChairsRangeV1 | None = None
    Countertops: CountertopsRangeV1 | None = None
    DemountablePartitions: DemountablePartitionsRangeV1 | None = None
    OtherFurnishings: OtherFurnishingsRangeV1 | None = None
    StorageFurniture: StorageFurnitureRangeV1 | None = None
    Tables: TablesRangeV1 | None = None
    WorkSurfaces: WorkSurfacesRangeV1 | None = None
