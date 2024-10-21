from abc import abstractmethod, ABC
from src.application.abstractions.repositories.i_waste_transfer_repository import IWasteTransferRepository
from src.application.builders.base import Builder


class IWasteTransferBuilder(Builder, ABC):

    @abstractmethod
    def set_repository(self, repository: IWasteTransferRepository) -> 'IWasteTransferBuilder':
        """Set the repository dependency."""
        raise NotImplementedError
