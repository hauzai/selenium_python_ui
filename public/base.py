from selenium.webdriver.remote.webdriver import WebDriver


class Page:
    '''
    :type driver:WebDriver

    '''

    def __init__(self, selenium_driver, url):
        self.driver = selenium_driver
        self.url = url

    def _open(self):
        # self.driver.get(self.url)
        pass

    def open(self):
        self.driver.get(self.url)

    def get_element(self, css):
        key = css[0].strip()
        value = css[1].strip()
        if key in ["id", "name", "class name", "link text", "xpath", "css selector"]:
            element = self.driver.find_element(key, value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element
