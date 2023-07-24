import requests

from signum_bot.sites.codewars.urls import *
from signum_bot.sites.codewars import CodeWarsUser
from sites.codewars.exceptions import check_response_status_code


def get_codewars_user(username: str) -> CodeWarsUser:
    response = requests.get(user_url(username))
    check_response_status_code(response.status_code)
    response = response.json()
    return CodeWarsUser(username=response['username'],
                        honor=response['honor'],
                        languages=response['ranks']['languages'],
                        total_completed=response['codeChallenges']['totalCompleted'])
