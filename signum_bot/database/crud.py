from loguru import logger

from signum_bot.services.users import *


def get_user(tg_id: int):
    return users.find_one({'_id': tg_id})
