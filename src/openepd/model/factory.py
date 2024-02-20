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
from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes, RootDocument
from openepd.model.epd import EpdFactory


class DocumentFactory:
    """A factory for creating documents regardless of the type."""

    DOCTYPE_TO_FACTORY: dict[str, type[BaseDocumentFactory]] = {
        OpenEpdDoctypes.Epd: EpdFactory,
    }

    @classmethod
    def from_dict(cls, data: dict) -> RootDocument:
        """
        Create a document from the dictionary.

        Type of the document will be recognized from the `doctype` field.
        :raise ValueError: if the document type is not specified or not supported.
        """
        doctype = data.get("doctype")
        if doctype is None:
            raise ValueError("The document type is not specified.")
        factory = cls.DOCTYPE_TO_FACTORY.get(doctype)
        if factory is None:
            raise ValueError(
                f"The document of type `{doctype}` is not supported. Supported documents are: "
                + ", ".join(cls.DOCTYPE_TO_FACTORY.keys())
            )
        return factory.from_dict(data)
