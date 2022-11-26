from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # constructor methos
    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def user_login(self):
        self.login(self.user, self.user_password)

    def admin_login(self):
        self.login(self.admin, self.admin_password)
        
    # def login_with_blank_username(self):
    #     self.login('','Demo-Access1')
       
    # def login_with_incorrect_credentials(self):
    #     self.login('ABC2','123')
        
    # both are redundand since we are combining in login test

