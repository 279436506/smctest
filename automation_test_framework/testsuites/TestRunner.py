# coding = utf-8
import unittest
import os
import time
import HTMLTestRunner
import io

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + ".html"
fp = open(HtmlFile,"wb")

suite = unittest.TestLoader().discover("testsuites")


if __name__=='__main__':
    #执行用例
    runner = HTMLTestRunner.HTMLTestReportCN(stream=fp,title=u'数码仓自动化测试报告',description=u'测试情况：')
    runner.run(suite)
    fp.close()