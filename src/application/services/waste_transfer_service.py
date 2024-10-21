from typing import List
from src.application.contracts.i_waste_transfer_service import IWasteTransferService
from src.application.domain.entities.waste_transfer import WasteTransferEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.quantity import Quantity
from src.logger import logger


class WasteTransferService(IWasteTransferService):

    async def create(self, organization_id: str, storage_id: str, waste_type_id: str, quantity: int) -> WasteTransferEntity:
        logger.info('Creating waste transfer')
        waste_transfer_entity = WasteTransferEntity(
            organization_id=ID(organization_id),
            storage_id=ID(storage_id),
            waste_type_id=ID(waste_type_id),
            quantity=Quantity(quantity)
        )
        logger.debug(f'Waste transfer created: {waste_transfer_entity}')
        waste_transfer = await self._repository.create(waste_transfer_entity)
        logger.debug(f'Waste transfer created: {waste_transfer}')
        logger.info('Waste transfer created')
        return waste_transfer

    async def get_by_organization_id(self, organization_id: str) -> List[WasteTransferEntity]:
        logger.info('Getting waste transfers by organization id')
        waste_transfer_entity = WasteTransferEntity(organization_id=ID(organization_id))
        logger.debug(f'Waste transfer entity: {waste_transfer_entity}')
        logger.info('Getting waste transfers by organization id')
        return await self._repository.get_by_organization_id(waste_transfer_entity)

    async def get_by_id(self, waste_transfer_id: str) -> WasteTransferEntity:
        logger.info('Getting waste transfer by id')
        logger.debug(f'Getting waste transfer by id: {waste_transfer_id}')
        waste_transfer_entity = WasteTransferEntity(id=ID(waste_transfer_id))
        logger.debug(f'Waste transfer entity: {waste_transfer_entity}')
        logger.info('Waste transfer found')
        return await self._repository.get_by_id(waste_transfer_entity)
