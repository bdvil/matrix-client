from dataclasses import dataclass

from matrix_client.api.http_methods import GET


@dataclass
class ServerDiscoveryEndpoints:
    well_known_client = GET("/.well-known/matrix/client")
    version = GET("/_matrix/client/versions")
