import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--url', action='store', default='http://google.ru',
                     help="Choose url")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")
    if browser_name == "chrome":
        print("\nstart browser for test..")
        browser = webdriver.Chrome(executable_path=r'C:\\Selenium\\chromedriver.exe')
        browser.implicitly_wait(200)


    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=r'C:\\Selenium\\geckodriver.exe')
        browser.implicitly_wait(200)
    

    yield browser
    print("\nquit browser..")
    browser.quit()
