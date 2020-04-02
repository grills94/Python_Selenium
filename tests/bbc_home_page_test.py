from selenium import webdriver
from bbc_site.bbc_home_page import BbcHomePage


driver = webdriver.Chrome("drivers/chromedriver")
driver.implicitly_wait(3)
BBC_HOME_PAGE = BbcHomePage(driver)


def test_go_to_home_page():
    BBC_HOME_PAGE.go_to_home_page()
    assert driver.current_url == BBC_HOME_PAGE.BBC_HOME_PAGE_URL

def test_click_on_sign_in_link():
    BBC_HOME_PAGE.go_to_home_page()
    BBC_HOME_PAGE.click_sign_in_link()
