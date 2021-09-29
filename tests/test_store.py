import pytest
import base
from datetime import datetime

order_array = [1, 3]


def test_return_pet_inventories_by_status():
    assert base.return_pet_inventories_by_status() == 200, f'Inventory is NOT success'


def test_order_pet():
    now = datetime.now()
    assert base.order_pet(now.strftime('%Y-%m-%dT%H:%M:%S.%f')[0:-3] + 'Z') == 200, f'Order is NOT added'


def test_find_purchase_order_by_id():
    assert base.find_purchase_order_by_id(order_array[0]) == 200, f'Purchase order № {order_array[0]} is NOT found'


def test_delete_purchase_order_by_id():
    assert base.delete_purchase_order_by_id(order_array[1]) == 200, f'Purchase order № {order_array[1]} is NOT deleted'
