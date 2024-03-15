from types import TracebackType

from aiohttp.client import ClientSession

from matrix_client.api import Endpoints
from matrix_client.api.auth import RegisterTokenValidityQuery
from matrix_client.exceptions import UnexpectedServerResponse
from matrix_client.types.auth import RegistrationTokenValidityResponse
from matrix_client.types.errors import (
    ForbiddenErrorResponse,
    TooManyRequestErrorResponse,
)


class MatrixClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = ClientSession()

    async def __aenter__(self) -> "MatrixClient":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.session.close()

    async def is_register_token_valid(
        self, query: RegisterTokenValidityQuery
    ) -> (
        RegistrationTokenValidityResponse
        | ForbiddenErrorResponse
        | TooManyRequestErrorResponse
    ):
        url = Endpoints.auth.get_registration_token_validity
        async with self.session.request(
            url.method_name, url.parse(None, query)
        ) as resp:
            match resp.status:
                case 200:
                    return RegistrationTokenValidityResponse.model_validate_json(
                        await resp.read()
                    )
                case 403:
                    return ForbiddenErrorResponse.model_validate_json(await resp.read())
                case 429:
                    return TooManyRequestErrorResponse.model_validate_json(
                        await resp.read()
                    )
        raise UnexpectedServerResponse()
