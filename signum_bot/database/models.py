from typing import Dict, List, Optional

from pydantic import BaseModel


class _BaseUserModel(BaseModel):
    _id: int  # telegram_id
    last_name: Optional[str]
    name: str
    father_name: str

    def delete_team(self):
        pass


class Admin(_BaseUserModel):
    """ Администратор - это учитель, telegram_id которого помещен в список администраторов"""

    @staticmethod
    def delete_student():
        pass

    @staticmethod
    def delete_teacher():
        pass

    @staticmethod
    def give_promo_code():
        """ Выдача специального промокода для регистарции преподавателем """
        pass


class _UserModel(_BaseUserModel):
    nicknames: Dict[str, str]  # имена пользователя с разных ресурсов
    teams: List[str]
    own_teams: List[Optional[int]]

    def get_info_about_me(self):
        pass

    def send_request(self):
        """ Отправка запроса на присоединение в команду """
        pass

    def get_info_of_team(self):
        pass

    def create_team(self):
        pass


class Student(_UserModel):
    teacher_id: Optional[int]  # telegram_id преподавателя


class Teacher(_UserModel):
    students_id: List[Optional[int]]  # telegram_id студентов, привязанных к этому преподавателю

    def get_info_of_student(self):
        """ Получение информации о студенте, который прикреплен к данному преподавателю """
        pass

    def attach_student(self):
        """ Прикрепляет студента к преподавателю """
        pass


class TeamLeader(_UserModel):
    def accept_request(self):
        """ Принять запрос на добавлние в команду """
        pass

    def reject_request(self):
        """ Отказать в запросе на добавление в команду """
        pass

    def rename_team(self):
        pass

    def kicked_off_team(self):
        """ Выгнать из состава команды """
        pass


class _TeamModel(BaseModel):
    _id: int  # telegram_id
    title: str
    amount_members: int
    members: List[int]
    owner_id: int  # telegram_id
    # score: int


class Team(_TeamModel):
    def get_info(self):
        pass
