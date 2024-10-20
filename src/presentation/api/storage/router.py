from typing import List, Dict
from fastapi import APIRouter, Query, Path
from pydantic import StrictStr, StrictInt
from src.application.contracts.i_storage_service import IStorageService
from src.application.domain.entities.storage import StorageEntity
from src.container import Container
from src.logger import logger


storage_router = APIRouter(prefix='/storage', tags=['Storage'])

@storage_router.post(path='/', status_code=201)
async def create_storage(
        name: StrictStr = Query(title='Name of storage'),
        biowaste_capacity: StrictInt = Query(title='Biowaste capacity of storage'),
        plastic_capacity: StrictInt = Query(title='Plastic capacity of storage'),
        glass_capacity: StrictInt = Query(title='Glass capacity of storage')
) -> Dict[str, str]:
    logger.start_trace()
    logger.info(f'Creating storage with name: {name}')
    logger.debug(f'Biowaste capacity: {biowaste_capacity}, plastic capacity: {plastic_capacity}, glass capacity: {glass_capacity}')
    service: IStorageService = await Container.get_service(IStorageService)
    logger.debug(f'Service created: {service}')
    storage: StorageEntity = await service.create(
        name=name,
        biowaste_capacity=biowaste_capacity,
        plastic_capacity=plastic_capacity,
        glass_capacity=glass_capacity
    )
    logger.debug(f'Storage created: {storage}')
    logger.info('Storage created')
    logger.end_trace()
    return storage.to_dict()


@storage_router.get(path='/', status_code=200)
async def get_storages() -> List[Dict[str, str]]:
    logger.start_trace()
    logger.info('Getting all storages')
    service: IStorageService = await Container.get_service(IStorageService)
    logger.debug(f'Service created: {service}')
    storages: List[StorageEntity] = await service.get_all()
    logger.debug(f'Storages: {storages}')
    logger.info('Storages found')
    logger.end_trace()
    return [storage.to_dict() for storage in storages]

@storage_router.get(path='/{storage_id}', status_code=200)
async def get_storage(storage_id: StrictStr = Path(title='ID of storage')) -> Dict[str, str]:
    logger.start_trace()
    logger.info(f'Getting storage with id: {storage_id}')
    service: IStorageService = await Container.get_service(IStorageService)
    logger.debug(f'Service created: {service}')
    storage: StorageEntity = await service.get_by_id(storage_id)
    logger.debug(f'Storage created: {storage}')
    logger.info('Storage found')
    logger.end_trace()
    return storage.to_dict()


@storage_router.put(path='/{storage_id}', status_code=200)
async def update_storage(
        storage_id: StrictStr = Path(title='ID of storage'),
        name: StrictStr = Query(title='Name of storage'),
        biowaste_capacity: StrictInt = Query(title='Biowaste capacity of storage'),
        plastic_capacity: StrictInt = Query(title='Plastic capacity of storage'),
        glass_capacity: StrictInt = Query(title='Glass capacity of storage')
) -> Dict[str, str]:
    logger.start_trace()
    logger.info(f'Updating storage with id: {storage_id}')
    service: IStorageService = await Container.get_service(IStorageService)
    logger.debug(f'Service created: {service}')
    storage: StorageEntity = await service.update(
        storage_id=storage_id,
        name=name,
        biowaste_capacity=biowaste_capacity,
        plastic_capacity=plastic_capacity,
        glass_capacity=glass_capacity
    )
    logger.debug(f'Storage updated: {storage}')
    logger.info('Storage updated')
    logger.end_trace()
    return storage.to_dict()

@storage_router.delete(path='/{storage_id}', status_code=200)
async def delete_storage(storage_id) -> Dict[str, str]:
    logger.start_trace()
    logger.info(f'Deleting storage with id: {storage_id}')
    service: IStorageService = await Container.get_service(IStorageService)
    logger.debug(f'Service created: {service}')
    await service.delete(storage_id)
    logger.debug(f'Storage deleted: {storage_id}')
    logger.info('Storage deleted')
    logger.end_trace()
    return {'status': 'deleted'}
