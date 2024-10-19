from abc import ABC, abstractmethod
from src.application.abstractions.repositories.base import Repository


class Builder(ABC):

    @abstractmethod
    def set_repository(self, repository: Repository) -> 'Builder':
        """Set the repository dependency."""
        raise NotImplementedError

    @abstractmethod
    def build(self):
        """Return the constructed object."""
        raise NotImplementedError
