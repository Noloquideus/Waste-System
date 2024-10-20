from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.repositories.i_waste_type_repository import IWasteTypeRepository
from src.application.contracts.base import Service
from src.application.domain.entities.waste_type import WasteTypeEntity


class IWasteTypeService(Service, ABC):

    def __init__(self, repository: IWasteTypeRepository):
        self._repository = repository

    @abstractmethod
    async def get_all(self) -> List[WasteTypeEntity]:
        raise NotImplementedError
