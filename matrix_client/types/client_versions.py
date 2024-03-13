from collections.abc import Mapping, Sequence

from pydantic import BaseModel


class ClientVersionsResponse(BaseModel):
    unstable_features: Mapping[str, bool] | None = None
    versions: Sequence[str]
