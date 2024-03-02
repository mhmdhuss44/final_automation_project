import json
from selenium import webdriver

class browserWrapper:
    # only this path worked
    JSON_URL = r"C:\Users\mhmdh\Desktop\new_final\final_automation_project\final_project_code\confg_info.json"
    def __init__(self):
        self.hub = None
        self.testing_mode = None
        self.webLink = None
        self.browsers_list = None
        self.cab_list=[]
        self.load_configurations()
        self.preapare_cab_list()
        self.driver=None



    def load_configurations(self):
        with open(self.JSON_URL, 'r') as file:
            data = json.load(file)
            self.hub = data.get('hub_url')
            self.testing_mode = data.get('testing_mode')
            self.webLink = data.get('web_link')
            self.emailChrome = data.get('emailChrome')
            self.passwordChrome = data.get('passwordchrome')
            self.emailFirefox = data.get('emailFirefox')
            self.passwordFirefox = data.get('passwordfirefox')
            self.sleep_time = data.get('sleep_time')
            browsers = data.get('browsers', [])
            self.browsers_list = [(browser.get('browser_name'), browser.get('platform_name')) for browser in browsers]


    def get_all_configurations(self):
        # self.load_configurations()
        return {
            "browsers_list": self.browsers_list,
            "hub_url": self.hub,
            "testing_mode": self.testing_mode,
            "web_link": self.webLink,
            "emailChrome": self.emailChrome,
            "passwordChrome": self.passwordChrome,
            "emailFirefox": self.emailFirefox,
            "passwordFirefox": self.passwordFirefox,
            "sleep_time":self.sleep_time
        }

    def preapare_cab_list(self):
        temp=self.get_all_configurations()
        browser_names = [name for name, _ in temp['browsers_list']]
        if "chrome" in browser_names:
            print("Chrome found")
            self.chrome_cab = webdriver.ChromeOptions()
            platform = [platform for name, platform in temp['browsers_list'] if name == "chrome"][0]
            self.chrome_cab.capabilities['platformName'] = platform
            self.cab_list.append((self.chrome_cab,1))

        if "firefox" in browser_names:
            print("Firefox found")
            self.fire_cab = webdriver.FirefoxOptions()
            platform = [platform for name, platform in temp['browsers_list'] if name == "firefox"][0]
            self.fire_cab.capabilities['platformName'] = platform
            self.cab_list.append((self.fire_cab,2))

    def quit_drive(self,driver):
        driver.quit()













