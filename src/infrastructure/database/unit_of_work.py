from abc import ABC, abstractmethod
from src.application.abstractions.daos.i_organization_dao import IOrganizationDao
from src.application.abstractions.daos.i_storage_dao import IStorageDao
from src.application.abstractions.daos.i_waste_transfer_dao import IWasteTransferDao
from src.application.abstractions.daos.i_waste_type_dao import IWasteTypeDao
from src.infrastructure.database.daos.organization_dao import OrganizationDao
from src.infrastructure.database.daos.storage_dao import StorageDao
from src.infrastructure.database.daos.waste_transfer_dao import WasteTransferDao
from src.infrastructure.database.daos.waste_type_dao import WasteTypeDao
from src.infrastructure.database.database import async_session_maker
from src.logger import logger


class IUnitOfWork(ABC):

    organization_dao: IOrganizationDao = None
    waste_type_dao: IWasteTypeDao = None
    storage_dao: IStorageDao = None
    waste_transfer_dao: IWasteTransferDao = None

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
        logger.debug('Unit of work created')
        self.__session = self.session_factory()
        self.organization_dao = OrganizationDao(self.__session)
        self.waste_type_dao = WasteTypeDao(self.__session)
        self.storage_dao = StorageDao(self.__session)
        self.waste_transfer_dao = WasteTransferDao(self.__session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        logger.debug('Unit of work closed')
        if exc_type:
            logger.debug(exc_tb)
            logger.debug('Rolling back')
            logger.error(exc_val)
            await self.rollback()
        else:
            logger.debug('Committing')
            await self.__session.flush()
            logger.debug('Session flushed')
            await self.commit()
            logger.debug('Session commited')

        logger.debug('Session closed')
        await self.__session.close()

    async def commit(self):
        logger.debug('Committing')
        await self.__session.commit()

    async def rollback(self):
        logger.debug('Rolling back')
        await self.__session.rollback()
