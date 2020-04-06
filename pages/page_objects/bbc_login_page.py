from selenium.webdriver.common.by import By
import re

class BbcLoginPage:

    # Regex validation
    ACCOUNT_URL_REGEX_VALIDATION = re.compile("https://account.bbc.com*")

    # Locator variables
    BBC_Login_Page_URL = "https://account.bbc.com"
    USERNAME_FIELD_ID = (By.ID, "user-identifier-input")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password-input']")

    def __init__(self, driver):
        self.driver = driver

    # page finders
    def find_username_field(self):
        return self.driver.find_element(*self.USERNAME_FIELD_ID)

    def find_password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD)

    #page actions

    def go_to_login_page(self):
        self.driver.get(self.BBC_Login_Page_URL)

    def click_password_field(self):
        self.find_password_field().click()

    def input_username(self, username_text):
        self.find_username_field().send_keys(username_text)