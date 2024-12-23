import pytest
from selenium import webdriver
from pages.logout_page import LogoutPage
from utils.data_loader import DataLoader
from pages.base_page import BasePage
from tests.test_login import test_login_valid_user


test_data = DataLoader.load_yaml("data/test_data.yml")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    

def test_logout_valid_user(driver):
    logout_page = LogoutPage(driver)
    test_login_valid_user(driver)
    logout_page.click_menu()
    logout_page.wait_time(LOGOUT_BUTTON)
    logout_page.click_logout()
    assert "Dashboard" not in driver.title
