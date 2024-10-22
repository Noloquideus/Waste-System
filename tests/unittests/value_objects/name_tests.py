import pytest
from src.application.domain.exceptions.exceptions import ValidationException
from src.application.domain.value_objects.name import Name
from src.core.exceptions.base import SystemException


def test_valid_name():
    name = Name("Valid_Name")
    assert name.value == "Valid_Name"


def test_empty_name():
    with pytest.raises(ValueError, match="Username cannot be empty"):
        Name("")


def test_name_with_spaces():
    with pytest.raises(ValidationException, match="Username cannot contain spaces"):
        Name("Invalid Name")


def test_name_with_leading_trailing_spaces():
    with pytest.raises(ValidationException, match="Username cannot contain leading or trailing spaces"):
        Name("  Invalid ")


def test_name_too_short():
    with pytest.raises(ValidationException, match="Username must be at least 3 characters long"):
        Name("AB")


def test_name_too_long():
    long_name = "A" * 51
    with pytest.raises(ValidationException, match="Username must be at most 50 characters long"):
        Name(long_name)


def test_name_immutability():
    name_obj = Name("test_user")

    with pytest.raises(SystemException, match="Cannot modify immutable attribute '_value'"):
        name_obj._value = "new_user"
