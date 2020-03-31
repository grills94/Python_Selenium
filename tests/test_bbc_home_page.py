from selenium import webdriver
from bbc_site.bbc_home_page import BbcHomePage


class TestBbcHomePage:

    driver = webdriver.Chrome("drivers/chromedriver")
    driver.implicitly_wait(3)
    BBC_HOME_PAGE = BbcHomePage(driver)

    def test_go_to_home_page(self):
        self.BBC_HOME_PAGE.go_to_home_page()
