from loguru import logger

from signum_bot.database.collections import *
from signum_bot.database.exceptions import *
from signum_bot.database.models import StudentModel, TeacherModel


def get_user(tg_id: int):
    return users.find_one({'_id': tg_id})


def create_user(tg_id: int, name: str, father_name: str, nicknames: dict, role: str, last_name: str = None) -> int:
    logger.info(f'Попытка создать нового пользователя -> {tg_id} ({role.lower()})')
    if get_user(tg_id):
        logger.info(f'Пользователь {tg_id} уже сущеуствует')
        raise UserExistsError

    user_data = {
        '_id': tg_id,
        'name': name,
        'last_name': last_name,
        'father_name': father_name,
        # TODO: Проверять уникальность имен, чтобы не могли разные люди сидеть на одном аккаунте
        'nicknames': {key.lower(): value for key, value in nicknames.items()}
    }

    logger.info(f"Проверка роли, создаваемого пользователя -> {tg_id}")
    match role.lower():
        case 'student':
            student = StudentModel(**user_data)
            res = users.insert_one(student.model_dump(by_alias=True))
        case 'teacher':
            teacher = TeacherModel(**user_data)
            res = users.insert_one(teacher.model_dump(by_alias=True))
        case _:
            raise ValueError

    logger.info(f"Пользователь создан -> {tg_id} ({role})")
    return res.inserted_id
