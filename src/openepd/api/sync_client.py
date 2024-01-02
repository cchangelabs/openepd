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
__all__ = ("OpenEpdApiClientSync",)

from requests.auth import AuthBase

from openepd.api.base_sync_client import SyncHttpClient, TokenAuth
from openepd.api.category.sync_api import CategoryApi
from openepd.api.epd.sync_api import EpdApi
from openepd.api.pcr.sync_api import PcrApi


class OpenEpdApiClientSync:
    """Synchronous API client for OpenEPD."""

    def __init__(self, base_url: str, auth_token: str | None, **kwargs) -> None:
        """
        Construct an API client.

        :param base_url: base URL of the API
        :param auth_token: authentication token
        :param kwargs: additional arguments to pass to the HTTP client. See SyncHttpClient constructor for details.
        """
        super().__init__()
        auth: AuthBase | None = TokenAuth(auth_token) if auth_token is not None else None
        self._http_client = SyncHttpClient(base_url, auth=auth, **kwargs)
        self.__epd_api: EpdApi | None = None
        self.__pcr_api: PcrApi | None = None
        self.__category_api: CategoryApi | None = None

    @property
    def epds(self) -> EpdApi:
        """Get the EPD API."""
        if self.__epd_api is None:
            self.__epd_api = EpdApi(self._http_client)
        return self.__epd_api

    @property
    def pcrs(self) -> PcrApi:
        """Get the PCR API."""
        if self.__pcr_api is None:
            self.__pcr_api = PcrApi(self._http_client)
        return self.__pcr_api

    @property
    def categories(self) -> CategoryApi:
        """Get the Category API."""
        if self.__category_api is None:
            self.__category_api = CategoryApi(self._http_client)
        return self.__category_api
