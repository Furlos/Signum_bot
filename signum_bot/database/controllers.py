from typing import Any

from signum_bot.database.models import *


def codewars_statistic(tg_id: int) -> Dict:
    user = UserModel.get(tg_id)
    return user.get_codewars_stat()


def create_student(student_data: dict[str, Any]) -> bool:
    """
    student_data:
        '_id': tg_id,\n
        'name': ...,\n
        'last_name': ...,\n
        'father_name': ...,\n
        'teacher_id': ...,\n
        'nicknames': {
            'codewars': ...,\n
            'leetcode': ...\n
        }
    """
    return Student(**student_data).create()


def create_teacher(teacher_data: dict[str, Any]) -> bool:
    """
    teacher_data:
        '_id': tg_id,\n
        'name': ...,\n
        'last_name': ...,\n
        'father_name': ...,\n
        'teacher_id': ...,\n
        'nicknames': {
            'codewars': ...,\n
            'leetcode': ...\n
        }
    """
    return Teacher(**teacher_data).create()
