from typing import List
from src.application.abstractions.repositories.i_waste_transfer_repository import IWasteTransferRepository
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.entities.waste_transfer import WasteTransferEntity
from src.application.domain.entities.waste_type import WasteTypeEntity
from src.application.domain.exceptions.exceptions import NotFoundException
from src.application.domain.value_objects.date import Date
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.infrastructure.database.models import WasteTransfer
from src.logger import logger


class WasteTransferRepository(IWasteTransferRepository):

    async def create(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransferEntity:
        logger.info('Creating waste transfer')
        logger.debug(f'Creating waste transfer: {waste_transfer_entity}')
        async with self._unit_of_work:
            logger.debug(f'Waste transfer created: {waste_transfer_entity}')
            waste_transfer = await self._unit_of_work.waste_transfer_dao.create(waste_transfer_entity)
            logger.debug(f'Getting waste type with id: {waste_transfer_entity.waste_type_id}')
            waste_type = await self._unit_of_work.waste_type_dao.get_by_id(
                WasteTypeEntity(id=waste_transfer_entity.waste_type_id))
            logger.debug(f'Waste type: {waste_type}')

            if waste_type is None:
                logger.exception(f'Waste type with id {waste_transfer_entity.waste_type_id} not found')
                raise NotFoundException('Waste type not found')

            if waste_type.name == 'biowaste':
                logger.debug(f'Adding biowaste to storage with id: {waste_transfer_entity.storage_id.value}')
                await self._unit_of_work.storage_dao.add_biowaste(
                    StorageEntity(id=waste_transfer_entity.storage_id, biowaste=Quantity(waste_transfer.quantity)))

            if waste_type.name == 'plastic':
                logger.debug(f'Adding plastic to storage with id: {waste_transfer_entity.storage_id.value}')
                await self._unit_of_work.storage_dao.add_plastic(
                    StorageEntity(id=waste_transfer_entity.storage_id, plastic=Quantity(waste_transfer.quantity)))

            if waste_type.name == 'glass':
                logger.debug(f'Adding glass to storage with id: {waste_transfer_entity.storage_id.value}')
                await self._unit_of_work.storage_dao.add_glass(
                    StorageEntity(id=waste_transfer_entity.storage_id, glass=Quantity(waste_transfer.quantity)))
                await self._unit_of_work.commit()

            logger.debug(f'Waste transfer added to session: {waste_transfer}')
            waste_transfer_entity = WasteTransferEntity(
                id=ID(str(waste_transfer.id)),
                organization_id=ID(str(waste_transfer.organization_id)),
                storage_id=ID(str(waste_transfer.storage_id)),
                waste_type_id=ID(str(waste_transfer.waste_type_id)),
                quantity=Quantity(waste_transfer.quantity)
            )
            logger.debug(f'Waste transfer flushed to session: {waste_transfer}')
            logger.info('Waste transfer created')
            return waste_transfer_entity

    async def get_by_organization_id(self, waste_transfer_entity: WasteTransferEntity) -> List[WasteTransferEntity]:
        logger.info('Getting waste transfers by organization id')
        logger.debug(f'Getting waste transfers by organization id: {waste_transfer_entity}')
        async with self._unit_of_work:
            logger.debug(f'Waste transfer query: {waste_transfer_entity}')
            waste_transfers: List[WasteTransfer] = await self._unit_of_work.waste_transfer_dao.get_by_organization_id(waste_transfer_entity)
            organization = await self._unit_of_work.organization_dao.get_by_id(OrganizationEntity(id=waste_transfer_entity.organization_id))
            logger.debug(f'Organization: {repr(organization)}')
            storage = await self._unit_of_work.storage_dao.get_by_id(StorageEntity(id=ID(str(waste_transfers[0].storage_id))))
            logger.debug(f'Storage: {storage}')
            waste_type = await self._unit_of_work.waste_type_dao.get_by_id(WasteTypeEntity(id=ID(str(waste_transfers[0].waste_type_id))))
            logger.debug(f'Waste type: {waste_type}')
            logger.debug(f'Waste transfers: {waste_transfers}')
            logger.info('Waste transfers found')
            return [WasteTransferEntity(
                id=ID(str(waste_transfer.id)),
                organization_id=ID(str(waste_transfer.organization_id)),
                storage_id=ID(str(waste_transfer.storage_id)),
                waste_type_id=ID(str(waste_transfer.waste_type_id)),
                quantity=Quantity(waste_transfer.quantity),
                organization_name=Name(organization.name),
                storage_name=Name(storage.name),
                waste_type_name=Name(waste_type.name),
                created_at=Date(waste_transfer.created_at)
            ) for waste_transfer in waste_transfers]

    async def get_by_id(self, waste_transfer_entity: WasteTransferEntity) -> WasteTransferEntity:
        logger.info('Getting waste transfer by id')
        logger.debug(f'Getting waste transfer by id: {waste_transfer_entity}')
        async with self._unit_of_work:
            logger.debug(f'Waste transfer query: {waste_transfer_entity}')
            waste_transfer = await self._unit_of_work.waste_transfer_dao.get_by_id(waste_transfer_entity)
            logger.debug(f'Waste transfer: {waste_transfer}')
            waste_transfer_entity = WasteTransferEntity(
                id=ID(str(waste_transfer.id)),
                organization_id=ID(str(waste_transfer.organization_id)),
                storage_id=ID(str(waste_transfer.storage_id)),
                waste_type_id=ID(str(waste_transfer.waste_type_id)),
                quantity=Quantity(waste_transfer.quantity)
            )
            logger.debug(f'Waste transfer result: {waste_transfer_entity}')
            logger.info('Waste transfer found')
            return waste_transfer_entity
