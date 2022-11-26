from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver) -> None:
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".controls__logout > span").click()

    def accounts(self):
        self.driver.find_element(By.CSS_SELECTOR, ".aside__label.main_color.accounts").click()

    def system_log(self):
        self.driver.find_element(By.CSS_SELECTOR, ".aside__label.main_color.system_logs").click()