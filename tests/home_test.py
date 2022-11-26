from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

def test_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.user_login()
    home_pg = HomePage(driver)
    home_pg.logout()
    sleep(5)
    assert "Login" in driver.page_source

@pytest.mark.smoke
def test_accounts(setup):
    driver = setup
    login_pg = LoginPage(driver)
    login_pg.user_login()
    home_pg = HomePage(driver)
    home_pg.accounts()
    sleep(5)
    assert 'Account number' in driver.page_source
    
@pytest.mark.smoke
def test_system_log(setup):
    driver = setup
    login_pg = LoginPage(driver)
    login_pg.admin_login()
    home_pg = HomePage(driver)
    home_pg.system_log()
    sleep(5)
    assert "Transaction Log" in driver.page_source