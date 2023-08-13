from typing import Dict, Optional, Tuple

from loguru import logger

from signum_bot.database.collections import *
from signum_bot.database.models import *
from signum_bot.database.exceptions import *
from signum_bot.database.crud import get_user

import signum_bot.sites.codewars.api as codewars_api


class BaseUser(BaseUserModel):
    def delete_team(self):
        pass


class Admin(BaseUser):
    """ Администратор - это учитель, telegram_id которого помещен в список администраторов """

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


class User(UserModel):
    @staticmethod
    def get(tg_id: int) -> UserModel:
        """ Получить данные пользователя из БД """

        logger.info(f'Получение пользователя {tg_id} из БД')
        user = get_user(tg_id)
        return super().__init__(**user)

    def get_nicknames(self) -> List[Optional[Tuple[str, str]]]:
        logger.info(f'Получение всех nicknames пользователя {self.tg_id} из БД')
        return list(self.nicknames.items())

    def get_codewars_stat(self) -> Dict:
        """ отправка запроса на сайт codewars для получения данных о пользователе """

        logger.info(f'Попытка получения статистики пользователя {self.id} с сайта codewars')
        if 'codewars' in self.nicknames:
            user_info = codewars_api.get_codewars_user(self.nicknames.get('codewars'))
            logger.info(f'Успешное получение статистики пользователя {self.id} с сайта codewars')
            return user_info.model_dump()
        logger.info(f'Не удалось получить статистику пользователя {self.id} так как он не указал аккаунт codewars')
        return dict()

    def send_request(self):
        """ Отправка запроса на присоединение в команду """
        pass

    def get_teams(self):
        pass

    def create_team(self):
        pass

    def _create(self) -> int:
        logger.info(f'Попытка создать нового {self.role} -> {self.id}')
        if users.find_one({'_id': self.id}):
            logger.info(f'Пользователь {self.id} уже сущеуствует')
            raise UserExistsError

        logger.info(f'Создание нового {self.role} -> {self.id}')
        self.nicknames = {key.lower(): value for key, value in self.nicknames.items()}
        data: dict = self.model_dump(by_alias=True)
        return users.insert_one(data)['_id']


class Student(StudentModel, User):
    def create(self):
        self._create()


class Teacher(TeacherModel, User):
    def create(self):
        self._create()

    def get_info_of_student(self):
        """ Получение информации о студенте, который прикреплен к данному преподавателю """
        pass

    def attach_student(self):
        """ Прикрепляет студента к преподавателю """
        pass
