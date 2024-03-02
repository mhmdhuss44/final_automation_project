import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra.wrapper import browserWrapper
from logic.article_add_logic import writeArticle
from logic.article_rename_logic import modify_article
from logic.login_sucsess_logic import loginLogic


class articleTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_article_writing(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_article_writing, self.infra_layer.cab_list)


    # this test is to verify that we can successfuly add a new article
    def test_verify_successful_article_writing(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        temp = self.loginPage.execute_all_log_in_flow_mod()

        self.article = writeArticle(browser_type,self.infra_layer.get_all_configurations(),cap,self.loginPage._driver)
        result = self.article.write_article_flow()
        assert result==True, "article wasnt added sucessfuly"

        self.infra_layer.quit_drive(self.article._driver)


    # this test is to verify that we can successfuly change an article name
    def test_verify_successful_article_reName(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        temp = self.loginPage.execute_all_log_in_flow_mod()

        self.articleName = modify_article(browser_type,self.infra_layer.get_all_configurations(),cap,self.loginPage._driver)
        result = self.articleName.modify_article_name_flow()
        # sleep for the final present - to make sure we can see a result
        time.sleep(5)
        assert result==True, "renaming an article failure"

        self.infra_layer.quit_drive(self.articleName._driver)


















