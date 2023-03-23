from base_page.base import BaseObject
from locators.locators import Auth as ap
from data_json import *


class AuthPage(BaseObject):
    def authorization(self):
        self.enter_user_name(correct_username)
        self.enter_password(correct_password)
        self.log_in()

    def enter_user_name(self, username):
        self.to_send_keys(ap.user_name, username)

    def enter_password(self, password):
        self.to_send_keys(ap.password, password)

    def log_in(self):
        self.click_on(ap.login_btn)

    def assert_text_error(self, expected_text):
        self.assert_text(ap.error_auth, expected_text)

    def assert_url_after_auth(self, expected_url):
        self.assert_url(expected_url)
