import json
import pytest
import unittest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from infra.wrapper import browserWrapper
from test_api.credit_card_tests_api import cardTests

class TestRunner:
    @staticmethod
    def run_serial():
        suite = unittest.TestLoader().loadTestsFromTestCase(cardTests)
        unittest.TextTestRunner().run(suite)

    @staticmethod
    def run_parallel(browsers):
        for cab, _ in browsers:
            browser_name = cab.capabilities['browserName']
            print(f"Running tests in {browser_name} browser:")
            driver = webdriver.Remote(command_executor='http://192.168.146.1:4444', options=cab)
            cardTests.driver = driver

            # Execute tests using pytest
            pytest.main(['-v', 'test_api/credit_card_tests_api.py'])

            driver.quit()

if __name__ == "__main__":
    # Serial execution
    # print("Running tests serially:")
    # TestRunner.run_serial()

    # Parallel execution with Selenium Grid
    print("\nRunning tests in parallel on different browsers:")
    browser_wrapper = browserWrapper()
    browsers_to_test = browser_wrapper.cab_list  # List of browser capabilities from browserWrapper
    TestRunner.run_parallel(browsers_to_test)

