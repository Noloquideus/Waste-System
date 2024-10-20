from typing import Dict, List
from fastapi import APIRouter
from fastapi.params import Query, Path
from pydantic import StrictStr, StrictInt
from src.application.contracts.i_organization_service import IOrganizationService
from src.application.domain.entities.organization import OrganizationEntity
from src.container import Container

organization_router = APIRouter(prefix='/organization', tags=['Organization'])

@organization_router.post(path='/', status_code=201)
async def create_organization(name: StrictStr = Query(title='Name of organization')) -> Dict[str, str]:
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    organization: OrganizationEntity = await service.create(name)
    return organization.to_dict()

@organization_router.get(path='/', status_code=200)
async def get_organizations() -> List[Dict[str, str]]:
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    organizations: List[OrganizationEntity] = await service.get_all()
    return [organization.to_dict() for organization in organizations]

@organization_router.get(path='/{organization_id}', status_code=200)
async def get_organization(organization_id: StrictStr = Path(title='ID of organization')) -> Dict[str, str]:
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    organization: OrganizationEntity = await service.get_by_id(organization_id)
    return organization.to_dict()

@organization_router.put(path='/{organization_id}', status_code=200)
async def update_organization(organization_id: StrictInt = Path(title='ID of organization')):
    pass

@organization_router.delete(path='/{organization_id}', status_code=200)
async def delete_organization(organization_id: StrictInt = Path(title='ID of organization')):
    pass
