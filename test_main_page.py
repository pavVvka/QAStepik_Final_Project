# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
