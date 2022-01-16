from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BUSKET_ITEMS), \
            "Cart is not empty, but should be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), \
            "No 'EMPTY BUSKET' message, but shoul be"
