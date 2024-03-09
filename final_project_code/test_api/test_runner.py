import unittest
import pytest
from test_api.credit_card_tests import cardTests


class TestRunner:
    @staticmethod
    def run_serial():
        suite = unittest.TestLoader().loadTestsFromTestCase(cardTests)
        unittest.TextTestRunner().run(suite)

    @staticmethod
    def run_parallel(browsers):
        pytest_args = ['--boxed']
        for browser in browsers:
            pytest_args.extend(['-n', 'auto', '--browser', browser])
        pytest.main(pytest_args)

if __name__ == "__main__":
    # Serial execution
    print("Running tests serially:")
    TestRunner.run_serial()

    # # Parallel execution with Selenium
    print("\nRunning tests in parallel on different browsers:")
    browsers_to_test = ['chrome', 'firefox']  # List of browsers to test
    TestRunner.run_parallel(browsers_to_test)