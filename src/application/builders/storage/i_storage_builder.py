from abc import ABC, abstractmethod
from src.application.abstractions.repositories.i_storage_repository import IStorageRepository
from src.application.builders.base import Builder


class IStorageBuilder(Builder, ABC):

    @abstractmethod
    def set_repository(self, repository: IStorageRepository) -> 'IStorageBuilder':
        """Set the repository dependency."""
        raise NotImplementedError
