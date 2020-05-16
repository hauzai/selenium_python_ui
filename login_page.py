from selenium import webdriver

from public.base import Page

class Login_page(Page):
    """
    Login页面，继承自Page基类
    """
    #定位器
    login_name_loc = ("id", "login_name")
    login_password_loc = ("id", "login_pwd")
    login_button_loc = ("id", "login")
    lgoin_error_loc = ("class name","toast-message")
    login_success_loc = ("xpath","//*[@id='app']/section/header/ul/li[7]/div/a")

    #页面元素操作
    def login_name(self,username):
        self.element_send_keys(self.login_name_loc,username)
    def login_password(self,password):
        self.element_send_keys(self.login_password_loc,password)
    def login_click(self):
        self.element_click(self.login_button_loc)
    def login_error_text(self):
        return self.element_get_text(self.lgoin_error_loc)
    def login_success_text(self):
        return self.element_get_text(self.login_success_loc)

    #登录操作
    def user_login(self,username,password):
        self.login_name(username)
        self.login_password(password)
        self.login_click()


if __name__ == '__main__':
    wb = webdriver.Chrome()
    test = Login_page(wb,"http://192.168.1.96:8082/passport")
    test.open()
    test.user_login("root","1")
    # print(test.login_success_text())
    print(test.login_error_text())
