import pytest
from data_json import *
from locators.locators import Products as pr

def test_add_one_product(auth_done):
    auth_done.add_product()
    auth_done.assert_prod_in_cart(1)


def test_add_three_products(auth_done):
    auth_done.add_products()
    auth_done.assert_prod_in_cart(3)


def test_remove_one_products(auth_done):
    auth_done.add_product()
    auth_done.assert_prod_in_cart(1)
    auth_done.remove_product()
    auth_done.cart_is_empty()


def test_remove_three_products(auth_done):
    auth_done.add_products()
    auth_done.assert_prod_in_cart(3)
    auth_done.remove_products()
    auth_done.cart_is_empty()


select_name_A_Z = [name_A_to_Z, name_products_up, pr.prods_container_by_name]
select_name_Z_A = [name_Z_to_A, name_products_down, pr.prods_container_by_name]
select_price_low_high = [price_l_to_h, price_products_up, pr.prods_container_by_price]
select_price_high_low = [price_h_to_l, price_products_down, pr.prods_container_by_price]


@pytest.mark.parametrize('item, expected_list, locator', (select_name_A_Z, select_name_Z_A, select_price_low_high,
                                                 select_price_high_low), ids=['selection_A_to_Z', 'selection_Z_to_A',
                                                                    'selection_low_to_high', 'selection_high_to_low'])
def test_selection_A_to_Z(auth_done, item, expected_list, locator):
    auth_done.select_item(item)
    auth_done.assert_products_list(expected_list, locator)
