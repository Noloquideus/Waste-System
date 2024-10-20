from abc import ABC, abstractmethod
from typing import Union
from src.application.abstractions.daos.base import Dao
from src.application.domain.entities.storage import StorageEntity
from src.infrastructure.database.models import Storage


class IStorageDao(Dao, ABC):

    @abstractmethod
    async def create(self, storage_entity: StorageEntity) -> Storage:
        raise NotImplementedError

    @abstractmethod
    async def _get_by_name(self, name: str) -> Union[Storage, None]:
        raise NotImplementedError
