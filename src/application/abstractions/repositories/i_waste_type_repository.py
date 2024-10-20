from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.repositories.base import Repository
from src.application.domain.entities.waste_type import WasteTypeEntity


class IWasteTypeRepository(Repository, ABC):

    @abstractmethod
    async def get_all(self) -> List[WasteTypeEntity]:
        raise NotImplementedError
