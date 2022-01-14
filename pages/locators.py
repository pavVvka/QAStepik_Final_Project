from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_IN_CART = (By.CSS_SELECTOR, ".alertinner strong")  # "div.alertinner>strong"
    ALERT_ADD_TO_CART = (By.CLASS_NAME, "alert:nth-child(1)")
    ALERT_CART_TOTAL = (By.CLASS_NAME, "alert-info")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
