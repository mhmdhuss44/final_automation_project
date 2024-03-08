import time

from infra.basePage import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class searchFail(base):

    SEARCH_BTN_XPAAH='//input[@class="ant-input ant-input-lg"]'
    PRESS_ON_SEARCH_BTN_XPATH='//button[@class="ant-btn ant-btn-default ant-btn-lg ant-input-search-button"]'
    FAIL_SEARCH_RESULT='//div[text()="No Results Found"]'


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num

    # a method to click on the search bar and write something
    def click_on_search_bar_and_type(self):
        search_bar = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BTN_XPAAH)))
        search_bar.click()
        search_bar.clear()  # Clear any existing text in the input field
        search_bar.send_keys("#$@%")

    # a method to click on the search
    def click_on_search_btn(self):
        search_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PRESS_ON_SEARCH_BTN_XPATH)))
        search_btn.click()

    # takes the first result and checks if its relevant
    def check_on_first_result(self):
        try:
            fail_result = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.FAIL_SEARCH_RESULT)))
            return True
        except Exception as e:
            return False






    def search_in_not_valid_flow(self):
        try:
            self.click_on_search_bar_and_type()
            time.sleep(2)
            self.click_on_search_btn()
            time.sleep(2)
            result=self.check_on_first_result()
            time.sleep(2)
            return result
        except Exception as e:
            print(e)
            return False


