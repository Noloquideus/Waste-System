from abc import ABC, abstractmethod
from src.application.abstractions.daos.i_organization_dao import IOrganizationDao
from src.application.abstractions.daos.i_waste_type_dao import IWasteTypeDao
from src.infrastructure.database.daos.organization_dao import OrganizationDao
from src.infrastructure.database.daos.waste_type_dao import WasteTypeDao
from src.infrastructure.database.database import async_session_maker


class IUnitOfWork(ABC):

    organization_dao: IOrganizationDao = None
    waste_type_dao: IWasteTypeDao = None

    def __init__(self):
        self.session_factory = async_session_maker

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):

    async def __aenter__(self):
        self.__session = self.session_factory()
        self.organization_dao = OrganizationDao(self.__session)
        self.waste_type_dao = WasteTypeDao(self.__session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.__session.close()

    async def commit(self):
        await self.__session.commit()

    async def rollback(self):
        await self.__session.rollback()
