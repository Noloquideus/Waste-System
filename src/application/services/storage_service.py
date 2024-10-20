from typing import List
from src.application.contracts.i_storage_service import IStorageService
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.logger import logger


class StorageService(IStorageService):

    async def create(self, name: str, biowaste_capacity: int, plastic_capacity: int, glass_capacity: int) -> StorageEntity:
        logger.info(f'Creating storage with name: {name} and capacities: {biowaste_capacity}, {plastic_capacity}, {glass_capacity}')
        storage_entity = StorageEntity(
            name=Name(name),
            biowaste_capacity=Quantity(biowaste_capacity),
            plastic_capacity=Quantity(plastic_capacity),
            glass_capacity=Quantity(glass_capacity),
        )
        logger.debug(f'Storage entity created: {storage_entity}')
        logger.info('Storage created')
        storage = await self._repository.create(storage_entity)
        logger.debug(f'Storage created: {storage}')
        logger.info('Storage created')
        return storage

    async def get_all(self) -> List[StorageEntity]:
        logger.info('Getting all storages')
        storages = await self._repository.get_all()
        logger.debug(f'Storages: {storages}')
        logger.info('Storages found')
        return storages

    async def get_by_id(self, storage_id: str) -> StorageEntity:
        logger.info(f'Getting storage with id: {storage_id}')
        storage_entity = StorageEntity(id=ID(storage_id))
        logger.debug(f'Storage entity created: {storage_entity}')
        storage = await self._repository.get_by_id(storage_entity)
        logger.debug(f'Storage created: {storage}')
        logger.info('Storage found')
        return storage

    async def update(self, storage_id: str, name: str, biowaste_capacity: str, plastic_capacity: str, glass_capacity: str) -> StorageEntity:
        logger.info(f'Updating storage with id: {storage_id}')
        storage_entity = StorageEntity(
            id=ID(storage_id),
            name=Name(name),
            biowaste_capacity=Quantity(biowaste_capacity),
            plastic_capacity=Quantity(plastic_capacity),
            glass_capacity=Quantity(glass_capacity),
        )
        logger.debug(f'Storage entity created: {storage_entity}')
        storage = await self._repository.update(storage_entity)
        logger.debug(f'Storage created: {storage}')
        logger.info('Storage updated')
        return storage

    async def delete(self, storage_id: str):
        logger.info(f'Deleting storage with id: {storage_id}')
        storage_entity = StorageEntity(id=ID(storage_id))
        logger.debug(f'Storage entity created: {storage_entity}')
        await self._repository.delete(storage_entity)
        logger.info('Storage deleted')
