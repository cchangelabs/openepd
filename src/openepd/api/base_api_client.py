import datetime
import logging
from typing import Final

from openepd.__version__ import VERSION
from openepd.api.common import no_trailing_slash, Throttler

USER_AGENT_DEFAULT: Final[str] = f"OpenEPD API Client/{VERSION}"

logger = logging.getLogger(__name__)


class BaseApiClient:
    HTTP_DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"
    DEFAULT_RETRY_INTERVAL_SEC = 10
    DEFAULT_TIMEOUT_SEC = (15, 2 * 60)

    def __init__(
        self,
        base_url: str,
        throttle_retry_timeout: float | int | datetime.timedelta = 300,
        requests_per_sec: float = 10,
        retry_count: int = 3,
        user_agent: str | None = None,
        timeout_sec: float | tuple[float, float] | None = None,
    ):
        self._base_url: str = no_trailing_slash(base_url)
        self._throttler = Throttler(rate_per_sec=requests_per_sec)
        self._throttle_retry_timeout: float = (
            float(throttle_retry_timeout)
            if isinstance(throttle_retry_timeout, float | int)
            else throttle_retry_timeout.total_seconds()
        )
        self.user_agent = user_agent
        self.timeout = timeout_sec or self.DEFAULT_TIMEOUT_SEC
        self._retry_count: int = retry_count

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
            headers["user-agent"] = self.user_agent or USER_AGENT_DEFAULT
        return headers

    def _get_url_for_request(self, path_or_url: str) -> str:
        """
        Generate url for given input.

        If absolute path is given it will be returned as is, otherwise the base url will be prepended.
        :param path_or_url: Either absolute url or base path.
        :return: absolute url
        """
        return self._base_url + path_or_url if not path_or_url.startswith("http") else path_or_url

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
