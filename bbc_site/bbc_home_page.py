from selenium.webdriver.common.by import By
from selenium import webdriver


class BbcHomePage:

    BBC_HOME_PAGE_URL = "https://www.bbc.co.uk/"
    SIGN_IN_LINK = (By.ID, "idcta-link")

    def __init__(self, driver):
        self.driver = driver
        driver.get(self.BBC_HOME_PAGE_URL)

    def go_to_home_page(self):
        self.driver.get(self.BBC_HOME_PAGE_URL)


if __name__ == '__main__':
    driver = webdriver.Chrome("../drivers/chromedriver")
    driver.implicitly_wait(3)
    x = BbcHomePage(driver)
    x.go_to_home_page()
