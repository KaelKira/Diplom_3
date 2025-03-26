import pytest
from selenium import webdriver
from constants import Constants


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif  request.param == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise ValueError('Unknown browser type')
    browser.get(Constants.MAIN_URL)
    yield browser
    browser.quit()