"""
400     Bad Request -- Something went wrong
401     Unauthorized -- Your API key is wrong
403     Forbidden -- You do not have permission to access this resource
404     Not Found -- The specified resource could not be found
405     Method Not Allowed -- You tried to access a resource with an invalid method
406     Not Acceptable -- You requested a format that isn't json
422     Unprocessable Entity -- Your input failed validation.
429     Too Many Requests -- You're making too many API requests.
500     Internal Server Error -- We had a problem with our server. Try again later.
503     Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
"""
from signum_bot.sites.codewars.api import get_codewars_user


# Todo posmotret chto takoe iskluchenie v pythone.
# Todo posmotret kak delat svoi usklucheniya

class Error400(Exception):
    def __init__(self):
        self.txt = "Bad Request -- Something went wrong"


def check_response_status_code(status_code: int) -> None:
    #TODO: написать документацию к функции(что она делает)
    match status_code:
        case 400:
            raise Error400
