from pymongo.errors import DuplicateKeyError


class NotFoundUserError(Exception):
    def __init__(self):
        self.message = "Not Found User -- The specified user could not be found"
        super().__init__(self.message)


class UserExistsError(DuplicateKeyError): ...
