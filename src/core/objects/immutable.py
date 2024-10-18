from abc import ABC
from src.core.exceptions.base import SystemException


class Immutable(ABC):
    def __init__(self, *args, **kwargs):
        self._frozen = False
        super().__init__(*args, **kwargs)
        self._frozen = True

    def __setattr__(self, key, value):
        if getattr(self, '_frozen', False):
            raise SystemException(f"Cannot modify immutable attribute '{key}'")
        super().__setattr__(key, value)
