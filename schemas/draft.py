
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DraftCreate(BaseModel):
    user_id: int
    title: str | None = None


class DraftUpdate(BaseModel):
    user_id: int | None = None
    title: str | None = None


class DraftResponse(BaseModel):
    id: int
    user_id: int
    title: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
