import re
from src.application.domain.exceptions.exceptions import ValidationException
from src.settings import SETTINGS
from src.application.domain.value_objects.base import ValueObject


class Name(ValueObject[str]):

    def _validate_type(self) -> None:
        if not isinstance(self.value, str):
            raise ValidationException('Username must be a string')

    def _validate_fields(self) -> None:
        if not self.value:
            raise ValueError('Username cannot be empty')
        if len(self.value) != len(self.value.strip()):
            raise ValidationException(message='Username cannot contain leading or trailing spaces')
        if ' ' in self.value:
            raise ValidationException(message='Username cannot contain spaces')
        if len(self.value) < SETTINGS.MIN_LENGTH_NAME.value:
            raise ValidationException(message='Username must be at least 3 characters long')
        if len(self.value) > SETTINGS.MAX_LENGTH_NAME.value:
            raise ValidationException(message='Username must be at most 50 characters long')
        if not re.match(pattern=SETTINGS.NAME_PATTERN, string=self.value):
            raise ValidationException(message='Username must be alphanumeric and can include "-" and "_"')
