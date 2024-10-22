from datetime import datetime
import pytest
from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.date import Date
from src.core.exceptions.base import SystemException


def test_date_creation():
    date = Date(datetime(2023, 1, 1))
    assert isinstance(date.value, datetime)
    assert date.value.year == 2023


def test_date_now():
    date = Date.now()
    assert isinstance(date.value, datetime)


def test_invalid_date_type():
    with pytest.raises(ValidationException, match="Value must be of type 'datetime'"):
        Date("2023-01-01")


def test_date_immutability():
    date_obj = Date(datetime.now())

    with pytest.raises(SystemException, match="Cannot modify immutable attribute '_value'"):
        date_obj._value = datetime.now()
