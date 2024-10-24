from typing import List
from src.application.abstractions.repositories.i_storage_repository import IStorageRepository
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.logger import logger


class StorageRepository(IStorageRepository):

    async def create(self, storage_entity: StorageEntity) -> StorageEntity:
        logger.info(f'Creating storage: {storage_entity}')
        async with self._unit_of_work:
            logger.debug(f'Storage entity created: {storage_entity}')
            storage = await self._unit_of_work.storage_dao.create(storage_entity)
            logger.debug(f'Storage created: {storage}')
            storage_entity = StorageEntity(
                id=ID(str(storage.id)),
                name=Name(storage.name),
                biowaste=Quantity(storage.biowaste),
                plastic=Quantity(storage.plastic),
                glass=Quantity(storage.glass),
                biowaste_capacity=Quantity(storage.biowaste_capacity),
                plastic_capacity=Quantity(storage.plastic_capacity),
                glass_capacity=Quantity(storage.glass_capacity),
                biowaste_remaining=Quantity(storage.biowaste_remaining),
                plastic_remaining=Quantity(storage.plastic_remaining),
                glass_remaining=Quantity(storage.glass_remaining),
            )
            logger.info('Storage created')
            logger.debug(f'Storage created: {storage_entity}')
            return storage_entity

    async def get_all(self) -> List[StorageEntity]:
        logger.info('Getting all storages')
        async with self._unit_of_work:
            logger.info('Start storages found')
            storages = await self._unit_of_work.storage_dao.get_all()
            logger.debug(f'Storages: {storages}')
            logger.info('Storages found')
            storage_entities = [
                StorageEntity(
                    id=ID(str(storage.id)),
                    name=Name(storage.name),
                    biowaste=Quantity(storage.biowaste),
                    plastic=Quantity(storage.plastic),
                    glass=Quantity(storage.glass),
                    biowaste_capacity=Quantity(storage.biowaste_capacity),
                    plastic_capacity=Quantity(storage.plastic_capacity),
                    glass_capacity=Quantity(storage.glass_capacity),
                    biowaste_remaining=Quantity(storage.biowaste_remaining),
                    plastic_remaining=Quantity(storage.plastic_remaining),
                    glass_remaining=Quantity(storage.glass_remaining),
                )
                for storage in storages
            ]
            return storage_entities

    async def get_by_id(self, storage_entity: StorageEntity) -> StorageEntity:
        logger.info(f'Getting storage with id: {storage_entity}')
        async with self._unit_of_work:
            logger.debug(f'Storage entity created: {storage_entity}')
            storage = await self._unit_of_work.storage_dao.get_by_id(storage_entity)
            logger.debug(f'Storage created: {storage}')
            logger.info('Storage found')
            storage_entity = StorageEntity(
                id=ID(str(storage.id)),
                name=Name(storage.name),
                biowaste=Quantity(storage.biowaste),
                plastic=Quantity(storage.plastic),
                glass=Quantity(storage.glass),
                biowaste_capacity=Quantity(storage.biowaste_capacity),
                plastic_capacity=Quantity(storage.plastic_capacity),
                glass_capacity=Quantity(storage.glass_capacity),
                biowaste_remaining=Quantity(storage.biowaste_remaining),
                plastic_remaining=Quantity(storage.plastic_remaining),
                glass_remaining=Quantity(storage.glass_remaining),
            )
            return storage_entity

    async def update(self, storage_entity: StorageEntity) -> StorageEntity:
        logger.info(f'Updating storage: {storage_entity}')
        async with self._unit_of_work:
            logger.debug(f'Storage entity created: {storage_entity}')
            storage = await self._unit_of_work.storage_dao.update(storage_entity)
            logger.debug(f'Storage created: {storage}')
            logger.info('Storage updated')
            storage_entity = StorageEntity(
                id=ID(str(storage.id)),
                name=Name(storage.name),
                biowaste=Quantity(storage.biowaste),
                plastic=Quantity(storage.plastic),
                glass=Quantity(storage.glass),
                biowaste_capacity=Quantity(storage.biowaste_capacity),
                plastic_capacity=Quantity(storage.plastic_capacity),
                glass_capacity=Quantity(storage.glass_capacity),
                biowaste_remaining=Quantity(storage.biowaste_remaining),
                plastic_remaining=Quantity(storage.plastic_remaining),
                glass_remaining=Quantity(storage.glass_remaining),
            )
            return storage_entity

    async def delete(self, storage_entity: StorageEntity):
        logger.info(f'Deleting storage: {storage_entity}')
        async with self._unit_of_work:
            await self._unit_of_work.storage_dao.delete(storage_entity)
            logger.info('Storage deleted')