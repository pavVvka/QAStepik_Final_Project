from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    BUSKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASS1 = (By.ID, "id_registration-password1")
    REGISTER_PASS2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")
    # REG_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert.alert-success")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_IN_CART = (By.CSS_SELECTOR, ".alertinner strong")  # "div.alertinner>strong"
    ALERT_ADD_TO_CART = (By.CLASS_NAME, "alert:nth-child(1)")
    ALERT_CART_TOTAL = (By.CLASS_NAME, "alert-info")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
