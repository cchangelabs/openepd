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
__all__ = (
    "HttpStreamReader",
    "SyncHttpClient",
    "DoRequest",
    "RetryHandler",
    "BaseApiMethodGroup",
    "USER_AGENT_DEFAULT",
)

import datetime
from functools import partial, wraps
from io import IOBase
import logging
import random
import shutil
import time
from typing import IO, Any, BinaryIO, Callable, Final, NamedTuple

import requests
from requests import PreparedRequest, Response, Session, Timeout
from requests import codes as requests_codes
from requests.auth import AuthBase
from requests.structures import CaseInsensitiveDict

from openepd.__version__ import VERSION
from openepd.api import errors
from openepd.api.common import Throttler, no_trailing_slash

logger = logging.getLogger(__name__)

USER_AGENT_DEFAULT: Final[str] = f"OpenEPD API Client/{VERSION}"

DoRequest = Callable[[], Response]
RetryHandler = Callable[[DoRequest], Response | None]
ErrorHandler = Callable[[Response, bool], Response | None]
"""
ErrorHandler is a callable that takes a response and a boolean indicating whether 
exception should be raised in case of error.
"""


class HttpStreamReader(IOBase):
    """A wrapper around a requests Response object that allows it to be used as a stream."""

    def __init__(self, http_response: Response, chunk_size: int = 1024) -> None:
        """
        Initialize HttpStreamReader with given HttpResponse in streaming mode.

        :param http_response: HTTP response object
        """
        super().__init__()
        self._http_response = http_response
        self.chunk_size = chunk_size

    def readable(self) -> bool:
        """Return True if the stream can be read from."""
        return True

    def seekable(self) -> bool:
        """Return True if the stream supports random access."""
        return False

    def writable(self) -> bool:
        """Return True if the stream supports writing."""
        return False

    def read(self, size: int = -1) -> bytes:
        """Read and return up to size bytes, where size is an int."""
        return self._http_response.raw.read(size)

    def readinto(self, target_stream: IO[bytes]) -> None:
        """Read bytes into a pre-allocated, writable bytes-like object target_stream."""
        shutil.copyfileobj(self._http_response.raw, target_stream)

    def raw(self) -> BinaryIO:
        """Return the underlying HTTP Response content."""
        return self._http_response.raw

    def detach(self) -> BinaryIO:
        """Separate the underlying HTTP Response from the HttpStreamReader and return it."""
        tmp = self._http_response
        self._http_response = None  # type: ignore
        return tmp.raw

    def close(self) -> None:
        """
        Releases the connection back to the pool.

        Once this method has been called the underlying ``raw`` object must not be accessed again.
        *Note: Should not normally need to be called explicitly.*
        """
        self._http_response.close()

    def get_size(self) -> int:
        """Return the size of the response in bytes."""
        return int(self._http_response.headers.get("Content-Length", 0))

    def get_content_type(self) -> str:
        """Return the content type of the response."""
        return self._http_response.headers.get("Content-Type", "")

    def get_status_code(self) -> int:
        """Return the status code of the response."""
        return self._http_response.status_code

    def get_headers(self) -> CaseInsensitiveDict[str]:
        """Return the headers of the response."""
        return self._http_response.headers


class TokenAuth(AuthBase):
    """Attach OpenEPD Token Authentication to the given Request object."""

    def __init__(self, token: str) -> None:
        super().__init__()
        self.token = token

    def __eq__(self, other):
        if other is None:
            return False
        if other.__class__ is not self.__class__:
            return False
        return self.token == other.token

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


class SyncHttpClient:
    """
    HTTP client to communicate with OpenEPD servers via HTTP.

    It works on top of requests library and provides some commonly needed features, such as throttling, retries, etc.
    """

    HTTP_DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"
    DEFAULT_RETRY_INTERVAL_SEC = 10

    def __init__(
        self,
        base_url: str,
        throttle_retry_timeout: float | int | datetime.timedelta = 300,
        requests_per_sec: float = 10,
        retry_count: int = 3,
        user_agent: str | None = None,
        timeout_sec: float | tuple[float, float] | None = None,
        auth: AuthBase | None = None,
    ):
        """
        Construct BaseApiClient.

        :param base_url: common part that all request URLs start with
        :param throttle_retry_timeout: how long to wait before retrying throttled request.
                                       Either number of seconds or timedelta
        :param requests_per_sec: requests per second
        :param user_agent: user agent to pass along with a request,
            if `None` then underlying library decides which one to pass
        :param timeout_sec: how long to wait for the server to send data before giving up,
            as a seconds (just a single float), or a (connect timeout, read timeout) tuple.
        :param retry_count: count of retries to perform in case of connection error or timeout.
        """
        self._base_url: str = no_trailing_slash(base_url)
        self._throttler = Throttler(rate_per_sec=requests_per_sec)
        self._throttle_retry_timeout: float = (
            float(throttle_retry_timeout)
            if isinstance(throttle_retry_timeout, (float, int))
            else throttle_retry_timeout.total_seconds()
        )
        self.user_agent = user_agent
        self.timeout = timeout_sec
        self._session: Session | None = None
        self._auth: AuthBase | None = auth
        self._retry_count: int = retry_count

        self._http_retry_handlers: dict[int, RetryHandler] = {}
        self._http_error_handlers: dict[int, ErrorHandler] = {}

        self.register_error_handler(400, DefaultOpenApiErrorHandlers.handle_bad_request)
        self.register_error_handler(401, DefaultOpenApiErrorHandlers.handle_unauthorized)
        self.register_error_handler(403, DefaultOpenApiErrorHandlers.handle_access_denied)
        self.register_error_handler(404, DefaultOpenApiErrorHandlers.handle_not_found)
        self.register_error_handler(500, DefaultOpenApiErrorHandlers.handle_server_error)

    @property
    def base_url(self) -> str:
        """Return base URL for all requests."""
        return self._base_url

    @base_url.setter
    def base_url(self, new_value: str):
        """Set base URL for all requests."""
        self._base_url = no_trailing_slash(new_value)

    @property
    def default_headers(self) -> dict[str, str]:
        """Default headers for requests. Implement if required."""
        headers = {}
        if self.user_agent:
            headers["user-agent"] = self.user_agent
        return headers

    def reset_session(self) -> None:
        """Reset current session (if any). This will clear all cookies and other session data."""
        self._session = None

    def read_bytes_from_url(self, url: str, method: str = "get", **kwargs) -> bytes:
        """
        Perform query to the given endpoint and returns response body as bytes.

        This method will load the ENTIRE CONTENT IN MEMORY. DO NOT USE it to download files. Consider using
        `write_to_stream` instead.
        The request will be performed in the context of API client, default error handling will be applied.

        :param url: url pointing the target endpoint
        :param method: optional HTTP method
        :param kwargs: any other arguments supported by _do_request. See `BaseApiClient._do_request`.
        :return: response content as bytes
        """
        r = self.do_request(method, url, **kwargs)
        content = r.content
        return content

    def read_url_write_to_stream(
        self, url: str, target_stream: IO[bytes], method: str = "get", chunk_size: int = 1024, **kwargs
    ) -> int:
        """
        Perform query to the given endpoint and writes response body to the given stream.

        :param url: url pointing the target endpoint
        :param target_stream: stream to write response body to
        :param method: optional HTTP method
        :param chunk_size: size of the chunk to read from the response
        :param kwargs: any other arguments supported by _do_request. See `BaseApiClient._do_request`.
        :return: number of bytes written
        """
        with self.do_request(method, url, stream=True, **kwargs) as r:
            size = 0
            for chunk in r.iter_content(chunk_size=chunk_size):
                target_stream.write(chunk)
                size += len(chunk)
            return size

    def read_stream_from_url(self, url: str, method: str = "get", **kwargs) -> HttpStreamReader | IO[bytes]:
        """
        Perform query to the given endpoint and returns response body as a stream.

        The request will be performed in the context of API client, default error handling will be applied.
        NOTE: Consider using it as a context manager to handle stream close correctly.

        :param url: url pointing the target endpoint
        :param method: optional HTTP method
        :param kwargs: any other arguments supported by _do_request. See `BaseApiClient._do_request`.
        :return: response content as a stream
        """
        r = self.do_request(method, url, stream=True, **kwargs)
        return HttpStreamReader(r)

    def register_retry_handler(self, http_error: int, retry_handler: RetryHandler | None) -> None:
        """
        Register retry handler for the given HTTP error code.

        This allows to override default error handling for the given HTTP error code from the subclass.
        """
        if retry_handler is not None:
            self._http_retry_handlers[http_error] = retry_handler

    def delete_retry_handler(self, http_error: int) -> None:
        """
        Delete retry handler for the given HTTP error code.

        See _register_error_handler for more details.
        """
        if http_error in self._http_retry_handlers:
            del self._http_retry_handlers[http_error]

    def register_error_handler(self, http_error: int, error_handler: ErrorHandler | None) -> None:
        """
        Register retry handler for the given HTTP error code.

        This allows to override default error handling for the given HTTP error code from the subclass.
        """
        if error_handler is not None:
            self._http_error_handlers[http_error] = error_handler

    def _delete_error_handler(self, http_error: int) -> None:
        """
        Delete retry handler for the given HTTP error code.

        See _register_error_handler for more details.
        """
        if http_error in self._http_error_handlers:
            del self._http_error_handlers[http_error]

    def _run_throttled_request(
        self,
        method: str,
        url: str,
        request_kwargs: dict[str, Any],
        session: Session | None = None,
    ) -> Response:
        left_time = self._throttle_retry_timeout
        # override current session to do request to some other server from the same API client
        session = session or self._current_session
        while True:
            with self._throttler.throttle():
                resp = session.request(method, url, **request_kwargs)
                if resp.status_code == requests_codes.too_many_requests:
                    timeout = self._get_timeout_from_retry_after_header(
                        resp.headers.get("Retry-After"), self.DEFAULT_RETRY_INTERVAL_SEC
                    )
                    if timeout > left_time:
                        return resp
                    logger.info("`%s %s` has been throttled for %s second(s)", method, url, timeout)
                    time.sleep(timeout)
                    left_time -= timeout
                    if left_time > 0:
                        continue
                return resp

    def do_request(
        self,
        method: str,
        endpoint: str,
        params=None,
        data=None,
        json=None,
        files=None,
        headers=None,
        session: Session | None = None,
        auth: AuthBase | None = None,
        raise_for_status: bool = True,
        **kwargs,
    ) -> Response:
        """
        Perform request to the given endpoint.

        See https://requests.readthedocs.io/en/master/api/#requests.request for more details on kwargs.
        """
        headers = headers or self.default_headers

        self._on_before_do_request()

        url = self._get_url_for_request(endpoint)

        request_kwargs = dict(
            params=params,
            data=data,
            json=json,
            files=files,
            headers=headers,
            timeout=self.timeout,
            auth=auth or self._auth,
        )
        request_kwargs.update(kwargs)

        do_request = self._handle_service_unavailable(
            method,
            url,
            self._retry_count,
            partial(self._run_throttled_request, method, url, request_kwargs, session=session),
        )

        response = do_request()

        if response.ok:
            return response

        retry_handler = self._http_retry_handlers.get(response.status_code, None)
        if retry_handler:
            result = retry_handler(do_request)
            response = result or response

        error_handler = self._http_error_handlers.get(response.status_code, None)
        if error_handler:
            response = error_handler(response, raise_for_status)

        if response.ok or not raise_for_status:
            return response

        response.raise_for_status()
        # This can't be handled by static checker because of the dynamic nature of the raise_for_status method
        raise RuntimeError("This line should never be reached")

    def _get_url_for_request(self, path_or_url: str) -> str:
        """
        Generate url for given input.

        If absolute path is given it will be returned as is, otherwise the base url will be prepended.
        :param path_or_url: Either absolute url or base path.
        :return: absolute url
        """
        return self._base_url + path_or_url if not path_or_url.startswith("http") else path_or_url

    @property
    def _current_session(self) -> Session:
        if self._session is None:
            self._session = Session()
        return self._session

    def _on_before_do_request(self):
        """
        Perform any actions before request is sent.

        This is a hook that will be called before `do_request`. Can be overridden to check / refresh access tokens.
        """
        pass

    def _get_timeout_from_retry_after_header(self, retry_after: str | None, default: float = 10.0) -> float:
        if retry_after is None:
            return default
        try:
            return float(retry_after)
        except ValueError:
            # This means the value is not at number of seconds but a date, so we parse it
            try:
                date_in_future = datetime.datetime.strptime(retry_after.strip(), self.HTTP_DATE_TIME_FORMAT)
                return (date_in_future - datetime.datetime.utcnow()).total_seconds()
            except ValueError:
                logger.warning("Invalid Retry-After header: %s", retry_after)
                return default

    @staticmethod
    def _handle_service_unavailable(method: str, url: str, retry_count: int, func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = retry_count
            response = None
            exception = None
            while attempts > 0:
                exception = None
                try:
                    response = func(*args, **kwargs)
                except (requests.exceptions.ConnectionError, ConnectionError, Timeout) as e:
                    exception = e

                if exception or response.status_code == requests_codes.service_unavailable:
                    secs = random.randint(60, 60 * 5)
                    logger.warning(
                        "%s %s is unavailable. Attempts left: %s. Waiting %s seconds...", method, url, attempts, secs
                    )

                    # wait random number of seconds and request again
                    time.sleep(secs)
                    attempts -= 1
                else:
                    break
            if exception:
                raise exception
            return response

        return wrapper


class DefaultOpenApiErrorHandlers:
    class _Error(NamedTuple):
        summary: str
        error_code: str | None
        details: dict[str, list[str]] | None

    @staticmethod
    def _parse_error_response(response: Response) -> _Error:
        error_text = response.text
        validation_errors: dict[str, Any] | None = None
        error_code: str | None = None
        if response.headers.get("content-type") == "application/json":
            json_error = response.json()
            error_text = json_error.get("detail", error_text)
            validation_errors = json_error.get("validation_errors", None)
            if validation_errors is not None:
                error_code = validation_errors.get("code", None)
                if isinstance(validation_errors.get("detail", 0), str):
                    error_text = validation_errors.get("detail", "")
                    validation_errors = dict(msg=validation_errors.get("detail", []))
                if error_code is not None:
                    error_text = f"[{error_code}] {error_text}"
        return DefaultOpenApiErrorHandlers._Error(error_text, error_code, validation_errors)

    @staticmethod
    def handle_bad_request(response: Response, raise_for_status: bool) -> Response | None:
        if raise_for_status:
            error = DefaultOpenApiErrorHandlers._parse_error_response(response)
            raise errors.ValidationError(
                response.status_code,
                error.summary,
                validation_errors=error.details,
                response=response,
                error_code=error.error_code,
            )
        return response

    @staticmethod
    def handle_not_found(response: Response, raise_for_status: bool) -> Response | None:
        if raise_for_status:
            error = DefaultOpenApiErrorHandlers._parse_error_response(response)
            raise errors.ObjectNotFound(response.status_code, error.summary, response, error_code=error.error_code)
        return response

    @staticmethod
    def handle_unauthorized(response: Response, raise_for_status: bool) -> Response | None:
        if raise_for_status:
            error = DefaultOpenApiErrorHandlers._parse_error_response(response)
            raise errors.NotAuthorizedError(response.status_code, error.summary, response, error_code=error.error_code)
        return response

    @staticmethod
    def handle_access_denied(response: Response, raise_for_status: bool) -> Response | None:
        if raise_for_status:
            error = DefaultOpenApiErrorHandlers._parse_error_response(response)
            raise errors.AccessDeniedError(response.status_code, error.summary, response, error_code=error.error_code)
        return response

    @staticmethod
    def handle_server_error(response: Response, raise_for_status: bool) -> Response | None:
        if raise_for_status:
            error = DefaultOpenApiErrorHandlers._parse_error_response(response)
            raise errors.ServerError(response.status_code, error.summary, response, error_code=error.error_code)
        return response


class BaseApiMethodGroup:
    """Base class for API method groups."""

    def __init__(self, client: SyncHttpClient) -> None:
        """
        Construct a method group.

        :param client: HTTP client to use for requests
        """
        super().__init__()
        self._client = client
