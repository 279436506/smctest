# coding=utf-8
from framework.base_page import BasePage
import time

class CustomerPage(BasePage):
    kehuziliao = "xpath=>//*[@id=\"sidebar\"]/ul/li[2]/ul/li[1]/a"
    addcus = "xpath=>/html/body/div[1]/div[4]/div/div/div/div[1]/div/form/div/div[2]/div/a[2]/span"
    cusname = "xpath=>//*[@id=\"customerFormData-table\"]/tbody/tr[1]/td[2]/span/input[1]"
    custype = "xpath=>//*[@id=\"customerFormData-table\"]/tbody/tr[2]/td[2]/span/input[1]"
    savebut = "xpath=>//*[@id=\"save\"]/span/span[1]"
    custype_z = "xpath=>//*[@id=\"_easyui_combobox_i1_2\"]"
    query = "xpath=>//*[@id=\"query_cunstomer\"]/span"
    hetong = "xpath=>//*[@id=\"sidebar\"]/ul/li[2]/a"
    iframe1 = "xpath=>//*[@id=\"tab_9945\"]/iframe"
    search_input = "xpath=>/html/body/div[1]/div[4]/div/div/div/div[1]/div/form/div/div[1]/span/span/input[1]"
    table_cn = "xpath=>//*[@id=\"datagrid-row-r2-2-0\"]/td[3]/div"
    alert_Y = "xpath=>/html/body/div[21]/div[3]/a[1]"
    choose = "xpath=>//*[@id=\"datagrid-row-r2-2-0\"]/td[1]/div/input"
    delete = "xpath=>//*[@id=\"delCustomerButton\"]/span"



    def click_hetong(self):
        self.click(self.hetong)
    def click_customer(self):
        self.click(self.kehuziliao)
    def click_addcus(self):
        self.click(self.addcus)
    def type_cusname(self,cname):
        self.type(self.cusname,cname)
    def click_custype(self):
        self.click(self.custype)
        time.sleep(2)
        self.click(self.custype_z)
    def click_save(self):
        self.click(self.savebut)
    def click_query(self):
        self.click(self.query)
    def type_search(self):
        self.type(self.search_input,'自动化测试用户')
    def duanyan(self):
        cusname = self.find_element(self.table_cn).text
        return cusname
    def click_sure(self):
        self.click(self.alert_Y)
    def click_choose(self):
        self.click(self.choose)
    def click_delete(self):
        self.click(self.delete)
