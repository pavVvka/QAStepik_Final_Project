import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Try to open in your --language=**")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Chrome(options=options)

    # browser.implicitly_wait(10)  # чтобы не мешал Explicit Waits
    yield browser
    # browser.quit()
    input("\n       Press Enter to FINISH test and QUIT Browser: ")
    browser.quit()
