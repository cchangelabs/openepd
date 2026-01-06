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

    @staticmethod
    def _extract_names(entry: dict, key: str) -> tuple[list[str], str]:
        """
        Extract names and their type from a category metadata entry for a given key.

        :param entry: Category metadata dictionary.
        :param key: The key to extract (e.g., 'unique_name', 'historical_names', etc.).
        :return: Tuple of (list of names, name type string).
        """
        if key == "historical_names":
            return entry.get("historical_names", []), "historical_name"
        value = entry.get(key)
        return ([value] if value else []), key

    def _find_duplicate_names(self, category_metadata: list[dict], name_keys: list[str]) -> list[str]:
        """
        Find duplicate names among the specified keys in category metadata.

        :param category_metadata: List of category metadata dicts.
        :param name_keys: List of keys to check for uniqueness
            (e.g., ["unique_name", "hierarchical_name", "historical_names"]).
        :return: List of duplicate name error messages.
        """
        name_to_categories: dict[str, set[str]] = defaultdict(set)
        name_type_map: dict[str, set[str]] = defaultdict(set)
        for entry in category_metadata:
            hierarchical_name = entry["hierarchical_name"]
            for key in name_keys:
                names, ntype = self._extract_names(entry, key)
                for name in names:
                    name_to_categories[name].add(hierarchical_name)
                    name_type_map[name].add(ntype)
        duplicates = []
        for name, categories in name_to_categories.items():
            if len(categories) > 1:
                details = ", ".join(sorted(categories))
                types = ", ".join(sorted(name_type_map[name]))
                duplicates.append(f"Name '{name}' (type(s): {types}) is used in multiple categories: {details}")
        return duplicates

    def test_unique_and_historical_names_are_unique(self) -> None:
        """
        Check that all unique_name and historical_names are unique across all category metadata entries.

        This test ensures that no unique_name or historical_name is reused in multiple categories, which could cause
        ambiguity or errors in category identification. display_name and alt_names are allowed to be duplicated.
        The error message specifies which type(s) of name were duplicated for each duplicate found.
        """
        category_metadata = collect_category_metadata()
        duplicates = self._find_duplicate_names(category_metadata, ["unique_name", "historical_names"])
        if duplicates:
            error_message = "Duplicate unique_name or historical_name found:\n" + "\n".join(duplicates)
            self.fail(msg=error_message)

    def test_unique_hierarchical_and_historical_names_are_unique(self) -> None:
        """
        Ensure unique_name, hierarchical_name, and historical_names are unique across all category metadata.

        This test ensures that no unique_name, hierarchical_name, or historical_name is reused in multiple categories,
        which could cause ambiguity or errors in category identification.
        display_name and alt_names are allowed to be duplicated.
        """
        category_metadata = collect_category_metadata()
        duplicates = self._find_duplicate_names(
            category_metadata, ["unique_name", "hierarchical_name", "historical_names"]
        )
        if duplicates:
            error_message = "Duplicate unique_name, hierarchical_name, or historical_name found:\n" + "\n".join(
                duplicates
            )
            self.fail(msg=error_message)

    def _check_duplicate_names(self, children: list[dict], key: str, parent: str | None) -> list[str]:
        """
        Check for duplicate values of a given key among children of a parent.

        :param children: List of child category metadata dicts.
        :param key: The key to check for uniqueness (e.g., 'display_name', 'short_name').
        :param parent: The parent category unique name or None.
        :return: List of error messages for duplicates found.
        """
        seen: dict[str, str] = {}
        errors: list[str] = []
        for child in children:
            child_name = child.get("unique_name", "<unknown>")
            value = child.get(key)
            if value:
                if value in seen:
                    errors.append(f"Duplicate {key} '{value}' under parent '{parent}': {seen[value]}, {child_name}")
                else:
                    seen[value] = child_name
        return errors

    def _check_duplicate_alt_names(self, children: list[dict], parent: str | None) -> list[str]:
        """
        Check for duplicate alt_names among children of a parent.

        :param children: List of child category metadata dicts.
        :param parent: The parent category unique name or None.
        :return: List of error messages for duplicates found.
        """
        seen: dict[str, str] = {}
        errors: list[str] = []
        for child in children:
            child_name = child.get("unique_name", "<unknown>")
            alt_names = child.get("alt_names", [])
            for alt_name in alt_names:
                if alt_name in seen:
                    errors.append(
                        f"Duplicate alt_name '{alt_name}' under parent '{parent}': {seen[alt_name]}, {child_name}"
                    )
                else:
                    seen[alt_name] = child_name
        return errors

    def test_display_alt_short_names_unique_within_parent(self) -> None:
        """
        Ensure that display_name, alt_names, and short_name are unique among siblings within each parent category.

        This test checks that for each parent category, no two direct children share the same display_name,
        any alt_name, or short_name. This prevents ambiguity in category identification within the same parent.
        """
        category_metadata = collect_category_metadata()
        parent_to_children: dict[str | None, list[dict]] = defaultdict(list)
        for entry in category_metadata:
            parent_to_children[entry.get("parent")].append(entry)

        errors: list[str] = []
        for parent, children in parent_to_children.items():
            errors.extend(self._check_duplicate_names(children, "display_name", parent))
            errors.extend(self._check_duplicate_names(children, "short_name", parent))
            errors.extend(self._check_duplicate_alt_names(children, parent))
        if errors:
            error_message = (
                "Duplicate display_name, alt_name, or short_name found within the same parent category:\n"
                + "\n".join(errors)
            )
            self.fail(msg=error_message)
