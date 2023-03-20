from selenium.webdriver.common.by import By


class AuthPage:
    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    error_auth = (By.CSS_SELECTOR, '.error-message-container.error')
    login_btn = (By.ID, 'login-button')
