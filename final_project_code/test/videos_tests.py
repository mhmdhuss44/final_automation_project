import concurrent.futures.thread
import time
import unittest
from functools import partial
from selenium import webdriver
import concurrent.futures
from infra.basePage import base
from infra.wrapper import browserWrapper
from logic.article_logic import writeArticle
from logic.login_logout_logic import loginLogic, unsucess_login, logout_logic
from logic.run_code_logic import RunCode
from logic.videos_logic import saveVideo, unsaveVideos


class videoTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def tearDown(self) -> None:
        self.driver.quit()

    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cab,num in self.infra_layer.cab_list:
            self.test_verify_successful_saving_video(cab,num)

    # def test_run_grid_parallel(self):
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.basePage.cab_list)) as executor:
    #         # Create a list of partial functions, each with one cap argument fixed
    #         partial_functions = [partial(self.test_execute_language, cap) for cap in self.basePage.cab_list]
    #         # Execute the partial functions in parallel
    #         executor.map(lambda f: f(), partial_functions)

    # test to verify that we can save a video and the saved video will appear under saved videos on the user profile
    def test_verify_successful_saving_video(self, cabs, browserType):
        try:
            self.savedVideo = saveVideo(browserType,self.configs,cabs)
            result = self.savedVideo.execute_all_save_video_process()
            self.driver = self.savedVideo._driver
            time.sleep(2)
            assert result, "video wasnt saved successfuly"
        except Exception as e:
            assert False, f"An error occurred: {str(e)}"

    # test to verify that we can like a video and that the liking count will increase by 1
    def test_verify_successful_unsave_video(self, cabs, browserType):
        try:
            self.unsavedVideo = unsaveVideos(browserType,self.configs,cabs)
            result = self.unsavedVideo.unsave_video_flow()
            self.driver = self.unsavedVideo._driver
            time.sleep(2)
            assert not result, "video wasnt unsaved successfuly"
        except Exception as e:
            assert False, f"An error occurred: {str(e)}"


















