from src.infrastructure.database.admin.base import View
from src.infrastructure.database.models import Storage


class StorageAdmin(View, model=Storage):
    column_list = [
        Storage.id,
        Storage.name,
        Storage.biowaste,
        Storage.plastic,
        Storage.glass,
        Storage.biowaste_capacity,
        Storage.plastic_capacity,
        Storage.glass_capacity,
        Storage.biowaste_remaining,
        Storage.plastic_remaining,
        Storage.glass_remaining
    ]
    column_labels = {
        'biowaste': 'Bio Waste',
        'plastic': 'Plastic',
        'glass': 'Glass',
        'biowaste_capacity': 'Bio Waste Capacity',
        'plastic_capacity': 'Plastic Capacity',
        'glass_capacity': 'Glass Capacity',
        'biowaste_remaining': 'Remaining Bio Waste',
        'plastic_remaining': 'Remaining Plastic',
        'glass_remaining': 'Remaining Glass'
    }
    name = 'Storage'
    name_plural = 'Storages'
    icon = 'fa-solid fa-boxes-stacked'
