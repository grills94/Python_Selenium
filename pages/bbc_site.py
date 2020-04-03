from pages.bbc_home_page import BbcHomePage
from pages.bbc_login_page import BbcLoginPage

class BbcSite:

    def __init__(self, driver):
        self.driver = driver

    def bbc_home_page(self):
        return BbcHomePage(self.driver)

    def bbc_sign_in_page(self):
        return BbcLoginPage(self.driver)
