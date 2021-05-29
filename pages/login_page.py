import pytest

from base_page import BasePage
from locators import MainPageLocators

# pytest.fixture(scope='class')


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        "url is right" in self.browser.currect_url == \
        ("selenium1py.pythonanywhere.com/en-gb/accounts/login/"), "url is false"
        assert True

    def should_be_login_form(self):
        self.is_element_present(*MainPageLocators.login_form), "login is false"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*MainPageLocators.register_form), "registration is false"
        assert True