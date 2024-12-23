from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def click(self, xpath):
        self.find_element(xpath).click()

    def input_text(self, xpath, text):
        self.find_element(xpath).send_keys(text)

    def wait_time(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
