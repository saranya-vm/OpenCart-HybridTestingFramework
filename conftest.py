# import pytest
# import sys
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# # Add project root to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#
# @pytest.fixture()
# def setup():
#     service = ChromeService(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from configurations import config
from pageObjects.LoginPage import LoginPage
from utilities.readData import load_login_data

@pytest.fixture(scope="class")
def setup():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def loginApp(setup):
    driver = setup
    data = load_login_data()
    driver.get(config.base_url)
    login_page = LoginPage(driver)
    login_page.enter_username(data["validUsername"])
    login_page.enter_password(data["validPassword"])
    login_page.click_login()
    return driver

