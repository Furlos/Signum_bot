from typing import Dict, List, Optional
import dataclasses

from pydantic import BaseModel, Field
from loguru import logger

import signum_bot.sites.codewars.api as codewars_api
from signum_bot.database.collections import users, teams, requests
from signum_bot.database.exceptions import *


class _BaseUserModel(BaseModel):
    id: int = Field(alias='_id') # telegram_id
    last_name: Optional[str] = ''
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
    nicknames: Dict[str, str]  # имена пользователя с разных ресурсов
    teams: Optional[List[str]] = []
    own_teams: Optional[List[int]] = []

    @staticmethod
    def get(tg_id: int):
        """ Получить данные пользователя из БД """

        logger.info(f'Получение пользователя {tg_id} из БД')
        user = users.find_one({'_id': tg_id})
        if user:
            return UserModel(**user)
        raise NotFoundUserError

    @staticmethod
    def get_nicknames(tg_id: int) -> Dict[str, str]:
        logger.info(f'Получение всех nicknames пользователя {tg_id} из БД')
        return UserModel.get(tg_id).nicknames

    def get_codewars_stat(self) -> Dict:
        """ отправка запроса на сайт codewars для получения данных о пользователе """

        logger.info(f'Попытка получения статистики пользователя {self.id} с сайта codewars')
        if 'codewars' in self.nicknames:
            user_info = codewars_api.get_codewars_user(self.nicknames.get('codewars'))
            logger.info(f'Успешное получение статистики пользователя {self.id} с сайта codewars')
            return dataclasses.asdict(user_info)
        logger.info(f'Не удалось получить статистику пользователя {self.id} так как он не указал аккаунт codewars')
        return dict()

    def send_request(self):
        """ Отправка запроса на присоединение в команду """
        pass

    def get_teams(self):
        pass

    def create_team(self):
        pass

    def _create(self, role):
        logger.info(f'Попытка создать нового {role} -> {self.id}')
        if users.find_one({'_id': self.id}):
            logger.info(f'Пользователь {self.id} уже сущеуствует')
            raise UserExistsError
        logger.info(f'Создание нового {role} -> {self.id}')
        self.nicknames = {key.lower(): value for key, value in self.nicknames.items()}
        additional_field = 'teacher_id' if role == 'student' else 'students_id'
        users.insert_one(
            {
                '_id': self.id,
                'last_name': self.last_name,
                'name': self.name,
                'father_name': self.father_name,
                'role': role,
                'nicknames': self.nicknames,
                'teams': [f'{role}s'],
                'own_teams': [],
                additional_field: []
            }
        )


class Student(UserModel):
    role: str = 'student'
    teacher_id: Optional[int] = None  # telegram_id преподавателя

    def create(self):
        print(self.__dict__)
        self._create(self.role)


class Teacher(UserModel):
    role: str = 'teacher'
    students_id: List[Optional[int]]  # telegram_id студентов, привязанных к этому преподавателю

    def create(self):
        self._create(self.role)

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
