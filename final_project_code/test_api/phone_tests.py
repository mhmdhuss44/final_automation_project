import unittest
import random2
from infra.api_wrapper import APIWrapper
from logic_api.phone_logic_api import phoneLogic


class phoneTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.phone_logic = phoneLogic(self.my_api)

    # test to make sure that the status is 200 for getting phone numbers
    def test_get_phone_numbers_sucess(self):
        phone_nums_result = self.phone_logic.get_phone_nums("IL", 3)
        self.assertEqual(phone_nums_result.status_code, 200, "Expected status code 200")

    # to test to verify that we actually get the n phone numbers - test with parameters
    def test_validate_number_of_results(self):
        phone_nums_result = self.phone_logic.get_phone_nums("IL", 3)
        phone_nums_json = phone_nums_result.json()
        self.assertEqual(len(phone_nums_json), 3, "Expected 3 phone numbers in the response")


    # test to check that all the numbers we get are valid israel numbers!
    def test_validate_israel_phone_numbers(self):
        phone_nums_result = self.phone_logic.get_phone_nums("IL", 3)
        phone_nums_json = phone_nums_result.json()
        all_valid = True
        for phone_num in phone_nums_json:
            if not (phone_num.startswith("+972") and len(phone_num) == 14):
                all_valid = False
                break
        self.assertTrue(all_valid, "At least one phone number is not a valid Israeli phone number")



    # now we make a test that chooses a random country code , then it gets phone numbers of this country and at the end it verifies if
    # they are valid phone numbers for this country
    def test_validate_phone_number_for_random_country(self):

        all_countries_result=self.phone_logic.get_all_countries_info()
        all_countries_json=all_countries_result.json()

        # Choose a random country code
        random_country = random2.choice(all_countries_json)
        print("Chosen country:", random_country["name"])
        country_code=random_country["countryCode"]
        print("Chosen country code:", country_code)

        phone_nums_result = self.phone_logic.get_phone_nums(country_code, 1)
        phone_nums_json = phone_nums_result.json()
        print("The result phone number",phone_nums_json)

        valid_phone=self.phone_logic.validate_phone_number(phone_nums_json[0],country_code)
        valid_phone_json=valid_phone.json()
        self.assertTrue(valid_phone_json, "the phone number we got is not valid for this country")























