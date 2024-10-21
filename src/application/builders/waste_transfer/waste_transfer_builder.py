from src.application.abstractions.repositories.i_waste_transfer_repository import IWasteTransferRepository
from src.application.builders.waste_transfer.i_waste_transfer_builder import IWasteTransferBuilder
from src.application.contracts.i_waste_transfer_service import IWasteTransferService
from src.application.services.waste_transfer_service import WasteTransferService


class WasteTransferBuilder(IWasteTransferBuilder):

    def __init__(self):
        self._repository = None

    def set_repository(self, repository: IWasteTransferRepository) -> 'WasteTransferBuilder':
        self._repository = repository
        return self

    def build(self) -> IWasteTransferService:
        if not self._repository:
            raise ValueError('Repository must be set before building the service.')

        return WasteTransferService(self._repository)
