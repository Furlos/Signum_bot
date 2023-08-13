from signum_bot.services.users import *
from signum_bot.database.crud import *


def codewars_statistic(tg_id: int) -> Dict:
    user = User.get(tg_id)
    return user.get_codewars_stat()


def create_user(tg_id: int, name: str, father_name: str, nicknames: dict, role: str, last_name: str = None) -> None:
    user_data = {
        '_id': tg_id,
        'name': name,
        'last_name': last_name,
        'father_name': father_name,
        'nicknames': nicknames
    }

    logger.info(f"Проверка роли, создаваемого пользователя -> {tg_id}")
    match role.lower():
        case 'student':
            Student(**user_data).create()
            logger.info(f"Студент создан -> {tg_id}")
        case 'teacher':
            Teacher(**user_data).create()
            logger.info(f"Учитель создан -> {tg_id}")
        case _:
            raise ValueError


def create_student(tg_id: int, name: str, father_name: str, nicknames: dict, last_name: str = None) -> None:
    create_user(tg_id, name, father_name, nicknames, 'student', last_name)


def create_teacher(tg_id: int, name: str, father_name: str, nicknames: dict, last_name: str = None) -> None:
    create_user(tg_id, name, father_name, nicknames, 'teacher', last_name)
