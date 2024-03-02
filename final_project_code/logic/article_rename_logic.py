from infra.basePage import base
from logic.login_sucsess_logic import loginLogic
import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class modify_article(base):
    ARTICLES_XPATH = '//a[@href="https://write.geeksforgeeks.org/?ref=footer"]'
    WRITING_ARTICLES = '//a[@href="/posts-new?ref=WHPWA"]'
    MY_ARTICLES = '//a[@href="/my-posts?page=1&statusFilter=All"]'
    PYTHON_TURTORIAL_XPATH = '//a[@href="https://www.geeksforgeeks.org/python-programming-language/"]'
    CLICK_ON_FIRST_ARTICLE='//div//a[@style="font-weight: bold;"]'
    TITLE_ARTICLE_XPATH='//input[@id="postTitle"]'
    LAST_SAVE_BTN='//button[@class="ui button button_primary button_save"]'
    MODFIED_MY_ARTICLES='//a[@href="/my-posts?page=1&statusFilter=All"]'


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        self.configInfo=list_info
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num

    # this methods is used to scroll down to the videos section
    def scroll_down_to_videos(self):
        # Scroll down to see comments
        for _ in range(1):
            self._driver.execute_script("window.scrollBy(0, 8500)")

    def click_on_articles(self):
        # Find the logged-in logo element and wait for it to be visible
        articles_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ARTICLES_XPATH)))
        articles_btn.click()

    def click_on_writing_articles(self):
        # Find the logged-in logo element and wait for it to be visible
        writeArticles_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.WRITING_ARTICLES)))
        writeArticles_btn.click()

    # we click on my articles
    def my_articles_click(self):
        myPosts = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MY_ARTICLES)))
        myPosts.click()

    # we try to modify the first article
    def first_of_articles_click(self):
        myfirstArticle = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CLICK_ON_FIRST_ARTICLE)))
        myfirstArticle.click()

    # to add a new title for the article
    def enter_tile_of_article(self):
        articles_title = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TITLE_ARTICLE_XPATH)))
        articles_title.click()
        articles_title.clear()  # Clear any existing text in the input field
        if self.num==1:
            articles_title.send_keys("changed! in chrome")
        else:
            articles_title.send_keys("changed again in firefox")

    def final_save_btn(self):
        Save_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LAST_SAVE_BTN)))
        Save_btn.click()

    def click_on_mod_articles(self):
        # Find the logged-in logo element and wait for it to be visible
        try:
            articles_btn = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.MODFIED_MY_ARTICLES)))
            articles_btn.click()
            return True
        except Exception as e:
            return False


    def modify_article_name_flow(self):
        try:
            # sleeps needed cause of scroll
            time.sleep(self.configInfo["sleep_time"])
            self.scroll_down_to_videos()
            time.sleep(self.configInfo["sleep_time"])
            self.click_on_articles()
            self._driver.execute_script("window.scrollBy(0, 100)")
            self.click_on_writing_articles()
            time.sleep(self.configInfo["sleep_time"])
            self.my_articles_click()
            self.first_of_articles_click()
            self.enter_tile_of_article()
            self._driver.execute_script("window.scrollBy(0, 300)")
            time.sleep(self.configInfo["sleep_time"])
            self.final_save_btn()
            result=self.click_on_mod_articles()
            # time.sleep(5)
            return result
        except Exception as e:
            print(e)
            return False



