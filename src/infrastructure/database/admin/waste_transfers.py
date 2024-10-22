from src.infrastructure.database.admin.base import View
from src.infrastructure.database.models import WasteTransfer


class WasteTransferAdmin(View, model=WasteTransfer):
    column_list = [
        WasteTransfer.id,
        WasteTransfer.organization_id,
        WasteTransfer.storage_id,
        WasteTransfer.waste_type_id,
        WasteTransfer.quantity,
        WasteTransfer.created_at
    ]
    column_labels = {
        'id': 'ID',
        'organization_id': 'Organization ID',
        'storage_id': 'Storage ID',
        'waste_type_id': 'Waste Type ID',
        'quantity': 'Quantity',
        'created_at': 'Created At'
    }
    name = 'Waste Transfer'
    name_plural = 'Waste Transfers'
    icon = 'fa-solid fa-truck'
