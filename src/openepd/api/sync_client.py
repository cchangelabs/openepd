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
__all__ = ("OpenEpdApiClientSync",)

from requests.auth import AuthBase

from openepd.api.average_dataset.generic_estimate_sync_api import GenericEstimateApi
from openepd.api.average_dataset.industry_epd_sync_api import IndustryEpdApi
from openepd.api.base_sync_client import SyncHttpClient, TokenAuth
from openepd.api.category.sync_api import CategoryApi
from openepd.api.epd.sync_api import EpdApi
from openepd.api.org.sync_api import OrgApi
from openepd.api.pcr.sync_api import PcrApi
from openepd.api.plant.sync_api import PlantApi
from openepd.api.standard.sync_api import StandardApi


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
        self.__org_api: OrgApi | None = None
        self.__plant_api: PlantApi | None = None
        self.__standard_api: StandardApi | None = None
        self.__category_api: CategoryApi | None = None
        self.__generic_estimate_api: GenericEstimateApi | None = None
        self.__industry_epd_api: IndustryEpdApi | None = None

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
    def orgs(self) -> OrgApi:
        """Get the Org API."""
        if self.__org_api is None:
            self.__org_api = OrgApi(self._http_client)
        return self.__org_api

    @property
    def plants(self) -> PlantApi:
        """Get the Plant API."""
        if self.__plant_api is None:
            self.__plant_api = PlantApi(self._http_client)
        return self.__plant_api

    @property
    def standards(self) -> StandardApi:
        """Get the Standard API."""
        if self.__standard_api is None:
            self.__standard_api = StandardApi(self._http_client)
        return self.__standard_api

    @property
    def categories(self) -> CategoryApi:
        """Get the Category API."""
        if self.__category_api is None:
            self.__category_api = CategoryApi(self._http_client)
        return self.__category_api

    @property
    def industry_epds(self) -> IndustryEpdApi:
        """Get the Category API."""
        if self.__industry_epd_api is None:
            self.__industry_epd_api = IndustryEpdApi(self._http_client)
        return self.__industry_epd_api

    @property
    def generic_estimates(self) -> GenericEstimateApi:
        """Get the GE API."""
        if self.__generic_estimate_api is None:
            self.__generic_estimate_api = GenericEstimateApi(self._http_client)
        return self.__generic_estimate_api
