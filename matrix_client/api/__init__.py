from abc import ABC
from dataclasses import dataclass
from typing import Any

from matrix_client.api.auth import AuthEndpoints


class HTTPMethod(ABC):
    def __init__(self, url: str, **kwargs: Any):
        self.url = url
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return self.url.format(**self.kwargs)


class GET(HTTPMethod):
    def __repr__(self) -> str:
        return "GET " + super().__repr__()


class POST(HTTPMethod):
    def __repr__(self) -> str:
        return "POST " + super().__repr__()


class PUT(HTTPMethod):
    def __repr__(self) -> str:
        return "PUT " + super().__repr__()


class DELETE(HTTPMethod):
    def __repr__(self) -> str:
        return "DELETE " + super().__repr__()


@dataclass
class Endpoints:
    auth: AuthEndpoints


__all__ = ["AuthEndpoints", "Endpoints", "GET", "POST", "PUT", "DELETE"]
