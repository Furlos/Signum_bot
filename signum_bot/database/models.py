from typing import Dict, List, Optional

from pydantic import BaseModel, Field, ConfigDict


class BaseUserModel(BaseModel):
    # model_config = ConfigDict(frozen=True)

    id: int = Field(alias='_id', frozen=True)  # telegram_id
    last_name: Optional[str]
    name: str
    father_name: str


class UserModel(BaseUserModel):
    nicknames: Dict[str, str]  # имена пользователя с разных ресурсов
    own_teams: List[Optional[int]] = []


class StudentModel(UserModel):
    role: str = 'student'
    teams: List[str] = ['students']
    teacher_id: Optional[int] = None  # telegram_id преподавателя


class TeacherModel(UserModel):
    role: str = 'teacher'
    teams: List[str] = ['teachers']
    students_id: List[Optional[int]] = []  # telegram_id студентов, привязанных к этому преподавателю


class TeamModel(BaseModel):
    id: int = Field(alias='_id')  # telegram_id
    title: str
    amount_members: int
    members: List[int]
    owner_id: int  # telegram_id
    # score: int
