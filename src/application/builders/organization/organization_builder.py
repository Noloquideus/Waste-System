from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.builders.organization.i_organization_builder import IOrganizationBuilder
from src.application.contracts.i_organization_service import IOrganizationService
from src.application.services.organization_service import OrganizationService

class OrganizationBuilder(IOrganizationBuilder):

    def __init__(self):
        self._repository = None

    def set_repository(self, repository: IOrganizationRepository) -> 'OrganizationBuilder':
        self._repository = repository
        return self

    def build(self) -> IOrganizationService:
        if not self._repository:
            raise ValueError('Repository must be set before building the service.')
        return OrganizationService(self._repository)
