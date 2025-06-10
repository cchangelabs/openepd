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
from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes, RootDocument
from openepd.model.epd import EpdFactory
from openepd.model.generic_estimate import GenericEstimateFactory
from openepd.model.industry_epd import IndustryEpdFactory


class DocumentFactory:
    """A factory for creating documents regardless of the type."""

    DOCTYPE_TO_FACTORY: dict[OpenEpdDoctypes, type[BaseDocumentFactory]] = {
        OpenEpdDoctypes.Epd: EpdFactory,
        OpenEpdDoctypes.GenericEstimate: GenericEstimateFactory,
        OpenEpdDoctypes.IndustryEpd: IndustryEpdFactory,
    }

    @classmethod
    def get_factory(cls, doctype: OpenEpdDoctypes | None) -> type[BaseDocumentFactory]:
        """
        Get a document factory by given doctype.

        :param doctype: doctype
        :return document factory
        :raise ValueError if doctype not supported or not found.
        """
        if doctype is None:
            msg = "The document type is not specified."
            raise ValueError(msg)
        factory = cls.DOCTYPE_TO_FACTORY.get(doctype)
        if factory is None:
            raise ValueError(
                f"The document of type `{doctype}` is not supported. Supported documents are: "
                + ", ".join(cls.DOCTYPE_TO_FACTORY.keys())
            )
        return factory

    @classmethod
    def from_dict(cls, data: dict) -> RootDocument:
        """
        Create a document from the dictionary.

        Type of the document will be recognized from the `doctype` field.
        :raise ValueError: if the document type is not specified or not supported.
        """
        doctype = data.get("doctype")
        if doctype is None or not isinstance(doctype, str | OpenEpdDoctypes):
            msg = (
                f"The document type is not specified or not supported. "
                f"Please specify it in `doctype` field. Supported are: {','.join(cls.DOCTYPE_TO_FACTORY)}"
            )
            raise ValueError(msg)

        factory = cls.get_factory(OpenEpdDoctypes(doctype))
        return factory.from_dict(data)
