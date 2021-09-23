import pytest
import base
from datetime import datetime


def test_return_pet_inventories_by_status():
    base.return_pet_inventories_by_status()


def test_order_pet():
    base.order_pet(f'{datetime.now().date()}t{str(datetime.now().time())[0:-3]}z')


def test_find_purchase_order_by_id():
    base.find_purchase_order_by_id('1')  # 1<=id<=10


def test_delete_purchase_order_by_id():
    base.delete_purchase_order_by_id('3')


if __name__ == '__main__':
    pytest.main()
