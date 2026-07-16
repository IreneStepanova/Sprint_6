import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data.urls import BASE_URL


@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
