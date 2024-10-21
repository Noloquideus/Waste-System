from typing import Union, List
from sqlalchemy import select
from src.application.abstractions.daos.i_storage_dao import IStorageDao
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.exceptions.exceptions import NotFoundException, CapacityException, InvalidTypeException
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

    async def add_biowaste(self, storage_entity: StorageEntity) -> Storage:

        if storage_entity.biowaste.value < 1 or storage_entity.biowaste.value is None:
            logger.exception(f'Invalid biowaste amount: {storage_entity.biowaste.value}')
            raise InvalidTypeException('Invalid biowaste amount')

        logger.info(f'Adding biowaste to storage with id: {storage_entity.id.value}')

        storage = await self.get_by_id(storage_entity)
        logger.debug(f'Storage: {storage}')

        if storage is None:
            logger.exception(f'Storage with id {storage_entity.id.value} not found')
            raise NotFoundException(f'Storage with id {storage_entity.id.value} not found')

        new_biowaste = storage.biowaste + storage_entity.biowaste.value
        logger.debug(f'New biowaste: {new_biowaste}')
        if new_biowaste > storage.biowaste_capacity:
            logger.exception(f'Adding {storage_entity.biowaste.value} would exceed capacity')
            raise CapacityException('Biowaste amount exceeds storage capacity')

        storage.biowaste = new_biowaste
        logger.debug(f'Updated biowaste: {storage.biowaste}')

        await self._session.flush()
        logger.debug('Session flushed')
        await self._session.refresh(storage)
        logger.debug(f'Storage refreshed: {storage}')
        logger.info('Biowaste added')
        return storage

    async def add_plastic(self, storage_entity: StorageEntity) -> Storage:

        if storage_entity.plastic.value < 1 or storage_entity.plastic.value is None:
            logger.exception(f'Invalid plastic amount: {storage_entity.plastic.value}')
            raise InvalidTypeException('Invalid plastic amount')

        logger.info(f'Adding plastic to storage with id: {storage_entity.id.value}')

        storage = await self.get_by_id(storage_entity)
        logger.debug(f'Storage: {storage}')

        if storage is None:
            logger.exception(f'Storage with id {storage_entity.id.value} not found')
            raise NotFoundException(f'Storage with id {storage_entity.id.value} not found')

        new_plastic = storage.plastic + storage_entity.plastic.value
        logger.debug(f'New plastic: {new_plastic}')
        if new_plastic > storage.plastic_capacity:
            logger.exception(f'Adding {storage_entity.plastic.value} would exceed capacity')
            raise CapacityException('Plastic amount exceeds storage capacity')

        storage.plastic = new_plastic
        logger.debug(f'Updated plastic: {storage.plastic}')

        await self._session.flush()
        logger.debug('Session flushed')
        await self._session.refresh(storage)
        logger.debug(f'Storage refreshed: {storage}')
        logger.info('Plastic added')
        return storage

    async def add_glass(self, storage_entity: StorageEntity) -> Storage:

        if storage_entity.glass.value < 1 or storage_entity.glass.value is None:
            logger.exception(f'Invalid glass amount: {storage_entity.glass.value}')
            raise InvalidTypeException('Invalid glass amount')

        logger.info(f'Adding glass to storage with id: {storage_entity.id.value}')

        storage = await self.get_by_id(storage_entity)
        logger.debug(f'Storage: {storage}')

        if storage is None:
            logger.exception(f'Storage with id {storage_entity.id.value} not found')
            raise NotFoundException(f'Storage with id {storage_entity.id.value} not found')

        new_glass = storage.glass + storage_entity.glass.value
        logger.debug(f'New glass: {new_glass}')

        if new_glass > storage.glass_capacity:
            logger.exception(f'Adding {storage_entity.glass.value} would exceed capacity')
            raise CapacityException('Glass amount exceeds storage capacity')

        storage.glass = new_glass
        logger.debug(f'Updated glass: {storage.glass}')

        await self._session.flush()
        logger.debug('Session flushed')
        await self._session.refresh(storage)
        logger.debug(f'Storage refreshed: {storage}')
        logger.info('Glass added')
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
        logger.info(f'Getting storage with id: {storage_entity.id.value}')
        query = select(Storage).where(Storage.id == storage_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        storage = result.scalars().one_or_none()
        logger.debug(f'Storage: {storage}')
        logger.info('Storage found')
        return storage

    async def update(self, storage_entity: StorageEntity) -> Storage:
        logger.info(f'Updating storage with id: {storage_entity.id.value}')
        query = select(Storage).where(Storage.id == storage_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        storage = result.scalars().one_or_none()
        logger.debug(f'Storage: {storage}')

        if storage is None:
            logger.exception(f'Storage with id {storage_entity.id.value} not found')
            raise NotFoundException(f'Storage with id {storage_entity.id.value} not found')

        storage.name = storage_entity.name.value
        storage.biowaste_capacity = storage_entity.biowaste_capacity.value
        storage.plastic_capacity = storage_entity.plastic_capacity.value
        storage.glass_capacity = storage_entity.glass_capacity.value
        logger.debug(f'Storage updated: {storage}')
        await self._session.flush()
        logger.debug('Session flushed')
        await self._session.refresh(storage)
        logger.debug(f'Storage refreshed: {storage}')
        logger.info('Storage updated')
        return storage

    async def delete(self, storage_entity: StorageEntity) -> Storage:
        logger.info(f'Deleting storage with id: {storage_entity.id.value}')
        query = select(Storage).where(Storage.id == storage_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        storage = result.scalars().one_or_none()
        logger.debug(f'Storage: {storage}')

        if storage is None:
            logger.exception(f'Storage with id {storage_entity.id.value} not found')
            raise NotFoundException(f'Storage with id {storage_entity.id.value} not found')

        await self._session.delete(storage)
        logger.debug(f'Storage deleted: {storage}')
        logger.info('Storage deleted')
        return storage

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
