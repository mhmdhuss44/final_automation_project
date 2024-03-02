import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra.wrapper import browserWrapper
from logic.search_fail_logic import searchFail
from logic.search_logic import searchHebrew


class videoTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_unsuccessful_search(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_unsuccessful_search, self.infra_layer.cab_list)


    # test to verify that we can search in hebrw langaue
    def test_verify_successful_search(self, cab_info):
        cap, browser_type = cab_info

        self.search_hebrew = searchHebrew(browser_type,self.infra_layer.get_all_configurations(),cap)
        result=self.search_hebrew.search_in_hebrew_flow()
        assert result==True, "search in hebrew has failed"

        self.infra_layer.quit_drive(self.search_hebrew._driver)


    # negative test : test to verify that when we search invalid input we dont get any serach result
    def test_verify_unsuccessful_search(self,cab_info):
        cap, browser_type = cab_info

        self.search_fail = searchFail(browser_type,self.infra_layer.get_all_configurations(),cap)
        result=self.search_fail.search_in_not_valid_flow()
        assert result==True, "search in hebrew has failed"

        self.infra_layer.quit_drive(self.search_fail._driver)

























