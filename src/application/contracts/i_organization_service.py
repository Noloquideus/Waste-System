from abc import ABC, abstractmethod
from typing import List
from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.contracts.base import Service
from src.application.domain.entities.organization import OrganizationEntity


class IOrganizationService(Service, ABC):

    def __init__(self, repository: IOrganizationRepository):
        self._repository = repository

    @abstractmethod
    async def create(self, name: str) -> OrganizationEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[OrganizationEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, organization_id: str) -> OrganizationEntity:
        raise NotImplementedError
