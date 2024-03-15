from abc import ABC
from collections.abc import Mapping
from typing import Any
from urllib import parse

from _typeshed import StrEnum


def _urlencode(data: Mapping[str, Any] | None) -> str:
    query = {}
    if data is None:
        return ""
    for key, val in data.items():
        if isinstance(val, bool):
            query[key] = str(val).lower()
        elif val is not None:
            query[key] = val
    return "?" + parse.urlencode(query)


class URL:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def combine(self, other: "URL | str") -> "URL":
        if isinstance(other, URL):
            other = other.base_url

        return URL(parse.urljoin(self.base_url, other))

    def __repr__(self) -> str:
        return self.base_url

    def __truediv__(self, other: "URL | str") -> "URL":
        return self.combine(other)


class HTTPMethodNames(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class HTTPMethod[T: Mapping[str, Any], U](ABC):
    method_name: HTTPMethodNames

    def __init__(self, url: str):
        self.url = url

    def parse(self, query_args: T | None = None, **kwargs: U) -> str:
        url = self.url.format(**kwargs)
        return f"{url}{_urlencode(query_args)}"

    def __repr__(self) -> str:
        return self.url


class GET[T: Mapping[str, Any], U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.GET

    def __repr__(self) -> str:
        return "GET " + super().__repr__()


class POST[T: Mapping[str, Any], U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.POST

    def __repr__(self) -> str:
        return "POST " + super().__repr__()


class PUT[T: Mapping[str, Any], U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.PUT

    def __repr__(self) -> str:
        return "PUT " + super().__repr__()


class DELETE[T: Mapping[str, Any], U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.DELETE

    def __repr__(self) -> str:
        return "DELETE " + super().__repr__()
