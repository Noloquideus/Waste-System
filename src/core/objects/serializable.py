import json
from abc import ABC


class Serializable(ABC):
    """
    Base class for serializable objects.

    Provides methods to convert an object's attributes into a dictionary or JSON
    format. This is useful for logging, debugging, or data persistence.
    """

    def to_dict(self):
        """
        Converts the object's attributes into a dictionary format.

        Attributes that start with an underscore or are callable are ignored.
        If an attribute is another Serializable object, it will be recursively
        converted to a dictionary or its value representation if available.

        Returns:
            dict: A dictionary representation of the object's attributes.
        """
        result = {}
        for attr_name in dir(self):
            if not attr_name.startswith('_') and not callable(getattr(self, attr_name)):
                attr_value = getattr(self, attr_name)

                if attr_value is None:
                    continue

                # Convert all types to string representation
                if isinstance(attr_value, Serializable):
                    if hasattr(attr_value, 'value'):
                        result[attr_name] = str(attr_value.value)
                    else:
                        result[attr_name] = str(attr_value.to_dict())
                else:
                    result[attr_name] = str(attr_value)
        return result

    def to_json(self):
        """
        Converts the object's attributes into a JSON formatted string.

        Returns:
            str: A JSON representation of the object's attributes.
        """
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        """
        Provides a string representation of the object by listing its attributes.

        Returns:
            str: A string representation of the object's attributes in key=value format.
        """
        attributes = ', '.join(f'{key}={value}' for key, value in self.to_dict().items())
        return f'{attributes}'

    def __repr__(self):
        """
        Provides a detailed string representation of the object, showing the class name
        and its attributes.

        Returns:
            str: A string representation including the class name and attribute values.
        """
        attributes = ", ".join(f"{key}={str(getattr(self, key))}" for key in dir(self)
                               if not key.startswith('_') and not callable(getattr(self, key)))
        return f'{self.__class__.__name__}({attributes})'