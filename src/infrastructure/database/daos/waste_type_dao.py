from typing import List
from sqlalchemy import select
from src.application.abstractions.daos.i_waste_type_dao import IWasteTypeDao
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
