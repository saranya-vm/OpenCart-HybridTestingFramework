from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    add_button = (By.XPATH, "//a[text()='Add Employee']")
    first_name = (By.NAME, "firstName")
    middle_name = (By.NAME, "middleName")
    last_name = (By.NAME, "lastName")
    employee_id = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
    save_button = (By.XPATH, "//button[@type='submit']")
    success_message = (By.XPATH, "//p[contains(text(),'Successfully Saved')]")

    employee_id_field = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
    search_button = (By.XPATH, "//button[@type='submit']")
    result_row = (By.XPATH, "//div[@role='row' and contains(., '0418')]")

    def go_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def click_add(self):
        self.driver.find_element(*self.add_button).click()

    def enter_employee_details(self, first, middle, last, emp_id):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.middle_name).send_keys(middle)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.employee_id).clear()
        self.driver.find_element(*self.employee_id).send_keys(emp_id)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def is_saved_successfully(self):
        return self.driver.find_element(*self.success_message).is_displayed()

    def search_by_employee_id(self, emp_id):
        self.driver.find_element(*self.employee_id_field).send_keys(emp_id)
        self.driver.find_element(*self.search_button).click()

    def is_employee_found(self):
        return self.driver.find_elements(*self.result_row) != []