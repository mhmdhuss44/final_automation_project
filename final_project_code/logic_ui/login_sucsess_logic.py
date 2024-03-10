import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.basePage import base


class loginLogic(base):
    # XPaths and CSS Selectors
    MENU_CLASS_CLASS='hamburger-menu'
    LOGIN_BTN_XPATH = "//li[@id='userProfileId']//a[text()='Sign In']"
    SIGN_IN_BTN_CSS = "a.gfg-sec-bg.color-white.login-modal-btn"
    USERNAME_INPUT_CSS_CHROME = "input#luser.modal-form-input"
    USERNAME_INPUT_XPATH_FOX = '//*[@id="luser"]'
    PASSWORD_INPUT_CSS = "input#password.modal-form-input"
    SIGN_IN_BTN_CSS_TWO = "button.btn.btn-green.signin-button"
    LOGGED_IN_LOGO_XPATH = '//li[@class="header-sidebar__list-item"]//p[@class="profileCard-profile-picture"]'
    LOGGED_IN_LOGO_FIRE_FOX='//div[@class="header-main__profile"]//p[@class="profileCard-profile-picture"]'
    def __init__(self, num, list_info, cabs,driver=None):
        super().__init__(list_info)
        self.confgInfo=list_info
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver=driver
        self.num = num

    # Method to click on the menu on the page (for Chrome)
    def click_on_menu(self):
        try:
            button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.MENU_CLASS_CLASS)))
            button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.MENU_CLASS_CLASS)))
            button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, self.MENU_CLASS_CLASS)))
            button.click()


    # Method to click on the login button on Firefox
    def click_on_login_fox(self):
        button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.LOGIN_BTN_XPATH)))
        button.click()

    # Method to click on the sign-in button after the menu is opened in Chrome
    def click_on_sign_in(self):
        sign_in_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SIGN_IN_BTN_CSS)))
        sign_in_button.click()

    # Method to enter an email address on the login page
    def enter_email_adress(self):
        if self.num == 1:
            username_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.USERNAME_INPUT_CSS_CHROME)))
            username_input.send_keys(self.confgInfo["emailChrome"])
        else:
            username_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.USERNAME_INPUT_XPATH_FOX)))
            username_input.send_keys(self.confgInfo["emailFirefox"])


    # Method to enter a password
    def enter_password(self, secret_pass):
        password_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.PASSWORD_INPUT_CSS)))
        password_input.send_keys(secret_pass)


    # Method to press Enter after adding the email and password
    def  press_on_enter(self):
        sign_in_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SIGN_IN_BTN_CSS_TWO)))
        sign_in_button.click()

    # Method to verify successful login
    def verify_successful_login(self):
        try:
            loggedIn_logo = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.LOGGED_IN_LOGO_XPATH)))
            return True
        except NoSuchElementException:
            return False

    # Method to verify successful login
    def verify_successful_login_fire(self):
        try:
            loggedIn_logo = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.LOGGED_IN_LOGO_FIRE_FOX)))
            return True
        except NoSuchElementException:
            return False


    # Method to execute all steps of the login process
    def execute_all_log_in_flow(self):
        try:
            if self.num == 1:
                self.click_on_menu()
                self.click_on_sign_in()
            else:
                self.click_on_login_fox()
            self.enter_email_adress()
            self.enter_password(self.confgInfo["passwordChrome"])
            self.press_on_enter()
            if self.num == 1:
                self.click_on_menu()
                result = self.verify_successful_login()
            else:
                result=self.verify_successful_login_fire()
            return result
        except Exception as e:
            print(e)
            return "failed"

    def execute_all_log_in_flow_mod(self):
        try:
            if self.num == 1:
                self.click_on_menu()
                self.click_on_sign_in()
            else:
                self.click_on_login_fox()
            self.enter_email_adress()
            self.enter_password(self.confgInfo["passwordChrome"])
            self.press_on_enter()
            return True
        except Exception as e:
            print(e)
            return "failed"









