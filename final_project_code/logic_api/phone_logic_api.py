
class phoneLogic:

    def __init__(self,api_object):
        self.my_api = api_object

    # get all thr qunatity of phone nums accroding to country code
    def get_phone_nums(self,countryCode,quantity):
        phone_nums_url = f"Phone/Generate?CountryCode={countryCode}&Quantity={quantity}"
        response = self.my_api.api_get_request(phone_nums_url)
        return response

    # get all possible countries in the system
    def get_all_countries_info(self):
        all_contries_url="Phone/Countries"
        response = self.my_api.api_get_request(all_contries_url)
        return response

    # validates a phone number
    def validate_phone_number(self,phone,country_code):
        # Find the index of the first space
        space_index = phone.index(' ')
        phone_start = phone[1:space_index]
        phone_num = phone[space_index + 1:].replace(' ', '')
        phone_url=f"Phone/Validate?telephone=%2B{phone_start}%20{phone_num}&CountryCode={country_code}"
        response = self.my_api.api_get_request(phone_url)
        return response
