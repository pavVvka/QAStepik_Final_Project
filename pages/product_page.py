from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_price_expected = None
    product_name_expected = None

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_product_price_in_store(self):
        """Func defines global 'product_price_expected' as product price from Product Page"""
        self.product_price_expected = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name_in_store(self):
        """Func defines and return global 'product_name_expected' as product name from Product Page"""
        self.product_name_expected = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return self.product_name_expected

    def should_be_add_to_cart_alert(self):
        """Func asserts presence of add to cart ALERT at Cart Page"""
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_CART), \
            "There is no ADD TO CART ALERT on Cart Page"

    def should_be_product_name_as_in_store(self):
        """Func asserts comparison of product NAME on Cart Page as in Product Page"""
        name_product_cart = self.browser.find_element(*ProductPageLocators.NAME_IN_CART).text
        assert self.product_name_expected == name_product_cart, \
            f"Name in Cart: '{name_product_cart}' is differ from Product Name in Store !"

    def should_be_cart_product_cost_alert(self):
        """Func asserts presence of cart total cost ALERT on Cart Page"""
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_TOTAL), \
            "There is no Message about Basket Total in Cart"

    def should_be_expected_product_price_in_cart(self):
        """Func asserts comparison of product PRICE in Cart Page as in Product Page"""
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert price_in_cart == self.product_price_expected, \
            f"{price_in_cart} is Not Expected Price of Product !"

    def should_not_be_success_message(self):
        """Func asserts absence of ALERT with success add to cart message on Product Page during timeout"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message presents, but should not be"

    def should_disappear_success_message(self):
        """Func asserts that ALERT with success add to cart message disappeared during timeout"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappeared, but should be"
