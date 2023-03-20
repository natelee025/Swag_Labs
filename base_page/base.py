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

    def click_on(self, locator):
        self.is_clickable(locator).click()

    def get_text(self, locator):
        return self.is_visible(locator).text

    def get_url(self):
        return self.driver.current_url

    # def to_select(self, locator):



