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
import dataclasses
from typing import Self


class MarkdownSectionBuilder:
    """
    A builder for Markdown sections.

    Allows to build a Markdown string from a list of sections (title + content).
    """

    @dataclasses.dataclass(kw_only=True)
    class _MdSection:
        title: str
        level: int = 1
        content: str | None = None

    def __init__(self) -> None:
        self._sections: list[MarkdownSectionBuilder._MdSection] = []

    def add_section(self, title: str, content: str | None = None, level: int = 1) -> Self:
        """Add a new section to the builder."""
        self._sections.append(MarkdownSectionBuilder._MdSection(title=title, content=content, level=level))
        return self

    @property
    def has_content(self) -> bool:
        """Return True if there are any sections added to the builder."""
        return len(self._sections) > 0

    @staticmethod
    def _build_section(section: _MdSection) -> str:
        return f"{'#' * section.level} {section.title}\n\n{section.content or ''}"

    def build(self) -> str:
        """Build the Markdown string."""
        return "\n\n".join([self._build_section(x) for x in self._sections if x.content is not None])
