import random2


class phoneLogic:

    def __init__(self, api_object, url):
        self.my_api = api_object
        self.url = url

    # get all thr qunatity of phone nums accroding to country code
    def get_phone_nums(self,countryCode,quantity):
        phone_nums_url = f"Phone/Generate?CountryCode={countryCode}&Quantity={quantity}"
        response = self.my_api.api_get_request(self.url+phone_nums_url)
        return response

    # get all possible countries in the system
    def get_all_countries_info(self):
        all_contries_url="Phone/Countries"
        response = self.my_api.api_get_request(self.url+all_contries_url)
        return response

    # validates a phone number
    def validate_phone_number(self,phone,country_code):
        # Find the index of the first space
        space_index = phone.index(' ')
        phone_start = phone[1:space_index]
        phone_num = phone[space_index + 1:].replace(' ', '')
        phone_url=f"Phone/Validate?telephone=%2B{phone_start}%20{phone_num}&CountryCode={country_code}"
        response = self.my_api.api_get_request(self.url+phone_url)
        return response


    def validate_random_country_phone_flow(self):
        all_countries_result = self.get_all_countries_info()
        all_countries_json = all_countries_result.json()

        # Choose a random country code
        random_country = random2.choice(all_countries_json)
        print("Chosen country:", random_country["name"])
        country_code = random_country["countryCode"]
        print("Chosen country code:", country_code)

        phone_nums_result = self.get_phone_nums(country_code, 1)
        phone_nums_json = phone_nums_result.json()
        print("The result phone number", phone_nums_json)

        valid_phone = self.validate_phone_number(phone_nums_json[0], country_code)
        valid_phone_json = valid_phone.json()
        return valid_phone_json

