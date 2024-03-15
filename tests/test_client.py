import asyncio

from matrix_client.api.auth import RegisterTokenValidityQuery
from matrix_client.client import MatrixClient


async def main():
    query = RegisterTokenValidityQuery(token="dummy")
    async with MatrixClient("http://localhost:8008") as client:
        resp = await client.is_register_token_valid(query)
        print(type(resp))
        print(resp)


def test_is_register_token_valid():
    asyncio.run(main())


if __name__ == "__main__":
    test_is_register_token_valid()
