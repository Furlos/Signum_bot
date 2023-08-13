from typing import Dict

import requests

from signum_bot.sites.leetcode.urls import get_user_url


def get_leetcode_user(nickname: str) -> Dict:
    return requests.get(get_user_url(nickname)).json()
