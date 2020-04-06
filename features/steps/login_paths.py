from behave import given, when, then
from selenium import webdriver
from pages.bbc_site import BbcSite

driver = webdriver.Chrome("drivers/chromedriver")
driver.implicitly_wait(3)
BBC_SITE = BbcSite(driver)


@given('I can access the home page')
def i_can_access_the_home_page(context):
    BBC_SITE.bbc_home_page().go_to_home_page()


@when('I click the sign in link')
def i_click_the_sign_in_link(context):
    BBC_SITE.bbc_home_page().click_sign_in_link()


@then(u'the account page is available')
def step_impl(context):
    assert BBC_SITE.bbc_sign_in_page().ACCOUNT_URL_REGEX_VALIDATION.match(BBC_SITE.driver.current_url)

