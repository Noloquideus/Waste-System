import inspect
from functools import wraps
from src.core.exceptions.base import SystemException

def validate_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        parameters = signature.parameters

        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        for name, value in bound_arguments.arguments.items():
            if name in parameters and parameters[name].annotation != inspect.Parameter.empty:
                expected_type = parameters[name].annotation
                if value is not None and not isinstance(value, expected_type):
                    raise SystemException(
                        f"Argument '{name}' must be of type {expected_type.__name__}, "
                        f"but got '{type(value).__name__ if value is not None else 'None'}'"
                    )

        return func(*args, **kwargs)

    return wrapper
