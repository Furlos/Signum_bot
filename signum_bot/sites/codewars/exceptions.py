class Error400(Exception):
    def __init__(self):
        self.message = "Bad Request -- Something went wrong"
        super().__init__(self.message)


class Error401(Exception):
    def __init__(self):
        self.message = "Unauthorized -- Your API key is wrong"
        super().__init__(self.message)


class Error403(Exception):
    def __init__(self):
        self.message = " Forbidden -- You do not have permission to access this resource"
        super().__init__(self.message)


class Error404(Exception):
    def __init__(self):
        self.message = "Not Found -- The specified resource could not be found"
        super().__init__(self.message)


class Error405(Exception):
    def __init__(self):
        self.message = "Method Not Allowed -- You tried to access a resource with an invalid method"
        super().__init__(self.message)


class Error406(Exception):
    def __init__(self):
        self.message = "Not Acceptable -- You requested a format that isn't json"
        super().__init__(self.message)


class Error422(Exception):
    def __init__(self):
        self.message = "Unprocessable Entity -- Your input failed validation."
        super().__init__(self.message)


class Error429(Exception):
    def __init__(self):
        self.message = "Too Many Requests -- You're making too many API requests."
        super().__init__(self.message)


class Error500(Exception):
    def __init__(self):
        self.message = "Internal Server Error -- We had a problem with our server. Try again later."
        super().__init__(self.message)


class Error503(Exception):
    def __init__(self):
        self.message = "Service Unavailable -- We're temporarily offline for maintenance. Please try again later."
        super().__init__(self.message)


def check_response_status_code(status_code: int) -> None:
    """
    Check the response status code and raise an exception if it indicates an error.
    This function is used to validate the HTTP status code received in response to a web request.
    """

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
