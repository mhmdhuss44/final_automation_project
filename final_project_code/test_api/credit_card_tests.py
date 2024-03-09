import time
import unittest
import random2
from infra.api_wrapper import APIWrapper
from logic_api.credit_card_logic_api import cardLogic
import pytest


class cardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.card_logic = cardLogic(self.my_api)

    # test to make sure that the status is 200 for getting card types
    def test_get_card_types_sucess(self):
        card_types_result = self.card_logic.get_card_types()
        self.assertEqual(card_types_result.status_code, 200, "Expected status code 200")


    # test to make sure that the status is 200 for getting card details
    def test_get_card_details_sucess(self):
        card_detail_result = self.card_logic.get_card_details("Visa")
        self.assertEqual(card_detail_result.status_code, 200, "Expected status code 200")



    # test to choose a random visa type and then get a random user of
    # this type and then verify that its cvv is of len 3
    def test_cvv_for_random_user(self):
        card_types_result = self.card_logic.get_card_types()
        card_types_result_json=card_types_result.json()

        # print(card_types_result_json)
        random_value = random2.choice(card_types_result_json)
        print("The chosen Credit Card type is ",random_value)

        card_detail_result = self.card_logic.get_card_details(random_value)
        card_detail_result_json=card_detail_result.json()
        print("Card User Name:",card_detail_result_json["fullName"])
        self.assertEqual(3,len(card_detail_result_json["cvv"]),"The CVV of the card is not of len 3")





























