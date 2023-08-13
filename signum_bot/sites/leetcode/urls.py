"""
Thanks https://github.com/JeremyTsaii/leetcode-stats-api/graphs/contributors
Using their project: https://github.com/JeremyTsaii/leetcode-stats-api
"""

URL = "https://leetcode-stats-api.herokuapp.com/user"


def get_user_url(nickname: str):
    return URL.replace('user', nickname)
