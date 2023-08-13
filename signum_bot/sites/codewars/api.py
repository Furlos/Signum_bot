import requests

from loguru import logger

from signum_bot.sites.user_info import CodeWarsUserInfo
from signum_bot.sites.codewars.urls import *
from signum_bot.sites.codewars.exceptions import check_response_status_code

"""
Example of response:

{
  "username": "some_user",
  "name": "Some Person",
  "honor": 544,
  "clan": "some clan",
  "leaderboardPosition": 134,
  "skills": [
    "ruby",
    "c#",
    ".net",
    "javascript",
    "coffeescript",
    "nodejs",
    "rails"
  ],
  "ranks": {
    "overall": {
      "rank": -3,
      "name": "3 kyu",
      "color": "blue",
      "score": 2116
    },
    "languages": {
      "javascript": {
        "rank": -3,
        "name": "3 kyu",
        "color": "blue",
        "score": 1819
      },
      "ruby": {
        "rank": -4,
        "name": "4 kyu",
        "color": "blue",
        "score": 1005
      },
      "coffeescript": {
        "rank": -4,
        "name": "4 kyu",
        "color": "blue",
        "score": 870
      }
    }
  },
  "codeChallenges": {
    "totalAuthored": 3,
    "totalCompleted": 230
  }
}
"""


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
