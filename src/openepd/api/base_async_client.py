import asyncio
import datetime
import logging
import time
from collections.abc import Callable
from typing import Awaitable, Any

from httpx import Auth, Response, AsyncClient
from httpx_retries import RetryTransport
from urllib3 import Retry

from openepd.api.base_api_client import BaseApiClient

DoRequest = Callable[[], Awaitable[Response]]
RetryHandler = Callable[[DoRequest], Awaitable[Response | None]]
ErrorHandler = Callable[[Response, bool], Awaitable[Response | None]]
"""
ErrorHandler is a callable that takes a response and a boolean indicating whether 
exception should be raised in case of error.
"""

logger = logging.getLogger(__name__)


class TokenBasedAuth(Auth):
    def __init__(self, token: str) -> None:
        self.token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        yield request


class AsyncHttpClient(BaseApiClient):
    def __init__(
        self,
        base_url: str,
        throttle_retry_timeout: float | int | datetime.timedelta = 300,
        requests_per_sec: float = 10,
        retry_count: int = 3,
        user_agent: str | None = None,
        timeout_sec: float | tuple[float, float] | None = None,
        auth: Auth | None = None,
    ):
        super().__init__(
            base_url=base_url,
            throttle_retry_timeout=throttle_retry_timeout,
            requests_per_sec=requests_per_sec,
            retry_count=retry_count,
            user_agent=user_agent,
            timeout_sec=timeout_sec,
        )
        self._auth = auth
        self._session: AsyncClient | None = None

        self._http_retry_handlers: dict[int, RetryHandler] = {}
        self._http_error_handlers: dict[int, ErrorHandler] = {}

    def reset_session(self) -> None:
        """Reset current session (if any). This will clear all cookies and other session data."""
        self._session = None

    @property
    def _current_session(self) -> AsyncClient:
        if self._session is None:
            retry_config = Retry(total=self._retry_count, backoff_factor=0.5, respect_retry_after_header=True)
            self._session = AsyncClient(
                auth=self._auth, transport=RetryTransport(retry=retry_config), follow_redirects=True
            )
        return self._session

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

    async def _run_throttled_request(
        self,
        method: str,
        url: str,
        request_kwargs: dict[str, Any],
        session: AsyncClient | None = None,
    ) -> Response:
        left_time = self._throttle_retry_timeout
        # override current session to do request to some other server from the same API client
        session = session or self._current_session
        while True:
            with self._throttler.throttle():
                resp = await session.request(method, url, **request_kwargs)
                if resp.status_code == 429:
                    timeout = self._get_timeout_from_retry_after_header(
                        resp.headers.get("Retry-After"), self.DEFAULT_RETRY_INTERVAL_SEC
                    )
                    if timeout > left_time:
                        return resp
                    logger.info(
                        "`%s %s` has been throttled for %s second(s)",
                        method,
                        url,
                        timeout,
                    )
                    await asyncio.sleep(timeout)
                    left_time -= timeout
                    if left_time > 0:
                        continue
                return resp

    async def do_request(
        self,
        method: str,
        endpoint: str,
        params=None,
        data=None,
        json=None,
        files=None,
        headers=None,
        client: AsyncClient | None = None,
        auth: Auth | None = None,
        raise_for_status: bool = True,
        **kwargs,
    ) -> Response:
        headers = headers or self.default_headers

        await self._on_before_do_request()

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

        response = await self._current_session.request(
            method, url, **request_kwargs
        )

        if response.is_success:
            return response
        # TODO: Retry? - probably no need considering httpx_retries is used
        # TODO: Error handling?

        if response.is_success or not raise_for_status:
            return response

        response.raise_for_status()
        # This can't be handled by static checker because of the dynamic nature of the raise_for_status method
        msg = "This line should never be reached"
        raise RuntimeError(msg)

    async def _on_before_do_request(self):
        """
        Perform any actions before request is sent.

        This is a hook that will be called before `do_request`. Can be overridden to check / refresh access tokens.
        """
        pass

    def close(self):
        if self._session is not None:
            self._session.close()


class DefaultOpenApiErrorHandlers:
    pass


class BaseApiMethodGroup:
    def __init__(self, client: AsyncHttpClient) -> None:
        """
        Construct a method group.

        :param client: HTTP client to use for requests
        """
        super().__init__()
        self._client = client
