from src.application.builders.organization.organization_builder import OrganizationBuilder
from src.application.builders.waste_type.waste_type_builder import WasteTypeBuilder
from src.application.contracts.i_organization_service import IOrganizationService
from src.application.contracts.i_waste_type_service import IWasteTypeService
from src.infrastructure.database.repositories.waste_type_repository import WasteTypeRepository
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

    @staticmethod
    async def construct_waste_type_service() -> IWasteTypeService:
        """Construct and return a service with all dependencies resolved."""

        # Create repository
        repository = WasteTypeRepository(unit_of_work=Director.__unit_of_work())

        # Use the builder to create the service
        waste_type_builder = WasteTypeBuilder()
        service = waste_type_builder.set_repository(repository).build()

        return service
