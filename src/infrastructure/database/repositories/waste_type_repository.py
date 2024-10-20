from typing import List
from src.application.abstractions.repositories.i_waste_type_repository import IWasteTypeRepository
from src.application.domain.entities.waste_type import WasteTypeEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.logger import logger


class WasteTypeRepository(IWasteTypeRepository):

    async def get_all(self) -> List[WasteTypeEntity]:
        logger.info('Getting all waste types')
        async with self._unit_of_work:
            logger.info('Start waste types found')
            waste_types = await self._unit_of_work.waste_type_dao.get_all()
            logger.debug(f'Waste types: {waste_types}')
            logger.info('Waste types found')
            return [WasteTypeEntity(id=ID(str(waste_type.id)), name=Name(waste_type.name)) for waste_type in waste_types]