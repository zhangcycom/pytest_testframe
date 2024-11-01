#Django自动化测试平台selenium自动化测试脚本—pytest封装
#功能名称：登录
#版本：V2.2_参数化设置_不同处理过程，不同参数
#描述：正常异常用户登录

import pytest
from selenium import webdriver
#1、创建测试类
class Test_Django_Login():
#2、创建测试方法
    #登录初始化
    def setup_method(self):
        self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    @pytest.mark.parametrize('uname,pwd', (["atstudy", "51testing"], ["atstudy1", "51testing"]))
    def test_login_02(self,uname,pwd):
        self.driver.find_element_by_name('username').send_keys(uname)
        self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
        #**********************************************************************************************
        #异常处理方法1通过try-except进行异常处理
        try:
            result = self.driver.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/caption/a').text
            print(result)
            # 3、通过断言进行判断
            assert result == "测试平台"
        except Exception as e:
            print(e)
            result = self.driver.find_element_by_xpath('//*[@id="content"]/p').text
            # 断言：包含比对
            assert "请输入" in result





