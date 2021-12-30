from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, " --> no 'login' in current url <-- "

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert LoginPageLocators.LOGIN_FORM, " --> Login Form is absent <-- "
        # assert not self.is_element_present(*LoginPageLocators.LOGIN_FORM), " --> Login Form is absent <-- "

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert not LoginPageLocators.REGISTER_FORM, " --> Register Form is absent <-- "
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), " --> Register Form is absent <-- "
