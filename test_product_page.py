# pytest -s -v --tb=line test_product_page.py
from .pages.product_page import *
from .pages.basket_page import *
import pytest
base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# link_data = [f"{base_link}{x}" for x in range(10)]
# pytest.param(link_data[7], marks=pytest.mark.xfail(reason="TYPO Wrong Name of Product in Cart"))
link_data = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"]


@pytest.mark.skip
@pytest.mark.parametrize("link", link_data)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # 1. Open link
    ppage = ProductPage(browser, link)
    ppage.open()
    ppage.get_product_price_in_store()
    pname = ppage.get_product_name_in_store()
    print(f">>> Product Name: '{pname}' | Expected Price is: {ppage.product_price_expected} <<<")

    # Test: No success add to cart MESSAGE should be at Product Page before adding product to cart
    ppage.should_not_be_success_message()

    # 2. Press "Add To Cart" button
    ppage.add_product_to_cart()

    # 3. Get and send result of solve_quiz_and_get_code() from BasePage
    ppage.solve_quiz_and_get_code()

#  Expected Tests Results :
# 1.1. Сообщение о том, что товар добавлен в корзину.
    ppage.should_be_add_to_cart_alert()
# 1.2. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    ppage.should_be_product_name_as_in_store()
# 2.1. Сообщение со стоимостью корзины.
    ppage.should_be_cart_product_cost_alert()
# 2.2. Стоимость корзины совпадает с ценой товара.
    ppage.should_be_expected_product_price_in_cart()
# Test: ALERT with success add to cart message should disappear
    # ppage.should_disappear_success_message() # no disappearance option yet


@pytest.mark.xfail(reason="after adding to cart Message already is")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    ppage = ProductPage(browser, link_data[0])
    ppage.open()
    ppage.add_product_to_cart()
    # ppage.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    ppage.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    ppage = ProductPage(browser, link_data[0])
    ppage.open()
    ppage.should_not_be_success_message()


@pytest.mark.xfail(reason="There is no disappearance option for message yet")
def test_message_disappeared_after_adding_product_to_basket(browser):
    ppage = ProductPage(browser, link_data[0])
    ppage.open()
    ppage.add_product_to_cart()
    ppage.should_disappear_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    ppage = ProductPage(browser, link)
    ppage.open()
    ppage.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    ppage = ProductPage(browser, link)
    ppage.open()
    ppage.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    1. Гость открывает страницу товара
    2. Переходит в корзину по кнопке в шапке
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    ppage = ProductPage(browser, link)
    ppage.open()
    ppage.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
