from typing import List
from src.application.abstractions.repositories.i_waste_type_repository import IWasteTypeRepository
from src.application.contracts.i_waste_type_service import IWasteTypeService
from src.application.domain.entities.waste_type import WasteTypeEntity
from src.logger import logger

class WasteTypeService(IWasteTypeService):

    def __init__(self, repository: IWasteTypeRepository):
        super().__init__(repository)

    async def get_all(self) -> List[WasteTypeEntity]:
        logger.info('Getting all waste types')
        waste_types = await self._repository.get_all()
        logger.info('Got all waste types')
        return waste_types
