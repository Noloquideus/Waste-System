import uuid
from sqladmin import ModelView


class View(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    page_size = 50
    page_size_options = [25, 50, 100, 200, 300, 500, 1000]
    can_export = True
    export_types = ['csv', 'json']

    def create(self, obj, **kwargs):
        """Method to generate UUID for each object created in UI"""
        if hasattr(obj, 'id') and obj.id is None:
            obj.id = uuid.uuid4()
        return super().create(obj, **kwargs)
