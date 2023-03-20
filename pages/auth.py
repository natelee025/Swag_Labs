from base_page.base import BaseObject
from locators.locators import AuthPage as ap


class AuthPage(BaseObject):
    def enter_user_name(self, username):
        self.to_send_keys(ap.user_name, username)

    def enter_password(self, password):
        self.to_send_keys(ap.password, password)

    def log_in(self):
        self.click_on(ap.login_btn)

    def assert_text(self, expected_text):
        actual_text = self.get_text(ap.error_auth)
        assert expected_text == actual_text, f'Failed. We expected text: {expected_text}, but got {actual_text}'

    def assert_url(self, expected_url):
        actual_url = self.get_url()
        assert actual_url == expected_url, \
            f'Failed. We expected url: {expected_url}, but got {actual_url}'