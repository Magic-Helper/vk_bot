from pydantic import BaseModel


class Check(BaseModel):
    steamid: str
    moderator_id: int
    start: int | None = None
    end: int | None = None
    server_number: int
    is_ban: bool = False


class CreateCheck(Check):
    moderator_id: int | None = None
    moderator_vk_id: int


class CheckInDB(Check):
    id: int
