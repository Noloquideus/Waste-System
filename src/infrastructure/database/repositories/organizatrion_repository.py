from typing import List
from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name


class OrganizationRepository(IOrganizationRepository):

    async def create(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        async with self._unit_of_work:
            organization = await self._unit_of_work.organization_dao.create(organization_entity)
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))

    async def get_all(self) -> List[OrganizationEntity]:
        async with self._unit_of_work:
            organizations = await self._unit_of_work.organization_dao.get_all()
            return [OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name)) for organization in organizations]

    async def get_by_id(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        async with self._unit_of_work:
            organization = await self._unit_of_work.organization_dao.get_by_id(organization_entity)
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))

    async def update(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        async with self._unit_of_work:
            organization = await self._unit_of_work.organization_dao.update(organization_entity)
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))

    async def delete(self, organization_entity: OrganizationEntity):
        async with self._unit_of_work:
            await self._unit_of_work.organization_dao.delete(organization_entity)
