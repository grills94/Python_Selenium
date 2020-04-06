from selenium import webdriver
from pages.bbc_site import BbcSite
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome("drivers/chromedriver")
    driver.implicitly_wait(3)
    BBC_SITE = BbcSite(driver)
    yield BBC_SITE
    driver.close()


def test_go_to_home_page(browser):
    browser.bbc_home_page().go_to_home_page()
    assert browser.driver.current_url == browser.bbc_home_page().BBC_HOME_PAGE_URL


def test_click_on_sign_in_link(browser):
    browser.bbc_home_page().go_to_home_page()
    browser.bbc_home_page().click_sign_in_link()
    browser.bbc_sign_in_page().find_username_field()
    assert browser.bbc_sign_in_page().ACCOUNT_URL_REGEX_VALIDATION.match(browser.driver.current_url)


def test_password_field_exists(browser):
    browser.bbc_sign_in_page().go_to_login_page()
    assert browser.bbc_sign_in_page().find_password_field() == True
