import pytest
from data_json import *
from data_xlsx import *
from locators.locators import Products as pr
import allure


@allure.title('Товар добавлен в корзину')
@allure.suite('Корзина')
@pytest.mark.smoke
@pytest.mark.cart
def test_check_added_prod(prods, cart):
    with allure.step('Добавить один товар в корзину'):
        prods.add_product()
    with allure.step('Перейти в корзину'):
        cart.to_cart()
    with allure.step('Проверить наличие выбранного товара в корзине'):
        cart.assert_prod_in_cart(sauce_labs_onesie)


@allure.title('Корректное заполнение информации о покупателе')
@allure.suite('Корзина')
@pytest.mark.smoke
@pytest.mark.cart
def test_info_customer_successful(prods, cart):
    with allure.step('Добавить один товар в корзину'):
        prods.add_product()
    with allure.step('Перейти в корзину'):
        cart.to_cart()
    with allure.step('Нажать кнопку Checkout и перейти на страницу заполнения информации о покупателе'):
        cart.checkout()
    with allure.step(f'Ввести имя: {first_name}'):
        cart.enter_first_name(first_name)
    with allure.step(f'Ввести фамилию: {last_name}'):
        cart.enter_last_name(last_name)
    with allure.step(f'Ввести почтовый индекс: {postal_code}'):
        cart.enter_postal_code(postal_code)
    with allure.step('Нажать кнопку Continue для перехода на страницу с информацией о заказе'):
        cart.cont()
    with allure.step('Проверить успешность перехода на страницу'):
        cart.assert_url_cart('https://www.saucedemo.com/checkout-step-two.html')


empty_all_info = ['', '', '', name_req]
empty_first_name = ['', last_name, postal_code, name_req]
empty_last_name = [first_name, '', postal_code, l_name_req]
empty_postal_code = [first_name, last_name, '', p_code_req]


@allure.title('Некорректное заполнение информации о покупателе')
@allure.suite('Корзина')
@pytest.mark.cart
@pytest.mark.parametrize('f_name, l_name, p_code, error', (empty_all_info, empty_first_name, empty_last_name,
                                                           empty_postal_code),
                         ids=['empty_all_info', 'empty_first_name', 'empty_last_name', 'empty_postal_code'])
def test_info_customer_errors(prods, cart, f_name, l_name, p_code, error):
    with allure.step('Добавить один товар в корзину'):
        prods.add_product()
    with allure.step('Перейти в корзину'):
        cart.to_cart()
    with allure.step('Нажать кнопку Checkout и перейти на страницу заполнения информации о покупателе'):
        cart.checkout()
    with allure.step(f'Ввести имя: {f_name}'):
        cart.enter_first_name(f_name)
    with allure.step(f'Ввести фамилию: {l_name}'):
        cart.enter_last_name(l_name)
    with allure.step(f'Ввести почтовый индекс: {p_code}'):
        cart.enter_postal_code(p_code)
    with allure.step('Нажать кнопку Continue для перехода на страницу с информацией о заказе'):
        cart.cont()
    with allure.step(f'Получить ошибку из-за незаполненных полей: {error}'):
        cart.assert_text_error(error)


@allure.title('Оформление заказа одного товара')
@allure.suite('Корзина')
@pytest.mark.smoke
@pytest.mark.cart
def test_order_one_prod(prods, cart):
    with allure.step('Добавить один товар в корзину'):
        prods.add_product()
    with allure.step('Перейти в корзину'):
        cart.to_cart()
    with allure.step(f'Проверить наличие товара в корзине: {sauce_labs_onesie}'):
        cart.assert_prod_in_cart(sauce_labs_onesie)
    with allure.step('Нажать кнопку Checkout и перейти на страницу заполнения информации о покупателе'):
        cart.checkout()
    with allure.step(f'Ввести имя: {first_name}'):
        cart.enter_first_name(first_name)
    with allure.step(f'Ввести фамилию: {last_name}'):
        cart.enter_last_name(last_name)
    with allure.step(f'Ввести почтовый индекс: {postal_code}'):
        cart.enter_postal_code(postal_code)
    with allure.step('Нажать кнопку Continue для перехода на страницу с информацией о заказе'):
        cart.cont()
    with allure.step(f'Проверить наличие добавленного товара в оформленном заказе: {sauce_labs_onesie}'):
        cart.assert_prod_in_cart(sauce_labs_onesie)
    with allure.step('Нажать кнопку Finish для перехода на страницу с сообщением о завершении заказа'):
        cart.finish()
    with allure.step('Проверить переход на страницу и текст сообщения'):
        cart.check_order_done('Thank you for your order!')
    with allure.step('Вернуться в каталог товаров'):
        cart.back_home()


@allure.title('Оформление заказа трех товаров')
@allure.suite('Корзина')
@pytest.mark.cart
def test_order_three_prod(prods, cart):
    with allure.step('Добавить один товар в корзину'):
        prods.add_product()
    with allure.step('Перейти в корзину'):
        cart.to_cart()
    with allure.step(f'Проверить наличие товара в корзине: {sauce_labs_onesie}'):
        cart.assert_prod_in_cart(sauce_labs_onesie)
    with allure.step('Вернуться из корзины в каталог товаров'):
        cart.cont_shopping()
    with allure.step('Добавить 3 товара в корзину'):
        prods.add_products()
    with allure.step('Перейти в корзину'):
        cart.to_cart()
    with allure.step(f'Проверить наличие товаров в корзине: {sauce_labs_onesie, sauce_labs_backpack, sauce_labs_fleece_jacket, t_shirt_red}'):
        cart.assert_prods_in_cart(expected_list=[sauce_labs_onesie, sauce_labs_backpack, sauce_labs_fleece_jacket,
                                                 t_shirt_red], locator=pr.prods_container_by_name)
    with allure.step('Нажать кнопку Checkout и перейти на страницу заполнения информации о покупателе'):
        cart.checkout()
    with allure.step('Вернуться на страницу со списком добавленных товаров'):
        cart.cancel()
    with allure.step('Удалить один товар'):
        prods.remove_product()
    with allure.step(f'Проверить наличие товаров в корзине: {sauce_labs_backpack, sauce_labs_fleece_jacket, t_shirt_red}'):
        cart.assert_prods_in_cart(expected_list=[sauce_labs_backpack, sauce_labs_fleece_jacket, t_shirt_red],
                                  locator=pr.prods_container_by_name)
    with allure.step('Нажать кнопку Checkout и перейти на страницу заполнения информации о покупателе'):
        cart.checkout()
    with allure.step(f'Ввести имя: {first_name}'):
        cart.enter_first_name(first_name)
    with allure.step(f'Ввести фамилию: {last_name}'):
        cart.enter_last_name(last_name)
    with allure.step(f'Ввести почтовый индекс: {postal_code}'):
        cart.enter_postal_code(postal_code)
    with allure.step('Нажать кнопку Continue для перехода на страницу с информацией о заказе'):
        cart.cont()
    with allure.step(f'Проверить наличие добавленных товаров в оформленном заказе: {sauce_labs_backpack, sauce_labs_fleece_jacket, t_shirt_red}'):
        cart.assert_prods_in_cart(expected_list=[sauce_labs_backpack, sauce_labs_fleece_jacket, t_shirt_red],
                                  locator=pr.prods_container_by_name)
    with allure.step('Нажать кнопку Finish для перехода на страницу с сообщением о завершении заказа'):
        cart.finish()
    with allure.step('Проверить переход на страницу и текст сообщения'):
        cart.check_order_done('Thank you for your order!')
    with allure.step('Вернуться в каталог товаров'):
        cart.back_home()
