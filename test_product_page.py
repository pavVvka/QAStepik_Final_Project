# pytest -s -v --tb=line test_product_page.py
# pytest -s -v --browser_name=firefox -m "new" --tb=line test_product_page.py
from .pages.product_page import *
from .pages.basket_page import *
from .pages.login_page import *
import pytest
import time

link_data = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"]
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

# ======== for parametrize tests of list of ['/?promo=offer' links] ==========
# base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# link_data = [f"{base_link}{x}" for x in range(10)]
# pytest.param(link_data[7], marks=pytest.mark.xfail(reason="TYPO Wrong Name of Product in Cart"))
# @pytest.mark.parametrize("link", link_data)
# def test_guest_can_add_product_to_basket(browser, link):
#     ppage = ProductPage(browser, link)
# ============================================================================


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """         1. открыть страницу регистрации;
                    2. зарегистрировать нового пользователя;
                    3. проверить, что пользователь залогинен.
        """
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "my_password")
        page.should_be_authorized_user()
        # print("----REGISTERED------->>> ", email, "   my_password")

    def test_user_cant_see_success_message(self, browser):
        ppage = ProductPage(browser, link_data[0])
        ppage.open()
        ppage.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        ppage = ProductPage(browser, link_data[0])
        ppage.open()
        ppage.get_product_price_in_store()
        ppage.get_product_name_in_store()
        print(f">>> Product Name: '{ppage.product_name_expected}' | Expected Price is: {ppage.product_price_expected} <<<")
        ppage.should_not_be_success_message()  # if no success message before adding product to cart
        ppage.add_product_to_cart()
        ppage.should_be_add_to_cart_alert()  # 1.1. message-Alert presents.
        ppage.should_be_product_name_as_in_store()  # 1.2. compare name in Cart as at Product Page
        ppage.should_be_cart_product_cost_alert()  # 2.1. message-Alert-cost presents.
        ppage.should_be_expected_product_price_in_cart()  # 2.2. compare product price with price in cart.


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    ppage = ProductPage(browser, link)
    ppage.open()
    ppage.get_product_price_in_store()  # price at product page
    ppage.get_product_name_in_store()  # name at product page
    print(f">>> Product Name: '{ppage.product_name_expected}' | Expected Price is: {ppage.product_price_expected} <<<")
    ppage.should_not_be_success_message()  # if no success message before adding product to cart
    ppage.add_product_to_cart()
    ppage.solve_quiz_and_get_code()  # Get and send result in quiz_form from Product Page
    #  Expected Tests Results :
    ppage.should_be_add_to_cart_alert()  # 1.1. if message-Alert presents.
    ppage.should_be_product_name_as_in_store()  # 1.2. compare name in Cart as at Product Page
    ppage.should_be_cart_product_cost_alert()  # 2.1. if message-Alert-cost presents.
    ppage.should_be_expected_product_price_in_cart()  # 2.2. compare product price with price in cart.
    # ppage.should_disappear_success_message()  # disappearance of ALERT with success add to cart message


# @pytest.mark.skip(reason="temporary skipped")
def test_guest_cant_see_success_message(browser):
    ppage = ProductPage(browser, link_data[0])
    ppage.open()
    ppage.should_not_be_success_message()


@pytest.mark.xfail(reason="success_message always presents after adding to cart")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    ppage = ProductPage(browser, link_data[0])
    ppage.open()
    ppage.add_product_to_cart()
    ppage.should_not_be_success_message()


@pytest.mark.xfail(reason="There is no disappearance option for message yet")
def test_message_disappeared_after_adding_product_to_basket(browser):
    ppage = ProductPage(browser, link_data[0])
    ppage.open()
    ppage.add_product_to_cart()
    ppage.should_disappear_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    ppage = ProductPage(browser, link2)
    ppage.open()
    ppage.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """     1. Гость открывает страницу товара
            2. Переходит в корзину по кнопке в шапке
            3. Ожидаем, что в корзине нет товаров
            4. Ожидаем, что есть текст о том что корзина пуста
    """
    ppage = ProductPage(browser, link2)
    ppage.open()
    ppage.go_to_basket_page()
    basket_page = BasketPage(browser, link2)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


# @pytest.mark.skip(reason="temporary skipped")
def test_guest_should_see_login_link_on_product_page(browser):
    ppage = ProductPage(browser, link2)
    ppage.open()
    ppage.should_be_login_link()
