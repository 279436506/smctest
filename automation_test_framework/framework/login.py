# coding=utf-8
import time
import unittest
from automation_test_framework.pageobjects.login_page import HomePage
import automation_test_framework.framework.browser_engine as d


class Login(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     """
    #     测试固件的setUp()的代码，主要是测试的前提准备工作
    #     :return:
    #     """
    #     browse = d.BrowserEngine(cls)
    #     cls.driver = browse.open_browser(cls)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     测试结束后的操作，这里基本上都是关闭浏览器
    #     :return:
    #     """
    #     cls.driver.quit()

    def login(self):
        homepage = HomePage(self.driver)
        homepage.type_u('15881901234')  # 调用页面对象中的方法
        homepage.type_p('qwe123456')
        time.sleep(3)
        # vc = input("please input verification:")
        # homepage.type_v(vc)
        # time.sleep(5)
        homepage.click_sub()
        # homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(3)




if __name__ == '__main__':
    unittest.main()