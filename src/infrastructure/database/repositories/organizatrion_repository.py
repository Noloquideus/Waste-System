from typing import List
from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.logger import logger

class OrganizationRepository(IOrganizationRepository):

    async def create(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        logger.debug(f'Organization entity created: {organization_entity}')
        async with self._unit_of_work:
            logger.info(f'Creating organization with name: {organization_entity.name}')
            organization = await self._unit_of_work.organization_dao.create(organization_entity)
            logger.debug(f'Organization created: {organization}')
            logger.info('Organization created')
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))

    async def get_all(self) -> List[OrganizationEntity]:
        logger.info('Getting all organizations')
        async with self._unit_of_work:
            logger.info('Start organizations found')
            organizations = await self._unit_of_work.organization_dao.get_all()
            logger.debug(f'Organizations: {organizations}')
            logger.info('Organizations found')
            return [OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name)) for organization in organizations]

    async def get_by_id(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        logger.info(f'Getting organization with id: {organization_entity.id}')
        async with self._unit_of_work:
            logger.info('Start organization found')
            organization = await self._unit_of_work.organization_dao.get_by_id(organization_entity)
            logger.debug(f'Organization: {organization}')
            logger.info('Organization found')
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))

    async def update(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        logger.info(f'Updating organization with id: {organization_entity.id}')
        async with self._unit_of_work:
            logger.info('Start organization updated')
            organization = await self._unit_of_work.organization_dao.update(organization_entity)
            logger.debug(f'Organization updated: {organization}')
            logger.info('Organization updated')
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))

    async def delete(self, organization_entity: OrganizationEntity):
        logger.info(f'Deleting organization with id: {organization_entity.id}')
        async with self._unit_of_work:
            logger.info('Start organization deleted')
            await self._unit_of_work.organization_dao.delete(organization_entity)
