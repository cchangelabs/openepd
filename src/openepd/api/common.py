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
from collections.abc import Iterable
from contextlib import contextmanager
from datetime import datetime, timedelta
import threading
from time import sleep
from typing import Callable, Generic, Iterator, cast

from openepd.api.dto.common import DEFAULT_PAGE_SIZE, MetaCollectionDto, OpenEpdApiResponse
from openepd.api.dto.meta import PagingMeta, PagingMetaMixin
from openepd.model.base import TOpenEpdObject


class Throttler:
    """Throttle calls to a function to a certain rate."""

    def __init__(self, rate_per_sec: float) -> None:
        """
        Construct a throttler.

        :param rate_per_sec: number of calls to throttle per second
        """
        super().__init__()

        self.rate: float = rate_per_sec

        self.__count_lock = threading.Lock()
        self.__time_lock = threading.Lock()

        self.__count = 0
        self.__start = datetime.now()
        self.__time_limit = timedelta(seconds=1)

    @contextmanager
    def throttle(self):
        """Create context manager which throttles inside the context."""
        with self.__count_lock:
            count = self.__count

        with self.__time_lock:
            diff = datetime.now() - self.__start
            if diff < self.__time_limit and count >= self.rate:
                seconds = (self.__time_limit - diff).total_seconds()
                sleep(seconds)
                self.__start = datetime.now()
                self.__count = count - self.rate

        with self.__count_lock:
            self.__count += 1

        yield


class StreamingListResponse(Iterable[TOpenEpdObject], Generic[TOpenEpdObject]):
    """
    Iterator over a list of objects which could be from remote API in batches by given fetch function.

    This class could work only with OpenEpdApiResponse which:
    a) contains a list of objects in payload
    b) contains PagingMeta in meta

    Typical use case:

        stream: StreamingListResponse[Epd] # Assume we collected this from somewhere (e.g. from API Client)

        # Iterate over all EPDs (this will fetch the next page when needed, one single page is buffered)
        for epd in stream:
            print(epd)
            print("Current page: ", stream.current_page)

        # Get specific page
        page = stream.goto_page(4)

        # Get paging information
        stream.get_paging_meta()
        # or
        stream.get_get_total_pages(), stream.get_total_items()

        # Iterate starting from specific page
        for epd in stream.iterator(4):
            print(epd)
        # Alternative approach
        stream.goto_page(4)
        for epd in stream:
            print(epd)
    """

    def __init__(
        self,
        fetch_handler: Callable[[int, int], OpenEpdApiResponse[list[TOpenEpdObject], MetaCollectionDto]],
        auto_init: bool = True,
        page_size: int | None = None,
    ):
        self.__fetch_handler = fetch_handler
        self.__page_size = page_size or DEFAULT_PAGE_SIZE
        self.__current_page = 0
        self.__recent_response: OpenEpdApiResponse[list[TOpenEpdObject], MetaCollectionDto] | None = None
        if auto_init:
            self.goto_page(1)

    def goto_page(self, page_num: int, force_reload: bool = False) -> list[TOpenEpdObject]:
        """
        Go to the given page and return items as result.

        This will query remote server to retrieve given page, the state of iterator will be updated accordingly.
        All information from the internal buffer will be overridden.

        :param page_num: page number to retrieve
        :param force_reload: if True, force reload of the page even if it was already loaded
        :return: list of items on the page
        """
        if page_num <= 0:
            raise ValueError("Page number must be positive")
        if self.__current_page != page_num or force_reload:
            self.__recent_response = self.__fetch_handler(page_num, self.__page_size)
            self.__current_page = page_num
        if self.__recent_response is None:
            raise RuntimeError("Response is empty, this should not happen, check if fetch_handler is compatible")
        if self.__recent_response.payload is None:
            raise ValueError("Response does not contain payload")
        if not isinstance(self.__recent_response.payload, list):
            raise ValueError("Response does not contain a list")
        if self.__recent_response.meta is None:
            raise ValueError("Response does not contain meta")
        if not isinstance(self.__recent_response.meta, PagingMetaMixin):
            raise ValueError("Response does not contain paging meta")
        return self.__recent_response.payload

    def get_paging_meta(self) -> PagingMeta:
        """
        Get paging meta from the most recent response.

        If object is not initialized (no pages were retrieved yet), the first page will be fetched automatically.
        See also: get_meta()
        :return: paging meta
        """
        paging_meta = cast(PagingMetaMixin, self.get_meta()).paging
        if paging_meta is None:
            raise ValueError("Response does not contain paging meta")
        return paging_meta

    def get_meta(self) -> MetaCollectionDto:
        """
        Get meta from the most recent response.

        If object is not initialized (no pages were retrieved yet), the first page will be fetched automatically.
        :return: paging meta
        """
        self._ensure_initialized()
        return self.__recent_response.meta  # type: ignore

    @property
    def current_page(self) -> int:
        """Get current page number (numbering is 1-based)."""
        return self.__current_page

    def get_total_pages(self) -> int:
        """Get total number of pages."""
        return self.get_paging_meta().total_pages

    def get_total_count(self) -> int:
        """Get total number of items."""
        return self.get_paging_meta().total_count

    def has_next_page(self) -> bool:
        """Check if there is a next page."""
        return self.current_page < self.get_total_pages()

    def reset(self):
        """Reset iterator to the very beginning, cleanup internal buffers."""
        self.__current_page = 0
        self.__recent_response = None

    def __iter__(self) -> Iterator[TOpenEpdObject]:
        """
        Iterate over all items, when needed the new pages from server will be requested.

        Iteration from starts from the current page.
        """
        return self.iterator(self.current_page)

    def iterator(self, start_from_page: int = 1) -> Iterator[TOpenEpdObject]:
        """
        Iterate over all items, when needed the new pages from server will be requested.

        :param start_from_page: page number to start from (1-based)
        """
        if start_from_page <= 0:
            start_from_page = 1
        self.goto_page(start_from_page)
        while True:
            items = self.goto_page(self.current_page)
            for x in items:
                yield x
            if not self.has_next_page():
                return  # no more pages
            else:
                self.goto_page(self.current_page + 1)

    def __len__(self):
        return self.get_total_count()

    def _is_initialized(self) -> bool:
        """Check if object is initialized (at least one page was retrieved)."""
        return self.__recent_response is not None

    def _ensure_initialized(self):
        """Ensure that object is initialized, if not - request the first page."""
        if not self._is_initialized():
            self.goto_page(1)


def no_trailing_slash(val: str) -> str:
    """
    Remove all trailing slashes from the given string. Might be useful to normalize URLs.

    Non-string input is considered as error.
    """
    while val.endswith("/"):
        val = val[:-1]
    return val
