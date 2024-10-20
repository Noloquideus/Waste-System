from typing import Dict, List
from fastapi import APIRouter
from fastapi.params import Query, Path
from pydantic import StrictStr
from src.application.contracts.i_organization_service import IOrganizationService
from src.application.domain.entities.organization import OrganizationEntity
from src.container import Container
from src.logger import logger

organization_router = APIRouter(prefix='/organization', tags=['Organization'])

@organization_router.post(path='/', status_code=201)
async def create_organization(name: StrictStr = Query(title='Name of organization')) -> Dict[str, str]:
    logger.start_trace()
    logger.info(f'Creating organization with name: {name}')
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    logger.info('Service created')
    logger.debug(f'Service created: {service}')
    organization: OrganizationEntity = await service.create(name)
    logger.debug(f'Organization created: {organization}')
    logger.info('Organization created')
    logger.end_trace()
    return organization.to_dict()

@organization_router.get(path='/', status_code=200)
async def get_organizations() -> List[Dict[str, str]]:
    logger.start_trace()
    logger.info('Getting all organizations')
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    logger.debug(f'Service created: {service}')
    organizations: List[OrganizationEntity] = await service.get_all()
    logger.debug(f'Organizations: {organizations}')
    logger.end_trace()
    return [organization.to_dict() for organization in organizations]

@organization_router.get(path='/{organization_id}', status_code=200)
async def get_organization(organization_id: StrictStr = Path(title='ID of organization')) -> Dict[str, str]:
    logger.start_trace()
    logger.info(f'Getting organization with id: {organization_id}')
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    logger.debug(f'Service created: {service}')
    organization: OrganizationEntity = await service.get_by_id(organization_id)
    logger.debug(f'Organization: {organization}')
    logger.info('Organization found')
    logger.end_trace()
    return organization.to_dict()

@organization_router.put(path='/{organization_id}', status_code=200)
async def update_organization(
        organization_id: StrictStr = Path(title='ID of organization'),
        new_name: StrictStr = Query(title='New name of organization')) -> Dict[str, str]:
    logger.start_trace()
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    organization: OrganizationEntity = await service.update(organization_id, new_name)
    logger.end_trace()
    return organization.to_dict()

@organization_router.delete(path='/{organization_id}', status_code=200)
async def delete_organization(organization_id: StrictStr = Path(title='ID of organization')):
    logger.start_trace()
    service: IOrganizationService = await Container.get_service(IOrganizationService)
    await service.delete(organization_id)
    logger.end_trace()
    return {'message': 'Organization deleted'}
