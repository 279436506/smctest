# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.customer_page import CustomerPage
from framework.login import Login



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
        #添加联系人
        customerpage.click_hetong()
        time.sleep(1)
        customerpage.click_customer()
        time.sleep(1)
        self.driver.switch_to_frame(0)
        time.sleep(2)
        customerpage.click_addcus()
        time.sleep(1)
        customerpage.click_custype()
        time.sleep(1)
        customerpage.type_cusname('自动化测试用户')
        time.sleep(1)
        customerpage.click_save()
        time.sleep(2)
        customerpage.type_search()
        time.sleep(1)
        customerpage.click_query()
        time.sleep(5)
        assert customerpage.duanyan() == u'自动化测试用户'
        #删除联系人
        customerpage.click_choose()
        time.sleep(1)
        customerpage.click_delete()
        time.sleep(2)
        customerpage.click_sure()
        time.sleep(1)
        customerpage.type_search()
        time.sleep(1)
        customerpage.click_query()
        time.sleep(5)
        try:
            assert customerpage.duanyan() == ''
            print("test pass.")
        except Exception as e:
            print("Test fail.", format(e))






if __name__ == '__main__':
    unittest.main()

