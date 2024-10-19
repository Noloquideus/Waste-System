from abc import abstractmethod, ABC
from src.application.abstractions.repositories.base import Repository
from src.application.domain.entities.organization import OrganizationEntity


class IOrganizationRepository(Repository, ABC):

    @abstractmethod
    async def create(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        raise NotImplementedError
