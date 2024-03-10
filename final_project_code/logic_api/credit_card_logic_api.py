import random2


class cardLogic:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url

    # get all available cards
    def get_card_types(self):
        card_types_url = "Card/Types"
        response = self.my_api.api_get_request(self.url+card_types_url)
        return response


    # return the info of a card of this card type
    def get_card_details(self,card_type):
        wanted_card_url = f"Card?type={card_type}"
        response = self.my_api.api_get_request(self.url+wanted_card_url)
        return response

    def random_user_card_cvv_flow(self):
        card_types_result = self.get_card_types()
        card_types_result_json = card_types_result.json()

        # print(card_types_result_json)
        random_value = random2.choice(card_types_result_json)
        print("The chosen Credit Card type is ", random_value)

        card_detail_result = self.get_card_details(random_value)
        card_detail_result_json = card_detail_result.json()
        print("Card User Name:", card_detail_result_json["fullName"])
        return len(card_detail_result_json["cvv"])





