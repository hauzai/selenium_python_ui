from public import browser

from public.base import Page

from public.log import MyLog

import logging

class Login_page(Page):
    """
    Login页面，继承自Page基类
    """
    # 定位器
    login_name_loc = ("id", "login_name")
    login_password_loc = ("id", "login_pwd")
    login_button_loc = ("id", "login")
    login_error_loc = ("class name", "toast-message")
    login_success_loc = ("xpath", "//*[@id='app']/section/header/ul/li[7]/div/a")

    # 页面元素操作
    def login_name(self, username):
        self.element_send_keys(self.login_name_loc, username)

    def login_password(self, password):
        self.element_send_keys(self.login_password_loc, password)

    def login_click(self):
        self.element_click(self.login_button_loc)

    def login_error_text(self):
        return self.element_get_text(self.login_error_loc)

    def login_success_text(self):
        return self.element_get_text(self.login_success_loc)

    # 登录操作
    def user_login(self, username, password):
        self.open()
        self.login_name(username)
        self.login_password(password)
        self.login_click()
        my_log = MyLog()
        my_log.debug("登录操作")


if __name__ == '__main__':
    wb = browser.select_browser(browser='Chrome')
    test = Login_page(wb, "http://192.168.1.96:8082/passport")
    # test.open()
    test.user_login("root", "zaq12wsx")
    print(test.login_success_text())
    test.close()
    # logging.basicConfig(level=logging.DEBUG,format='%(name)s-%(filename)s-%(funcName)s')
    # logging.info("测试日志")
    # print(test.login_error_text())
    # my_log = MyLog()
    # my_log.debug("测试日志")

