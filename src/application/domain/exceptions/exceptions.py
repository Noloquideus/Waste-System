from src.application.domain.exceptions.base import ApplicationException
from src.core.enums.status_code import StatusCode
from src.core.objects.sealed import Sealed


class ValidationException(Sealed, ApplicationException):
    def __init__(self, status_code: StatusCode = StatusCode.BAD_REQUEST.value, message: str = 'Validation error'):
        super().__init__(status_code=status_code, message=message)
