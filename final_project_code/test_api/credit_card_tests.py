import unittest
import random2
from infra.api_wrapper import APIWrapper
from logic_api.credit_card_logic_api import cardLogic


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






    # # to test to verify that we actually get the n phone numbers - test with parameters
    # def test_validate_number_of_results(self):
    #     phone_nums_result = self.phone_logic.get_phone_nums("IL", 3)
    #     phone_nums_json = phone_nums_result.json()
    #     self.assertEqual(len(phone_nums_json), 3, "Expected 3 phone numbers in the response")
    #
    #
    # # test to check that all the numbers we get are valid israel numbers!
    # def test_validate_israel_phone_numbers(self):
    #     phone_nums_result = self.phone_logic.get_phone_nums("IL", 3)
    #     phone_nums_json = phone_nums_result.json()
    #     all_valid = True
    #     for phone_num in phone_nums_json:
    #         if not (phone_num.startswith("+972") and len(phone_num) == 14):
    #             all_valid = False
    #             break
    #     self.assertTrue(all_valid, "At least one phone number is not a valid Israeli phone number")
    #
    #
    #
    # # now we make a test that chooses a random country code , then it gets phone numbers of this country and at the end it verifies if
    # # they are valid phone numbers for this country
    # def test_validate_phone_number_for_random_country(self):
    #
    #     all_countries_result=self.phone_logic.get_all_countries_info()
    #     all_countries_json=all_countries_result.json()
    #
    #     # Choose a random country code
    #     random_country = random2.choice(all_countries_json)
    #     print("Chosen country:", random_country["name"])
    #     country_code=random_country["countryCode"]
    #     print("Chosen country code:", country_code)
    #
    #     phone_nums_result = self.phone_logic.get_phone_nums(country_code, 1)
    #     phone_nums_json = phone_nums_result.json()
    #     print("The result phone number",phone_nums_json)
    #
    #     valid_phone=self.phone_logic.validate_phone_number(phone_nums_json[0],country_code)
    #     valid_phone_json=valid_phone.json()
    #     self.assertTrue(valid_phone_json, "the phone number we got is not valid for this country")























