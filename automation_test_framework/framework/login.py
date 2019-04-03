# coding=utf-8
import time
import unittest
from automation_test_framework.pageobjects.login_page import HomePage


class Login(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     """
    #     测试固件的setUp()的代码，主要是测试的前提准备工作
    #     :return:
    #     """
    #     browse = BrowserEngine(cls)
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
        homepage.type_u('LZB04')  # 调用页面对象中的方法
        homepage.type_p('111111')
        time.sleep(3)
        # vc = input("please input verification:")
        # homepage.type_v(vc)
        time.sleep(5)
        homepage.click_sub()
        # homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(3)
        # try:
        #     assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
        #     print('Test Pass.')
        # except Exception as e:
        #     print('Test Fail.', format(e))

    # def test_search2(self):
    #     homepage = HomePage(self.driver)
    #     homepage.type_search('python')  # 调用页面对象中的方法
    #     homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
    #     time.sleep(2)
    #     homepage.get_windows_img()  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()