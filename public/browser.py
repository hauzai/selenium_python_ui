from selenium import webdriver


def select_browser(browser='chrome'):
    if browser == 'Chrome':
        return webdriver.chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
