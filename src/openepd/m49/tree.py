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

__all__ = [
    "GeographyItem",
    "GeographyTree",
    "get_m49_tree",
    "get_openepd_geography_tree",
]
from collections.abc import Callable
import dataclasses
import functools

from . import const as m49_const
from . import utils as m49_utils


@dataclasses.dataclass(slots=True)
class GeographyItem:
    verbose_name: str
    openepd_code: str
    m49_codes: set[str]
    iso_codes: set[str] | None
    level: int
    children: list["GeographyItem"] | None = None
    openepd_special_region: bool = False

    def add_children(self, children: list["GeographyItem"]) -> None:
        if self.children is None:
            self.children = []
        self.children.extend(children)

    @property
    def is_leaf(self) -> bool:
        return not self.children

    def to_dict(self) -> dict:
        return {
            "verbose_name": self.verbose_name,
            "openepd_code": self.openepd_code,
            "m49_codes": list(self.m49_codes),
            "iso_codes": list(self.iso_codes) if self.iso_codes else None,
            "level": self.level,
            "children": [child.to_dict() for child in self.children] if self.children else None,
            "openepd_special_region": self.openepd_special_region,
        }


class GeographyTree:
    def __init__(self, root: GeographyItem):
        self.root = root

    def to_dict(self) -> dict:
        return self.root.to_dict()

    def filter(self, condition: Callable[[GeographyItem], bool]) -> list[GeographyItem]:
        matched_items: list[GeographyItem] = []

        def _traverse(item: GeographyItem):
            if condition(item):
                matched_items.append(item)
            if item.children:
                for child in item.children:
                    _traverse(child)

        _traverse(self.root)
        return matched_items

    def traverse(self, action: Callable[[GeographyItem], None]) -> None:
        def _traverse(item: GeographyItem):
            action(item)
            if item.children:
                for child in item.children:
                    _traverse(child)

        _traverse(self.root)

    def find_all(self, m49_codes: set[str] | None = None, is_leaf: bool | None = None) -> list[GeographyItem]:
        def _filter_fn(item: GeographyItem) -> bool:
            if is_leaf is not None and item.is_leaf != is_leaf:
                return False
            if m49_codes is not None:
                return not m49_codes.isdisjoint(item.m49_codes)
            return True

        return self.filter(_filter_fn)


def _create_geography_item_from_m49(m49_code: str, level: int) -> GeographyItem:
    openepd_code = m49_code
    iso_codes: set[str] | None = None
    try:
        openepd_code = m49_utils.m49_to_openepd({m49_code}).pop()
    except ValueError:
        pass
    try:
        iso_codes = m49_utils.m49_to_iso({m49_code})
    except ValueError:
        pass
    verbose_name = m49_utils.m49_to_region_and_country_names([m49_code]).pop()
    return GeographyItem(
        verbose_name=verbose_name,
        openepd_code=openepd_code,
        m49_codes={m49_code},
        iso_codes=iso_codes,
        level=level,
        children=None,
    )


@functools.cache
def get_m49_tree() -> GeographyTree:
    """Generate the geography tree based on M49 structure."""

    world = _create_geography_item_from_m49(m49_const.M49_CODE_WORLD, level=0)

    # AFRICA
    africa = _create_geography_item_from_m49(m49_const.M49_CODE_AFRICA, level=1)
    # - Northern Africa
    northern_africa = _create_geography_item_from_m49("015", level=2)
    sub_saharan_africa = _create_geography_item_from_m49("202", level=2)
    africa.add_children([northern_africa, sub_saharan_africa])
    for x in m49_const.NORTHERN_AFRICA:
        northern_africa.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    # - Sub-Saharan Africa
    western_africa = _create_geography_item_from_m49("011", level=3)
    eastern_africa = _create_geography_item_from_m49("014", level=3)
    middle_africa = _create_geography_item_from_m49("017", level=3)
    southern_africa = _create_geography_item_from_m49("018", level=3)
    sub_saharan_africa.add_children([western_africa, eastern_africa, middle_africa, southern_africa])
    for x in m49_const.WESTERN_AFRICA:
        western_africa.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=4)])
    for x in m49_const.EASTERN_AFRICA:
        eastern_africa.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=4)])
    for x in m49_const.MIDDLE_AFRICA:
        middle_africa.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=4)])
    for x in m49_const.SOUTHERN_AFRICA:
        southern_africa.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=4)])

    # NORTH AMERICA
    north_america = _create_geography_item_from_m49(m49_const.M49_CODE_NORTH_AMERICA, level=1)
    caribbean = _create_geography_item_from_m49("029", level=2)
    central_america = _create_geography_item_from_m49("013", level=2)
    northern_america = _create_geography_item_from_m49("021", level=2)
    north_america.add_children([caribbean, central_america, northern_america])
    for x in m49_const.CARIBBEAN:
        caribbean.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.CENTRAL_AMERICA:
        central_america.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.NORTHERN_AMERICA:
        northern_america.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])

    # SOUTH AMERICA
    south_america = _create_geography_item_from_m49(m49_const.M49_CODE_SOUTH_AMERICA, level=1)
    for x in m49_const.SOUTH_AMERICA:
        south_america.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=2)])

    # OCEANIA
    oceania = _create_geography_item_from_m49(m49_const.M49_CODE_OCEANIA, level=1)
    australia_and_new_zealand = _create_geography_item_from_m49("053", level=2)
    melanesia = _create_geography_item_from_m49("054", level=2)
    micronesia = _create_geography_item_from_m49("057", level=2)
    polynesia = _create_geography_item_from_m49("061", level=2)
    oceania.add_children([australia_and_new_zealand, melanesia, micronesia, polynesia])
    for x in m49_const.AUSTRALIA_AND_NEW_ZEALAND:
        australia_and_new_zealand.add_children(
            [_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)]
        )
    for x in m49_const.MELANESIA:
        melanesia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.MICRONESIA:
        micronesia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.POLYNESIA:
        polynesia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])

    # CENTRAL AMERICA
    for x in m49_const.CENTRAL_AMERICA:
        central_america.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=2)])

    # M49_CODE_ASIA
    asia = _create_geography_item_from_m49(m49_const.M49_CODE_ASIA, level=1)
    central_asia = _create_geography_item_from_m49("143", level=2)
    eastern_asia = _create_geography_item_from_m49("030", level=2)
    southern_asia = _create_geography_item_from_m49("034", level=2)
    south_eastern_asia = _create_geography_item_from_m49("035", level=2)
    western_asia = _create_geography_item_from_m49("145", level=2)
    asia.add_children([central_asia, eastern_asia, southern_asia, south_eastern_asia, western_asia])
    for x in m49_const.CENTRAL_ASIA:
        central_asia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.EASTERN_ASIA:
        eastern_asia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.SOUTHERN_ASIA:
        southern_asia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.SOUTH_EASTERN_ASIA:
        south_eastern_asia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.WESTERN_ASIA:
        western_asia.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])

    # EUROPE
    europe = _create_geography_item_from_m49(m49_const.M49_CODE_EUROPE, level=1)
    eastern_europe = _create_geography_item_from_m49("151", level=2)
    northern_europe = _create_geography_item_from_m49("154", level=2)
    southern_europe = _create_geography_item_from_m49("039", level=2)
    western_europe = _create_geography_item_from_m49("155", level=2)
    europe.add_children([eastern_europe, northern_europe, southern_europe, western_europe])
    for x in m49_const.EASTERN_EUROPE:
        eastern_europe.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.NORTHERN_EUROPE:
        northern_europe.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.SOUTHERN_EUROPE:
        southern_europe.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])
    for x in m49_const.WESTERN_EUROPE:
        western_europe.add_children([_create_geography_item_from_m49(m49_utils.iso_to_m49({x}).pop(), level=3)])

    world.add_children([north_america, europe, south_america, asia, oceania, africa])
    return GeographyTree(world)


@functools.cache
def get_openepd_geography_tree() -> GeographyTree:
    """Generate the M49 geography tree with OpenEPD special regions added."""

    m49_tree = get_m49_tree()
    special_regions: list[GeographyItem] = []
    special_regions.append(
        GeographyItem(
            verbose_name="NAFTA",
            openepd_code="NAFTA",
            m49_codes=set(m49_const.OPENEPD_SPECIAL_REGIONS["NAFTA"].m49_codes),
            iso_codes={m49_utils.m49_to_iso({x}).pop() for x in m49_const.OPENEPD_SPECIAL_REGIONS["NAFTA"].m49_codes},
            level=1,
            children=m49_tree.find_all(m49_codes=set(m49_const.OPENEPD_SPECIAL_REGIONS["NAFTA"].m49_codes)),
            openepd_special_region=True,
        )
    )
    special_regions.append(
        GeographyItem(
            verbose_name="EU27",
            openepd_code="EU27",
            m49_codes=set(m49_const.OPENEPD_SPECIAL_REGIONS["EU27"].m49_codes),
            iso_codes={m49_utils.m49_to_iso({x}).pop() for x in m49_const.OPENEPD_SPECIAL_REGIONS["EU27"].m49_codes},
            level=1,
            children=m49_tree.find_all(m49_codes=set(m49_const.OPENEPD_SPECIAL_REGIONS["EU27"].m49_codes)),
            openepd_special_region=True,
        )
    )
    assert len(special_regions) == len(m49_const.OPENEPD_SPECIAL_REGIONS), (
        "Some special regions were not created, forgot to update m49.tree.get_openepd_geography_tree()?"
    )
    m49_tree.root.add_children(special_regions)
    return GeographyTree(m49_tree.root)
