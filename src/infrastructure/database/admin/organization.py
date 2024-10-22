from src.infrastructure.database.admin.base import View
from src.infrastructure.database.models import Organization


class OrganizationAdmin(View, model=Organization):
    column_list = [Organization.id, Organization.name]
    column_labels = {'id': 'ID', 'name': 'Name'}
    name = 'Organization'
    name_plural = 'Organizations'
    icon = 'fa-solid fa-building'
