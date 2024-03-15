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


class HTTPMethodNames(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class HTTPMethod[T: Mapping[str, Any] | None, U]:
    method_name: HTTPMethodNames

    def __init__(self, url: str):
        if isinstance(url, HTTPMethod):
            self.url = url.url
        else:
            self.url = url

    def parse(self, query_args: T, **kwargs: U) -> str:
        url = self.url.format(**kwargs)
        return f"{url}{_urlencode(query_args)}"

    def __repr__(self) -> str:
        return self.url


class GET[T: Mapping[str, Any] | None, U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.GET

    def __repr__(self) -> str:
        return "GET " + super().__repr__()


class POST[T: Mapping[str, Any] | None, U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.POST

    def __repr__(self) -> str:
        return "POST " + super().__repr__()


class PUT[T: Mapping[str, Any] | None, U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.PUT

    def __repr__(self) -> str:
        return "PUT " + super().__repr__()


class DELETE[T: Mapping[str, Any] | None, U](HTTPMethod[T, U]):
    method_name = HTTPMethodNames.DELETE

    def __repr__(self) -> str:
        return "DELETE " + super().__repr__()
