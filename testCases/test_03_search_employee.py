import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.PIMPage import PIMPage
from utilities.readData import load_login_data
from utilities.logger import get_logger
from configurations import config

class Test_SearchEmployee:
    def test_search_by_employee_id(self, loginApp):
        logger = get_logger()
        data = load_login_data()
        driver = loginApp
        logger.info("Logged in successfully")

        # Navigate to PIM
        pim = PIMPage(driver)
        pim.go_to_pim()
        logger.info("Navigated to PIM")

        # Search by Employee ID
        pim.search_by_employee_id(data["employeeId"])
        logger.info(f"Searched by Employee ID: {data['employeeId']}")

        assert pim.is_employee_found(), "Employee not found in the result"
        logger.info("Employee record found successfully")
