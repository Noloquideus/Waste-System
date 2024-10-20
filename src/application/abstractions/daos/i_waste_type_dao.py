from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.daos.base import Dao
from src.infrastructure.database.models import WasteType


class IWasteTypeDao(Dao, ABC):

    @abstractmethod
    async def get_all(self) -> List[WasteType]:
        raise NotImplementedError
