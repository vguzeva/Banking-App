from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage

def test_landing_page():
    driver = webdriver.Firefox()
    driver.get("https://demo.ebanq.com/log-in")
    driver.maximize_window()
    sleep(5)
    assert driver.title == 'EBANQ'
    driver.quit()

def test_user_login():
    driver = webdriver.Firefox()
    driver.get("https://demo.ebanq.com/log-in")
    driver.maximize_window()
    sleep(5)
    login_pg = LoginPage(driver)
    login_pg.user_login()
    sleep(5)
    assert "Log Out" in driver.page_source
    driver.quit()