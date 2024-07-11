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
import csv

# Tool to generate geography enums for openEPD.
# We would like to materialize enums so that a. they can be picked up by the openapi tooling b. no need to manually
# support the country lists.
import os

import jinja2
import pycountry

special_regions = {
    "EU27": "27 members of the Euro bloc",
    "NAFTA": "North American Free Trade Agreement",
}


def filter__to_python_name(n: str) -> str:
    """Jinja filter to clean up the names."""
    return n.replace("-", "_")


def __get_m49_codes() -> dict[str, str]:
    """Read attached CSV and return m49code:name for regions, subregions, world, and countries"""
    result = {}
    regions = {"001": "Global"}
    with open(os.path.join(os.path.dirname(__file__), "UNSD — Methodology.csv"), "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            result[row["M49 Code"]] = row["Country or Area"]
            if row["Region Code"]:
                regions[row["Region Code"]] = row["Region Name"]
            if row["Sub-region Code"]:
                regions[row["Sub-region Code"]] = row["Sub-region Name"]

    return {**regions, **result}


def generate_enums() -> None:
    """
    Generate geography-related enums.

    Data sources:
    1. Pycountry library (which mirrors debian's country list package) - for ISO 2-character names, and subdivisions
       of the USA and Canada
    2. Manual list of zones of interest - global organisations such as EU and NAFTA.
    3. M49 codification by UN, countries are broken down into regions (such as Northern Africa). List can be downloaded
       at https://unstats.un.org/unsd/methodology/m49/overview/.
    """
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
    environment.filters["to_python_name"] = filter__to_python_name
    template = environment.get_template("geography_enum.py.tpl")

    us_canada_subdivisions = {
        c.code: f"{c.name}, {c.country.name}"
        for c in sorted(
            [*pycountry.subdivisions.lookup("US"), *pycountry.subdivisions.lookup("CA")], key=lambda c: c.code
        )
    }
    print(
        template.render(
            countries={c.alpha_2: c.name for c in sorted(pycountry.countries, key=lambda c: c.alpha_2)},
            us_canada_subdivisions=us_canada_subdivisions,
            special_regions=special_regions,
            m49_codes=__get_m49_codes(),
        )
    )


if __name__ == "__main__":
    generate_enums()
