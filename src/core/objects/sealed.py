from src.core.exceptions.base import SystemException


class Sealed:
    _is_sealed = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__bases__[0]._is_sealed:
            raise SystemException(f"The class '{cls.__bases__[0].__name__}' cannot be inherited since it is sealed")
        cls._is_sealed = True
