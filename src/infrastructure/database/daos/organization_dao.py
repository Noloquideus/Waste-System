from typing import Union, List
from sqlalchemy import select
from src.application.abstractions.daos.i_organization_dao import IOrganizationDao
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.exceptions.exceptions import NotFoundException
from src.infrastructure.database.models.organization import Organization


class OrganizationDao(IOrganizationDao):

    async def create(self, organization_entity: OrganizationEntity) -> Organization:
        checking = await self._get_by_name(organization_entity.name.value)

        if checking is not None:
            raise NotFoundException(f'Organization with name {organization_entity.name.value} already exists')

        organization = Organization(name=organization_entity.name.value)
        self._session.add(organization)
        await self._session.flush()
        return organization

    async def get_all(self) -> List[Organization]:
        query = select(Organization)
        result = await self._session.execute(query)
        organizations = result.scalars().all()
        return organizations

    async def get_by_id(self, organization_entity: OrganizationEntity) -> Organization:

        query = select(Organization).where(Organization.id == organization_entity.id.value)
        result = await self._session.execute(query)
        organization = result.scalars().one_or_none()

        if organization is None:
            raise NotFoundException(f'Organization with id {organization_entity.id.value} not found')

        return organization

    async def update(self, organization_entity: OrganizationEntity) -> Organization:

        query = select(Organization).where(Organization.id == organization_entity.id.value)
        result = await self._session.execute(query)
        organization = result.scalars().one_or_none()

        if organization is None:
            raise NotFoundException(f'Organization with id {organization_entity.id.value} not found')

        organization.name = organization_entity.name.value
        await self._session.flush()
        return organization

    async def delete(self, organization_entity: OrganizationEntity):

        query = select(Organization).where(Organization.id == organization_entity.id.value)
        result = await self._session.execute(query)
        organization = result.scalars().one_or_none()

        if organization is None:
            raise NotFoundException(f'Organization with id {organization_entity.id.value} not found')

        await self._session.delete(organization)

    async def _get_by_name(self, name: str) -> Union[Organization, None]:
        query = select(Organization).where(Organization.name == name)
        result = await self._session.execute(query)
        organization = result.scalars().one_or_none()
        return organization


