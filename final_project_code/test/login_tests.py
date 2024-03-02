import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra.wrapper import browserWrapper
from logic.login_fail_logic import unsucess_login
from logic.login_sucsess_logic import loginLogic
from logic.logout_logic import logout_logic


class loginTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_logout(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_login, self.infra_layer.cab_list)


    # this test is used to verify that we can successfully login with the right email and password
    def test_verify_successful_login(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type,self.infra_layer.get_all_configurations(),cap)
        result = self.loginPage.execute_all_log_in_flow()
        assert result == True , "Login was not successful"

        self.infra_layer.quit_drive(self.loginPage._driver)




    # negative test: this test is used to verify that we cant successed to login with right email and wrong password
    def test_verify_unsuccessful_login(self, cab_info):
        cap, browser_type = cab_info

        self.failLogin = unsucess_login(browser_type,self.infra_layer.get_all_configurations(),cap)
        result = self.failLogin.execute_all_fail_log_in()

        assert result == True, "BE careful ,Login with wrong password was successful!!!"

        self.infra_layer.quit_drive(self.failLogin._driver)





    # this test is used to verify that the user can successfully logout after he logged in
    def test_verify_successful_logout(self, cab_info):
        cap, browser_type = cab_info

        # in order to do logout we have to do login first! so we use the login flow
        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        result = self.loginPage.execute_all_log_in_flow_mod()

        # now we do the logout
        self.logoutPage = logout_logic(browser_type,self.infra_layer.get_all_configurations(),cap,self.loginPage._driver)
        result = self.logoutPage.execute_all_log_out()
        print("55555", result)
        assert result == True, "Logout was not successful"

        self.infra_layer.quit_drive(self.logoutPage._driver)



















