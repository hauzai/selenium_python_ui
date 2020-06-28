import unittest
from public.base import Page
from public import browser


class MyTest(unittest.TestCase, Page):

    @classmethod
    def setUp(self):
        self.driver = browser.select_browser(browser='Chrome')
        Page(self.driver).max_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()
