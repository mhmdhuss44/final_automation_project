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


class gridProject(unittest.TestCase):
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


    # this test is used to verify that we can successfully login with the right email and password
    def test_verify_successful_login(self, cabs, browserType):
        self.loginPage = loginLogic(browserType,self.configs,cabs)
        result = self.loginPage.execute_all_log_in()
        self.driver=self.loginPage._driver
        assert result, "Login was not successful"




    # negative test: this test is used to verify that we cant successed to login with right email and wrong password
    def test_verify_unsuccessful_login(self, cabs, browserType):
        self.failLogin = unsucess_login(browserType,self.configs,cabs)
        result = self.failLogin.execute_all_fail_log_in()
        self.driver = self.failLogin._driver
        time.sleep(1)
        assert result, "BE careful ,Login with wrong password was successful!!!"




    # this test is used to verify that the user can successfully logout after he logged in
    def test_verify_successful_logout(self, cabs, browserType):
        self.logoutPage = logout_logic(browserType,self.configs,cabs)
        result = self.logoutPage.execute_all_log_out()
        self.driver = self.logoutPage._driver
        assert result, "Logut was not successful"



    def test_verify_successful_code_run(self, cabs, browserType):
        self.runCodes = RunCode(browserType,self.configs,cabs)
        result = self.runCodes.execute_all_run_code_process()
        self.driver=self.runCodes._driver
        # this sleep is need because the code needs sometime to run!
        assert result == 6, "Result is not equal to 6"




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

    def test_verify_successful_article_writing(self, cabs, browserType):
        try:
            self.article = writeArticle(browserType,self.configs,cabs)
            result = self.article.write_article_flow()
            self.driver = self.article._driver
            time.sleep(2)
            # assert result, "video wasnt saved successfuly"
        except Exception as e:
            assert False, f"An error occurred: {str(e)}"
















