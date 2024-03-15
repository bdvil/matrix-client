from matrix_client.api.http_methods import GET


class ServerDiscoveryEndpoints:
    well_known_client = GET("/.well-known/matrix/client")
    version = GET("/_matrix/client/versions")
