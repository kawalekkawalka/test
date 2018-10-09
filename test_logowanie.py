from selenium import webdriver


def login_test(login, password):
    driver = webdriver.Firefox()
    driver.get("https://tjsoftware.autologyx.com/")
    link = driver.find_element_by_link_text("Sign In")
    link.click()
    email_input = driver.find_element_by_name("credentials-username")
    email_input.send_keys(login)
    pass_input = driver.find_element_by_name("credentials-password")
    pass_input.send_keys(password)
    login_btn = driver.find_element_by_name("_save")
    login_btn.click()
    assert "My Account" not in driver.page_source
    driver.close()


if __name__ == "__main__":
    login_test("", "")




