
class passwordLogic:

    def __init__(self,api_object):
        self.my_api = api_object

    # get a password with all the conditions
    def get_strong_password(self,passLen,conatins_digit,has_upper,has_special):
        new_pass_url = f"Text/Password?length={passLen}&hasDigits={conatins_digit}&hasUppercase={has_upper}&hasSpecial={has_special}"
        response = self.my_api.api_get_request(new_pass_url)
        return response

    # to verify that a password has a digit
    def pass_include_digits(self, currentPass):
        return any(char.isdigit() for char in currentPass)

    # to verify that the passowoed contains at least one upper letter
    def pass_include_upper(self, currentPass):
        return any(char.isupper() for char in currentPass)

    # to verify that the passowoed contains at least one special char
    def pass_include_special(self, currentPass):
        special_characters = "!@#$%^&*()_-+=<>?/"
        return any(char in special_characters for char in currentPass)

    # a flow function to call all of the above methods
    def strong_pass_check_flow(self,passLen, contains_digit, has_upper, has_special):
        strong_password = self.get_strong_password(passLen, contains_digit, has_upper, has_special)
        strong_password_json=strong_password.json()
        print("The generated password is:",strong_password_json)
        if contains_digit and not self.pass_include_digits(strong_password_json):
            return False
        if has_upper and not self.pass_include_upper(strong_password_json):
            return False
        if has_special and not self.pass_include_special(strong_password_json):
            return False

        return True









