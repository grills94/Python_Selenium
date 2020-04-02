from selenium.webdriver.common.by import By
from selenium import webdriver

class BbcHomePage:

    # Locators
    BBC_HOME_PAGE_URL = "https://www.bbc.co.uk/"
    SIGN_IN_LINK = (By.ID, "idcta-link")

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(self.BBC_HOME_PAGE_URL)

    def click_sign_in_link(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()

