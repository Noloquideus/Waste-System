from src.application.abstractions.repositories.i_organization_repository import IOrganizationRepository
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name


class OrganizationRepository(IOrganizationRepository):

    async def create(self, organization_entity: OrganizationEntity) -> OrganizationEntity:
        async with self._unit_of_work:
            organization = await self._unit_of_work.organization_dao.create(organization_entity)
            return OrganizationEntity(id=ID(str(organization.id)), name=Name(organization.name))