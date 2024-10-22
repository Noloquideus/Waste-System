from abc import ABC
from src.core.objects.immutable import Immutable
from src.core.objects.serializable import Serializable


class Entity(Serializable, Immutable, ABC):
    """Base class for entities"""
    pass
