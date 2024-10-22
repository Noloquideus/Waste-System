import pytest
from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.id import ID
from src.core.exceptions.base import SystemException


def test_id_creation():
    id_value = "12345"
    id_obj = ID(id_value)
    assert id_obj.value == id_value


def test_invalid_id_type():
    with pytest.raises(ValidationException, match="ID must be a string"):
        ID(12345)


def test_id_immutability():
    id_obj = ID("12345")

    with pytest.raises(SystemException, match="Cannot modify immutable attribute '_value'"):
        id_obj._value = "67890"
