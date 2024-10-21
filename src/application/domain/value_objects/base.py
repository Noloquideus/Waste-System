from abc import ABC, abstractmethod
from typing_extensions import Self
from src.core.objects.immutable import Immutable
from src.core.objects.serializable import Serializable


class ValueObject[T](Serializable, Immutable, ABC):
    """
    Base class for value objects.

    A value object represents an immutable and comparable object with a
    specific value. Value objects are used when object identity is
    determined by its properties rather than a unique identifier.

    This class provides type validation, value validation, and immutability
    features, and it can be easily converted to a dictionary or JSON format
    through inheritance from the `Serializable` class.

    Args:
        value (T): The value to be encapsulated by the value object.

    Raises:
        SystemException: If the object is modified after being frozen.
        NotImplementedError: If `_validate_fields` or `_validate_type` are not implemented in a derived class.
    """

    def __init__(self, value: T):
        """
        Initializes the ValueObject with a specified value.
        Performs type and field validation during initialization.

        Args:
            value (T): The value to initialize the value object with.
        """
        self._value = value
        super().__init__()
        self._validate_type()
        self._validate_fields()

    @property
    def value(self) -> T:
        """
        Returns the encapsulated value.

        Returns:
            T: The value stored in the value object.
        """
        return self._value

    @abstractmethod
    def _validate_fields(self) -> None:
        """
        Validates the fields of the value object. Must be implemented in subclasses.

        Raises:
            NotImplementedError: If not overridden in a derived class.
        """
        raise NotImplementedError

    @abstractmethod
    def _validate_type(self) -> None:
        """
        Validates the type of the value. Must be implemented in subclasses.

        Raises:
            NotImplementedError: If not overridden in a derived class.
        """
        raise NotImplementedError

    def __eq__(self, other: Self) -> bool:
        """
        Compares two ValueObject instances for equality based on their values.

        Args:
            other (Self): The other ValueObject instance to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.value == other.value

    def __ne__(self, other) -> bool:
        """
        Compares two ValueObject instances for inequality.

        Args:
            other (Self): The other ValueObject instance to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """
        Returns the hash of the ValueObject based on its attributes.

        Returns:
            int: The hash value of the object.
        """
        return hash(frozenset(self.__dict__.items()))

    def __str__(self) -> str:
        """
        Returns the string representation of the encapsulated value.

        Returns:
            str: The string representation of the value.
        """
        return str(self.value)