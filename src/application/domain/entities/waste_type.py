from src.application.domain.entities.base import Entity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.core.decorators.validate_types import validate_types
from src.core.objects.sealed import Sealed


class WasteTypeEntity(Sealed, Entity):

    @validate_types
    def __init__(
            self,
            id: ID = None,
            name: Name = None,
    ):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
