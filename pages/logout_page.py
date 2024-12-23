from pages.base_page import BasePage
from data.locators import LogoutPageLocators

class LogoutPage(BasePage):

    def click_logout(self):
        self.click(LogoutPageLocators.LOGOUT_BUTTON)

    def click_menu(self):
        self.click(LogoutPageLocators.MENU_BUTTON)
