from src.application.domain.exceptions.exceptions import ValidationException
from src.core.decorators.validate_types import validate_types


class Collector:
    def __init__(self):
        self.data_storage = []
        self.capacity = 1

    def __validate_types(self):

        if not isinstance(self.data_storage, list):
            raise ValidationException('data must be a list')

        if not isinstance(self.capacity, int):
            raise ValidationException('capacity must be an integer')

    def __validate_capacity(self):
        if 0 >= self.capacity:
            raise ValidationException('capacity must be greater than 0')

    def __validate_data(self):
        if len(self.data_storage) > self.capacity:
            raise ValidationException(f'data must be between 0 and {self.capacity}')

    @validate_types
    def collect(self, data: str):
        self.data_storage.append(data)
        self.__validate_data()

    def clear_data(self):
        self.data_storage.clear()

    def interesting_volume(self):
        return len(self.data_storage)

    def serialize_to_string(self):
        total_string = ''
        for i in range(len(self.data_storage)):
            intermediate_string = self.data_storage[i] + '\n'
            total_string += intermediate_string
        return total_string

    def unload(self):
        data = self.serialize_to_string()
        self.clear_data()
        return data
