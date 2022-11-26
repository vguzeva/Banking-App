import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture()
def setup():
    # steps you run before wach test case
    driver = webdriver.Firefox()
    driver.get("https://demo.ebanq.com/log-in")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    # steps to run after each test case
    driver.quit()




