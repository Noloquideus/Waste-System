from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.base import ValueObject


class ID(ValueObject[str]):

    def _validate_type(self) -> None:
        if not isinstance(self._value, str):
            raise ValidationException(f'ID must be a string, {type(self._value)} given')

    def _validate_fields(self) -> None:
        pass
