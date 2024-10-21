from abc import ABC
from src.core.exceptions.base import SystemException


class Incomparable(ABC):
    """
    Base class for objects that cannot be compared.

    Any attempt to perform comparison or hashing operations will raise an exception.
    This is useful for objects where comparison logic does not make sense.
    """

    def __eq__(self, other):
        """Raises an exception when trying to check equality."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __ne__(self, other):
        """Raises an exception when trying to check inequality."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __lt__(self, other):
        """Raises an exception when trying to check if less than."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __le__(self, other):
        """Raises an exception when trying to check if less than or equal."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __gt__(self, other):
        """Raises an exception when trying to check if greater than."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __ge__(self, other):
        """Raises an exception when trying to check if greater than or equal."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __hash__(self):
        """Raises an exception when trying to hash the object."""
        raise SystemException(f'{self.__class__.__name__} objects cannot be hashed')
