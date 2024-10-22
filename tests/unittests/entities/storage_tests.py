import pytest
from src.application.domain.entities.storage import StorageEntity
from src.application.domain.value_objects.id import ID
from src.application.domain.value_objects.name import Name
from src.application.domain.value_objects.quantity import Quantity
from src.core.exceptions.base import SystemException


def test_storage_entity_creation():
    id_obj = ID("storage123")
    name_obj = Name("MainStorage")
    biowaste = Quantity(100)
    plastic = Quantity(200)
    glass = Quantity(150)
    biowaste_capacity = Quantity(500)
    plastic_capacity = Quantity(700)
    glass_capacity = Quantity(600)
    biowaste_remaining = Quantity(400)
    plastic_remaining = Quantity(500)
    glass_remaining = Quantity(450)

    storage_entity = StorageEntity(
        id=id_obj,
        name=name_obj,
        biowaste=biowaste,
        plastic=plastic,
        glass=glass,
        biowaste_capacity=biowaste_capacity,
        plastic_capacity=plastic_capacity,
        glass_capacity=glass_capacity,
        biowaste_remaining=biowaste_remaining,
        plastic_remaining=plastic_remaining,
        glass_remaining=glass_remaining
    )

    assert storage_entity.id == id_obj
    assert storage_entity.name == name_obj
    assert storage_entity.biowaste == biowaste
    assert storage_entity.plastic == plastic
    assert storage_entity.glass == glass
    assert storage_entity.biowaste_capacity == biowaste_capacity
    assert storage_entity.plastic_capacity == plastic_capacity
    assert storage_entity.glass_capacity == glass_capacity
    assert storage_entity.biowaste_remaining == biowaste_remaining
    assert storage_entity.plastic_remaining == plastic_remaining
    assert storage_entity.glass_remaining == glass_remaining


def test_storage_entity_immutability():
    id_obj = ID("storage123")
    name_obj = Name("MainStorage")
    storage_entity = StorageEntity(id=id_obj, name=name_obj)

    with pytest.raises(SystemException):
        storage_entity._id = ID("new_id")

    with pytest.raises(SystemException):
        storage_entity._name = Name("NewStorage")

    assert storage_entity.id == id_obj
    assert storage_entity.name == name_obj


def test_storage_entity_properties():
    id_obj = ID("storage123")
    name_obj = Name("MainStorage")
    biowaste = Quantity(100)
    plastic = Quantity(200)
    glass = Quantity(150)
    biowaste_capacity = Quantity(500)
    plastic_capacity = Quantity(700)
    glass_capacity = Quantity(600)
    biowaste_remaining = Quantity(400)
    plastic_remaining = Quantity(500)
    glass_remaining = Quantity(450)

    storage_entity = StorageEntity(
        id=id_obj,
        name=name_obj,
        biowaste=biowaste,
        plastic=plastic,
        glass=glass,
        biowaste_capacity=biowaste_capacity,
        plastic_capacity=plastic_capacity,
        glass_capacity=glass_capacity,
        biowaste_remaining=biowaste_remaining,
        plastic_remaining=plastic_remaining,
        glass_remaining=glass_remaining
    )

    assert storage_entity.id == id_obj
    assert storage_entity.name == name_obj
    assert storage_entity.biowaste == biowaste
    assert storage_entity.plastic == plastic
    assert storage_entity.glass == glass
    assert storage_entity.biowaste_capacity == biowaste_capacity
    assert storage_entity.plastic_capacity == plastic_capacity
    assert storage_entity.glass_capacity == glass_capacity
    assert storage_entity.biowaste_remaining == biowaste_remaining
    assert storage_entity.plastic_remaining == plastic_remaining
    assert storage_entity.glass_remaining == glass_remaining
