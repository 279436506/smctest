# coding=utf-8
from automation_test_framework.framework.base_page import BasePage


class HomePage(BasePage):
    userName = "id=>userName"
    passWord = "id=>password"
    verifyCode = "id=>verifyCode"
    submit = "id=>button"

    def type_u(self, username):
        self.type(self.userName, username)

    def type_p(self, pwd):
        self.type(self.passWord, pwd)

    def type_v(self, vc):
        self.type(self.verifyCode, vc)

    def click_sub(self):
        self.click(self.submit)