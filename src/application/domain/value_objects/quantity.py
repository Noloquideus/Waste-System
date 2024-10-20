from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.base import ValueObject


class Quantity(ValueObject[int]):

    def _validate_type(self) -> None:
        if not isinstance(self._value, int):
            raise ValidationException(f'Quantity must be an integer, {type(self._value)} given')

    def _validate_fields(self) -> None:
        if self._value < 0:
            raise ValidationException(f'Quantity must be non-negative, {self._value} given')