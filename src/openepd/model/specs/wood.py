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
from enum import StrEnum

import pydantic as pyd

from openepd.model.org import OrgRef
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.numbers import RatioFloat


class TimberSpecies(StrEnum):
    """Timber species enum."""

    Alaska_Cedar = "Alaska Cedar"
    Douglas_Fir_Larch = "Douglas Fir-Larch"
    Eastern_Spruce = ("Eastern Spruce",)
    Hem_Fir = "Hem-Fir"
    Softwood_Species = "Softwood Species"
    Southern_Pine = ("Southern Pine",)
    Spruce_Pine_Fir = "Spruce-Pine-Fir"
    Group_A_Hardwoods = ("Group A Hardwoods",)
    Group_B_Hardwoods = "Group B Hardwoods"
    Group_C_Hardwoods = ("Group C Hardwoods",)
    Group_D_Hardwoods = "Group D Hardwoods"
    Alaska_Hemlock = "Alaska Hemlock"
    Alaska_Spruce = ("Alaska Spruce",)
    Alaska_Yellow_Cedar = "Alaska Yellow Cedar"
    Aspen = "Aspen"
    Baldcypress = ("Baldcypress",)
    Balsam_Fir = "Balsam Fir"
    Beech_Birch_Hickory = ("Beech-Birch-Hickory",)
    Coast_Sitka_Spruce = "Coast Sitka Spruce"
    Coast_Species = "Coast Species"
    Cottonwood = ("Cottonwood",)
    Douglas_Fir_Larch_North = "Douglas Fir-Larch (North)"
    Douglas_Fir_South = ("Douglas Fir-South",)
    Eastern_Hemlock = "Eastern Hemlock"
    Eastern_Hemlock_Balsam_Fir = ("Eastern Hemlock-Balsam Fir",)
    Eastern_Hemlock_Tamarack = ("Eastern Hemlock-Tamarack",)
    Eastern_Hemlock_Tamarack_North = "Eastern Hemlock-Tamarack (North)"
    Eastern_Softwoods = ("Eastern Softwoods",)
    Eastern_White_Pine = "Eastern White Pine"
    Eastern_White_Pine_North = ("Eastern White Pine (North)",)
    Hem_Fir_North = "Hem-Fir (North)"
    Mixed_Maple = "Mixed Maple"
    Mixed_Oak = ("Mixed Oak",)
    Mixed_Southern_Pine = "Mixed Southern Pine"
    Mountain_Hemlock = ("Mountain Hemlock",)
    Northern_Pine = "Northern Pine"
    Northern_Red_Oak = "Northern Red Oak"
    Northern_Species = ("Northern Species",)
    Northern_White_Cedar = "Northern White Cedar"
    Ponderosa_Pine = "Ponderosa Pine"
    Red_Maple = ("Red Maple",)
    Red_Oak = "Red Oak"
    Red_Pine = "Red Pine"
    Redwood = "Redwood"
    Sitka_Spruce = ("Sitka Spruce",)
    Scots_Pine = "Scots Pine"
    Spruce_Pine_Fir_South = ("Spruce-Pine-Fir (South)",)
    Western_Cedars = "Western Cedars"
    Western_Cedars_North = ("Western Cedars (North)",)
    Western_Hemlock = "Western Hemlock"
    Western_Hemlock_North = ("Western Hemlock (North)",)
    Western_White_Pine = "Western White Pine"
    Western_Woods = "Western Woods"
    White_Oak = ("White Oak",)
    Yellow_Cedar = "Yellow Cedar"
    Yellow_Poplar = "Yellow Poplar"


class TimberFabrication(StrEnum):
    """Timber fabrication enum."""

    Bonded_Strand = "Bonded Strand"
    CLT = "CLT"
    DLT = "DLT"
    Fiberboard = "Fiberboard"
    GLT = "GLT"
    LVL = "LVL"
    NLT = "NLT"
    OSB = "OSB"
    Plywood = "Plywood"


class TimberV1(BaseOpenEpdHierarchicalSpec):
    """Timber specific specs."""

    _EXT_VERSION = "1.0"

    # tood restore this if needed? No data in DB.
    # timber_strength_grade: str | None = pyd.Field(default=None, description="Timber strength grade")

    # Forest Stewardship Council certified proportion.  Range is 0 to 1; express as a percentage.
    fsc_certified: RatioFloat | None = pyd.Field(
        default=None, description="Forest Stewardship Council certified proportion"
    )
    recycled_content: RatioFloat | None = pyd.Field(default=None, description="Recycled content")

    weather_exposed: bool | None = pyd.Field(default=False, description="Weather exposed")
    fire_retardant: bool | None = pyd.Field(default=None, description="Fire retardant")
    decay_resistant: bool | None = pyd.Field(default=None, description="Decay resistant")

    timber_species: TimberSpecies | None = pyd.Field(default=None, description="Timber species")
    fabrication: TimberFabrication | None = pyd.Field(default=None, description="Timber fabrication")

    forest_practices_certifiers: list[OrgRef] | None = pyd.Field(
        default=None, description="List of organizations that certify forest practices."
    )
    # Todo forest practices certifiers
    # rel_forest_practices_certifiers: neomodel.ZeroOrMore = ogm.RelationshipFrom(
    #     Org, RelType.FOREST_PRACTICES_CERTIFIED, model=ogm.CertifiesRel
    # )
