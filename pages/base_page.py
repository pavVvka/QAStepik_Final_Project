from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import *


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.CART_BUTTON)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link disabled"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True  # Если тут не указать "return True", функция вернет None (что есть False).

    def is_not_element_present(self, how, what, timeout=4):
        """Method waits for ALERT message will not appear during timeout:
        Return: FALSE, if element was found in time of "timeout"
              :  TRUE, if element was not found in time of "timeout" as TimeoutException appeared."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """ Method waits for ALERT message will disappear until timeout:
        Return: TRUE, if element has disappeared in time of "timeout"
               FALSE, if element has not disappeared during "timeout" as TimeoutException appeared."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print("  x --> ", x, "| alert.text --> ", alert.text)
        print("=======================================")
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f">>>>>>>>>>>>>  Your code: {alert_text.split()[-1]} <<<<<<<<<<<<<")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
