import unittest
import random2
from infra.api_wrapper import APIWrapper
from logic_api.manpulate_text_logic_api import textManpulate


class textTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.text_logic = textManpulate(self.my_api,self.my_api.url)

    # test_ui to make sure that the status is 200 for modifying text
    def test_post_test_modify_sucess(self):
        modify_text_result = self.text_logic.post_text_change_words("Replace","mhmd","king",self.my_api.text)
        self.assertEqual(modify_text_result.status_code, 200, "Expected status code 200")


    # test_ui to a text and change every occurance of word1 to word2
    def test_post_test_modify_result(self):
        modify_text_result = self.text_logic.post_text_change_words("Replace","mhmd","king",self.my_api.text)
        card_types_result_json=modify_text_result.json()
        print(card_types_result_json)
        if "mhmd" in card_types_result_json:
            text_in=False
        else:
            text_in=True
        self.assertTrue(text_in,"error! at least one word was'nt modfied!")

































