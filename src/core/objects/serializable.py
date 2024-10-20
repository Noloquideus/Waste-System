import json
from abc import ABC


class Serializable(ABC):

    def to_dict(self):
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
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.to_dict().items())
        return f'{attributes}'

    def __repr__(self):
        attributes = ", ".join(f"{key}={str(getattr(self, key))}" for key in dir(self)
                               if not key.startswith('_') and not callable(getattr(self, key)))
        return f'{self.__class__.__name__}({attributes})'
