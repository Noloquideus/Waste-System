from src.application.builders.organization.organization_builder import OrganizationBuilder
from src.application.contracts.i_organization_service import IOrganizationService
from src.infrastructure.database.unit_of_work import UnitOfWork, IUnitOfWork
from src.infrastructure.database.repositories.organizatrion_repository import OrganizationRepository

class Director:
    __unit_of_work = UnitOfWork

    @staticmethod
    async def construct_organization_service() -> IOrganizationService:
        """Construct and return a service with all dependencies resolved."""

        # Create repository
        repository = OrganizationRepository(unit_of_work=Director.__unit_of_work())

        # Use the builder to create the service
        organization_builder = OrganizationBuilder()
        service = organization_builder.set_repository(repository).build()

        return service
