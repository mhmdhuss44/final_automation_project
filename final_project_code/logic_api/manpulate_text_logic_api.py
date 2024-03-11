
class textManpulate:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url



    # change all occurance of word 1 to word 2
    def post_text_change_words(self,action_type,find,replace,body):
        text_replace_url = f"Text/Transform?textActionType={action_type}&find={find}&replace={replace}"
        response = self.my_api.api_post_request(self.url+text_replace_url,body)
        return response







