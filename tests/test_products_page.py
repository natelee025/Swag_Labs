import pytest
from data_json import *
from locators.locators import Products as pr
import allure


select_name_A_Z = [name_A_to_Z, name_products_up, pr.prods_container_by_name]
select_name_Z_A = [name_Z_to_A, name_products_down, pr.prods_container_by_name]
select_price_low_high = [price_l_to_h, price_products_up, pr.prods_container_by_price]
select_price_high_low = [price_h_to_l, price_products_down, pr.prods_container_by_price]


@allure.title('Добавить и удалить один товар')
@allure.suite('Каталог товаров')
@pytest.mark.smoke
@pytest.mark.prods
def test_add_and_remove_one_product(prods):
    with allure.step('Добавить один товар в корзину'):
        prods.add_product()
    with allure.step(f'Проверить количество добавленных товаров в корзину: {1}'):
        prods.assert_prod_in_cart(1)
    with allure.step('Удалить товар из корзины'):
        prods.remove_product()
    with allure.step('Проверить, что корзина пуста'):
        prods.cart_is_empty()


@allure.title('Добавить и удалить три товара')
@allure.suite('Каталог товаров')
@pytest.mark.prods
def test_add_and_remove_three_products(prods):
    with allure.step('Добавить три товара в корзину'):
        prods.add_products()
    with allure.step(f'Проверить количество добавленных товаров в корзину: {3}'):
        prods.assert_prod_in_cart(3)
    with allure.step('Удалить товары из корзины'):
        prods.remove_product()
    with allure.step('Проверить, что корзина пуста'):
        prods.cart_is_empty()


@allure.title('Отбор товаров по выборкам')
@allure.suite('Каталог товаров')
@pytest.mark.prods
@pytest.mark.parametrize('item, expected_list, locator', (select_name_A_Z, select_name_Z_A, select_price_low_high,
                                                          select_price_high_low),
                         ids=['selection_A_to_Z', 'selection_Z_to_A',
                              'selection_low_to_high', 'selection_high_to_low'])
def test_selection_A_to_Z(prods, item, expected_list, locator):
    with allure.step(f'Отсортировать каталог товаров по выборке: {item}'):
        prods.select_item(item)
    with allure.step('Проверить корректность сортировки товаров'):
        prods.assert_products_list(expected_list, locator)
