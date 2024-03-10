import time
import unittest
import random2
from infra.api_wrapper import APIWrapper
from logic_api.credit_card_logic_api import cardLogic
import pytest


class cardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.card_logic = cardLogic(self.my_api,self.my_api.url)

    # test_ui to make sure that the status is 200 for getting card types
    def test_get_card_types_sucess(self):
        card_types_result = self.card_logic.get_card_types()
        self.assertEqual(card_types_result.status_code, 200, "Expected status code 200")


    # test_ui to make sure that the status is 200 for getting card details
    def test_get_card_details_sucess(self):
        card_detail_result = self.card_logic.get_card_details("Visa")
        self.assertEqual(card_detail_result.status_code, 200, "Expected status code 200")



    # test_ui to choose a random visa type and then get a random user of
    # this type and then verify that its cvv is of len 3
    def test_cvv_for_random_user(self):
        card_types_result = self.card_logic.random_user_card_cvv_flow()
        self.assertEqual(3,card_types_result,"The CVV of the card is not of len 3")





























