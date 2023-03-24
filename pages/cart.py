from base_page.base import BaseObject
from locators.locators import Cart as cr
from locators.locators import Products as pr

class CartPage(BaseObject):
    def to_cart(self):
        self.click_on(cr.shopping_cart_link)

    def assert_prod_in_cart(self, expected_prod):
        self.assert_text(pr.prods_container_by_name, expected_prod)

    def check_order_done(self, text):
        self.assert_text(cr.complete_order, text)

    def assert_url_cart(self, expected_url):
        self.assert_url(expected_url)

    def get_list_for_assertion(self, locator):
        get_products_container = self.are_visible(locator)
        list_products = []
        for i in get_products_container:
            product = i.text
            list_products.append(product)
        return list_products

    def assert_prods_in_cart(self, expected_list, locator):
        actual_list = self.get_list_for_assertion(locator)
        assert expected_list == actual_list, f'Failed. We expected products in cart: {expected_list}, but got {actual_list}'

    def cont_shopping(self):
        self.click_on(cr.btn_cont_shop)

    def checkout(self):
        self.click_on(cr.btn_checkout)

    def cont(self):
        self.click_on(cr.btn_continue)

    def cancel(self):
        self.click_on(cr.btn_cancel)

    def back_home(self):
        self.click_on(cr.btn_back_home)

    def finish(self):
        self.click_on(cr.btn_finish)

    def enter_first_name(self, key):
        self.to_send_keys(cr.first_name, key)

    def enter_last_name(self, key):
        self.to_send_keys(cr.last_name, key)

    def enter_postal_code(self, key):
        self.to_send_keys(cr.postal_code, key)

    def assert_text_error(self, expected_text):
        self.assert_text(cr.error_on_info, expected_text)

