from abc import abstractmethod, ABC
from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.builders.base import Builder

class IOrganizationBuilder(Builder, ABC):

    @abstractmethod
    def set_repository(self, repository: IOrganizationRepository) -> 'IOrganizationBuilder':
        """Set the repository dependency."""
        raise NotImplementedError
