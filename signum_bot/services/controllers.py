from signum_bot.services.users import *
from signum_bot.database.crud import create_user


def codewars_statistic(tg_id: int) -> Dict:
    user = User.get(tg_id)
    return user.get_codewars_stat()


def create_student(tg_id: int, name: str, father_name: str, nicknames: dict, last_name: str = None) -> int:
    return create_user(tg_id, name, father_name, nicknames, 'student', last_name)


def create_teacher(tg_id: int, name: str, father_name: str, nicknames: dict, last_name: str = None) -> int:
    return create_user(tg_id, name, father_name, nicknames, 'teacher', last_name)
