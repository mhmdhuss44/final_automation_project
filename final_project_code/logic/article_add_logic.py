from infra.basePage import base
import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class writeArticle(base):
    ARTICLES_XPATH='//a[@href="https://write.geeksforgeeks.org/?ref=footer"]'
    WRITING_ARTICLES='//a[@href="/posts-new?ref=WHPWA"]'
    TITLE_ARTICLE_XPATH='//input[@id="postTitle"]'
    BODY_ARTICLE_XPATH='//div[@class="ContentEditable__root"]'
    SELECT_CATEGORY_XPATH='//div[text()="Select category"]'
    SELECT_FROM_CATEGOREIS='//span[text()="Project"]'
    SAVE_BTN='//button[text()="Save for later"]'
    MY_ARTICLES='//a[@href="/my-posts?page=1&statusFilter=All"]'
    PYTHON_TURTORIAL_XPATH = '//a[@href="https://www.geeksforgeeks.org/python-programming-language/"]'

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
        articles_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ARTICLES_XPATH)))
        articles_btn.click()

    def click_on_writing_articles(self):
        writeArticles_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.WRITING_ARTICLES)))
        writeArticles_btn.click()

    def enter_tile_of_article(self):
        articles_title = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TITLE_ARTICLE_XPATH)))
        articles_title.click()
        articles_title.clear()  # Clear any existing text in the input field
        if self.num==1:
            articles_title.send_keys("beyond dev automation course")
        else:
            articles_title.send_keys("searching for jobs!")


    def enter_body_of_article(self):
            articles_body = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.BODY_ARTICLE_XPATH)))
            articles_body.click()
            articles_body.clear()  # ]Clear any existing text in the input field
            if self.num==1:
                text = """In an era where technology evolution is relentless, staying ahead of the curve is paramount for professionals in the software development industry. Enter the "Beyond Dev" course, a comprehensive program designed to equip learners with the skills needed to navigate the intricacies of automation and software testing. This article delves into the enriching experience of this course, highlighting its key components and the invaluable knowledge gained.
    
                The journey commences with a deep dive into QA automation, laying a solid foundation for understanding the nuances of testing in software development. Participants are introduced to various testing types, encompassing both functional and non-functional aspects. From validating functionalities to assessing performance metrics, learners gain insights into the diverse facets of ensuring software quality.
    
                Central to the curriculum is the exploration of the software development lifecycle (SDLC), elucidating the stages involved in bringing a software product from conception to deployment. Understanding SDLC is crucial as it provides a roadmap for effective testing strategies at each phase of development, ultimately fostering a culture of quality assurance.
    
                As the course progresses, participants delve into the practical application of testing methodologies, preparing comprehensive documents such as test plans (STP), test designs (STD), and test reports (STR). Utilizing industry-standard tools like TestRail and Jira, learners harness the power of efficient test management, streamlining the testing process for enhanced productivity and collaboration.
    
                Transitioning seamlessly into the second phase of the course, the focus shifts towards automation in Python. Building upon a strong foundation in object-oriented programming (OOP) and Python basics, participants embark on an exhilarating journey into the realm of automation scripting.
    
                Hands-on experience with Selenium and Selenium Grid empowers learners to automate test cases across various web applications, leveraging the versatility of Python scripting. From functional testing to cross-browser compatibility, participants gain proficiency in executing a myriad of test scenarios with precision and efficiency."""

                articles_body.send_keys(text)
            else:
                text_two="hello everyone , my name is mohammed hussien and now im currently looking for an open job"
                for char in text_two:
                    articles_body.send_keys(char)
                    time.sleep(0.1)  # Adjust the delay as needed

    def select_category(self):
        category = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_CATEGORY_XPATH)))
        category.click()

    # we select from category
    def select_from_categorys(self):
        category = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_FROM_CATEGOREIS)))
        category.click()

    # we click on save article
    def save_article(self):
        try:
            saveAll = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SAVE_BTN)))
            saveAll.click()
        except ElementClickInterceptedException:
            saveAll = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SAVE_BTN)))
            saveAll.click()

    # the process failed so we return false
    def my_articles_click(self):
        try:
            myPosts = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.MY_ARTICLES)))
            myPosts.click()
            return True
        except Exception as e:
            return False



    # writing an article flow
    def write_article_flow(self):
        try:
            time.sleep(self.configInfo["sleep_time"])
            self.scroll_down_to_videos()
            time.sleep(self.configInfo["sleep_time"])
            self.click_on_articles()
            self._driver.execute_script("window.scrollBy(0, 100)")
            time.sleep(self.configInfo["sleep_time"])
            self.click_on_writing_articles()
            time.sleep(2)
            self.enter_tile_of_article()
            time.sleep(2)
            self.enter_body_of_article()
            time.sleep(self.configInfo["sleep_time"])
            self._driver.execute_script("window.scrollBy(0, 400)")
            time.sleep(self.configInfo["sleep_time"])
            self.select_category()
            self.select_from_categorys()
            self._driver.execute_script("window.scrollBy(0, 400)")
            time.sleep(self.configInfo["sleep_time"])
            self.save_article()
            result=self.my_articles_click()
            time.sleep(self.configInfo["sleep_time"])
            return result
        except Exception as e:
            print(e)
            return False







