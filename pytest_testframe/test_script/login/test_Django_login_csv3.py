import csv
import pytest
from selenium import webdriver
import time

class Test_Django_Login():
#2、创建测试方法
    #登录初始化
    def setup_method(self):
        self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    #正常登录测试方法

    def test_login_01(self):
        f=open('logindata.csv','r')
        rows=csv.reader(f)
        for row in rows:
            print(row[0])
            self.driver.find_element_by_name('username').send_keys(row[0])
            self.driver.find_element_by_name('password').send_keys(row[1])
            self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
            #  统一检查点
            result = self.driver.current_url
            print(result)
            if row[2]=='1':
                assert result != self.url
            else:
                assert result == self.url
                time.sleep(1)
                self.driver.find_element_by_name('username').clear()
                self.driver.find_element_by_name('password').clear()


    def teardown_method(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_allure_example11.py','-s', '-q', '--alluredir', './tmp/report'])