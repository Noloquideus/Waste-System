from typing import Dict, Type

from src.application.abstractions.repositories.base import Repository
from src.application.builders.storage.storage_builder import StorageBuilder
from src.application.builders.waste_type.waste_type_builder import WasteTypeBuilder
from src.application.contracts.base import Service
from src.application.contracts.i_storage_service import IStorageService
from src.application.contracts.i_waste_type_service import IWasteTypeService
from src.application.domain.exceptions.exceptions import NotRegisteredException
from src.infrastructure.database.repositories.storage_repository import StorageRepository
from src.infrastructure.database.repositories.waste_type_repository import WasteTypeRepository
from src.infrastructure.database.unit_of_work import IUnitOfWork, UnitOfWork
from src.application.builders.base import Builder
from src.application.builders.organization.organization_builder import OrganizationBuilder
from src.application.contracts.i_organization_service import IOrganizationService
from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.infrastructure.database.repositories.organizatrion_repository import OrganizationRepository


class Container:

    __unit_of_work: IUnitOfWork = UnitOfWork

    # Dictionary for storing builder types and their corresponding interfaces
    __service_builders: Dict[Type[Service], Type[Builder]] = {
        IOrganizationService: OrganizationBuilder,
        IWasteTypeService: WasteTypeBuilder,
        IStorageService: StorageBuilder
    }

    # Dictionary for storing correspondence between services and repositories
    __service_repositories: Dict[Type[Service], Type[Repository]] = {
        IOrganizationService: OrganizationRepository,
        IWasteTypeService: WasteTypeRepository,
        IStorageService: StorageRepository
    }

    @staticmethod
    async def get_service(service_type: Type[Service]) -> Service:

        if service_type not in Container.__service_builders:
            raise NotRegisteredException(f'No builder registered for service type {service_type}')

        if service_type not in Container.__service_repositories:
            raise NotRegisteredException(f'No repository registered for service type {service_type}')

        builder_class = Container.__service_builders[service_type]()
        repository_class = Container.__service_repositories[service_type]

        unit_of_work = Container.__unit_of_work()

        repository = repository_class(unit_of_work)

        service = builder_class.set_repository(repository).build()
        return service
