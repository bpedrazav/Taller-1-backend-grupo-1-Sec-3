import traceback

class APIException(Exception):
    def __init__(self, message: str, code: int = 400, error: str = None):
        self.message = message
        self.code = code
        if error is None:
            tb = traceback.extract_stack()[-2]
            self.error = f"{self.__class__.__name__}: line {tb.lineno} in {tb.filename}"
        else:
            self.error = error
        super().__init__(self.message)

class PetNotFoundException(APIException):
    def __init__(self, line_info: str = "controllers/pet_controller.py"):
        super().__init__(
            message="The requested pet does not exist",
            code=404,
            error=f"PetNotFoundException: line 28 in {line_info}"
        )

class StudentNotFoundException(APIException):
    def __init__(self, line_info: str = "controllers/student_controller.py"):
        super().__init__(
            message="The requested student does not exist",
            code=404,
            error=f"StudentNotFoundException: line 15 in {line_info}"
        )