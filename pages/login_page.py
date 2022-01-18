from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # Проверка на корректный url адрес
        assert "login" in self.browser.current_url, " --> no 'login' in current url <-- "

    def should_be_login_form(self):  # Проверка, что есть форма логина
        # assert LoginPageLocators.LOGIN_FORM, " --> Login Form is absent <-- "
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), " --> Login Form is absent <-- "

    def should_be_register_form(self):  # Проверка, что есть форма регистрации на странице
        # assert not LoginPageLocators.REGISTER_FORM, " --> Register Form is absent <-- "
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), " --> Register Form is absent <-- "

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pasword1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        pasword2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        mail.send_keys(email)
        pasword1.send_keys(password)
        pasword2.send_keys(password)
        reg = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg.click()
