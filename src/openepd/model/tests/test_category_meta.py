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
from collections import defaultdict
from unittest import TestCase

from openepd.model.category_meta import collect_category_metadata


class CategoryMetaTestCase(TestCase):
    def test_all_hierarchical_specs_have_category_meta(self) -> None:
        """
        Verify that every instance of BaseOpenEpdHierarchicalSpec has the `_CATEGORY_META` attribute assigned.

        This test ensures that all hierarchical specification classes in the category model are properly annotated
        with required category metadata, which is essential for correct category handling and introspection.
        """
        collect_category_metadata(require_meta=True)

    def test_all_category_names_are_unique(self) -> None:
        """
        Check that all category names are unique across all category metadata entries.

        This test ensures that no name (unique_name, display_name, alt_names, historical_names) is reused in
        multiple categories, which could cause ambiguity or errors in category identification.
        """
        category_metadata = collect_category_metadata()
        name_to_categories: dict[str, dict[str, set[str]]] = defaultdict(dict)
        for entry in category_metadata:
            hierarchical_name = entry["hierarchical_name"]
            # unique_name
            self._add_name_occurrence(entry["unique_name"], hierarchical_name, "unique_name", name_to_categories)
            # display_name
            self._add_name_occurrence(entry["display_name"], hierarchical_name, "display_name", name_to_categories)
            # alt_names
            for alt_name in entry.get("alt_names", []):
                self._add_name_occurrence(alt_name, hierarchical_name, "alt_name", name_to_categories)
            # historical_names
            for historical_name in entry.get("historical_names", []):
                self._add_name_occurrence(historical_name, hierarchical_name, "historical_name", name_to_categories)

        error_message = self._build_duplicate_names_message(name_to_categories)
        if error_message:
            self.fail(msg=error_message)

    def _add_name_occurrence(
        self, name: str, hierarchical_name: str, name_type: str, name_to_categories: dict[str, dict[str, set[str]]]
    ) -> None:
        """
        Add a name occurrence to the tracking dictionary.

        :param name: The name to track (unique_name, display_name, alt_name, or historical_name).
        :param hierarchical_name: The hierarchical name of the category.
        :param name_type: The type of the name (e.g., 'unique_name', 'display_name', etc.).
        :param name_to_categories: The dictionary tracking name occurrences.
        """
        if name not in name_to_categories:
            name_to_categories[name] = {}
        if hierarchical_name not in name_to_categories[name]:
            name_to_categories[name][hierarchical_name] = set()
        name_to_categories[name][hierarchical_name].add(name_type)

    def _format_details(self, categories: dict[str, set[str]]) -> list[str]:
        """
        Format details for duplicate names across categories.

        :param categories: Dictionary mapping hierarchical names to sets of name types.
        :return: List of formatted detail strings.
        """
        details = []
        for hierarchical_name, name_types in categories.items():
            types_str = ", ".join(sorted(name_types))
            details.append(f"{hierarchical_name} (as {types_str})")
        return details

    def _is_allowed_display_unique(self, name_types: set[str]) -> bool:
        """
        Check if only display_name and unique_name are present.

        :param name_types: Set of name types for a given name in a category.
        :return: True if only display_name and unique_name are present, False otherwise.
        """
        return len(name_types) == 2 and "unique_name" in name_types and "display_name" in name_types

    def _build_duplicate_names_message(self, name_to_categories: dict[str, dict[str, set[str]]]) -> str:
        """
        Build an error message listing all names that are not unique across or within categories.

        This method allows a display_name to match the unique_name within the same category without
        being considered a duplicate. All other duplicate scenarios are still reported.

        :param name_to_categories: The dictionary tracking name occurrences.
        :return: An error message string if duplicates are found, otherwise an empty string.
        """
        duplicates: list[str] = []
        for name, categories in name_to_categories.items():
            # Check for duplicates across categories
            if len(categories) > 1:
                details = self._format_details(categories)
                duplicates.append(f"Name '{name}' is used in multiple categories: {', '.join(details)}")
            # Check for duplicates within the same category (multiple name types)
            for hierarchical_name, name_types in categories.items():
                if self._is_allowed_display_unique(name_types):
                    continue
                if len(name_types) > 1:
                    types_str = ", ".join(sorted(name_types))
                    duplicates.append(
                        f"Name '{name}' is used multiple times in category '{hierarchical_name}' (as {types_str})"
                    )
        if duplicates:
            return "Duplicate category names found:\n" + "\n".join(duplicates)
        return ""
