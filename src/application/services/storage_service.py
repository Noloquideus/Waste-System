from src.application.contracts.i_storage_service import IStorageService
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.logger import logger


class StorageService(IStorageService):

    async def create(self, name: str, biowaste_capacity: str, plastic_capacity: str, glass_capacity: str) -> StorageEntity:
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
