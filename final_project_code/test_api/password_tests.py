import unittest
import random2
from infra.api_wrapper import APIWrapper
from logic_api.credit_card_logic_api import cardLogic
from logic_api.password_logic_api import passwordLogic


class passwordTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.password_logic = passwordLogic(self.my_api,self.my_api.url)


    # test_ui to make sure that the status is 200 for getting a strong password
    def test_get_strong_password_sucess(self):
        # first variable is the wanted password len , third is for conating any digit, third for upper case letter and fourth for special char
        strong_pass_result = self.password_logic.get_strong_password(8,True,True,True)
        print("The generated password is:",strong_pass_result.json())
        self.assertEqual(strong_pass_result.status_code, 200, "Expected status code 200")


    # test_ui to check the generated password if it contains all of the condition
    def test_valid_strong_password(self):
        # first variable is the wanted password len , third is for conating any digit, third for upper case letter and fourth for special char
        strong_pass_result = self.password_logic.strong_pass_check_flow(8, True, True, True)
        self.assertTrue(strong_pass_result, "the generated password is missing something!")

