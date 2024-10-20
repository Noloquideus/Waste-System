from typing import Union, List
from sqlalchemy import select
from src.application.abstractions.daos.i_organization_dao import IOrganizationDao
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.exceptions.exceptions import NotFoundException
from src.infrastructure.database.models.organization import Organization
from src.logger import logger

class OrganizationDao(IOrganizationDao):

    async def create(self, organization_entity: OrganizationEntity) -> Organization:
        logger.info(f'Creating organization with name: {organization_entity.name}')
        checking = await self._get_by_name(organization_entity.name.value)
        logger.debug(f'Status search: {checking}')

        if checking is not None:
            logger.exception(f'Organization with name {organization_entity.name.value} already exists')
            raise NotFoundException(f'Organization with name {organization_entity.name.value} already exists')

        organization = Organization(name=organization_entity.name.value)
        logger.debug(f'Organization created: {organization}')
        self._session.add(organization)
        logger.debug(f'Organization added to session: {organization}')
        await self._session.flush()
        logger.debug('Session flushed')
        logger.info('Organization created')
        return organization

    async def get_all(self) -> List[Organization]:
        logger.info('Getting all organizations')
        query = select(Organization)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        organizations = result.scalars().all()
        logger.debug(f'Organizations: {organizations}')
        logger.info('Organizations found')
        return organizations

    async def get_by_id(self, organization_entity: OrganizationEntity) -> Organization:
        logger.info(f'Getting organization with id: {organization_entity.id}')
        query = select(Organization).where(Organization.id == organization_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        organization = result.scalars().one_or_none()
        logger.debug(f'Organization: {organization}')

        if organization is None:
            logger.exception(f'Organization with id {organization_entity.id.value} not found')
            raise NotFoundException(f'Organization with id {organization_entity.id.value} not found')

        logger.info('Organization found')
        return organization

    async def update(self, organization_entity: OrganizationEntity) -> Organization:
        logger.info(f'Updating organization with id: {organization_entity.id}')
        query = select(Organization).where(Organization.id == organization_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        organization = result.scalars().one_or_none()
        logger.debug(f'Organization: {organization}')

        if organization is None:
            logger.exception(f'Organization with id {organization_entity.id.value} not found')
            raise NotFoundException(f'Organization with id {organization_entity.id.value} not found')

        organization.name = organization_entity.name.value
        logger.debug(f'Organization updated: {organization}')
        await self._session.flush()
        logger.debug('Session flushed')
        logger.info('Organization updated')
        return organization

    async def delete(self, organization_entity: OrganizationEntity):
        logger.info(f'Deleting organization with id: {organization_entity.id}')
        query = select(Organization).where(Organization.id == organization_entity.id.value)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        organization = result.scalars().one_or_none()
        logger.debug(f'Organization: {organization}')

        if organization is None:
            logger.exception(f'Organization with id {organization_entity.id.value} not found')
            raise NotFoundException(f'Organization with id {organization_entity.id.value} not found')
        await self._session.delete(organization)
        logger.info('Organization deleted')

    async def _get_by_name(self, name: str) -> Union[Organization, None]:
        logger.info(f'Searching organization with name: {name}')
        query = select(Organization).where(Organization.name == name)
        logger.debug(f'Query: {query}')
        result = await self._session.execute(query)
        logger.debug(f'Result: {result}')
        organization = result.scalars().one_or_none()
        logger.debug(f'Organization: {organization}')
        logger.info('Organization found')
        return organization
