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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import CountertopMaterial
from openepd.model.validation.quantity import LengthMmStr


class DemountablePartitionTrackV1(BaseOpenEpdHierarchicalSpec):
    """Track for modular partitions."""

    _EXT_VERSION = "1.0"


class ChairsV1(BaseOpenEpdHierarchicalSpec):
    """Chairs."""

    _EXT_VERSION = "1.0"


class CountertopsV1(BaseOpenEpdHierarchicalSpec):
    """Raised, flat, and horizontal surfaces often used in kitchens, bathrooms, and workrooms."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="30 mm")
    countertop_material: CountertopMaterial | None = pyd.Field(default=None, description="", example="Stone")


class DemountablePartitionsV1(BaseOpenEpdHierarchicalSpec):
    """Demountable partitions."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    DemountablePartitionTrack: DemountablePartitionTrackV1 | None = None


class OtherFurnishingsV1(BaseOpenEpdHierarchicalSpec):
    """Other furnishings."""

    _EXT_VERSION = "1.0"


class StorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """Storage Furniture."""

    _EXT_VERSION = "1.0"


class TablesV1(BaseOpenEpdHierarchicalSpec):
    """Tables."""

    _EXT_VERSION = "1.0"


class WorkSurfacesV1(BaseOpenEpdHierarchicalSpec):
    """Work surfaces."""

    _EXT_VERSION = "1.0"


class FurnishingsV1(BaseOpenEpdHierarchicalSpec):
    """Home and office furnishings."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Chairs: ChairsV1 | None = None
    Countertops: CountertopsV1 | None = None
    DemountablePartitions: DemountablePartitionsV1 | None = None
    OtherFurnishings: OtherFurnishingsV1 | None = None
    StorageFurniture: StorageFurnitureV1 | None = None
    Tables: TablesV1 | None = None
    WorkSurfaces: WorkSurfacesV1 | None = None
