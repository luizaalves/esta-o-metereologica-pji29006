class BaseError():
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
    
    def __repr__(self):
        return '{"code":"%s", "message":"%s"}' % (str(self.code), self.message)

class NotFoundError(BaseError):
    def __init__(self, description: str):
        super().__init__(404, "NOT FOUND")
        self.description = description

class BadRequestError(BaseError):
    def __init__(self, description: str):
        super().__init__(400, "BAD REQUEST")
        self.description = description

class ConflictError(BaseError):
    def __init__(self, description: str):
        super().__init__(409, "CONFLICT")
        self.description = description

class InternalServerError(BaseError):
    def __init__(self, description: str):
        super().__init__(500, "INTERNAL SERVER ERROR")
        self.description = description