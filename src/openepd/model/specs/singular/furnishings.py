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
import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CountertopMaterial
from openepd.model.validation.quantity import AreaM2Str, LengthMmStr, VolumeStr


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
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["30 mm"])
    countertop_material: CountertopMaterial | None = pydantic.Field(default=None, description="", examples=["Stone"])


class DemountablePartitionsV1(BaseOpenEpdHierarchicalSpec):
    """Demountable partitions."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    DemountablePartitionTrack: DemountablePartitionTrackV1 | None = None


class OtherFurnishingsV1(BaseOpenEpdHierarchicalSpec):
    """Other furnishings."""

    _EXT_VERSION = "1.0"


class OpenStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Open Storage.

    Open Storage furniture which is static and has no moving parts.
    """

    _EXT_VERSION = "1.0"


class ClosedStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Closed Storage.

    Closed storage furniture making use of doors, sliding and/or hinged parts.
    """

    _EXT_VERSION = "1.0"


class RetractableStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Retractable Storage.

    Storage Furniture with retractable (drawer) elements.
    """

    _EXT_VERSION = "1.0"


class MobileStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Mobile Storage.

    Mobile storage furniture having wheels or casters for movement.
    """

    _EXT_VERSION = "1.0"


class WallMountedStorageShelvingV1(BaseOpenEpdHierarchicalSpec):
    """
    Wall Mounted Shelving.

    Storage furniture which requires usage of a vertical structure for attachment and functional support.
    """

    _EXT_VERSION = "1.0"


class OtherStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """Other Storage Furniture."""

    _EXT_VERSION = "1.0"


class StorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """Storage Furniture."""

    _EXT_VERSION = "1.1"

    # Nested specs:
    OpenStorageFurniture: OpenStorageFurnitureV1 | None = None
    ClosedStorageFurniture: ClosedStorageFurnitureV1 | None = None
    RetractableStorageFurniture: RetractableStorageFurnitureV1 | None = None
    MobileStorageFurniture: MobileStorageFurnitureV1 | None = None
    WallMountedStorageShelving: WallMountedStorageShelvingV1 | None = None
    OtherStorageFurniture: OtherStorageFurnitureV1 | None = None


class TablesV1(BaseOpenEpdHierarchicalSpec):
    """Tables."""

    _EXT_VERSION = "1.0"


class WorkSurfacesV1(BaseOpenEpdHierarchicalSpec):
    """Work surfaces."""

    _EXT_VERSION = "1.0"


class WorkspacesV1(BaseOpenEpdHierarchicalSpec):
    """
    Workspaces.

    Office furniture and furniture systems for performing office work, such as cubicle systems.
    Typically includes component(s) that may fit in other categories.
    """

    _EXT_VERSION = "1.0"


class FurnishingsV1(BaseOpenEpdHierarchicalSpec):
    """Home and office furnishings."""

    _EXT_VERSION = "1.1"

    # Own fields:
    functional_floor_area_m2: AreaM2Str | None = pydantic.Field(
        default=None,
        title="Functional Floor Area",
        description="The floor area that the product occupies.",
        examples=["1 m2"],
    )
    work_surface_area_m2: AreaM2Str | None = pydantic.Field(
        default=None,
        title="Work Surface Area",
        description="The usable work surface area that the product provides.",
        examples=["1 m2"],
    )
    functional_storage_volume_m3: VolumeStr | None = pydantic.Field(
        default=None,
        title="Functional Storage Volume",
        description="",
        examples=["1 m3"],
    )
    functional_seating_capacity: pydantic.NonNegativeInt | None = pydantic.Field(
        default=None,
        title="Functional Seating Capacity",
        description="Intended number of individuals the product seats. This value is used in calculating impact per functional unit.",
        examples=[1],
    )
    installation_waste_factor: float | None = pydantic.Field(
        default=None,
        title="Installation Waste Factor",
        description="Typical increase in impacts to account for installation waste.",
        examples=[0.01],
        ge=0,
        le=1,
    )

    # Nested specs:
    Chairs: ChairsV1 | None = None
    Countertops: CountertopsV1 | None = None
    DemountablePartitions: DemountablePartitionsV1 | None = None
    OtherFurnishings: OtherFurnishingsV1 | None = None
    StorageFurniture: StorageFurnitureV1 | None = None
    Tables: TablesV1 | None = None
    WorkSurfaces: WorkSurfacesV1 | None = None
    Workspaces: WorkspacesV1 | None = None
