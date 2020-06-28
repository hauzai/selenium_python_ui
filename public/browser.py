from selenium import webdriver


def select_browser(browser='Chrome'):
    if browser == 'Chrome':
        return webdriver.Chrome()
    elif browser == "Firefox":
        return webdriver.Firefox()
