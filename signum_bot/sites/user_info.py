from pydantic import BaseModel


class CodeWarsUserInfo(BaseModel):
    username: str
    honor: int
    languages: dict
    total_completed: int


class LeetCodeUserInfo(BaseModel): ...
