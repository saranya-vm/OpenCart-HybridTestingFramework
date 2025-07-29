import pytest
from pageObjects.LoginPage import LoginPage

class TestLogin:
    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        assert "dashboard" in self.driver.current_url.lower(), "Login failed or not redirected to dashboard"


    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(self.driver)
        login.enter_username("invalidUser")
        login.enter_password("wrongPass")
        login.click_login()

        error_text = login.get_error_message()

        assert "Invalid credentials" in error_text, f"Unexpected error message: {error_text}"
