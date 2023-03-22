import pytest
from data_json import *
from data_xlsx import *

locked_out_username = [locked_out_username, correct_password, locked_out]
incorrect_username = [incorrect_username, correct_password, not_match]
incorrect_password = [correct_username, incorrect_password,not_match]

empty_username = ['', correct_password, empty_login]
empty_password = [correct_username, '', empty_password]
empty_fields = ['', '', empty_login]

space_username = [' ', correct_password, not_match]
space_password = [correct_username, ' ', not_match]


def test_successful_login(auth):
    auth.enter_user_name(correct_username)
    auth.enter_password(correct_password)
    auth.log_in()
    auth.assert_url('https://www.saucedemo.com/inventory.html')


@pytest.mark.parametrize('username, password, text', (locked_out_username, incorrect_username),
                         ids=['blocked_username', 'incorrect_username'])
def test_unsuccessful_login(auth, username, password, text):
    auth.enter_user_name(username)
    auth.enter_password(password)
    auth.log_in()
    auth.assert_text_error(text)


@pytest.mark.parametrize('username, password, text', (empty_username, empty_password, empty_fields,
                                                      space_username, space_password),
                         ids=['empty_username', 'empty_password', 'empty_fields', 'space_username', 'space_password'])
def test_empty_fields(auth, username, password, text):
    auth.enter_user_name(username)
    auth.enter_password(password)
    auth.log_in()
    auth.assert_text_error(text)
