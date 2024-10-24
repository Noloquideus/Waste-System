from abc import ABC
from sqlalchemy.ext.asyncio import AsyncSession


class Dao(ABC):
    """Base class for DAOs"""
    __slots__ = ['_session']

    def __init__(self, session: AsyncSession):
        self._session = session
