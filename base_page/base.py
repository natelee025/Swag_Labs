from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def to_send_keys(self, locator, key):
        self.is_visible(locator).send_keys(key)

    def are_visible(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click_on(self, *locator):
        for i in locator:
            self.is_clickable(i).click()

    def get_text(self, locator):
        return self.is_visible(locator).text

    def get_url(self):
        return self.driver.current_url

    def to_select(self, locator, text):
        select = Select(self.is_visible(locator))
        select.select_by_visible_text(text)

    def not_have_element(self, locator):
        return self.wait.until_not(ec.visibility_of_element_located(locator))

    def assert_text(self, locator, expected_text):
        actual_text = self.get_text(locator)
        assert expected_text == actual_text, f'Failed. We expected text: {expected_text}, but got {actual_text}'

    def assert_url(self, expected_url):
        actual_url = self.get_url()
        assert actual_url == expected_url, \
            f'Failed. We expected url: {expected_url}, but got {actual_url}'


