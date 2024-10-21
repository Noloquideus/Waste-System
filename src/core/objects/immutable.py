from abc import ABC
from src.core.exceptions.base import SystemException


class Immutable(ABC):
    """
    Base class for immutable objects.

    Once the object is initialized, any attempt to modify its attributes
    will raise an exception. This ensures that the object remains in a
    consistent state after creation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the Immutable object. Sets the '_frozen' flag to False initially,
        allowing attribute setting during initialization. After initialization,
        the '_frozen' flag is set to True, making the object immutable.
        """
        self._frozen = False
        super().__init__(*args, **kwargs)
        self._frozen = True

    def __setattr__(self, key, value):
        """
        Prevents modification of attributes once the '_frozen' flag is set to True.
        Raises:
            SystemException: If an attempt is made to modify an immutable attribute.
        """
        if getattr(self, '_frozen', False):
            raise SystemException(f"Cannot modify immutable attribute '{key}'")
        super().__setattr__(key, value)
