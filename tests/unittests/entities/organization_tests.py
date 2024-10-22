import pytest
from src.application.domain.entities.organization import OrganizationEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.core.exceptions.base import SystemException


def test_organization_entity_creation():
    id_obj = ID("org123")
    name_obj = Name("TestOrganization")

    org_entity = OrganizationEntity(id=id_obj, name=name_obj)

    assert org_entity.id == id_obj
    assert org_entity.name == name_obj


def test_organization_entity_invalid_id_type():
    with pytest.raises(SystemException):
        OrganizationEntity(id="invalid_id", name=Name("TestOrganization"))


def test_organization_entity_immutability():
    id_obj = ID("org123")
    name_obj = Name("TestOrganization")
    org_entity = OrganizationEntity(id=id_obj, name=name_obj)

    with pytest.raises(SystemException):
        org_entity._id = ID("new_id")

    with pytest.raises(SystemException):
        org_entity._name = Name("NewOrganization")

    assert org_entity.id == id_obj
    assert org_entity.name == name_obj


def test_organization_entity_properties():
    id_obj = ID("org123")
    name_obj = Name("TestOrganization")

    org_entity = OrganizationEntity(id=id_obj, name=name_obj)

    assert org_entity.id == id_obj
    assert org_entity.name == name_obj
