"""
400 	Bad Request -- Something went wrong
401 	Unauthorized -- Your API key is wrong
403 	Forbidden -- You do not have permission to access this resource
404 	Not Found -- The specified resource could not be found
405 	Method Not Allowed -- You tried to access a resource with an invalid method
406 	Not Acceptable -- You requested a format that isn't json
422 	Unprocessable Entity -- Your input failed validation.
429 	Too Many Requests -- You're making too many API requests.
500 	Internal Server Error -- We had a problem with our server. Try again later.
503 	Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
"""

import requests

from signum_bot.api.codewars.urls import *
from signum_bot.api.codewars.user import User


def user_url(username: str) -> str:
    return GET_USER.replace('{user}', username)


def get_user(username: str) -> User:
    # TODO: посмотреть как обрабатывать коды ошибок HTTP
    user = requests.get(user_url(username))
    if user.status_code >= 400:
        return User()
    user = user.json()
    return User(username=user['username'],
                honor=user['honor'],
                languages=user['ranks']['languages'],
                total_completed=user['codeChallenges']['totalCompleted'])
