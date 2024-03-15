from matrix_client.api.auth import AuthEndpoints
from matrix_client.api.http_methods import (
    DELETE,
    GET,
    POST,
    PUT,
    HTTPMethod,
    HTTPMethodNames,
)
from matrix_client.api.server_discovery import ServerDiscoveryEndpoints


class Endpoints:
    auth = AuthEndpoints
    server_discovery = ServerDiscoveryEndpoints


__all__ = [
    "Endpoints",
    "AuthEndpoints",
    "ServerDiscoveryEndpoints",
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "HTTPMethod",
    "HTTPMethodNames",
]
