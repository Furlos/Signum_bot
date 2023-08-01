from typing import Dict, List, Optional
import dataclasses

from pydantic import BaseModel
from loguru import logger

import signum_bot.sites.codewars.api as codewars_api
from signum_bot.database.collections import users, teams, requests


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


class UserModel(_BaseUserModel):
    role: str
    nicknames: Dict[str, str]  # имена пользователя с разных ресурсов
    teams: List[str]
    own_teams: List[Optional[int]]

    @staticmethod
    def get(tg_id: int):
        """ Получить данные пользователя из БД """

        logger.info(f'Получение пользователя {tg_id} из БД')
        return UserModel(**users.find_one({'_id': tg_id}, {'_id': 0}))

    @staticmethod
    def get_nicknames(tg_id: int) -> Dict[str, str]:
        logger.info(f'Получение всех nicknames пользователя {tg_id} из БД')
        return UserModel.get(tg_id).nicknames

    def get_codewars_stat(self) -> Dict:
        """ отправка запроса на сайт codewars для получения данных о пользователе """

        logger.info(f'Попытка получения статистики пользователя {self._id} с сайта codewars')
        nicknames = UserModel.get_nicknames(self._id)
        if 'codewars' in nicknames:
            user_info = codewars_api.get_codewars_user(nicknames.get('codewars'))
            logger.info(f'Успешное получение статистики пользователя {self._id} с сайта codewars')
            return dataclasses.asdict(user_info)
        logger.info(f'Не удалось получить статистику пользователя {self._id} так как он не указал аккаунт codewars')
        return dict()

    def send_request(self):
        """ Отправка запроса на присоединение в команду """
        pass

    def get_teams(self):
        pass

    def create_team(self):
        pass

    def _create(self, role) -> bool:
        logger.info(f'Попытка создать нового {role} -> {self._id}')
        if users.find_one({'_id': self._id}):
            logger.info(f'Пользователся {self._id} уже сущеуствует')
            return False
        logger.info(f'Создание нового {role} -> {self._id}')
        self.nicknames = {key.lower(): value for key, value in self.nicknames.items()}
        users.insert_one(
            {
                '_id': self._id,
                'last_name': self.last_name,
                'name': self.name,
                'father_name': self.father_name,
                'role': role,
                'nicknames': self.nicknames,
                'teams': [f'{role}s'],
                'own_teams': []
            }
        )
        return True


class Student(UserModel):
    teacher_id: Optional[int]  # telegram_id преподавателя

    def create(self) -> bool:
        return self._create('student')


class Teacher(UserModel):
    students_id: List[Optional[int]]  # telegram_id студентов, привязанных к этому преподавателю

    def create(self) -> bool:
        return self._create('teacher')

    def get_info_of_student(self):
        """ Получение информации о студенте, который прикреплен к данному преподавателю """
        pass

    def attach_student(self):
        """ Прикрепляет студента к преподавателю """
        pass


class TeamLeader(UserModel):
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
