from abc import ABC, abstractmethod
from typing_extensions import Self
from src.core.objects.immutable import Immutable
from src.core.objects.serializable import Serializable


class ValueObject[T](Serializable, Immutable, ABC):
    """Base class for value objects"""
    def __init__(self, value: T):
        self._value = value
        super().__init__()
        self._validate_type()
        self._validate_fields()

    @property
    def value(self) -> T:
        return self._value

    @abstractmethod
    def _validate_fields(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _validate_type(self) -> None:
        raise NotImplementedError

    def __eq__(self, other: Self) -> bool:
        return self.value == other.value

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(frozenset(self.__dict__.items()))

    def __str__(self) -> str:
        return str(self.value)
