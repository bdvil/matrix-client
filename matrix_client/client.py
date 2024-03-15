from matrix_client.api import Endpoints
from matrix_client.api.auth import RegisterTokenValidityQuery


class MatrixClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def is_register_token_valid(self, query: RegisterTokenValidityQuery):
        pass
        # url = Endpoints.auth.get_registration_token_validity.parse(query)
