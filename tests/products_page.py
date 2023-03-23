import pytest
from data_json import *
from locators.locators import Products as pr


def test_add_and_remove_one_product(prods):
    prods.add_product()
    prods.assert_prod_in_cart(1)
    prods.remove_product()
    prods.cart_is_empty()


def test_add_and_remove_three_products(prods):
    prods.add_products()
    prods.assert_prod_in_cart(3)
    prods.remove_products()
    prods.cart_is_empty()


select_name_A_Z = [name_A_to_Z, name_products_up, pr.prods_container_by_name]
select_name_Z_A = [name_Z_to_A, name_products_down, pr.prods_container_by_name]
select_price_low_high = [price_l_to_h, price_products_up, pr.prods_container_by_price]
select_price_high_low = [price_h_to_l, price_products_down, pr.prods_container_by_price]


@pytest.mark.parametrize('item, expected_list, locator', (select_name_A_Z, select_name_Z_A, select_price_low_high,
                                                          select_price_high_low),
                         ids=['selection_A_to_Z', 'selection_Z_to_A',
                              'selection_low_to_high', 'selection_high_to_low'])
def test_selection_A_to_Z(prods, item, expected_list, locator):
    prods.select_item(item)
    prods.assert_products_list(expected_list, locator)
