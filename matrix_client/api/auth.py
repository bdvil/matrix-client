from dataclasses import dataclass
from typing import TypedDict

from matrix_client.api.http_methods import GET


class RegisterTokenValidityQuery(TypedDict):
    token: str


@dataclass
class AuthEndpoints:
    get_registration_token_validity: GET[None, RegisterTokenValidityQuery] = GET(
        "/_matrix/client/v1/register/m.login.registration_token/validity"
    )
