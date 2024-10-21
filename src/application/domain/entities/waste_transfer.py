from src.application.domain.entities.base import Entity
from src.application.domain.value_objects.date import Date
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.core.decorators.validate_types import validate_types
from src.core.objects.sealed import Sealed


class WasteTransferEntity(Sealed, Entity):

    @validate_types
    def __init__(
            self,
            id: ID = None,
            organization_id: ID = None,
            storage_id: ID = None,
            waste_type_id: ID = None,
            quantity: Quantity = None,
            organization_name: Name = None,
            storage_name: Name = None,
            waste_type_name: Name = None,
            created_at: Date = None
    ):
        self._id = id
        self._organization_id = organization_id
        self._storage_id = storage_id
        self._waste_type_id = waste_type_id
        self._quantity = quantity
        self._organization_name = organization_name
        self._storage_name = storage_name
        self._waste_type_name = waste_type_name
        self._created_at = created_at

    @property
    def id(self):
        return self._id

    @property
    def organization_id(self):
        return self._organization_id

    @property
    def storage_id(self):
        return self._storage_id

    @property
    def waste_type_id(self):
        return self._waste_type_id

    @property
    def quantity(self):
        return self._quantity

    @property
    def organization_name(self):
        return self._organization_name

    @property
    def storage_name(self):
        return self._storage_name

    @property
    def waste_type_name(self):
        return self._waste_type_name

    @property
    def created_at(self):
        return self._created_at
