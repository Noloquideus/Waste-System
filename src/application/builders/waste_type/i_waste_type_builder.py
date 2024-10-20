from abc import ABC, abstractmethod
from src.application.abstractions.repositories.i_waste_type_repository import IWasteTypeRepository
from src.application.builders.base import Builder


class IWasteTypeBuilder(Builder, ABC):

    @abstractmethod
    def set_repository(self, repository: IWasteTypeRepository) -> 'IWasteTypeBuilder':
        """Set the repository dependency."""
        raise NotImplementedError
