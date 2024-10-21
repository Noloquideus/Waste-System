from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.daos.base import Dao
from src.application.domain.entities.waste_transfer import WasteTransferEntity
from src.infrastructure.database.models import WasteTransfer


class IWasteTransferDao(Dao, ABC):

    @abstractmethod
    async def create(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransfer:
        raise NotImplementedError

    @abstractmethod
    async def get_by_organization_id(self, waste_transfer_entity: WasteTransferEntity) -> List[WasteTransfer]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransferEntity:
        raise NotImplementedError
