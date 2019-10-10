# coding=utf-8
import time
import unittest
from automation_test_framework.framework.browser_engine import BrowserEngine
from automation_test_framework.pageobjects.customer_page import CustomerPage
from automation_test_framework.framework.login import Login



class Addcustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_addcus(self):
        #登录系统
        customerpage = CustomerPage(self.driver)
        Login.login(self)
        try:
            assert customerpage.duanyan() == ''
            print("test pass.")
        except Exception as e:
            print("Test fail.", format(e))






if __name__ == '__main__':
    unittest.main()

