import concurrent.futures.thread
import unittest
import concurrent.futures
from infra.wrapper import browserWrapper
from logic.login_sucsess_logic import loginLogic
from logic.run_code_logic import RunCode


class codeRunTest(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_code_run(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_code_run, self.infra_layer.cab_list)


    # test to make sure than we can successfully run code
    def test_verify_successful_code_run(self, cab_info):
        cab, browser_type = cab_info

        login_page = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cab)
        num = login_page.execute_all_log_in_flow_mod()

        run_codes = RunCode(browser_type, self.infra_layer.get_all_configurations(), cab, login_page._driver)
        result = run_codes.execute_all_run_code_process()
        assert result == 6, "Result is not equal to 6"

        self.infra_layer.quit_drive(run_codes._driver)





















