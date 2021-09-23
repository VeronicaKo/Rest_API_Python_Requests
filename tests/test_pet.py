import pytest
import base
from mimesis import Person


def test_upload_image():
    base.upload_image()


def test_add_new_pet():
    for i in range(2, 10):
        base.add_new_pet(str(i), Person('en').name())


def test_update_and_existing_pet():
    base.update_an_existing_pet('2', 'shushu')


def test_find_pet_by_status():
    stat = ['pending', 'available', 'sold']
    for i in stat:
        base.find_pet_by_status(i)


def test_find_pet_by_id():
    base.find_pet_by_id('3')


def test_update_pet_with_data():
    base.update_pet_with_data('2', 'ricki', 'sold')


def test_deletes_pet():
    base.deletes_pet('1')


if __name__ == '__main__':
    pytest.main()
