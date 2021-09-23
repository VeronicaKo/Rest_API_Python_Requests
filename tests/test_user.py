import pytest
import base


def test_create_list_of_users():
    base.create_list_of_users()


def test_get_user_by_user_name():
    base.get_user_by_user_name('string')


def test_updated_user():
    base.updated_user('string')


def test_delete_user():
    base.delete_user('string')


def test_logs_user_into_the_system():
    base.logs_user_into_the_system('bob', 'password')


def test_logs_out_current_logged_in_user_session():
    base.logs_out_current_logged_in_user_session()


def test_create_user():
    base.create_user()

if __name__ == '__main__':
    pytest.main()

