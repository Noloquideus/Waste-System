from typing import Union, List
from sqlalchemy import select
from src.application.abstractions.daos.i_storage_dao import IStorageDao
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.exceptions.exceptions import NotFoundException
from src.infrastructure.database.models import Storage
from src.logger import logger


class StorageDao(IStorageDao):

    async def create(self, storage_entity: StorageEntity) -> Storage:
        logger.info(f'Creating storage with name: {storage_entity.name}')
        checking = await self._get_by_name(storage_entity.name.value)
        logger.debug(f'Status search: {checking}')

        if checking is not None:
            logger.exception(f'Storage with name {storage_entity.name.value} already exists')
            raise NotFoundException(f'Storage with name {storage_entity.name.value} already exists')

        storage = Storage(
            name=storage_entity.name.value,
            biowaste_capacity=storage_entity.biowaste_capacity.value,
            plastic_capacity=storage_entity.plastic_capacity.value,
            glass_capacity=storage_entity.glass_capacity.value,
        )
        logger.debug(f'Storage created: {storage}')
        logger.info('Storage created')
        self._session.add(storage)
        logger.debug(f'Storage added to session: {storage}')
        await self._session.flush()
        logger.debug('Session flushed')
        logger.info('Storage created')
        return storage

    async def get_all(self) -> List[Storage]:
        logger.info('Getting all storages')
        query = select(Storage)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        storages = result.scalars().all()
        logger.debug(f'Storages: {storages}')
        logger.info('Storages found')
        return storages

    async def get_by_id(self, storage_entity: StorageEntity) -> Storage:
        pass

    async def _get_by_name(self, name: str) -> Union[Storage, None]:
        logger.info(f'Searching storage with name: {name}')
        query = select(Storage).where(Storage.name == name)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        storage = result.scalars().one_or_none()
        logger.debug(f'Storage: {storage}')
        logger.info('Storage found')
        return storage
