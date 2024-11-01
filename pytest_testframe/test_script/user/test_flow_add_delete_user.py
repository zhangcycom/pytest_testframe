#添加用户&删除用户业务场景pytest封装
#传递username这个参数，删除指定刚添加的用户
import time

import pytest
from selenium import webdriver
@pytest.mark.smoke2
class Test_add_delete_user():
    #登录初始化：只做一次
    def setup_class(self):
        self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.find_element_by_name('username').send_keys('atstudy')
        self.driver.find_element_by_name('password').send_keys('51testing')
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    #添加用户
    #添加固件标签
    @pytest.fixture()
    def test_add_user(self):
        url = 'http://testplt.share.atstudy.com/admin/auth/user/add/'
        self.driver.get(url)
        username='user77'
        self.driver.find_element_by_id('id_username').send_keys(username)
        self.driver.find_element_by_id('id_password1').send_keys("123456Pwd")
        self.driver.find_element_by_id('id_password2').send_keys("123456Pwd")
        # 点击保存
        self.driver.find_element_by_xpath('//*[@id="user_form"]/div/div/input[1]').click()
        time.sleep(3)
        return username
    #删除指定用户
    def test_delete_user(self,test_add_user):
        url='http://testplt.share.atstudy.com/admin/auth/user/'
        self.driver.get(url)
        num=len(self.driver.find_elements_by_class_name('field-username'))
        print(num)
        for i in range(1,num+1):
            # time.sleep(1)
            uname=self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr['+str(i)+']/th/a').text
            print(uname)
            if uname==test_add_user:
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[' + str(i) + ']/th/a').click()
                #点击删除按钮
                self.driver.find_element_by_xpath('//*[@id="user_form"]/div/div/p/a').click()
                #获取新页面的句柄
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.find_element_by_xpath('//*[@id="content"]/form/div/input[2]').click()
                #跳出循环
                break
