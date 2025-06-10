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
    "ChairsRangeV1",
    "ClosedStorageFurnitureRangeV1",
    "CountertopsRangeV1",
    "DemountablePartitionTrackRangeV1",
    "DemountablePartitionsRangeV1",
    "FurnishingsRangeV1",
    "MobileStorageFurnitureRangeV1",
    "OpenStorageFurnitureRangeV1",
    "OtherFurnishingsRangeV1",
    "OtherStorageFurnitureRangeV1",
    "RetractableStorageFurnitureRangeV1",
    "StorageFurnitureRangeV1",
    "TablesRangeV1",
    "WallMountedStorageShelvingRangeV1",
    "WorkSurfacesRangeV1",
    "WorkspacesRangeV1",
)

import pydantic

from openepd.model.common import RangeInt, RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CountertopMaterial
from openepd.model.validation.quantity import AmountRangeAreaM2, AmountRangeLengthMm, AmountRangeVolume

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


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

    thickness: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    countertop_material: list[CountertopMaterial] | None = pydantic.Field(default=None, description="")


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


class OpenStorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Open Storage.

    Open Storage furniture which is static and has no moving parts.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ClosedStorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Closed Storage.

    Closed storage furniture making use of doors, sliding and/or hinged parts.

    Range version.
    """

    _EXT_VERSION = "1.0"


class RetractableStorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Retractable Storage.

    Storage Furniture with retractable (drawer) elements.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MobileStorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Mobile Storage.

    Mobile storage furniture having wheels or casters for movement.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WallMountedStorageShelvingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wall Mounted Shelving.

    Storage furniture which requires usage of a vertical structure for attachment and functional support.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherStorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other Storage Furniture.

    Range version.
    """

    _EXT_VERSION = "1.0"


class StorageFurnitureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Storage Furniture.

    Range version.
    """

    _EXT_VERSION = "1.1"

    OpenStorageFurniture: OpenStorageFurnitureRangeV1 | None = None
    ClosedStorageFurniture: ClosedStorageFurnitureRangeV1 | None = None
    RetractableStorageFurniture: RetractableStorageFurnitureRangeV1 | None = None
    MobileStorageFurniture: MobileStorageFurnitureRangeV1 | None = None
    WallMountedStorageShelving: WallMountedStorageShelvingRangeV1 | None = None
    OtherStorageFurniture: OtherStorageFurnitureRangeV1 | None = None


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


class WorkspacesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Workspaces.

    Office furniture and furniture systems for performing office work, such as cubicle systems.
    Typically includes component(s) that may fit in other categories.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FurnishingsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Home and office furnishings.

    Range version.
    """

    _EXT_VERSION = "1.1"

    functional_floor_area_m2: AmountRangeAreaM2 | None = pydantic.Field(
        default=None,
        title="Functional Floor Area",
        description="The floor area that the product occupies.",
    )
    work_surface_area_m2: AmountRangeAreaM2 | None = pydantic.Field(
        default=None,
        title="Work Surface Area",
        description="The usable work surface area that the product provides.",
    )
    functional_storage_volume_m3: AmountRangeVolume | None = pydantic.Field(
        default=None, title="Functional Storage Volume", description=""
    )
    functional_seating_capacity: RangeInt | None = pydantic.Field(
        default=None,
        title="Functional Seating Capacity",
        description="Intended number of individuals the product seats. This value is used in calculating impact per functional unit.",
    )
    installation_waste_factor: RangeRatioFloat | None = pydantic.Field(
        default=None,
        title="Installation Waste Factor",
        description="Typical increase in impacts to account for installation waste.",
    )
    Chairs: ChairsRangeV1 | None = None
    Countertops: CountertopsRangeV1 | None = None
    DemountablePartitions: DemountablePartitionsRangeV1 | None = None
    OtherFurnishings: OtherFurnishingsRangeV1 | None = None
    StorageFurniture: StorageFurnitureRangeV1 | None = None
    Tables: TablesRangeV1 | None = None
    WorkSurfaces: WorkSurfacesRangeV1 | None = None
    Workspaces: WorkspacesRangeV1 | None = None
