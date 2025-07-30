from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    profile_icon = (By.CLASS_NAME, "oxd-userdropdown-name")
    logout_link = (By.XPATH, "//a[text()='Logout']")

    def click_profile_icon(self):
        self.driver.find_element(*self.profile_icon).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()