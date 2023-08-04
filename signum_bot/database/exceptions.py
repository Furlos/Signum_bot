class NotFoundUserError(Exception):
    def __init__(self):
        self.message = "Not Found User -- The specified user could not be found"
        super().__init__(self.message)


class UserExistsError(Exception):
    def __init__(self):
        self.message = "The User Exists -- The specified user already exists"
        super().__init__(self.message)
