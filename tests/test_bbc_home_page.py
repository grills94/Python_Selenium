from selenium import webdriver
from bbc_site.bbc_home_page import BbcHomePage

driver = webdriver.Chrome("drivers/chromedriver")
driver.implicitly_wait(3)

BBC_HOME_PAGE = BbcHomePage(driver)

class TestBbcHomePage:

    def __init__(self):
        self.BBC_HOME_PAGE = BbcHomePage()

    def go_to_home_page():
        BBC_HOME_PAGE.go_to_home_page()
