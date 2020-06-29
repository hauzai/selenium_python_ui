from page.login_page import Login_page
from public.myunit import MyTest
from public.base import Page
import unittest
import logging



class login_Test(MyTest, Page):

    def test_login_test_success(self):
        test_page = Login_page(self.driver)
        test_page.user_login("root", "zaq12wsx")
        self.assertEqual(test_page.login_success_text(), "root")


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(level=logging.DEBUG)
    logging.warning("hello")
