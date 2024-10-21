from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.repositories.base import Repository
from src.application.domain.entities.waste_transfer import WasteTransferEntity


class IWasteTransferRepository(Repository, ABC):

    @abstractmethod
    async def create(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransferEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_by_organization_id(self, waste_transfer_entity: WasteTransferEntity) -> List[WasteTransferEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransferEntity:
        raise NotImplementedError
