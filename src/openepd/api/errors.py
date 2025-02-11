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
from typing import Any


class ApiError(Exception):
    """Base class for all API errors."""

    def __init__(
        self, http_status: int, error_summary: str, response: Any = None, error_code: str | None = None
    ) -> None:
        super().__init__(error_summary)
        self.error_summary = error_summary
        self.http_status = http_status
        self.error_code = error_code
        self.response = response


class ObjectNotFound(ApiError):
    """Object not found error."""

    pass


class ServerError(ApiError):
    """Server error."""

    pass


class ValidationError(ApiError):
    """Validation error."""

    def __init__(
        self,
        http_status: int,
        error_summary: str,
        validation_errors: dict[str, list[str]] | None,
        response: Any,
        error_code: str | None,
    ) -> None:
        super().__init__(http_status, error_summary, response, error_code)
        self.validation_errors: dict[str, list[str]] = validation_errors or {}

    @staticmethod
    def __flatten(nested_errors: dict[str, Any], parent_key: str = "") -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        for key, value in nested_errors.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                nested_result = ValidationError.__flatten(value, full_key)
                for nested_key, nested_errors in nested_result.items():  # type: ignore[assignment]
                    result.setdefault(nested_key, []).extend(nested_errors)
            else:
                result.setdefault(full_key, []).extend(value)
        return result

    def __str__(self) -> str:
        result: list[str] = ["Validation errors:"]
        for code, errors in self.__flatten(self.validation_errors).items():  # type: ignore[arg-type]
            result.append(f"{code}:")
            for e in errors:
                result.append(f"  {e}")
        return "\n".join(result)


class AuthError(ApiError):
    """Common class for any authentication related errors."""

    pass


class NotAuthorizedError(AuthError):
    """Not authorized error."""

    pass


class AccessDeniedError(AuthError):
    """Access denied error."""

    pass
