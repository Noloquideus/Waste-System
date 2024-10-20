from abc import ABC, abstractmethod
from src.application.abstractions.repositories.base import Repository
from src.application.domain.entities.storage import StorageEntity


class IStorageRepository(Repository, ABC):

    @abstractmethod
    async def create(self, storage_entity: StorageEntity) -> StorageEntity:
        raise NotImplementedError
