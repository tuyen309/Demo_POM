from pages.base_page import BasePage
from data.locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        self.input_text(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
