import pytest
from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.quantity import Quantity
from src.core.exceptions.base import SystemException


def test_valid_quantity():
    quantity = Quantity(10)
    assert quantity.value == 10


def test_negative_quantity():
    with pytest.raises(ValidationException, match="Quantity must be non-negative"):
        Quantity(-5)


def test_invalid_quantity_type():
    with pytest.raises(ValidationException, match="Quantity must be an integer"):
        Quantity("10")


def test_quantity_immutability():
    quantity_obj = Quantity(10)

    with pytest.raises(SystemException, match="Cannot modify immutable attribute '_value'"):
        quantity_obj._value = 20