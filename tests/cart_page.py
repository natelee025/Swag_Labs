'''
1. Добавить товар и сравнить его в корзине
2. Поля информации полностью заполненные, переход на след. стр (проверка ссылки)
3. Поля информации: пустые, потом заполнить каждое поле по очереди
4. Сделать обычный заказ со всеми полями
5. Сделать заказ с ремувами и канселами
'''

import pytest
from data_json import *
from data_xlsx import *


def test_check_added_prod(prods, cart):
    prods.add_product()
    cart.to_cart()
    cart.assert_prod_in_cart(sauce_labs_onesie)


def test_info_customer_successful(prods, cart):
    prods.add_product()
    cart.to_cart()
    cart.checkout()
    cart.enter_first_name(first_name)
    cart.enter_last_name(last_name)
    cart.enter_postal_code(postal_code)
    cart.cont()
    cart.assert_url_cart('https://www.saucedemo.com/checkout-step-two.html')


empty_all_info = ['', '', '', name_req]
empty_first_name = ['', last_name, postal_code, name_req]
empty_last_name = [first_name, '', postal_code, l_name_req]
empty_postal_code = [first_name, last_name, '', p_code_req]


@pytest.mark.parametrize('f_name, l_name, p_code, error', (empty_all_info, empty_first_name, empty_last_name,
                                                           empty_postal_code),
                         ids=['empty_all_info', 'empty_first_name', 'empty_last_name', 'empty_postal_code'])
def test_info_customer_errors(prods, cart, f_name, l_name, p_code, error):
    prods.add_product()
    cart.to_cart()
    cart.checkout()
    cart.enter_first_name(f_name)
    cart.enter_last_name(l_name)
    cart.enter_postal_code(p_code)
    cart.cont()
    cart.assert_text_error(error)

