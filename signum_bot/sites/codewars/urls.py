GET_USER = 'https://www.codewars.com/api/v1/users/{user}'
LIST_COMPLETED_CHALLENGES = 'https://www.codewars.com/api/v1/users/{user}/code-challenges/completed?page={page}'


def user_url(username: str) -> str:
    return GET_USER.replace('{user}', username)
