from typing import List
from sqlalchemy import select
from src.application.abstractions.daos.i_waste_type_dao import IWasteTypeDao
from src.application.domain.entities.waste_type import WasteTypeEntity
from src.infrastructure.database.models import WasteType
from src.logger import logger


class WasteTypeDao(IWasteTypeDao):

    async def get_all(self) -> List[WasteType]:
        logger.info('Getting all waste types')
        query = select(WasteType)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        waste_types = result.scalars().all()
        logger.debug(f'Waste types: {waste_types}')
        logger.info('Waste types found')
        return waste_types

    async def get_by_id(self, waste_type_entity: WasteTypeEntity) -> WasteType:
        logger.info(f'Getting waste type with id: {waste_type_entity.id.value}')
        query = select(WasteType).where(WasteType.id == waste_type_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        waste_type = result.scalars().one_or_none()
        logger.debug(f'Waste type: {waste_type}')
        logger.info('Waste type found')
        return waste_type
