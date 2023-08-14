from pydantic import BaseModel


class CodeWarsUserInfo(BaseModel):
    username: str
    honor: int
    languages: dict
    total_completed: int


class LeetCodeUserInfo(BaseModel):
    totalSolved: int
    easySolved: int
    mediumSolved: int
    hardSolved: int
    ranking: int
    reputation: int
