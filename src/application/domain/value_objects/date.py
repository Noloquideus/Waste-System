from datetime import datetime
from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.base import ValueObject


class Date(ValueObject[datetime]):
    def __init__(self, value: datetime):
        super().__init__(value)

    def _validate_type(self) -> None:
        if not isinstance(self.value, datetime):
            raise ValidationException(f"Value must be of type 'datetime', got {type(self.value).__name__}")

    def _validate_fields(self) -> None:
        if self.value is None:
            raise ValidationException('Date value cannot be None')

    @classmethod
    def now(cls) -> 'Date':
        """Creates a Date object with the current datetime."""
        return cls(datetime.now())

    def __str__(self) -> str:
        return self.value.isoformat()
