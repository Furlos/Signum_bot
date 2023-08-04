from dataclasses import dataclass


@dataclass
class CodeWarsUserInfo:
    # TODO: посмотреть динамическое/автоматичесоке создание полей класса из объекта json
    username: str = None
    honor: int = None
    languages: dict = None
    total_completed: int = None
