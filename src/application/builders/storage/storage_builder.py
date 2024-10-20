from src.application.abstractions.repositories.i_storage_repository import IStorageRepository
from src.application.builders.storage.i_storage_builder import IStorageBuilder
from src.application.contracts.i_storage_service import IStorageService
from src.application.services.storage_service import StorageService


class StorageBuilder(IStorageBuilder):

    def __init__(self):
        self._repository = None

    def set_repository(self, repository: IStorageRepository) -> 'StorageBuilder':
        self._repository = repository
        return self

    def build(self) -> IStorageService:
        if not self._repository:
            raise ValueError('Repository must be set before building the service.')

        return StorageService(self._repository)