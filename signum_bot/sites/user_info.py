from pydantic import BaseModel


class CodeWarsUserInfo(BaseModel):
    # TODO: посмотреть динамическое/автоматичесоке создание полей класса из объекта json
    username: str
    honor: int
    languages: dict
    total_completed: int


class LeetCodeUserInfo(BaseModel): ...
