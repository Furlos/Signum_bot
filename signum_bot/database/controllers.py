from typing import Any
from loguru import logger

from signum_bot.database.models import *
from signum_bot.database.exceptions import *


def codewars_statistic(tg_id: int) -> Dict:
    try:
        user = UserModel.get(tg_id)
        return user.get_codewars_stat()
    except NotFoundUserError as e:
        logger.info(f'Попытка получить статистику не существующего пользователя {tg_id}')
        logger.info(f'{e}')
        return dict()


def create_student(student_data: dict[str, Any]) -> bool:
    """
    student_data:
        '_id': tg_id,\n
        'name': ...,\n
        'last_name': ...,\n
        'father_name': ...,\n
        'nicknames': {
            'codewars': ...,\n
            'leetcode': ...\n
        }
    """
    try:
        Student(**student_data).create()
        return True
    except UserExistsError:
        logger.info(f'Не получилось создать пользователя -> {student_data["_id"]}, так как уже существует')
        return False


def create_teacher(teacher_data: dict[str, Any]) -> bool:
    """
    teacher_data:
        '_id': tg_id,\n
        'name': ...,\n
        'last_name': ...,\n
        'father_name': ...,\n
        'nicknames': {
            'codewars': ...,\n
            'leetcode': ...\n
        }
    """
    try:
        Teacher(**teacher_data).create()
        return True
    except UserExistsError:
        logger.info(f'Не получилось создать пользователя -> {teacher_data["_id"]}, так как уже существует')
        return False
