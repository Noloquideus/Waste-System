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

