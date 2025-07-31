import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage
from pageObjects.PIMPage import PIMPage
from utilities.readData import load_login_data
from utilities.logger import get_logger
from configurations import config

class Test_AddEmployee:
    def test_add_employee(self, loginApp):
        logger = get_logger()
        data = load_login_data()
        driver = loginApp
        logger.info("Logged in successfully")

        # Add Employee
        pim = PIMPage(driver)
        pim.go_to_pim()
        logger.info("Navigated to PIM")

        pim.click_add()
        logger.info("Clicked Add button")

        pim.enter_employee_details(data["Add_Employee"]["first"], data["Add_Employee"]["middle"], data["Add_Employee"]["last"], data["Add_Employee"]["emp_id"])
        logger.info("Entered employee details")

        pim.click_save()
        logger.info("Clicked Save button")

        # Verify Toast Message
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class,'oxd-toast-content')]//p")
                )
            )
            popup = driver.find_element(By.XPATH, "//div[contains(@class,'oxd-toast-content')]//p")
            assert "Success" in popup.text
            logger.info("Employee added successfully - Toast popup detected.")
        except Exception as e:
            logger.error(f"Popup not found or failed to assert: {e}")
            raise
