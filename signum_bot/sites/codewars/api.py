import requests

from loguru import logger

from signum_bot.sites.codewars.urls import *
from signum_bot.sites.codewars.user import CodeWarsUserInfo
from signum_bot.sites.codewars.exceptions import check_response_status_code


def get_codewars_user(nickname: str) -> CodeWarsUserInfo:
    logger.debug(f'Отправка запроса для получение данных пользователя {nickname} с сайта codewars')
    response = requests.get(user_url(nickname))
    logger.debug('Проверка статуса ответа')
    check_response_status_code(response.status_code)
    response = response.json()
    logger.debug(f'успешное получение данных пользователя {nickname} с сайта codewars')
    return CodeWarsUserInfo(username=response['username'],
                            honor=response['honor'],
                            languages=response['ranks']['languages'],
                            total_completed=response['codeChallenges']['totalCompleted'])
