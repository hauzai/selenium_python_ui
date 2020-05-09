from selenium import webdriver


class my_webdriver:
    def __init__(self, browser='Chrome'):
        if browser == 'Chrome':
            return webdriver.chrome()
