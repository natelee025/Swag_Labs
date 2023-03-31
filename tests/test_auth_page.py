import pytest
from data_json import *
from data_xlsx import *
import allure

locked_out_username = [locked_out_username, correct_password, locked_out]
incorrect_username = [incorrect_username, correct_password, not_match]
incorrect_password = [correct_username, incorrect_password, not_match]

empty_username = ['', correct_password, empty_login]
empty_password = [correct_username, '', empty_password]
empty_all = ['', '', empty_login]

space_username = [' ', correct_password, not_match]
space_password = [correct_username, ' ', not_match]


@allure.title('Успешная вторизация с корректным логином')
@allure.suite('Авторизация')
@pytest.mark.smoke
@pytest.mark.auth
def test_successful_login(auth):
    with allure.step(f'Заполнить поле логина: {correct_username}'):
        auth.enter_user_name(correct_username)
    with allure.step(f'Заполнить поле пароля: {correct_password}'):
        auth.enter_password(correct_password)
    with allure.step('Нажать на кнопку Login'):
        auth.log_in()
    with allure.step('Проверить успешность перехода на страницу каталога товара'):
        auth.assert_url_after_auth('https://www.saucedemo.com/inventory.html')


@allure.title('Неудачная авторизация с некорректным логином')
@allure.suite('Авторизация')
@pytest.mark.auth
@pytest.mark.parametrize('username, password, text', (locked_out_username, incorrect_username, incorrect_password),
                         ids=['blocked_username', 'incorrect_username', 'incorrect_password'])
def test_unsuccessful_login(auth, username, password, text):
    with allure.step(f'Заполнить поле логина: {username}'):
        auth.enter_user_name(username)
    with allure.step(f'Заполнить поле пароля: {password}'):
        auth.enter_password(password)
    with allure.step('Нажать на кнопку Login'):
        auth.log_in()
    with allure.step(f'Получить ошибку из-за ввода некорректных данных: {text}'):
        auth.assert_text_error(text)


@allure.title('Неудачная авторизация с пустыми полями')
@allure.suite('Авторизация')
@pytest.mark.auth
@pytest.mark.parametrize('username, password, text', (empty_username, empty_password, empty_all,
                                                      space_username, space_password),
                         ids=['empty_username', 'empty_password', 'empty_fields', 'space_username', 'space_password'])
def test_empty_fields(auth, username, password, text):
    with allure.step(f'Заполнить поле логина: {username}'):
        auth.enter_user_name(username)
    with allure.step(f'Заполнить поле пароля: {password}'):
        auth.enter_password(password)
    with allure.step('Нажать на кнопку Login'):
        auth.log_in()
    with allure.step(f'Получить ошибку из-за незаполненных полей: {text}'):
        auth.assert_text_error(text)
