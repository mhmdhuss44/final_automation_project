import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.basePage import base


class loginLogic(base):
    # XPaths and CSS Selectors
    LOGIN_BTN_XPATH = "/html/body/nav/div/div[1]/ul[2]/li[4]/a"
    SIGN_IN_BTN_CSS = "a.gfg-sec-bg.color-white.login-modal-btn"
    USERNAME_INPUT_CSS_CHROME = "input#luser.modal-form-input"
    USERNAME_INPUT_XPATH_FOX = '//*[@id="luser"]'
    PASSWORD_INPUT_CSS = "input#password.modal-form-input"
    # SIGN_IN_BTN_CSS = "button.btn.btn-green.signin-button"
    LOGGED_IN_LOGO_XPATH = '/html/body/nav/div/div[3]/ul/li[1]/p'
    def __init__(self, num, list_info, cabs):
        super().__init__(list_info)
        self.driver_set_up(cabs)
        self.num = num

    # Method to click on the menu on the page (for Chrome)
    def click_on_menu(self):
        try:
            button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "hamburger-menu")))
            button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "hamburger-menu")))
            button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "hamburger-menu")))
            button.click()

    # Method to click on the login button on Firefox
    def click_on_login_fox(self):
        # Find the button element using the provided XPath and wait for it to be clickable
        button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.LOGIN_BTN_XPATH)))
        # Click the button
        button.click()

    # Method to click on the sign-in button after the menu is opened in Chrome
    def click_on_sign_in(self):
        # Find the Sign In button and wait for it to be clickable
        sign_in_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SIGN_IN_BTN_CSS)))
        # Click the "Sign In" button
        sign_in_button.click()

    # Method to enter an email address on the login page
    def enter_email_adress(self):
        if self.num == 1:
            # Find the username input field and wait for it to be visible
            username_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.USERNAME_INPUT_CSS_CHROME)))
        else:
            username_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.USERNAME_INPUT_XPATH_FOX)))
        username_input.send_keys("mhmdhuss44@gmail.com")

    # Method to enter a password
    def enter_password(self, secret_pass):
        # Find the password input field and wait for it to be visible
        password_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.PASSWORD_INPUT_CSS)))
        password_input.send_keys(secret_pass)

    # Method to press Enter after adding the email and password
    def press_on_enter(self):
        # Find the Sign In button and wait for it to be clickable
        sign_in_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-green.signin-button")))
        # Click the "Sign In" button
        sign_in_button.click()

    # Method to verify successful login
    def verify_successful_login(self):
        try:
            time.sleep(5)
            # Find the logged-in logo element and wait for it to be visible
            loggedIn_logo = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/p')))
            return True
        except NoSuchElementException:
            return False

    # Method to verify successful login
    def verify_successful_login_fire(self):
        try:
            # Find the logged-in logo element and wait for it to be visible
            loggedIn_logo = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/nav/div/div[1]/ul[2]/li[4]/div/p')))
            return True
        except NoSuchElementException:
            return False

    # Method to execute all steps of the login process
    def execute_all_log_in(self):
        if self.num == 1:
            self.click_on_menu()
            self.click_on_sign_in()
        else:
            self.click_on_login_fox()
        self.enter_email_adress()
        self.enter_password("MHMDhuss2001@")
        self.press_on_enter()
        if self.num == 1:
            self.click_on_menu()
            result = self.verify_successful_login()
        else:
            result=self.verify_successful_login_fire()
        return result

# Class to handle another test, ensuring that we can't login with the wrong password
class unsucess_login(loginLogic):
    def __init__(self, num,list_info, cabs):
        super().__init__(num, list_info, cabs)

    # Method to check if an error message successfully appears if we enter wrong details
    def error_message_showing(self):
        try:
            # Find the error message element and wait for it to be visible
            error_message = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Login"]/div[1]/div/div')))
            return True
        except NoSuchElementException:
            return False

    # Method to execute all steps of the unsuccessful login process
    def execute_all_fail_log_in(self):
        if self.num == 1:
            self.click_on_menu()
            self.click_on_sign_in()
        else:
            self.click_on_login_fox()
        self.enter_email_adress()
        self.enter_password("123456789")
        self.press_on_enter()
        result = self.error_message_showing()
        return result

# Class to handle logout logic
class logout_logic(loginLogic):
    def __init__(self, num, list_info, cabs):
        super().__init__(num, list_info, cabs)

    # Method to press on logout
    def press_on_logout(self):
        # Find the logout button and wait for it to be clickable
        logout_btn = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/table/tbody/tr[3]/td[2]/a')))
        # Click the logout button
        logout_btn.click()

    # Method to check if the sign-in button appears after logout
    def check_for_sign_in(self):
        try:
            # Find the Sign In button and wait for it to be visible
            sign_in_button = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.gfg-sec-bg.color-white.login-modal-btn")))
            return True
        except NoSuchElementException:
            return False

    # Method to verify successful login
    def check_for_sign_in_fox(self):
        # Find the logged-in logo element and wait for it to be visible
        loggedIn_logo = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/nav/div/div[1]/ul[2]/li[4]/div/p')))
        loggedIn_logo.click()

    # Method to verify successful login
    def click_on_log_out_fox(self):
        # Find the logged-in logo element and wait for it to be visible
        log_out_btn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/nav/div/div[1]/ul[2]/li[4]/ul/li[7]/a')))
        log_out_btn.click()

    # Method to click on the login button on Firefox
    def check_login_btn_fox(self):
        try:
            # Find the button element using the provided XPath and wait for it to be clickable
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/div[1]/ul[2]/li[4]/a")))
            return True
        except NoSuchElementException:
            return False




    # Method to execute all steps of the logout process
    def execute_all_log_out(self):
        if self.num == 1:
            self.click_on_menu()
            self.click_on_sign_in()
        else:
            self.click_on_login_fox()
        self.enter_email_adress()
        self.enter_password("MHMDhuss2001@")
        self.press_on_enter()
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
