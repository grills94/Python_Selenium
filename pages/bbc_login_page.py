from selenium.webdriver.common.by import By
import re

class BbcLoginPage:

    # Regex validation
    ACCOUNT_URL_REGEX_VALIDATION = re.compile("https://account.bbc.com*")

    # Locators
    BBC_Login_Page_URL = "https://account.bbc.com"
    USERNAME_FIELD_ID = (By.ID, "user-identifier-input")

    def __init__(self, driver):
        self.driver = driver

    def find_username_field(self):
        self.driver.find_element(*self.USERNAME_FIELD_ID)
