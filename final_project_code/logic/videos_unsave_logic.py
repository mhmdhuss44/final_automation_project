from selenium.webdriver import Keys, ActionChains
from infra.basePage import base
from logic.login_sucsess_logic import loginLogic
import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class unsaveVideos(base):
    FIRST_VIDEO_SAVED_CLASS='VideoCard_generalVideoCardContainer__fSg7p'
    FIRST_VIDEO='//a[@href="https://www.geeksforgeeks.org/videos/problem-of-the-day-26022024-power-set/"]'
    SECOND_VIDEO='//a[@href="https://www.geeksforgeeks.org/videos/problem-of-the-day-25022024-reach-a-given-score/"]'
    VIDEO_NAME_XPATH='//div[@class="videoParam_videoTitle__PmRna"]'
    SAVE_VIDEO_BTN_XPATH='//i[@class="gfg-icon  GfgIcon_gfg-icon-black-empty-save__TmyJO "]'
    SAVED_VIDEOS_XPATH='//a[@href="https://www.geeksforgeeks.org/videos/watchlist/"]'
    MENU_XPATH='//span[@class="hamburgerMenu"]'
    ALL_SAVED_VIDEOS_CLASS='//span[@class="VideoCard_videoCardTextData__2gcXl"]'
    LOGGEDIN_LOGO_XPATH = '//div[@class="defaultProfileImg"]'
    SAVED_VIDEOS_FIRE_XPATH='//a[@href="https://www.geeksforgeeks.org/videos/watchlist/"]'
    CLOSE_AD_BTN='//span[@class="AuthModule_close___MZaU"]'
    CLICK_SAVED_VIDEOS='//span[@class="SaveLikeSharePallet_sideMargin__FVroq SaveLikeSharePallet_saveContainer__KK8lV "]'
    VIDEO_LINK_XPATH='//a[@href="https://www.geeksforgeeks.org/videos/problem-of-the-day-28022024-check-if-a-number-is-divisible-by-8/"]'


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
            self._driver.execute_script("window.scrollBy(0, 3400)")  # Scroll down by 500 pixels


    # this methood is to find and click on the first video
    def click_on_video(self):
        if self.num == 1:
            firstVid = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SECOND_VIDEO)))
            firstVid.click()
        else:
            try:
                secondVid = WebDriverWait(self._driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.VIDEO_LINK_XPATH)))
                secondVid.click()
            except ElementNotInteractableException:
                secondVid = WebDriverWait(self._driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,self.VIDEO_LINK_XPATH)))
                secondVid.click()





    # a method to save the current video name!
    def save_video_name(self):
        videoName = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.VIDEO_NAME_XPATH)))
        # Get the text content of the element
        self.oldName = videoName.text
        print(self.oldName)


    # this methood is to find and click on the first video
    def click_on_save_video(self):
        try:
            saveVideoBtn = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,self.CLICK_SAVED_VIDEOS )))
            saveVideoBtn.click()
        except StaleElementReferenceException:
            saveVideoBtn = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.CLICK_SAVED_VIDEOS)))
            saveVideoBtn.click()

    # a method to click on saved videos on the user profile
    def click_on_saved_videos(self):
        savedVideosBtn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SAVED_VIDEOS_XPATH)))
        savedVideosBtn.click()

    # a method to click on saved videos on the user profile -firefox
    def click_on_saved_videos_fire(self):
        savedVideosBtn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SAVED_VIDEOS_FIRE_XPATH)))
        savedVideosBtn.click()

    # a method to open a menu
    def open_menu(self):
        menuBtn = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.MENU_XPATH)))
        menuBtn.click()

    # a method that returns true if the video we saved is under the saved videos
    def check_text_equals_num(self):
            # Find all elements with the specified class name
        elements_videos = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.ALL_SAVED_VIDEOS_CLASS)))

            # Iterate through each element and check if its text equals num
        for element in elements_videos:
            if element.text== self.oldName:
                return True

        # If none of the elements' text equals num, return False
        return False

    def check_for_sign_in_fox(self):
        # Find the logged-in logo element and wait for it to be visible
        loggedIn_logo = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGGEDIN_LOGO_XPATH)))
        loggedIn_logo.click()



    def click_on_close_ad(self):
        try:
            savedVideosBtn = WebDriverWait(self._driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, self.CLOSE_AD_BTN)))
            savedVideosBtn.click()
        except Exception as e:
            pass  # Do nothing and continue execution



    # a method to click on the first video
    def click_on_first_saved(self):
        allvideos = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, self.FIRST_VIDEO_SAVED_CLASS)))
        if self.num==1:
            allvideos[0].click()
        else:
            allvideos[1].click()


    # a flow function for reloading a page - needed (problem in geeksForgeeks)
    def reload_page(self):
        self._driver.refresh()  # Refresh the page

    # a flow function for unsavinf a video
    def unsave_video_flow(self):
        try:
            self.click_on_first_saved()
            self.reload_page()
            self.save_video_name()
            self.click_on_save_video()
            time.sleep(self.configInfo["sleep_time"])
            if self.num == 1:
                self.open_menu()
                self.click_on_saved_videos()
            else:
                self.check_for_sign_in_fox()
                self.click_on_saved_videos_fire()

            result = self.check_text_equals_num()
            return result
        except Exception as e:
            print(e)
            return False






