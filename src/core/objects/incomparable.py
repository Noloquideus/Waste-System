from abc import ABC
from src.core.exceptions.base import SystemException


class Incomparable(ABC):
    def __eq__(self, other):
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __ne__(self, other):
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __lt__(self, other):
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __le__(self, other):
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __gt__(self, other):
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __ge__(self, other):
        raise SystemException(f'{self.__class__.__name__} objects cannot be compared')

    def __hash__(self):
        raise SystemException(f'{self.__class__.__name__} objects cannot be hashed')
