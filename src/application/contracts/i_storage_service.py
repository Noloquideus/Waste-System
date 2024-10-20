from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.repositories.i_storage_repository import IStorageRepository
from src.application.contracts.base import Service
from src.application.domain.entities.storage import StorageEntity


class IStorageService(Service, ABC):

    def __init__(self, repository: IStorageRepository):
        self._repository = repository

    @abstractmethod
    async def create(self, name: str, biowaste_capacity: int, plastic_capacity: int, glass_capacity: int) -> StorageEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[StorageEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, storage_id: str) -> StorageEntity:
        raise NotImplementedError

    @abstractmethod
    async def update(self, storage_id: str, name: str, biowaste_capacity: int, plastic_capacity: int, glass_capacity: int) -> StorageEntity:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, storage_id: str):
        raise NotImplementedError
