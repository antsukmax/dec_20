from wsgiref.validate import assert_

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

def open_page_s6(browser):
    browser.get('https://www.demoblaze.com/')
    galaxy_s6 = browser.find_element(By.LINK_TEXT, value = 'Samsung galaxy s6')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, value = 'h2')
    assert title.text == 'Samsung galaxy s6'