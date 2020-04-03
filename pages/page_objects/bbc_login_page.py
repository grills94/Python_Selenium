from selenium.webdriver.common.by import By
import re

class BbcLoginPage:

    # Regex validation
    ACCOUNT_URL_REGEX_VALIDATION = re.compile("https://account.bbc.com*")

    # Locators
    BBC_Login_Page_URL = "https://account.bbc.com"
    USERNAME_FIELD_ID = (By.ID, "user-identifier-input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".field__input field__input--password-toggle")

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get(self.BBC_Login_Page_URL)

    def find_username_field(self):
        self.driver.find_element(*self.USERNAME_FIELD_ID)

    def password_field_exists(self):
        self.driver.find_element(*self.PASSWORD_FIELD)

    def input_username(self, username_text):
        self.find_username_field().send_keys(username_text)