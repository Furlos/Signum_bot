from loguru import logger


class BadRequestError(Exception):
    def __init__(self):
        self.message = "Bad Request -- Something went wrong"
        super().__init__(self.message)


class UnauthorizedError(Exception):
    def __init__(self):
        self.message = "Unauthorized -- Your API key is wrong"
        super().__init__(self.message)


class ForbiddenError(Exception):
    def __init__(self):
        self.message = " Forbidden -- You do not have permission to access this resource"
        super().__init__(self.message)


class NotFoundError(Exception):
    def __init__(self):
        self.message = "Not Found -- The specified resource could not be found"
        super().__init__(self.message)


class MethodNotAllowedError(Exception):
    def __init__(self):
        self.message = "Method Not Allowed -- You tried to access a resource with an invalid method"
        super().__init__(self.message)


class NotAcceptableError(Exception):
    def __init__(self):
        self.message = "Not Acceptable -- You requested a format that isn't json"
        super().__init__(self.message)


class UnprocessableEntityError(Exception):
    def __init__(self):
        self.message = "Unprocessable Entity -- Your input failed validation."
        super().__init__(self.message)


class TooManyRequestsError(Exception):
    def __init__(self):
        self.message = "Too Many Requests -- You're making too many API requests."
        super().__init__(self.message)


class InternalServerError(Exception):
    def __init__(self):
        self.message = "Internal Server Error -- We had a problem with our server. Try again later."
        super().__init__(self.message)


class ServiceUnavailableError(Exception):
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
            logger.error(f'CodeWars response -> status {status_code} (BadRequestError)')
            raise BadRequestError
        case 401:
            logger.error(f'CodeWars response -> status {status_code} (UnauthorizedError)')
            raise UnauthorizedError
        case 403:
            logger.error(f'CodeWars response -> status {status_code} (ForbiddenError)')
            raise ForbiddenError
        case 404:
            logger.error(f'CodeWars response -> status {status_code} (NotFoundError)')
            raise NotFoundError
        case 405:
            logger.error(f'CodeWars response -> status {status_code} (MethodNotAllowedError)')
            raise MethodNotAllowedError
        case 406:
            logger.error(f'CodeWars response -> status {status_code} (NotAcceptableError)')
            raise NotAcceptableError
        case 422:
            logger.error(f'CodeWars response -> status {status_code} (UnprocessableEntityError)')
            raise UnprocessableEntityError
        case 429:
            logger.error(f'CodeWars response -> status {status_code} (TooManyRequestsError)')
            raise TooManyRequestsError
        case 500:
            logger.error(f'CodeWars response -> status {status_code} (InternalServerError)')
            raise InternalServerError
        case 503:
            logger.error(f'CodeWars response -> status {status_code} (ServiceUnavailableError)')
            raise ServiceUnavailableError
