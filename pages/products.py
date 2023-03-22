from base_page.base import BaseObject
from locators.locators import Products as pr


class ProductsPage(BaseObject):
    def add_product(self):
        self.click_on(pr.btn_add_backpack)

    def remove_product(self):
        self.click_on(pr.btn_remove_backpack)

    def add_products(self):
        self.click_on(pr.btn_add_backpack, pr.btn_add_jacket, pr.btn_add_red_tshirt)

    def remove_products(self):
        self.click_on(pr.btn_remove_backpack, pr.btn_remove_jacket, pr.btn_remove_red_tshirt)

    def assert_prod_in_cart(self, expected_number):
        actual_text = self.get_text(pr.shopping_cart_badge)
        assert str(expected_number) == actual_text, f'Failed. We expected text: {expected_number}, but got {actual_text}'

    def cart_is_empty(self):
        self.not_have_element(pr.shopping_cart_badge)

    def select_item(self, item):
        self.to_select(pr.selection_menu, item)

    def get_list_for_assertion(self, locator):
        get_products_container = self.are_visible(locator)
        list_products = []
        for i in get_products_container:
            product = i.text
            list_products.append(product)
        return list_products

    def assert_products_list(self, expected_list, locator):
        actual_list = self.get_list_for_assertion(locator)
        assert expected_list == actual_list, f'Failed. We expected list: {expected_list}, but got {actual_list}'

