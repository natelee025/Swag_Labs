from selenium.webdriver.common.by import By


class Auth:
    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    error_auth = (By.CSS_SELECTOR, '.error-message-container.error')
    login_btn = (By.ID, 'login-button')


class Products:
    prods_container_by_name = (By.CLASS_NAME, 'inventory_item_name')
    prods_container_by_price = (By.CLASS_NAME, 'inventory_item_price')
    selection_menu = (By.CLASS_NAME, 'product_sort_container')
    btn_add_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    btn_remove_backpack = (By.ID, 'remove-sauce-labs-backpack')
    btn_add_jacket = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    btn_remove_jacket = (By.ID, 'remove-sauce-labs-fleece-jacket')
    btn_add_red_tshirt = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    btn_remove_red_tshirt = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')
    btn_add_onesie = (By.ID, 'add-to-cart-sauce-labs-onesie')
    btn_remove_onesie = (By.ID, 'remove-sauce-labs-onesie')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')


class Cart:
    shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')
    btn_cont_shop = (By.ID, 'continue-shopping')
    btn_checkout = (By.ID, 'checkout')
    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    postal_code = (By.ID, 'postal-code')
    btn_continue = (By.ID, 'continue')
    btn_cancel = (By.ID, 'cancel')
    btn_finish = (By.ID, 'finish')
    btn_back_home = (By.ID, 'back-to-products')
    complete_order = (By.CLASS_NAME, 'complete-header')
    error_on_info = (By.CSS_SELECTOR, '.error-message-container.error')

