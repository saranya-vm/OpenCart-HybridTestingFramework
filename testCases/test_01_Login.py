from pageObjects.LoginPage import LoginPage
from utilities.readData import load_login_data
from utilities.logger import get_logger
from configurations import config

class Test_Login:
    def test_valid_login(self, setup):
        logger = get_logger()
        data = load_login_data()
        driver = setup
        driver.get(config.base_url)
        logger.info("Opened OrangeHRM login page")

        login = LoginPage(driver)
        login.enter_username(data["validUsername"])
        logger.info(f"Entered username: {data['validUsername']}")

        login.enter_password(data["validPassword"])
        logger.info("Entered password")

        login.click_login()
        logger.info("Clicked login button")

        assert "dashboard" in driver.current_url.lower(), "Login failed"
        logger.info("Login successful")

    def test_invalid_login(self, setup):
        logger = get_logger()
        data = load_login_data()
        driver = setup
        driver.get(config.base_url)
        logger.info("Opened OrangeHRM login page")

        login = LoginPage(driver)
        login.enter_username("invalidUser")
        login.enter_password("wrongPass")
        login.click_login()
        logger.info("Attempted invalid login")

        error_text = login.get_error_message()
        assert "Invalid credentials" in error_text, f"Unexpected error message: {error_text}"
        logger.info("Invalid login test passed")
