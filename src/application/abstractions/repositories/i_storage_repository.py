from abc import ABC, abstractmethod
from typing import List

from src.application.abstractions.repositories.base import Repository
from src.application.domain.entities.storage import StorageEntity


class IStorageRepository(Repository, ABC):

    @abstractmethod
    async def create(self, storage_entity: StorageEntity) -> StorageEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[StorageEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, storage_entity: StorageEntity) -> StorageEntity:
        raise NotImplementedError
