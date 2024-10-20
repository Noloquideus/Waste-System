from typing import List
from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.contracts.i_organization_service import IOrganizationService
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.logger import logger


class OrganizationService(IOrganizationService):

    def __init__(self, repository: IOrganizationRepository):
        super().__init__(repository)

    async def create(self, name: str) -> OrganizationEntity:
        logger.info(f'Creating organization with name: {name}')
        organization_entity = OrganizationEntity(name=Name(name))
        logger.debug(f'Organization entity created: {organization_entity}')
        organization = await self._repository.create(organization_entity)
        logger.debug(f'Organization created: {organization}')
        logger.info('Organization created')
        return organization

    async def get_all(self) -> List[OrganizationEntity]:
        logger.info('Getting all organizations')
        organizations = await self._repository.get_all()
        logger.debug(f'Organizations: {organizations}')
        logger.info('Organizations found')
        return organizations

    async def get_by_id(self, organization_id: str) -> OrganizationEntity:
        organization_entity = OrganizationEntity(id=ID(organization_id))
        organization = await self._repository.get_by_id(organization_entity)
        return organization

    async def update(self, organization_id: str, new_name: str) -> OrganizationEntity:
        organization_entity = OrganizationEntity(id=ID(organization_id), name=Name(new_name))
        organization = await self._repository.update(organization_entity)
        return organization

    async def delete(self, organization_id: str):
        organization_entity = OrganizationEntity(id=ID(organization_id))
        await self._repository.delete(organization_entity)
