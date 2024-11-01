#选择若干权限，调用提交用户，选中需要的权限

#导入包文件
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
g_number=88

class Test_select_autho_addgroup():
    # 登录初始化：只做一次
    def setup_class(self):
        self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.find_element_by_name('username').send_keys('atstudy')
        self.driver.find_element_by_name('password').send_keys('51testing')
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    # @pytest.fixture()
    # def random_number(self):
    #     num=random.randint(1,88)
    #     return num
    #选择权限
    @pytest.fixture()
    def test_select_autho(self):
        autholist=[]
        url='http://testplt.share.atstudy.com/admin/auth/permission/'
        self.driver.get(url)
        # for i in range(1,89):
        #     if i==number:
        for j in range(0,g_number):
            #生成随机数
            i=random.randint(1,88)
            print(i)
            autho=self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr['+str(i)+']/th/a').text
            autholist.append(autho)
        print(autholist)
        return(autholist)
    #添加组

    def test_add_group(self,test_select_autho):
        url = 'http://testplt.share.atstudy.com/admin/auth/group/add/'
        self.driver.get(url)
        self.driver.find_element_by_id('id_name').send_keys("group1")
        # 选中权限添加
        for autho in test_select_autho:
            select_auto=self.driver.find_element_by_id('id_permissions_from')
            Select(select_auto).select_by_visible_text(autho)
        # Select(autho).select_by_visible_text('auth | 权限 | Can change permission')
        self.driver.find_element_by_id('id_permissions_add_link').click()

class Test_02():
    def test_02_01(self):
        print("test02-01")

if __name__ == '__main__':
    pytest.main(['-s','test_flow_select_autho_addgroup.py'])