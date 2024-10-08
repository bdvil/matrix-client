from enum import StrEnum
from typing import Literal

from pydantic import BaseModel


class MatrixErrorCodes(StrEnum):
    # Generic codes
    M_FORBIDDEN = "M_FORBIDDEN"
    M_UNKNOWN_TOKEN = "M_UNKNOWN_TOKEN"
    M_MISSING_TOKEN = "M_MISSING_TOKEN"
    M_BAD_JSON = "M_BAD_JSON"
    M_NOT_JSON = "M_NOT_JSON"
    M_NOT_FOUND = "M_NOT_FOUND"
    M_LIMIT_EXCEEDED = "M_LIMIT_EXCEEDED"
    M_UNRECOGNIZED = "M_UNRECOGNIZED"
    M_UNKNOWN = "M_UNKNOWN"
    # API endpoit specific
    M_UNAUTHORIZED = "M_UNAUTHORIZED"
    M_USER_DEACTIVATED = "M_USER_DEACTIVATED"
    M_USER_IN_USE = "M_USER_IN_USE"
    M_INVALID_USERNAME = "M_INVALID_USERNAME"
    M_ROOM_IN_USE = "M_ROOM_IN_USE"
    M_INVALID_ROOM_STATE = "M_INVALID_ROOM_STATE"
    M_THREEPID_IN_USE = "M_THREEPID_IN_USE"
    M_THREEPID_NOT_FOUND = "M_THREEPID_NOT_FOUND"
    M_THREEPID_AUTH_FAILED = "M_THREEPID_AUTH_FAILED"
    M_THREEPID_DENIED = "M_THREEPID_DENIED"
    M_SERVER_NOT_TRUSTED = "M_SERVER_NOT_TRUSTED"
    M_UNSUPPORTED_ROOM_VERSION = "M_UNSUPPORTED_ROOM_VERSION"
    M_INCOMPATIBLE_ROOM_VERSION = "M_INCOMPATIBLE_ROOM_VERSION"
    M_BAD_STATE = "M_BAD_STATE"
    M_GUEST_ACCESS_FORBIDDEN = "M_GUEST_ACCESS_FORBIDDEN"
    M_CAPTCHA_NEEDED = "M_CAPTCHA_NEEDED"
    M_CAPTCHA_INVALID = "M_CAPTCHA_INVALID"
    M_MISSING_PARAM = "M_MISSING_PARAM"
    M_INVALID_PARAM = "M_INVALID_PARAM"
    M_TOO_LARGE = "M_TOO_LARGE"
    M_EXCLUSIVE = "M_EXCLUSIVE"
    M_RESOURCE_LIMIT_EXCEEDED = "M_RESOURCE_LIMIT_EXCEEDED"
    M_CANNOT_LEAVE_SERVER_NOTICE_ROOM = "M_CANNOT_LEAVE_SERVER_NOTICE_ROOM"


class ErrorResponseBase(BaseModel):
    error: str | None = None


class ErrorResponse(BaseModel):
    errcode: MatrixErrorCodes


class ForbiddenErrorResponse(ErrorResponse):
    pass


class TooManyRequestErrorResponse(ErrorResponseBase):
    errcode: Literal[MatrixErrorCodes.M_LIMIT_EXCEEDED]

    retry_after_ms: int | None = None
