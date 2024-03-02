from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.basePage import base

# Class to handle logout logic
class logout_logic(base):
    LOGOUT_XPATH = '//span[@class="gfg-icon gfg-icon_default-pos gfg-icon_logout"]'
    SIGN_IN_BUTTON_CSS = 'a.gfg-sec-bg.color-white.login-modal-btn'
    LOGGEDIN_LOGO_XPATH = '//div[@class="header-main__profile"]//p[@class="profileCard-profile-picture"]'
    LOG_OUT_BTN_XPATH = '//a[@href="https://auth.geeksforgeeks.org/logout.php/?to=https://www.geeksforgeeks.org/"]'
    LOGIN_BTN_XPATH_FOX = "//li[@id='userProfileId']//a[text()='Sign In']"
    MENU_CLASS='hamburger-menu'

    def __init__(self, num, list_info, cabs,driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num

    # Method to press on logout
    def press_on_logout(self):
        logout_btn = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.LOGOUT_XPATH)))
        logout_btn.click()

    # Method to check if the sign-in button appears after logout
    def check_for_sign_in(self):
        try:
            sign_in_button = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SIGN_IN_BUTTON_CSS)))
            return True
        except NoSuchElementException:
            return False


    def check_for_sign_in_fox(self):
        try:
            loggedIn_logo = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGGEDIN_LOGO_XPATH)))
            loggedIn_logo.click()
        except ElementClickInterceptedException:
            loggedIn_logo = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGGEDIN_LOGO_XPATH)))
            loggedIn_logo.click()


    def click_on_log_out_fox(self):
        log_out_btn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOG_OUT_BTN_XPATH)))
        log_out_btn.click()

    def click_on_menu(self):
        try:
            button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.MENU_CLASS)))
            button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.MENU_CLASS)))
            button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, self.MENU_CLASS)))
            button.click()

    # Method to click on the login button on Firefox
    def check_login_btn_fox(self):
        try:
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH_FOX)))
            return True
        except NoSuchElementException:
            return False


    # Method to execute all steps of the logout process
    def execute_all_log_out(self):
        # try:
        if self.num == 1:
            self.click_on_menu()
            self.press_on_logout()
            self.click_on_menu()
            result = self.check_for_sign_in()
        else:
            self.check_for_sign_in_fox()
            self.click_on_log_out_fox()
            result=self.check_login_btn_fox()
        return result
        # except Exception as e:
        #     print(e)
        #     return "failed"