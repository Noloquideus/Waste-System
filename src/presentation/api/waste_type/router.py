from typing import List, Dict
from fastapi import APIRouter
from src.application.contracts.i_waste_type_service import IWasteTypeService
from src.container import Container
from src.core.enums.status_code import StatusCode
from src.logger import logger

waste_type_router = APIRouter(prefix='/waste_type', tags=['Waste Type'])

@waste_type_router.get(path='/', status_code=StatusCode.OK.value)
async def get_waste_types() -> List[Dict[str, str]]:
    logger.start_trace()
    service: IWasteTypeService = await Container.get_service(IWasteTypeService)
    logger.debug(f'Service created: {service}')
    waste_types = await service.get_all()
    logger.debug(f'Waste types: {[waste_type.to_dict() for waste_type in waste_types]}')
    logger.info('Waste types found')
    logger.end_trace()
    return [waste_type.to_dict() for waste_type in waste_types]
