#  pytest -v --tb=line --language=en test_main_page.py

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# def go_to_login_page(browser):
#     link = browser.find_element_by_css_selector("#login_link")
#     link.click()

"""
def test_guest_can_go_to_login_page(browser):
    # browser.get(link)
    # go_to_login_page(browser)

    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


def test_quest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

"""


def test_should_be_at_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
