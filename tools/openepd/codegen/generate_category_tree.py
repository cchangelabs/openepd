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
import os

import jinja2

from openepd.model.category_meta import collect_category_metadata
from openepd.model.specs.singular import Specs


def render_category_tree_template() -> str:
    """
    Render the category tree metadata using the Jinja2 template.

    This function collects metadata for all categories in the OpenEPD hierarchy, then renders it using the
    'category_generated.py.tpl' Jinja2 template found in the same directory as this script. The rendered output
    is returned as a formatted string.

    :return: Rendered string containing the category tree metadata.
    """
    category_metadata = collect_category_metadata()
    template_dir = os.path.dirname(__file__)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))  # noqa: S701
    template = jinja_env.get_template("category_generated.py.tpl")
    return template.render(categories=category_metadata)


def main() -> None:
    """Generate and print the category tree metadata."""
    print(render_category_tree_template())


if __name__ == "__main__":
    main()
