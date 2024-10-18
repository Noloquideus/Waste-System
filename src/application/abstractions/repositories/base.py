from abc import ABC
from src.infrastructure.database.unit_of_work import IUnitOfWork


class Repository(ABC):
    __slots__ = ['_unit_of_work']

    def __init__(self, unit_of_work: IUnitOfWork):
        self._unit_of_work = unit_of_work
