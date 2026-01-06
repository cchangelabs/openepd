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
import pydantic

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CountertopMaterial
from openepd.model.validation.quantity import AreaM2Str, LengthMmStr, VolumeStr


class DemountablePartitionTrackV1(BaseOpenEpdHierarchicalSpec):
    """Track for modular partitions."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="DemountablePartitionTrack",
        display_name="Demountable Partition Track",
        short_name="Track",
        historical_names=["Furnishings >> Partitions >> Track"],
        description="Track for modular partitions.",
        masterformat="10 22 00 Partitions",
        declared_unit=Amount(qty=1, unit="m"),
    )


class ChairsV1(BaseOpenEpdHierarchicalSpec):
    """Chairs."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Chairs",
        display_name="Seating",
        historical_names=["Furnishings >> Seating"],
        description="Chairs and other seating",
        masterformat="12 52 00 Seating",
        declared_unit=Amount(qty=1, unit="item"),
    )


class CountertopsV1(BaseOpenEpdHierarchicalSpec):
    """Raised, flat, and horizontal surfaces often used in kitchens, bathrooms, and workrooms."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Countertops",
        display_name="Countertops",
        description="Raised, flat, and horizontal surfaces often used in kitchens, bathrooms, and workrooms",
        masterformat="12 36 00 Countertops",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["30 mm"])
    countertop_material: CountertopMaterial | None = pydantic.Field(default=None, description="", examples=["Stone"])


class DemountablePartitionsV1(BaseOpenEpdHierarchicalSpec):
    """Demountable partitions."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="DemountablePartitions",
        display_name="Demountable Partitions",
        short_name="Partitions",
        historical_names=["Furnishings >> Partitions"],
        description="Demountable, modular, and other partitions are interior wall systems that are not permanently attached to the floor or walls and can easily be moved. They can be free-standing or guided with a top-hung or floor-mounted track.",
        masterformat="10 22 00 Partitions",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Nested specs:
    DemountablePartitionTrack: DemountablePartitionTrackV1 | None = None


class OtherFurnishingsV1(BaseOpenEpdHierarchicalSpec):
    """Other furnishings."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherFurnishings",
        display_name="Other Furnishings",
        short_name="Other",
        historical_names=["Furnishings >> Other"],
        description="Other furnishings",
        masterformat="12 00 00 Furnishings",
        declared_unit=Amount(qty=1, unit="item"),
    )


class OpenStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Open Storage.

    Open Storage furniture which is static and has no moving parts.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OpenStorageFurniture",
        display_name="Open Storage",
        historical_names=["Furnishings >> Storage >> Open Storage"],
        description="Open Storage furniture which is static and has no moving parts",
        masterformat="10 50 00 Storage Specialties",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ClosedStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Closed Storage.

    Closed storage furniture making use of doors, sliding and/or hinged parts.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ClosedStorageFurniture",
        display_name="Closed Storage",
        historical_names=["Furnishings >> Storage >> Closed Storage"],
        description="Closed storage furniture making use of doors, sliding and/or hinged parts.",
        masterformat="10 50 00 Storage Specialties",
        declared_unit=Amount(qty=1, unit="item"),
    )


class RetractableStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Retractable Storage.

    Storage Furniture with retractable (drawer) elements.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="RetractableStorageFurniture",
        display_name="Retractable Storage",
        historical_names=["Furnishings >> Storage >> Retractable Storage"],
        description="Storage Furniture with retractable (drawer) elements",
        masterformat="10 50 00 Storage Specialties",
        declared_unit=Amount(qty=1, unit="item"),
    )


class MobileStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """
    Mobile Storage.

    Mobile storage furniture having wheels or casters for movement.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MobileStorageFurniture",
        display_name="Mobile Storage",
        historical_names=["Furnishings >> Storage >> Mobile Storage"],
        description="Mobile storage furniture having wheels or casters for movement",
        masterformat="10 56 26 Mobile Storage Shelving",
        declared_unit=Amount(qty=1, unit="item"),
    )


class WallMountedStorageShelvingV1(BaseOpenEpdHierarchicalSpec):
    """
    Wall Mounted Shelving.

    Storage furniture which requires usage of a vertical structure for attachment and functional support.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WallMountedStorageShelving",
        display_name="Wall Mounted Shelving",
        short_name="Wall-Mounted Shelving",
        historical_names=["Furnishings >> Storage >> Wall-Mounted Shelving"],
        description="Storage furniture which requires usage of a vertical structure for attachment and functional support",
        masterformat="10 56 17 Wall-Mounted Standards and Shelving",
        declared_unit=Amount(qty=1, unit="item"),
    )


class OtherStorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """Other Storage Furniture."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherStorageFurniture",
        display_name="Other Storage Furniture",
        short_name="Other",
        historical_names=["Furnishings >> Storage >> Other"],
        description="Other Storage Furniture",
        masterformat="10 50 00 Storage Specialties",
        declared_unit=Amount(qty=1, unit="item"),
    )


class StorageFurnitureV1(BaseOpenEpdHierarchicalSpec):
    """Storage Furniture."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="StorageFurniture",
        display_name="Storage Furniture",
        short_name="Storage",
        historical_names=["Furnishings >> Storage"],
        description="Storage Furniture",
        masterformat="10 56 00 Storage Assemblies",
        declared_unit=Amount(qty=1, unit="item"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="Tables",
        display_name="Tables",
        description="Tables which are not primarily work surfaces",
        masterformat="12 64 16 Tables",
        declared_unit=Amount(qty=1, unit="item"),
    )


class WorkSurfacesV1(BaseOpenEpdHierarchicalSpec):
    """Work surfaces."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WorkSurfaces",
        display_name="Work Surfaces",
        historical_names=["Furnishings >> Work Surfaces"],
        description="Work surfaces such as desks, countertops, and work benches.",
        masterformat="12 51 00 Office Furniture",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class WorkspacesV1(BaseOpenEpdHierarchicalSpec):
    """
    Workspaces.

    Office furniture and furniture systems for performing office work, such as cubicle systems.
    Typically includes component(s) that may fit in other categories.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Workspaces",
        display_name="Workspaces",
        description="Office furniture and furniture systems for performing office work, such as cubicle systems. Typically includes component(s) that may fit in other categories.",
        masterformat="12 59 00 Systems Furniture",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class FurnishingsV1(BaseOpenEpdHierarchicalSpec):
    """Home and office furnishings."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="Furnishings",
        display_name="Furnishings",
        description="Home and office furnishings",
        masterformat="12 00 00 Furnishings",
    )

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
