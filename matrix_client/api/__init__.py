from dataclasses import dataclass

from matrix_client.api.auth import AuthEndpoints
from matrix_client.api.http_methods import DELETE, GET, POST, PUT, URL, HTTPMethodNames
from matrix_client.api.server_discovery import ServerDiscoveryEndpoints


@dataclass
class Endpoints:
    auth: AuthEndpoints
    server_discovery: ServerDiscoveryEndpoints


__all__ = [
    "Endpoints",
    "AuthEndpoints",
    "ServerDiscoveryEndpoints",
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "URL",
    "HTTPMethodNames",
]
