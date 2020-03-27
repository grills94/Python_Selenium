from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Error_text

short_password_error_text = "Sorry, that password is too short. It needs to be eight characters or more."

# driver management
driver = webdriver.Chrome("../web_drivers/chromedriver")
driver.implicitly_wait(3)

# actions below
# Home page
driver.get("https://www.bbc.co.uk/")
sign_in_link = driver.find_element_by_id("idcta-link")
sign_in_link.click()

# account login page
username_field = driver.find_element_by_id("user-identifier-input")
username_field.send_keys("test@gmail.com")
username_field.send_keys(Keys.TAB)

password_field = driver.find_element_by_id("password-input")
password_field.send_keys("1234")

password_field.send_keys(Keys.RETURN)

password_error_text = driver.find_element_by_id("form-message-password").text

assert password_error_text == short_password_error_text

driver.close()





