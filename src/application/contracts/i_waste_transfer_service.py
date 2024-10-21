from abc import ABC, abstractmethod
from typing import List

from src.application.abstractions.repositories.i_waste_transfer_repository import IWasteTransferRepository
from src.application.contracts.base import Service
from src.application.domain.entities.waste_transfer import WasteTransferEntity


class IWasteTransferService(Service, ABC):

    def __init__(self, repository: IWasteTransferRepository):
        self._repository = repository

    @abstractmethod
    async def create(self, organization_id: str, storage_id: str, waste_type_id: str, quantity: int) -> WasteTransferEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_by_organization_id(self, organization_id: str) -> List[WasteTransferEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, waste_transfer_id: str) -> WasteTransferEntity:
        raise NotImplementedError
