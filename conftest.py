import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage
import data


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    binary_firefox_driver_file = './geckodriver'
    service = webdriver.FirefoxService(executable_path=binary_firefox_driver_file)
    driver = webdriver.Firefox(service=service, options=options)
    options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.get_url(data.MAIN_URL)
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return page


@pytest.fixture
def redirect_page(driver):
    page = RedirectPage(driver)
    return page
