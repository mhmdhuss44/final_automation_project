import concurrent.futures.thread
import time
import unittest
from functools import partial
from selenium import webdriver
import concurrent.futures
from infra.basePage import base
from infra.wrapper import browserWrapper
from logic.login_logout_logic import loginLogic, unsucess_login, logout_logic


class gridProject(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.infra_layer.load_configurations()
        # self.basePage=base(self.infra_layer.get_all_configurations())
        self.infra_layer.preapare_cab_list()
        self.configs=self.infra_layer.get_all_configurations()


    def tearDown(self) -> None:
        self.driver.quit()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cab,num in self.infra_layer.cab_list:
            self.test_verify_successful_login(cab,num)

    # def test_run_grid_parallel(self):
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.basePage.cab_list)) as executor:
    #         # Create a list of partial functions, each with one cap argument fixed
    #         partial_functions = [partial(self.test_execute_language, cap) for cap in self.basePage.cab_list]
    #         # Execute the partial functions in parallel
    #         executor.map(lambda f: f(), partial_functions)


    # this test is used to verify that we can successfully login with the right email and password
    def test_verify_successful_login(self, cabs, browserType):
        try:
            self.loginPage = loginLogic(browserType,self.configs,cabs)
            result = self.loginPage.execute_all_log_in()
            self.driver=self.loginPage._driver
            time.sleep(1)
            assert result, "Login was not successful"
        except Exception as e:
            assert False, f"An error occurred: {str(e)}"



    # negative test: this test is used to verify that we cant successed to login with right email and wrong password
    def test_verify_unsuccessful_login(self, cabs, browserType):
        try:
            self.failLogin = unsucess_login(browserType,self.configs,cabs)
            result = self.failLogin.execute_all_fail_log_in()
            self.driver = self.failLogin._driver
            time.sleep(1)
            assert result, "BE careful ,Login with wrong password was successful!!!"
        except Exception as e:
            assert False, f"An error occurred: {str(e)}"



    # this test is used to verify that the user can successfully logout after he logged in
    def test_verify_successful_logout(self, cabs, browserType):
        try:
            self.logoutPage = logout_logic(browserType,self.configs,cabs)
            result = self.logoutPage.execute_all_log_out()
            self.driver = self.logoutPage._driver
            time.sleep(2)
            assert result, "Login was not successful"
        except Exception as e:
            assert False, f"An error occurred: {str(e)}"















