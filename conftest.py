import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.auth import AuthPage


@pytest.fixture()
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture()
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture()
def auth(setup):
    return AuthPage(setup)

