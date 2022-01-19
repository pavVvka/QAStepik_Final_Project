from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        """ делегирование аргументов инициализатору родительского класса """
        super().__init__(*args, **kwargs)


"""
# ==========> Способ 1 вернуть нужный Page Object :  
# в методе иниициализировать новый объект Page и вернуть его: 

from .locators import MainPageLocators
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

        return LoginPage(browser=self.browser, url=self.browser.current_url)
        # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы
        # с браузером, а в качестве url передаем текущий адрес.
        
        # Тогда этот метод в тесте будет вызываться так:
        # page = MainPage(browser, link)
        # login_page = page.go_to_login_page()

# ==========> Способ 2 вернуть нужный Page Object :  
# в самом тесте иниициализировать новый объект Page явно:
        
        # Убрать: return LoginPage(browser=self.browser, url=self.browser.current_url)
        
        # Тогда этот метод в тесте будет вызываться так:
        # page = MainPage(browser, link)
        # login_page = LoginPage(browser, browser.current_url)

"""
