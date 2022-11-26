from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage
import pytest

# def test_landing_page(setup):
#     driver = setup
#     sleep(5)
#     assert driver.title == 'EBANQ'
    

# def test_user_login(setup):
#     driver = setup
#     login_pg = LoginPage(driver)
#     login_pg.user_login()
#     sleep(5)
#     assert "Log Out" in driver.page_source

# def test_login_with_blank_username(setup):
#     driver = setup
#     login_pg = LoginPage(driver)
#     login_pg.login_with_blank_username()
#     sleep(5)
#     assert "Field is required" in driver.page_source

# def test_login_with_incorrect_credentials(setup):
#     driver = setup
#     login_pg = LoginPage(driver)
#     login_pg.login_with_incorrect_credentials()
#     sleep(5)
#     assert "Wrong username or password" in driver.page_source

def test_admin_login(setup):
    driver = setup
    login_pg = LoginPage(driver)
    login_pg.admin_login()
    sleep(5)
    assert "Log Out" in driver.page_source


invalid_login_data = [
   ('','', 'Field is required'),
   ('ABC2','123', 'Wrong username or password'),
   ('abc','123', 'Should be minimum 4 char')
]

@pytest.mark.parametrize("username, password,checkpoint", invalid_login_data)
def test_invalid_login(setup, username, password, checkpoint):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username, password)
    sleep(6)
    assert checkpoint in driver.page_source