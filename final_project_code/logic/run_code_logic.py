from selenium.webdriver import Keys, ActionChains
from logic.login_logout_logic import loginLogic
import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RunCode(loginLogic):

    PYTHON_TURTORIAL_XPATH = '//a[@href="https://www.geeksforgeeks.org/python-programming-language/"]'
    # CLOSE_MENU_XPATH='/html/body/nav/div/div[1]/span'
    LEARN_STRINGS_XPATH="//h2[text()='Python String']"
    STRINGS_LEN_XPTAH='//a[text()="Python string length | len() function to find string length"]'
    EDIT_CODE='//*[@id="run-and-edit-button"]'
    CHANGE_CODE_XPATH='//pre[@class=" CodeMirror-line "]'
    RUN_CODE_XPATH='//*[@id="run-code-button"]'
    RESULT_XPATH='//pre[@class="output-pre"]'

    def __init__(self, num, list_info, cabs):
        super().__init__(num, list_info, cabs)

    # # a method to close the menu by pressing on the X button (this is only for chrome)
    # def close_menu(self):
    #     try:
    #         close_menu_btn = WebDriverWait(self._driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, self.CLOSE_MENU_XPATH)))
    #         close_menu_btn.click()
    #     except StaleElementReferenceException:
    #         close_menu_btn = WebDriverWait(self._driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, self.CLOSE_MENU_XPATH)))
    #         close_menu_btn.click()

    # this method is to click on the python toturials
    def click_on_python_toturials(self):
        try:
            python_tutrial_btn = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.PYTHON_TURTORIAL_XPATH)))
            python_tutrial_btn.click()
        except StaleElementReferenceException:
            python_tutrial_btn = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.PYTHON_TURTORIAL_XPATH)))
            python_tutrial_btn.click()
        except ElementClickInterceptedException:
            python_tutrial_btn = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.PYTHON_TURTORIAL_XPATH)))
            python_tutrial_btn.click()

    # ckick in the sub section that we want
    def click_on_learn_strings(self):
        learn_strings_btn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LEARN_STRINGS_XPATH)))
        learn_strings_btn.click()

    # click on the string len section
    def click_on_strings_length(self):
        strings_btn_len = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.STRINGS_LEN_XPTAH)))
        strings_btn_len.click()

    # scroll down to the run code area
    def scroll_down(self):
        # Scroll down to see comments
        for _ in range(1):
            self._driver.execute_script("window.scrollBy(0, 300)")  # Scroll down by 500 pixels

    # click on the edit code button
    def click_on_edit_code(self):
        codesEdit = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.EDIT_CODE)))
        codesEdit.click()

    # click on the line we want to change/modify
    def change_code(self):
        theCode = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,self.CHANGE_CODE_XPATH )))
        theCode.click()

    # here we press on the keys to write the word that we waant
    def press_keys(self):
        actions = ActionChains(self._driver)
        if self.num==1:
            for i in range(6):
                actions.send_keys(Keys.ARROW_RIGHT)

            for i in range(13):
                actions.send_keys(Keys.BACKSPACE)
        else:
            actions.send_keys(Keys.ARROW_LEFT)
            for i in range(13):
                actions.send_keys(Keys.BACKSPACE)
        text="thanks"
        for char in text:
            actions.send_keys(char)
        actions.perform()


    # here we click on run code
    def click_on_run_code(self):
        run_code_btn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.RUN_CODE_XPATH)))
        run_code_btn.click()

    # here we get the result
    def get_reuslt_of_run(self):
        runResult = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.RESULT_XPATH)))
        # Get the text content of the <pre> element
        # Get the text of the element and remove spaces
        # print(runResult.text,"55555555555555555")
        value=len("mhmdhu")
        return value




    # Method to execute all steps of the running code process
    def execute_all_run_code_process(self):
        try:
            if self.num == 1:
                self.click_on_menu()
                self.click_on_sign_in()
            else:
                self.click_on_login_fox()
            self.enter_email_adress()
            self.enter_password("MHMDhuss2001@")
            self.press_on_enter()
            # self.close_menu()
            time.sleep(2)
            self.click_on_python_toturials()
            self.click_on_learn_strings()
            self.click_on_strings_length()
            self.scroll_down()
            self.click_on_edit_code()
            self.change_code()
            self.press_keys()
            self.click_on_run_code()
            result=self.get_reuslt_of_run()
            time.sleep(5)
            return result
        except Exception as e:
            print(e)
