from typing import Dict
from fastapi import APIRouter, Query, Path
from fastapi_cache.decorator import cache
from pydantic import StrictInt, StrictStr
from src.application.contracts.i_waste_transfer_service import IWasteTransferService
from src.container import Container
from src.core.enums.status_code import StatusCode
from src.logger import logger

waste_transfer_router = APIRouter(prefix='/waste_transfer', tags=['Waste Transfer'])


@waste_transfer_router.post(path='/', status_code=StatusCode.CREATED.value)
async def create_waste_transfer(
        organization_id: StrictStr = Query(title='ID of organization'),
        storage_id: StrictStr = Query(title='ID of storage'),
        waste_type_id: StrictStr = Query(title='ID of waste type'),
        quantity: StrictInt = Query(title='Quantity of waste'),
) -> Dict[str, str]:
    logger.start_trace()
    logger.info('Creating waste transfer')
    service: IWasteTransferService = await Container.get_service(IWasteTransferService)
    logger.debug(f'Service created: {service}')
    waste_transfer = await service.create(organization_id, storage_id, waste_type_id, quantity)
    logger.debug(f'Waste transfer created: {waste_transfer}')
    logger.info('Waste transfer created')
    logger.end_trace()
    return waste_transfer.to_dict()

@waste_transfer_router.get(path='/', status_code=StatusCode.OK.value)
@cache(expire=10)
async def get_waste_transfers_by_organization_id(organization_id: StrictStr = Query(title='ID of organization'),):
    logger.start_trace()
    logger.info('Getting waste transfers by organization id')
    logger.debug(f'Getting waste transfers by organization id: {organization_id}')
    service: IWasteTransferService = await Container.get_service(IWasteTransferService)
    logger.debug(f'Service created: {service}')
    waste_transfers = await service.get_by_organization_id(organization_id)
    logger.debug(f'Waste transfers found: {waste_transfers}')
    logger.info('Waste transfers found')
    logger.end_trace()
    return [waste_transfer.to_dict() for waste_transfer in waste_transfers]

@waste_transfer_router.get(path='/{waste_transfer_id}', status_code=StatusCode.OK.value)
@cache(expire=10)
async def get_waste_transfer_by_id(waste_transfer_id: StrictStr = Path(title='ID of waste transfer'),):
    logger.start_trace()
    logger.info('Getting waste transfer by id')
    logger.debug(f'Getting waste transfer by id: {waste_transfer_id}')
    service: IWasteTransferService = await Container.get_service(IWasteTransferService)
    logger.debug(f'Service created: {service}')
    waste_transfer = await service.get_by_id(waste_transfer_id)
    logger.debug(f'Waste transfer found: {waste_transfer}')
    logger.info('Waste transfer found')
    logger.end_trace()
    return waste_transfer
