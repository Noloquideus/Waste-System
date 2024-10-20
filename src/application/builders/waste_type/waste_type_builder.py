from src.application.abstractions.repositories.i_waste_type_repository import IWasteTypeRepository
from src.application.builders.waste_type.i_waste_type_builder import IWasteTypeBuilder
from src.application.contracts.i_waste_type_service import IWasteTypeService
from src.application.services.waste_type_service import WasteTypeService


class WasteTypeBuilder(IWasteTypeBuilder):

    def __init__(self):
        self._repository = None

    def set_repository(self, repository: IWasteTypeRepository) -> 'IWasteTypeBuilder':
        self._repository = repository
        return self

    def build(self) -> IWasteTypeService:
        if not self._repository:
            raise ValueError('Repository must be set before building the service.')

        return WasteTypeService(self._repository)
