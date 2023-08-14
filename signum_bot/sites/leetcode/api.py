from typing import Dict

import requests

from signum_bot.sites.leetcode.urls import get_user_url
from signum_bot.sites.leetcode.exceptions import ServerError, UserNotFoundError


def get_leetcode_user(nickname: str) -> Dict:
    #TODO: изучить работу через cookies
    response = requests.get(get_user_url(nickname))

    if response.status_code != 200:
        raise ServerError

    response = response.json()

    if response['status'] == 'error':
        raise UserNotFoundError(response['message'])

    return response
