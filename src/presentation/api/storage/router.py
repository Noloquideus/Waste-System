from fastapi import APIRouter, Query
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
):
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
async def get_storages():
    pass

@storage_router.get(path='/{storage_id}', status_code=200)
async def get_storage(storage_id):
    pass

@storage_router.put(path='/{storage_id}', status_code=200)
async def update_storage(storage_id):
    pass

@storage_router.delete(path='/{storage_id}', status_code=200)
async def delete_storage(storage_id):
    pass
