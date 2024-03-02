import concurrent.futures.thread
import unittest
import concurrent.futures
from infra.wrapper import browserWrapper
from logic.login_sucsess_logic import loginLogic
from logic.videos_save_logic import saveVideo
from logic.videos_unsave_logic import unsaveVideos


class videoTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()

    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_saving_video(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_saving_video, self.infra_layer.cab_list)


    # test to verify that we can save a video and the saved video will appear under saved videos on the user profile
    def test_verify_successful_saving_video(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        temp = self.loginPage.execute_all_log_in_flow_mod()

        self.savedVideo = saveVideo(browser_type,self.infra_layer.get_all_configurations(),cap,self.loginPage._driver)
        result = self.savedVideo.execute_all_save_video_process()
        assert result, "video wasnt saved successfuly"

        self.infra_layer.quit_drive(self.savedVideo._driver)


    # test to verify that we can unsave a video
    def test_verify_successful_unsave_video(self, cab_info):
        cap, browser_type = cab_info

        # first we log in
        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        temp = self.loginPage.execute_all_log_in_flow_mod()

        # then we save a video
        self.savedVideo = saveVideo(browser_type, self.infra_layer.get_all_configurations(), cap, self.loginPage._driver)
        result = self.savedVideo.execute_all_save_video_process()

        # then the unsave video test
        self.unsavedVideo = unsaveVideos(browser_type,self.infra_layer.get_all_configurations(),cap,self.savedVideo._driver)
        result = self.unsavedVideo.unsave_video_flow()
        self.driver = self.unsavedVideo._driver
        assert not result, "video wasnt unsaved successfuly"

        self.infra_layer.quit_drive(self.unsavedVideo._driver)




















