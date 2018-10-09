from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://tjsoftware.autologyx.com/")
link = driver.find_element_by_link_text("Sign In")
link.click()
email_input = driver.find_element_by_name("credentials-username")
email_input.send_keys("test_alx@tjsoftware.co")
pass_input = driver.find_element_by_name("credentials-password")
pass_input.send_keys("qazse123")
login_btn = driver.find_element_by_name("_save")
login_btn.click()
assert "My Account" in driver.page_source
driver.close()
