from selenium import webdriver
class base:
    def __init__(self,list_info):
        # we want it to be protected
        self._driver=None
        self.info=list_info




    def driver_set_up(self,cap):
        hub_url = self.info.get('hub_url')
        web_url = self.info.get('web_link')

        if not hub_url:
            raise ValueError("Hub URL not provided in the configuration.")

        if not web_url:
            raise ValueError("Web URL not provided in the configuration.")


        self._driver = webdriver.Remote(command_executor=hub_url, options=cap)
        self._driver.get(web_url)



