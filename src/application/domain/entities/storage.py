from src.application.domain.entities.base import Entity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.core.decorators.validate_types import validate_types
from src.core.objects.sealed import Sealed


class StorageEntity(Sealed, Entity):

    @validate_types
    def __init__(
            self,
            id: ID = None,
            name: Name = None,
            biowaste: Quantity = None,
            plastic: Quantity = None,
            glass: Quantity = None,
            biowaste_capacity: Quantity = None,
            plastic_capacity: Quantity = None,
            glass_capacity: Quantity = None,
            biowaste_remaining: Quantity = None,
            plastic_remaining: Quantity = None,
            glass_remaining: Quantity = None
    ):
        self._id = id
        self._name = name
        self._biowaste = biowaste
        self._plastic = plastic
        self._glass = glass
        self._biowaste_capacity = biowaste_capacity
        self._plastic_capacity = plastic_capacity
        self._glass_capacity = glass_capacity
        self._biowaste_remaining = biowaste_remaining
        self._plastic_remaining = plastic_remaining
        self._glass_remaining = glass_remaining
        super().__init__()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def biowaste(self):
        return self._biowaste

    @property
    def plastic(self):
        return self._plastic

    @property
    def glass(self):
        return self._glass

    @property
    def biowaste_capacity(self):
        return self._biowaste_capacity

    @property
    def plastic_capacity(self):
        return self._plastic_capacity

    @property
    def glass_capacity(self):
        return self._glass_capacity

    @property
    def biowaste_remaining(self):
        return self._biowaste_remaining

    @property
    def plastic_remaining(self):
        return self._plastic_remaining

    @property
    def glass_remaining(self):
        return self._glass_remaining
