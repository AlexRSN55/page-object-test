from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == self.browser.currect_url, "No login url"


    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.login_form), "login is false"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.register_form), "registration is false"
        assert True