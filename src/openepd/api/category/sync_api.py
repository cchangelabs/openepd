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
from openepd.api.base_sync_client import BaseApiMethodGroup
from openepd.api.category.dto import CategoryTreeResponse
from openepd.model.category import Category


class CategoryApi(BaseApiMethodGroup):
    """API methods for reading categories."""

    def get_tree_raw(self) -> CategoryTreeResponse:
        """
        Get categories tree.

        :return: categories tree wrapped in OpenEpdApiResponse
        """
        response = self._client.do_request("get", "/v2/categories/tree")
        return CategoryTreeResponse.parse_raw(response.content)

    def get_tree(self) -> Category:
        """
        Get categories tree.

        :return: categories tree
        """
        response = self.get_tree_raw()
        return response.payload
