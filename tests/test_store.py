import pytest
import base
from datetime import datetime


def test_return_pet_inventories_by_status():
    assert base.return_pet_inventories_by_status(), f'Inventory is NOT success'


def test_order_pet():
    assert base.order_pet(f'{datetime.now().date()}t{str(datetime.now().time())[0:-3]}z'), f'Order is NOT added'


def test_find_purchase_order_by_id():
    assert base.find_purchase_order_by_id('1'), f'Purchase order № {1} is NOT found'


def test_delete_purchase_order_by_id():
    assert base.delete_purchase_order_by_id('3'), f'Purchase order № {3} is NOT deleted'


if __name__ == '__main__':
    pytest.main()
