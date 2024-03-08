
class cardLogic:

    def __init__(self,api_object):
        self.my_api = api_object

    # get all available cards
    def get_card_types(self):
        card_types_url = "Card/Types"
        response = self.my_api.api_get_request(card_types_url)
        return response


    # return the info of a card of this card type
    def get_card_details(self,card_type):
        wanted_card_url = f"Card?type={card_type}"
        response = self.my_api.api_get_request(wanted_card_url)
        return response




