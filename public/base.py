from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    """
    :type driver:WebDriver

    """

    def __init__(self, selenium_driver, url):
        self.driver = selenium_driver
        self.url = url

    def _open(self, url):
        # self.driver.get(self.url)
        pass

    def open(self):
        self.driver.get(self.url)

    def get_element(self, css):
        """
        获取页面中元素
        :param css: 定位器 （定位方法，定位值）
        :return: 返回定位到的元素
        """
        key = css[0].strip()
        value = css[1].strip()
        if key in ["id", "name", "class name", "link text", "xpath", "css selector"]:
            try:
                element = self.driver.find_element(key, value)
                return element
            except exceptions.NoSuchElementException as e:
                # TODO 2020-5-15 16:31 需要打印日志功能
                print("未发现该元素")
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def max_window(self):
        """
        最大化浏览器
        :return:
        """
        self.driver.maximize_window()

    def close(self):
        """
        关闭浏览器页面
        :return:
        """
        self.driver.close()

    def quit(self):
        """
        退出
        :return:
        """
        self.driver.quit()

    def element_wait(self, css, sec=5):
        """
        等待元素加载完毕
        :param css: 定位器
        :param sec: 等待时间
        :return: 加载完毕的元素
        """
        if self._css_check(css):
            try:
                WebDriverWait(self.driver, sec, 0.5).until(EC.presence_of_element_located(css), "根据条件查找不到对应元素")
            except exceptions.TimeoutException as e:
                print(e)

    def _css_check(self, css):
        if css[0].strip() in ["id", "name", "class name", "link text", "xpath", "css selector"]:
            return True
        else:
            return False


if __name__ == '__main__':
    wb = webdriver.Chrome()
    test = Page(wb, "http://192.168.1.96:8082/passport")
    test.open()
    test.max_window()
    login = test.get_element(("id", "login_name"))
    login.send_keys("root")
    test.close()
    test.quit()
