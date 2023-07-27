from signum_bot.sites.codewars.api import get_codewars_user


# Todo posmotret chto takoe iskluchenie v pythone.
# Todo posmotret kak delat svoi usklucheniya

class Error400(Exception):
    def __init__(self):
        self.txt = "Bad Request -- Something went wrong"


class Error401(Exception):
    def __init__(self):
        self.txt = "Unauthorized -- Your API key is wrong"


class Error403(Exception):
    def __init__(self):
        self.txt = " Forbidden -- You do not have permission to access this resource"


class Error404(Exception):
    def __init__(self):
        self.txt = "Not Found -- The specified resource could not be found"


class Error405(Exception):
    def __init__(self):
        self.txt = "Method Not Allowed -- You tried to access a resource with an invalid method"


class Error406(Exception):
    def __init__(self):
        self.txt = "Not Acceptable -- You requested a format that isn't json"


class Error422(Exception):
    def __init__(self):
        self.txt = "Unprocessable Entity -- Your input failed validation."


class Error429(Exception):
    def __init__(self):
        self.txt = "Too Many Requests -- You're making too many API requests."


class Error500(Exception):
    def __init__(self):
        self.txt = "Internal Server Error -- We had a problem with our server. Try again later."


class Error503(Exception):
    def __init__(self):
        self.txt = "Service Unavailable -- We're temporarily offline for maintenance. Please try again later."


def check_response_status_code(status_code: int) -> None:
    # TODO: написать документацию к функции(что она делает)

    # Check the response status code and raise an exception if it indicates an error.
    # This function is used to validate the HTTP status code received in response to a web request. It helps to ensure
    # that the request was successful and that the server responded with the expected status code.

    match status_code:
        case 400:
            raise Error400
        case 401:
            raise Error401
        case 403:
            raise Error403
        case 404:
            raise Error404
        case 405:
            raise Error405
        case 406:
            raise Error406
        case 422:
            raise Error422
        case 429:
            raise Error429
        case 500:
            raise Error500
        case 503:
            raise Error503
