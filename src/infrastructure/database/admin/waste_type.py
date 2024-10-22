from src.infrastructure.database.admin.base import View
from src.infrastructure.database.models import WasteType


class WasteTypeAdmin(View, model=WasteType):
    column_list = [WasteType.id, WasteType.name]
    column_labels = {'id': 'ID', 'name': 'Name'}
    name = 'Waste Type'
    name_plural = 'Waste Types'
    icon = 'fa-solid fa-recycle'

