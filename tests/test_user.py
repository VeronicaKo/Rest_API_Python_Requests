import pytest
import base

user_array = ['Harry', 'Oliver', 'Jack', 'Charlie', 'Thomas', 'Jacob', 'Alfie', 'Riley', 'William',
              'James']


@pytest.mark.parametrize('user_name', user_array)
def test_create_list_of_users_with_given_input_array(user_name):
    assert base.create_list_of_users_with_given_input_array(user_name) == 200, f'User {user_name} is NOT added'


def test_get_user_by_user_name():
    assert base.get_user_by_user_name(user_array[3]) == 200, f'User {user_array[3]} is NOT found'


def test_updated_user():
    assert base.updated_user(user_array[2]) == 200, f'User {user_array[2]} is NOT updated'


def test_delete_user():
    assert base.delete_user(user_array[4]) == 200, f'User {user_array[4]} is NOT deleted'


def test_logs_user_into_the_system():
    assert base.logs_user_into_the_system(user_array[5], user_array[5]) == 200, f'User {user_array[5]} is NOT logged'


def test_logs_out_current_logged_in_user_session():
    assert base.logs_out_current_logged_in_user_session() == 200, f'User is NOT logout'


def test_create_user():
    new_user = "Denis"
    assert base.create_user(new_user) == 200, f'User {new_user} is NOT created'
