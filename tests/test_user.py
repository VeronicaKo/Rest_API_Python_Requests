import pytest
import base


def test_create_list_of_users_with_given_input_array():
    users_list = ['Harry', 'Oliver', 'Jack', 'Charlie', 'Thomas', 'Jacob', 'Alfie', 'Riley', 'William',
                  'James']
    for i in users_list:
        assert base.create_list_of_users_with_given_input_array(i) < 400, f'User {i} is NOT added'


def test_get_user_by_user_name():
    assert base.get_user_by_user_name('Charlie') < 400, f'User {"Charlie"} is NOT found'


def test_updated_user():
    assert base.updated_user('Oliver') < 400, f'User {"Oliver"} is NOT updated'


def test_delete_user():
    assert base.delete_user('Alfie') < 400, f'User {"Alfie"} is NOT deleted'


def test_logs_user_into_the_system():
    assert base.logs_user_into_the_system('Jack', 'Jack') < 400, f'User {"Jack"} is NOT logged'


def test_logs_out_current_logged_in_user_session():
    assert base.logs_out_current_logged_in_user_session() < 400, f'User is NOT logout'


def test_create_user():
    assert base.create_user("Denis") < 400, f'User {"Denis"} is NOT created'


if __name__ == '__main__':
    pytest.main()
