from dataclasses import dataclass

from matrix_client.api import GET


@dataclass
class AuthEndpoints:
    get_registration_token_validity = GET(
        "/_matrix/client/v1/register/m.login.registration_token/validity"
    )
