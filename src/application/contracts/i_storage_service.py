from abc import ABC, abstractmethod
from src.application.abstractions.repositories.i_storage_repository import IStorageRepository
from src.application.contracts.base import Service
from src.application.domain.entities.storage import StorageEntity


class IStorageService(Service, ABC):

    def __init__(self, repository: IStorageRepository):
        self._repository = repository

    @abstractmethod
    async def create(self, name: str, biowaste_capacity: str, plastic_capacity: str, glass_capacity: str) -> StorageEntity:
        raise NotImplementedError
