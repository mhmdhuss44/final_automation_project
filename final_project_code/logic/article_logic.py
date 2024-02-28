from selenium.webdriver import Keys, ActionChains
from logic.login_logout_logic import loginLogic
import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class writeArticle(loginLogic):
    # ARTICLES_XPATH='//*[@id="gfg-footer"]/div[1]/div[2]/div[4]/ul[6]/li[2]'
    # WRITING_ARTICLES='//*[@id="root"]/div[2]/div/div[2]/div/div/div[3]'


    def __init__(self, num, list_info, cabs):
        super().__init__(num, list_info, cabs)

    # this methods is used to scroll down to the videos section
    def scroll_down_to_videos(self):
        # Scroll down to see comments
        for _ in range(1):
            self._driver.execute_script("window.scrollBy(0, 8000)")

    def click_on_log_articles(self):
        # Find the logged-in logo element and wait for it to be visible
        articles_btn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ARTICLES_XPATH)))
        articles_btn.click()

    def click_on_writing_articles(self):
        # Find the logged-in logo element and wait for it to be visible
        writeArticles_btn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.WRITING_ARTICLES)))
        writeArticles_btn.click()


    def write_article_flow(self):
        if self.num == 1:
            self.click_on_menu()
            self.click_on_sign_in()
        else:
            self.click_on_login_fox()
        self.enter_email_adress()
        self.enter_password("MHMDhuss2001@")
        self.press_on_enter()
        time.sleep(1)
        self.scroll_down_to_videos()
        time.sleep(1)
        self.click_on_log_articles()
        self._driver.execute_script("window.scrollBy(0, 100)")
        self.click_on_writing_articles()
