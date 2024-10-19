from abc import ABC, abstractmethod
from typing import Union, List
from src.application.abstractions.daos.base import Dao
from src.application.domain.entities.organization import OrganizationEntity
from src.infrastructure.database.models.organization import Organization


class IOrganizationDao(Dao, ABC):

    @abstractmethod
    async def create(self, organization_entity: OrganizationEntity) -> Organization:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[Organization]:
        raise NotImplementedError

    @abstractmethod
    async def _get_by_name(self, name: str) -> Union[Organization, None]:
        raise NotImplementedError
