from selenium.webdriver import Keys, ActionChains
from infra.basePage import base
import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RunCode(base):

    PYTHON_TURTORIAL_XPATH = '//a[@href="https://www.geeksforgeeks.org/python-programming-language/"]'
    LEARN_STRINGS_XPATH="//h2[text()='Python String']"
    STRINGS_LEN_XPTAH='//a[text()="Python string length | len() function to find string length"]'
    EDIT_CODE='//*[@id="run-and-edit-button"]'
    CHANGE_CODE_XPATH='//pre[@class=" CodeMirror-line "]'
    RUN_CODE_XPATH='//*[@id="run-code-button"]'
    RESULT_XPATH='//pre[@class="output-pre"]'
    SEARCH_BTN_XPAAH = '//input[@class="ant-input ant-input-lg"]'
    PRESS_ON_SEARCH_BTN_XPATH = '//button[@class="ant-btn ant-btn-default ant-btn-lg ant-input-search-button"]'
    FIRST_SEARCH_RESULT = '//div[@class="ant-row"]//a[@class="font-primary"]'
    SPINNER_CLASS="spinner-loading-overlay"


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        self.configInfo=list_info
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num



    # a method to click on the search bar and write something
    def click_on_search_bar_and_type(self):
        # Wait for the overlay to be invisible before attempting to click on the element
        WebDriverWait(self._driver, 10).until_not(
            EC.visibility_of_element_located((By.CLASS_NAME, self.SPINNER_CLASS))
        )

        try:
            search_bar = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_BTN_XPAAH)))
            search_bar.click()
            search_bar.clear()  # Clear any existing text in the input field
            search_bar.send_keys("python string len")
        except Exception as e:
            # Wait for the overlay to be invisible before attempting to click on the element
            WebDriverWait(self._driver, 10).until_not(
                EC.visibility_of_element_located((By.CLASS_NAME, self.SPINNER_CLASS))
            )
            search_bar = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_BTN_XPAAH)))
            search_bar.click()
            search_bar.clear()  # Clear any existing text in the input field
            search_bar.send_keys("python string len")


    # a method to click on the search
    def click_on_search_btn(self):
        search_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PRESS_ON_SEARCH_BTN_XPATH)))
        search_btn.click()

    # takes the first result and checks if its relevant
    def check_on_first_result(self):
        first_result = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_SEARCH_RESULT)))
        first_result.click()

    # this method is to click on the python toturials
    def click_on_python_toturials(self):
        # Wait for the overlay to be invisible before attempting to click on the element
        WebDriverWait(self._driver, 10).until_not(
            EC.visibility_of_element_located((By.CLASS_NAME, self.SPINNER_CLASS))
        )

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
            self._driver.execute_script("window.scrollBy(0, 200)")  # Scroll down by 500 pixels

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
        while runResult.text==" Request Compiling...":
            pass
        value=runResult.text[0]
        # print(runResult.text[0])
        return int(value)




    # Method to execute all steps of the running code process
    def execute_all_run_code_process(self):
        try:
            self.click_on_search_bar_and_type()
            time.sleep(self.configInfo["sleep_time"])
            self.click_on_search_btn()
            time.sleep(2)
            self.check_on_first_result()
            time.sleep(self.configInfo["sleep_time"])
            self.scroll_down()
            self.click_on_edit_code()
            time.sleep(1)
            self.change_code()
            self.press_keys()
            self.click_on_run_code()
            result=self.get_reuslt_of_run()
            time.sleep(2)
            return result
        except Exception as e:
            print(e)
            return False

