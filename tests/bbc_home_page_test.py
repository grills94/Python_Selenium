from selenium import webdriver
from pages.bbc_site import BbcSite


driver = webdriver.Chrome("drivers/chromedriver")
driver.implicitly_wait(3)
BBC_SITE = BbcSite(driver)


def test_go_to_home_page():
    BBC_SITE.bbc_home_page().go_to_home_page()
    assert driver.current_url == BBC_SITE.bbc_home_page().BBC_HOME_PAGE_URL

def test_click_on_sign_in_link():
    BBC_SITE.bbc_home_page().go_to_home_page()
    BBC_SITE.bbc_home_page().click_sign_in_link()
    BBC_SITE.bbc_sign_in_page().find_username_field()
    assert BBC_SITE.bbc_sign_in_page().ACCOUNT_URL_REGEX_VALIDATION.match(driver.current_url)
