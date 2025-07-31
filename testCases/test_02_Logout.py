import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readData import load_login_data
from utilities.logger import get_logger

class Test_Logout:
    def test_logout(self, loginApp):
        logger = get_logger()
        data = load_login_data()
        driver = loginApp
        logger.info("Logged in successfully")

        # Logout
        home = HomePage(driver)
        home.click_profile_icon()
        logger.info("Clicked on profile icon")
        home.click_logout()
        logger.info("Clicked on logout")

        assert "login" in driver.current_url.lower(), "Logout failed or not redirected to login page"
        logger.info("Logout successful")
