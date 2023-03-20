import pytest


def test_successful_login(auth):
    auth.enter_user_name('standard_user')
    auth.enter_password('secret_sauce')
    auth.log_in()
    auth.assert_url('https://www.saucedemo.com/inventory.html')


blocked_username = ['locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.']
incorrect_username = ['not_user', 'secret_sauce',
                      'Epic sadface: Username and password do not match any user in this service']


@pytest.mark.parametrize('username, password, text', (blocked_username, incorrect_username),
                         ids=['blocked_username', 'incorrect_username'])
def test_unsuccessful_login(auth, username, password, text):
    auth.enter_user_name(username)
    auth.enter_password(password)
    auth.log_in()
    auth.assert_text(text)
