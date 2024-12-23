import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_loader import DataLoader
# Load dữ liệu từ YAML
test_data = DataLoader.load_yaml("data/test_data.yml")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to(test_data["base_url"])
    login_page.enter_username(test_data["valid_user"]["username"])
    login_page.enter_password(test_data["valid_user"]["password"])
    login_page.click_login()
    assert "Swag Labs" in driver.title
