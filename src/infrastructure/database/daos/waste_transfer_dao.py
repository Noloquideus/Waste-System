import uuid
from typing import List
from sqlalchemy import select
from src.application.abstractions.daos.i_waste_transfer_dao import IWasteTransferDao
from src.application.domain.entities.waste_transfer import WasteTransferEntity
from src.application.domain.exceptions.exceptions import NotFoundException
from src.infrastructure.database.models import WasteTransfer
from src.logger import logger


class WasteTransferDao(IWasteTransferDao):

    async def create(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransfer:
        logger.debug(f'Creating waste transfer: {waste_transfer_entity}')
        waste_transfer = WasteTransfer(
            id=uuid.uuid4(),  # without manual generation an error occurs
            organization_id=waste_transfer_entity.organization_id.value,
            storage_id=waste_transfer_entity.storage_id.value,
            waste_type_id=waste_transfer_entity.waste_type_id.value,
            quantity=waste_transfer_entity.quantity.value
        )
        logger.debug(f'Waste transfer created: {waste_transfer}')
        self._session.add(waste_transfer)
        logger.debug(f'Waste transfer added to session: {waste_transfer}')
        await self._session.flush()
        logger.debug(f'Waste transfer flushed to session: {waste_transfer}')
        logger.info('Waste transfer created')
        return waste_transfer

    async def get_by_organization_id(self, waste_transfer_entity: WasteTransferEntity) -> List[WasteTransfer]:
        logger.info('Getting waste transfers by organization id')
        logger.debug(f'Getting waste transfers by organization id: {waste_transfer_entity}')
        query = select(WasteTransfer).where(WasteTransfer.organization_id == waste_transfer_entity.organization_id.value)
        logger.debug(f'Waste transfer query: {query}')
        waste_transfers = await self._session.execute(query)
        logger.debug(f'Waste transfers: {waste_transfers}')
        logger.info('Waste transfers found')
        return waste_transfers.scalars().all()

    async def get_by_id(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransferEntity:
        logger.debug(f'Getting waste transfer by id: {waste_transfer_entity}')
        query = select(WasteTransfer).where(WasteTransfer.id == waste_transfer_entity.id.value)
        logger.debug(f'Waste transfer query: {query}')
        waste_transfer = await self._session.execute(query)
        logger.debug(f'Waste transfer: {waste_transfer}')
        result = waste_transfer.scalars().one_or_none()
        logger.debug(f'Waste transfer result: {result}')

        if result is None:
            logger.exception(f'Waste transfer with id {waste_transfer_entity.id} not found')
            raise NotFoundException('Waste transfer not found')

        logger.info('Waste transfer found')
        return result
