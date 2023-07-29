import requests

from signum_bot.sites.codewars.urls import *
from signum_bot.sites.codewars import CodeWarsUserInfo
from signum_bot.sites.codewars.exceptions import check_response_status_code


def get_codewars_user(username: str) -> CodeWarsUserInfo:
    response = requests.get(user_url(username))
    check_response_status_code(response.status_code)
    response = response.json()
    return CodeWarsUserInfo(username=response['username'],
                            honor=response['honor'],
                            languages=response['ranks']['languages'],
                            total_completed=response['codeChallenges']['totalCompleted'])
