from pydantic import BaseModel, ConfigDict, Field


class HomeserverInformation(BaseModel):
    base_url: str
    """The base URL for the homeserver for client-server connections."""


class IdentityServerInformation(BaseModel):
    base_url: str
    """The base URL for the identity server for client-server connections."""


class DiscoveryInformation(BaseModel):
    model_config = ConfigDict(extra="allow")

    homeserver: HomeserverInformation = Field(alias="m.homeserver")
    """Used by clients to discover homeserver information."""

    identity_server: IdentityServerInformation | None = Field(
        alias="m.identity_server", default=None
    )
    """Used by clients to discover identity server information."""
