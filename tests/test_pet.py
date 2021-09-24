import pytest
import base
from mimesis import Person


# @pytest.mark.pet1
def test_upload_image():
    file_name = 'dog.jpg'
    file = {'file': (file_name, open(file_name, 'rb'), 'image/jpg', {'Expires': '0'})}
    assert base.upload_image('1', file) < 400, f"Image {file_name} not upload added  for pet № {1}"


def test_add_new_pet():
    for i in range(2, 10):
        assert base.add_new_pet(str(i), Person('en').name()) < 400, f"Not added pet № {i}"


def test_update_and_existing_pet():
    assert base.update_an_existing_pet('2', 'shushu') < 400, f"Not updated pet № {2}"


def test_find_pet_by_status():
    stat = ['pending', 'available', 'sold']
    for i in stat:
        assert base.find_pet_by_status(i) < 400, f'Pet with status {i} is NOT found'


def test_find_pet_by_id():
    assert base.find_pet_by_id('1') < 400, f'Pet № {1} is NOT found.'


def test_update_pet_with_data():
    assert base.update_pet_with_data('2', 'ricki', 'sold') < 400, f'Pet № {2} is NOT updated'


def test_deletes_pet():
    base.deletes_pet('1')


if __name__ == '__main__':
    pytest.main()
